/****************************************************************************
**
** Copyright (C) 2018 Klarälvdalens Datakonsult AB, a KDAB Group company, info@kdab.com, author Marc Mutz <marc.mutz@kdab.com>
** Copyright (C) 2018 Klarälvdalens Datakonsult AB, a KDAB Group company, info@kdab.com, author Giuseppe D'Angelo <giuseppe.dangelo@kdab.com>
** Copyright (C) 2020 The Qt Company Ltd.
** Contact: https://www.qt.io/licensing/
**
** This file is part of the QtCore module of the Qt Toolkit.
**
** $QT_BEGIN_LICENSE:LGPL$
** Commercial License Usage
** Licensees holding valid commercial Qt licenses may use this file in
** accordance with the commercial license agreement provided with the
** Software or, alternatively, in accordance with the terms contained in
** a written agreement between you and The Qt Company. For licensing terms
** and conditions see https://www.qt.io/terms-conditions. For further
** information use the contact form at https://www.qt.io/contact-us.
**
** GNU Lesser General Public License Usage
** Alternatively, this file may be used under the terms of the GNU Lesser
** General Public License version 3 as published by the Free Software
** Foundation and appearing in the file LICENSE.LGPL3 included in the
** packaging of this file. Please review the following information to
** ensure the GNU Lesser General Public License version 3 requirements
** will be met: https://www.gnu.org/licenses/lgpl-3.0.html.
**
** GNU General Public License Usage
** Alternatively, this file may be used under the terms of the GNU
** General Public License version 2.0 or (at your option) the GNU General
** Public license version 3 or any later version approved by the KDE Free
** Qt Foundation. The licenses are as published by the Free Software
** Foundation and appearing in the file LICENSE.GPL2 and LICENSE.GPL3
** included in the packaging of this file. Please review the following
** information to ensure the GNU General Public License requirements will
** be met: https://www.gnu.org/licenses/gpl-2.0.html and
** https://www.gnu.org/licenses/gpl-3.0.html.
**
** $QT_END_LICENSE$
**
****************************************************************************/

#if 0
#pragma qt_sync_skip_header_check
#pragma qt_sync_stop_processing
#endif

#ifndef QCONTAINERTOOLS_IMPL_H
#define QCONTAINERTOOLS_IMPL_H

#include <QtCore/qglobal.h>
#include <QtCore/qtypeinfo.h>

#include <cstring>
#include <iterator>
#include <memory>
#include <algorithm>

QT_BEGIN_NAMESPACE

namespace QtPrivate
{

/*!
  \internal

  Returns whether \a p is within a range [b, e). In simplest form equivalent to:
  b <= p < e.
*/
template<typename T, typename Cmp = std::less<>>
static constexpr bool q_points_into_range(const T *p, const T *b, const T *e,
                                          Cmp less = {}) noexcept
{
    return !less(p, b) && less(p, e);
}

template <typename T, typename N>
void q_uninitialized_relocate_n(T* first, N n, T* out)
{
    if constexpr (QTypeInfo<T>::isRelocatable) {
        if (n != N(0)) { // even if N == 0, out == nullptr or first == nullptr are UB for memmove()
            std::memmove(static_cast<void*>(out),
                         static_cast<const void*>(first),
                         n * sizeof(T));
        }
    } else {
        std::uninitialized_move_n(first, n, out);
        if constexpr (QTypeInfo<T>::isComplex)
            std::destroy_n(first, n);
    }
}

template<typename iterator, typename N>
void q_relocate_overlap_n_left_move(iterator first, N n, iterator d_first)
{
    // requires: [first, n) is a valid range
    // requires: d_first + n is reachable from d_first
    // requires: iterator is at least a random access iterator
    // requires: value_type(iterator) has a non-throwing destructor

    Q_ASSERT(n);
    Q_ASSERT(d_first < first); // only allow moves to the "left"
    using T = typename std::iterator_traits<iterator>::value_type;

    // Watches passed iterator. Unless commit() is called, all the elements that
    // the watched iterator passes through are deleted at the end of object
    // lifetime. freeze() could be used to stop watching the passed iterator and
    // remain at current place.
    //
    // requires: the iterator is expected to always point to an invalid object
    //           (to uninitialized memory)
    struct Destructor
    {
        iterator *iter;
        iterator end;
        iterator intermediate;

        Destructor(iterator &it) noexcept : iter(std::addressof(it)), end(it) { }
        void commit() noexcept { iter = std::addressof(end); }
        void freeze() noexcept
        {
            intermediate = *iter;
            iter = std::addressof(intermediate);
        }
        ~Destructor() noexcept
        {
            for (const int step = *iter < end ? 1 : -1; *iter != end;) {
                std::advance(*iter, step);
                (*iter)->~T();
            }
        }
    } destroyer(d_first);

    const iterator d_last = d_first + n;
    // Note: use pair and explicitly copy iterators from it to prevent
    // accidental reference semantics instead of copy. equivalent to:
    //
    // auto [overlapBegin, overlapEnd] = std::minmax(d_last, first);
    auto pair = std::minmax(d_last, first);

    // overlap area between [d_first, d_first + n) and [first, first + n) or an
    // uninitialized memory area between the two ranges
    iterator overlapBegin = pair.first;
    iterator overlapEnd = pair.second;

    // move construct elements in uninitialized region
    while (d_first != overlapBegin) {
        // account for std::reverse_iterator, cannot use new(d_first) directly
        new (std::addressof(*d_first)) T(std::move_if_noexcept(*first));
        ++d_first;
        ++first;
    }

    // cannot commit but have to stop - there might be an overlap region
    // which we don't want to delete (because it's part of existing data)
    destroyer.freeze();

    // move assign elements in overlap region
    while (d_first != d_last) {
        *d_first = std::move_if_noexcept(*first);
        ++d_first;
        ++first;
    }

    Q_ASSERT(d_first == destroyer.end + n);
    destroyer.commit(); // can commit here as ~T() below does not throw

    while (first != overlapEnd)
        (--first)->~T();
}

/*!
  \internal

  Relocates a range [first, n) to [d_first, n) taking care of potential memory
  overlaps. This is a generic equivalent of memmove.

  If an exception is thrown during the relocation, all the relocated elements
  are destroyed and [first, n) may contain valid but unspecified values,
  including moved-from values (basic exception safety).
*/
template<typename T, typename N>
void q_relocate_overlap_n(T *first, N n, T *d_first)
{
    static_assert(std::is_nothrow_destructible_v<T>,
                  "This algorithm requires that T has a non-throwing destructor");

    if (n == N(0) || first == d_first || first == nullptr || d_first == nullptr)
        return;

    if constexpr (QTypeInfo<T>::isRelocatable) {
        std::memmove(static_cast<void *>(d_first), static_cast<const void *>(first), n * sizeof(T));
    } else { // generic version has to be used
        if (d_first < first) {
            q_relocate_overlap_n_left_move(first, n, d_first);
        } else { // first < d_first
            auto rfirst = std::make_reverse_iterator(first + n);
            auto rd_first = std::make_reverse_iterator(d_first + n);
            q_relocate_overlap_n_left_move(rfirst, n, rd_first);
        }
    }
}

template <typename Iterator>
using IfIsInputIterator = typename std::enable_if<
    std::is_convertible<typename std::iterator_traits<Iterator>::iterator_category, std::input_iterator_tag>::value,
    bool>::type;

template <typename Iterator>
using IfIsForwardIterator = typename std::enable_if<
    std::is_convertible<typename std::iterator_traits<Iterator>::iterator_category, std::forward_iterator_tag>::value,
    bool>::type;

template <typename Iterator>
using IfIsNotForwardIterator = typename std::enable_if<
    !std::is_convertible<typename std::iterator_traits<Iterator>::iterator_category, std::forward_iterator_tag>::value,
    bool>::type;

template <typename Container,
          typename InputIterator,
          IfIsNotForwardIterator<InputIterator> = true>
void reserveIfForwardIterator(Container *, InputIterator, InputIterator)
{
}

template <typename Container,
          typename ForwardIterator,
          IfIsForwardIterator<ForwardIterator> = true>
void reserveIfForwardIterator(Container *c, ForwardIterator f, ForwardIterator l)
{
    c->reserve(static_cast<typename Container::size_type>(std::distance(f, l)));
}

template <typename Iterator, typename = std::void_t<>>
struct AssociativeIteratorHasKeyAndValue : std::false_type
{
};

template <typename Iterator>
struct AssociativeIteratorHasKeyAndValue<
        Iterator,
        std::void_t<decltype(std::declval<Iterator &>().key()),
                    decltype(std::declval<Iterator &>().value())>
    >
    : std::true_type
{
};

template <typename Iterator, typename = std::void_t<>, typename = std::void_t<>>
struct AssociativeIteratorHasFirstAndSecond : std::false_type
{
};

template <typename Iterator>
struct AssociativeIteratorHasFirstAndSecond<
        Iterator,
        std::void_t<decltype(std::declval<Iterator &>()->first),
                    decltype(std::declval<Iterator &>()->second)>
    >
    : std::true_type
{
};

template <typename Iterator>
using IfAssociativeIteratorHasKeyAndValue =
    typename std::enable_if<AssociativeIteratorHasKeyAndValue<Iterator>::value, bool>::type;

template <typename Iterator>
using IfAssociativeIteratorHasFirstAndSecond =
    typename std::enable_if<AssociativeIteratorHasFirstAndSecond<Iterator>::value, bool>::type;

template <typename T, typename U>
using IfIsNotSame =
    typename std::enable_if<!std::is_same<T, U>::value, bool>::type;

template<typename T, typename U>
using IfIsNotConvertible = typename std::enable_if<!std::is_convertible<T, U>::value, bool>::type;

template <typename Container, typename T>
auto sequential_erase(Container &c, const T &t)
{
    // avoid a detach in case there is nothing to remove
    const auto cbegin = c.cbegin();
    const auto cend = c.cend();
    const auto t_it = std::find(cbegin, cend, t);
    auto result = std::distance(cbegin, t_it);
    if (result == c.size())
        return result - result; // `0` of the right type

    const auto e = c.end();
    const auto it = std::remove(std::next(c.begin(), result), e, t);
    result = std::distance(it, e);
    c.erase(it, e);
    return result;
}

template <typename Container, typename T>
auto sequential_erase_with_copy(Container &c, const T &t)
{
    using CopyProxy = std::conditional_t<std::is_copy_constructible_v<T>, T, const T &>;
    const T &tCopy = CopyProxy(t);
    return sequential_erase(c, tCopy);
}

template <typename Container, typename T>
auto sequential_erase_one(Container &c, const T &t)
{
    const auto cend = c.cend();
    const auto it = std::find(c.cbegin(), cend, t);
    if (it == cend)
        return false;
    c.erase(it);
    return true;
}

template <typename Container, typename Predicate>
auto sequential_erase_if(Container &c, Predicate &pred)
{
    // avoid a detach in case there is nothing to remove
    const auto cbegin = c.cbegin();
    const auto cend = c.cend();
    const auto t_it = std::find_if(cbegin, cend, pred);
    auto result = std::distance(cbegin, t_it);
    if (result == c.size())
        return result - result; // `0` of the right type

    const auto e = c.end();
    const auto it = std::remove_if(std::next(c.begin(), result), e, pred);
    result = std::distance(it, e);
    c.erase(it, e);
    return result;
}

template <typename T, typename Predicate>
qsizetype qset_erase_if(QSet<T> &set, Predicate &pred)
{
    qsizetype result = 0;
    auto it = set.begin();
    const auto e = set.end();
    while (it != e) {
        if (pred(*it)) {
            ++result;
            it = set.erase(it);
        } else {
            ++it;
        }
    }
    return result;
}


// Prerequisite: F is invocable on ArgTypes
template <typename R, typename F, typename ... ArgTypes>
struct is_invoke_result_explicitly_convertible : std::is_constructible<R, std::invoke_result_t<F, ArgTypes...>>
{};

// is_invocable_r checks for implicit conversions, but we need to check
// for explicit conversions in remove_if. So, roll our own trait.
template <typename R, typename F, typename ... ArgTypes>
constexpr bool is_invocable_explicit_r_v = std::conjunction_v<
    std::is_invocable<F, ArgTypes...>,
    is_invoke_result_explicitly_convertible<R, F, ArgTypes...>
>;

template <typename Container, typename Predicate>
auto associative_erase_if(Container &c, Predicate &pred)
{
    // we support predicates callable with either Container::iterator
    // or with std::pair<const Key &, Value &>
    using Iterator = typename Container::iterator;
    using Key = typename Container::key_type;
    using Value = typename Container::mapped_type;
    using KeyValuePair = std::pair<const Key &, Value &>;

    typename Container::size_type result = 0;

    auto it = c.begin();
    const auto e = c.end();
    while (it != e) {
        if constexpr (is_invocable_explicit_r_v<bool, Predicate &, Iterator &>) {
            if (pred(it)) {
                it = c.erase(it);
                ++result;
            } else {
                ++it;
            }
        } else if constexpr (is_invocable_explicit_r_v<bool, Predicate &, KeyValuePair &&>) {
            KeyValuePair p(it.key(), it.value());
            if (pred(std::move(p))) {
                it = c.erase(it);
                ++result;
            } else {
                ++it;
            }
        } else {
            static_assert(sizeof(Container) == 0, "Predicate has an incompatible signature");
        }
    }

    return result;
}

} // namespace QtPrivate

QT_END_NAMESPACE

#endif // QCONTAINERTOOLS_IMPL_H
