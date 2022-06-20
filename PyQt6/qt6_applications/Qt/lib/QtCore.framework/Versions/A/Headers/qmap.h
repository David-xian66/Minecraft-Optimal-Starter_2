/****************************************************************************
**
** Copyright (C) 2020 Klarälvdalens Datakonsult AB, a KDAB Group company, info@kdab.com, author Giuseppe D'Angelo <giuseppe.dangelo@kdab.com>
** Copyright (C) 2016 The Qt Company Ltd.
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

#ifndef QMAP_H
#define QMAP_H

#include <QtCore/qiterator.h>
#include <QtCore/qlist.h>
#include <QtCore/qrefcount.h>
#include <QtCore/qpair.h>
#include <QtCore/qshareddata.h>
#include <QtCore/qshareddata_impl.h>

#include <functional>
#include <initializer_list>
#include <map>
#include <algorithm>

QT_BEGIN_NAMESPACE

// common code shared between QMap and QMultimap
template <typename AMap>
class QMapData : public QSharedData
{
public:
    using Map = AMap;
    using Key = typename Map::key_type;
    using T = typename Map::mapped_type;
    using value_type = typename Map::value_type;
    using size_type = typename Map::size_type;
    using iterator = typename Map::iterator;
    using const_iterator = typename Map::const_iterator;

    static_assert(std::is_nothrow_destructible_v<Key>, "Types with throwing destructors are not supported in Qt containers.");
    static_assert(std::is_nothrow_destructible_v<T>, "Types with throwing destructors are not supported in Qt containers.");

    Map m;

    QMapData() = default;
    explicit QMapData(const Map &other)
        : m(other)
    {}

    explicit QMapData(Map &&other)
        : m(std::move(other))
    {}

    // used in remove(); copies from source all the values not matching key.
    // returns how many were NOT copied (removed).
    size_type copyIfNotEquivalentTo(const Map &source, const Key &key)
    {
        Q_ASSERT(m.empty());

        size_type result = 0;
        const auto &keyCompare = source.key_comp();
        const auto filter = [&result, &key, &keyCompare](const auto &v)
        {
            if (!keyCompare(key, v.first) && !keyCompare(v.first, key)) {
                // keys are equivalent (neither a<b nor b<a) => found it
                ++result;
                return true;
            }
            return false;
        };

        std::remove_copy_if(source.cbegin(), source.cend(),
                            std::inserter(m, m.end()),
                            filter);
        return result;
    }

    // used in key(T), count(Key, T), find(key, T), etc; returns a
    // comparator object suitable for algorithms with std::(multi)map
    // iterators.
    static auto valueIsEqualTo(const T &value)
    {
        return [&value](const auto &v) { return v.second == value; };
    }

    Key key(const T &value, const Key &defaultKey) const
    {
        auto i = std::find_if(m.cbegin(),
                              m.cend(),
                              valueIsEqualTo(value));
        if (i != m.cend())
            return i->first;

        return defaultKey;
    }

    QList<Key> keys() const
    {
        QList<Key> result;
        result.reserve(m.size());

        const auto extractKey = [](const auto &v) { return v.first; };

        std::transform(m.cbegin(),
                       m.cend(),
                       std::back_inserter(result),
                       extractKey);
        return result;
    }

    QList<Key> keys(const T &value) const
    {
        QList<Key> result;
        result.reserve(m.size());
        // no std::transform_if...
        for (const auto &v : m) {
            if (v.second == value)
                result.append(v.first);
        }
        result.shrink_to_fit();
        return result;
    }

    QList<T> values() const
    {
        QList<T> result;
        result.reserve(m.size());

        const auto extractValue = [](const auto &v) { return v.second; };

        std::transform(m.cbegin(),
                       m.cend(),
                       std::back_inserter(result),
                       extractValue);
        return result;
    }

    size_type count(const Key &key) const
    {
        return m.count(key);
    }

    // Used in erase. Allocates a new QMapData and copies, from this->m,
    // the elements not in the [first, last) range. The return contains
    // the new QMapData and an iterator in its map pointing at the first
    // element after the erase.
    struct EraseResult {
        QMapData *data;
        iterator it;
    };

    EraseResult erase(const_iterator first, const_iterator last) const
    {
        EraseResult result;
        result.data = new QMapData;
        result.it = result.data->m.end();
        const auto newDataEnd = result.it;

        auto i = m.begin();
        const auto e = m.end();

        // copy over all the elements before first
        while (i != first) {
            result.it = result.data->m.insert(newDataEnd, *i);
            ++i;
        }

        // skip until last
        while (i != last)
            ++i;

        // copy from last to the end
        while (i != e) {
            result.data->m.insert(newDataEnd, *i);
            ++i;
        }

        if (result.it != newDataEnd)
            ++result.it;

        return result;
    }
};

//
// QMap
//

template <class Key, class T>
class QMap
{
    using Map = std::map<Key, T>;
    using MapData = QMapData<Map>;
    QtPrivate::QExplicitlySharedDataPointerV2<MapData> d;

    friend class QMultiMap<Key, T>;

public:
    using key_type = Key;
    using mapped_type = T;
    using difference_type = qptrdiff;
    using size_type = qsizetype;

    QMap() = default;

    // implicitly generated special member functions are OK!

    void swap(QMap<Key, T> &other) noexcept
    {
        qSwap(d, other.d);
    }

    QMap(std::initializer_list<std::pair<Key, T>> list)
    {
        for (auto &p : list)
            insert(p.first, p.second);
    }

    explicit QMap(const std::map<Key, T> &other)
        : d(other.empty() ? nullptr : new MapData(other))
    {
    }

    explicit QMap(std::map<Key, T> &&other)
        : d(other.empty() ? nullptr : new MapData(std::move(other)))
    {
    }

    std::map<Key, T> toStdMap() const &
    {
        if (d)
            return d->m;
        return {};
    }

    std::map<Key, T> toStdMap() &&
    {
        if (d) {
            if (d.isShared())
                return d->m;
            else
                return std::move(d->m);
        }

        return {};
    }

    template <typename AKey = Key, typename AT = T> friend
    QTypeTraits::compare_eq_result<AKey, AT> operator==(const QMap &lhs, const QMap &rhs)
    {
        if (lhs.d == rhs.d)
            return true;
        if (!lhs.d)
            return rhs == lhs;
        Q_ASSERT(lhs.d);
        return rhs.d ? (lhs.d->m == rhs.d->m) : lhs.d->m.empty();
    }

    template <typename AKey = Key, typename AT = T> friend
    QTypeTraits::compare_eq_result<AKey, AT> operator!=(const QMap &lhs, const QMap &rhs)
    {
        return !(lhs == rhs);
    }
    // TODO: add the other comparison operators; std::map has them.

    size_type size() const { return d ? size_type(d->m.size()) : size_type(0); }

    bool isEmpty() const { return d ? d->m.empty() : true; }

    void detach()
    {
        if (d)
            d.detach();
        else
            d.reset(new MapData);
    }

    bool isDetached() const noexcept
    {
        return d ? !d.isShared() : false; // false makes little sense, but that's shared_null's behavior...
    }

    bool isSharedWith(const QMap<Key, T> &other) const noexcept
    {
        return d == other.d; // also this makes little sense?
    }

    void clear()
    {
        if (!d)
            return;

        if (!d.isShared())
            d->m.clear();
        else
            d.reset();
    }

    size_type remove(const Key &key)
    {
        if (!d)
            return 0;

        if (!d.isShared())
            return size_type(d->m.erase(key));

        MapData *newData = new MapData;
        size_type result = newData->copyIfNotEquivalentTo(d->m, key);

        d.reset(newData);

        return result;
    }

    template <typename Predicate>
    size_type removeIf(Predicate pred)
    {
        return QtPrivate::associative_erase_if(*this, pred);
    }

    T take(const Key &key)
    {
        if (!d)
            return T();

        // TODO: improve. There is no need of copying all the
        // elements (the one to be removed can be skipped).
        detach();

        auto i = d->m.find(key);
        if (i != d->m.end()) {
            T result(std::move(i->second));
            d->m.erase(i);
            return result;
        }
        return T();
    }

    bool contains(const Key &key) const
    {
        if (!d)
            return false;
        auto i = d->m.find(key);
        return i != d->m.end();
    }

    Key key(const T &value, const Key &defaultKey = Key()) const
    {
        if (!d)
            return defaultKey;

        return d->key(value, defaultKey);
    }

    T value(const Key &key, const T &defaultValue = T()) const
    {
        if (!d)
            return defaultValue;
        const auto i = d->m.find(key);
        if (i != d->m.cend())
            return i->second;
        return defaultValue;
    }

    T &operator[](const Key &key)
    {
        detach();
        auto i = d->m.find(key);
        if (i == d->m.end())
            i = d->m.insert({key, T()}).first;
        return i->second;
    }

    // CHANGE: return T, not const T!
    T operator[](const Key &key) const
    {
        return value(key);
    }

    QList<Key> keys() const
    {
        if (!d)
            return {};
        return d->keys();
    }

    QList<Key> keys(const T &value) const
    {
        if (!d)
            return {};
        return d->keys(value);
    }

    QList<T> values() const
    {
        if (!d)
            return {};
        return d->values();
    }

    size_type count(const Key &key) const
    {
        if (!d)
            return 0;
        return d->count(key);
    }

    size_type count() const
    {
        return size();
    }

    inline const Key &firstKey() const { Q_ASSERT(!isEmpty()); return constBegin().key(); }
    inline const Key &lastKey() const { Q_ASSERT(!isEmpty()); return (--constEnd()).key(); }

    inline T &first() { Q_ASSERT(!isEmpty()); return *begin(); }
    inline const T &first() const { Q_ASSERT(!isEmpty()); return *constBegin(); }
    inline T &last() { Q_ASSERT(!isEmpty()); return *(--end()); }
    inline const T &last() const { Q_ASSERT(!isEmpty()); return *(--constEnd()); }

    class const_iterator;

    class iterator
    {
        friend class QMap<Key, T>;
        friend class const_iterator;

        typename Map::iterator i;
        explicit iterator(typename Map::iterator it) : i(it) {}
    public:
        using iterator_category = std::bidirectional_iterator_tag;
        using difference_type = qptrdiff;
        using value_type = T;
        using pointer = T *;
        using reference = T &;

        iterator() = default;

        const Key &key() const { return i->first; }
        T &value() const { return i->second; }
        T &operator*() const { return i->second; }
        T *operator->() const { return &i->second; }
        friend bool operator==(const iterator &lhs, const iterator &rhs) { return lhs.i == rhs.i; }
        friend bool operator!=(const iterator &lhs, const iterator &rhs) { return lhs.i != rhs.i; }

        iterator &operator++()
        {
            ++i;
            return *this;
        }
        iterator operator++(int)
        {
            iterator r = *this;
            ++i;
            return r;
        }
        iterator &operator--()
        {
            --i;
            return *this;
        }
        iterator operator--(int)
        {
            iterator r = *this;
            --i;
            return r;
        }
    };

    class const_iterator
    {
        friend class QMap<Key, T>;
        typename Map::const_iterator i;
        explicit const_iterator(typename Map::const_iterator it) : i(it) {}

    public:
        using iterator_category = std::bidirectional_iterator_tag;
        using difference_type = qptrdiff;
        using value_type = T;
        using pointer = const T *;
        using reference = const T &;

        const_iterator() = default;
        Q_IMPLICIT const_iterator(const iterator &o) : i(o.i) {}

        const Key &key() const { return i->first; }
        const T &value() const { return i->second; }
        const T &operator*() const { return i->second; }
        const T *operator->() const { return &i->second; }
        friend bool operator==(const const_iterator &lhs, const const_iterator &rhs) { return lhs.i == rhs.i; }
        friend bool operator!=(const const_iterator &lhs, const const_iterator &rhs) { return lhs.i != rhs.i; }

        const_iterator &operator++()
        {
            ++i;
            return *this;
        }
        const_iterator operator++(int)
        {
            const_iterator r = *this;
            ++i;
            return r;
        }
        const_iterator &operator--()
        {
            --i;
            return *this;
        }
        const_iterator operator--(int)
        {
            const_iterator r = *this;
            --i;
            return r;
        }
    };

    class key_iterator
    {
        const_iterator i;

    public:
        typedef typename const_iterator::iterator_category iterator_category;
        typedef typename const_iterator::difference_type difference_type;
        typedef Key value_type;
        typedef const Key *pointer;
        typedef const Key &reference;

        key_iterator() = default;
        explicit key_iterator(const_iterator o) : i(o) { }

        const Key &operator*() const { return i.key(); }
        const Key *operator->() const { return &i.key(); }
        bool operator==(key_iterator o) const { return i == o.i; }
        bool operator!=(key_iterator o) const { return i != o.i; }

        inline key_iterator &operator++() { ++i; return *this; }
        inline key_iterator operator++(int) { return key_iterator(i++);}
        inline key_iterator &operator--() { --i; return *this; }
        inline key_iterator operator--(int) { return key_iterator(i--); }
        const_iterator base() const { return i; }
    };

    typedef QKeyValueIterator<const Key&, const T&, const_iterator> const_key_value_iterator;
    typedef QKeyValueIterator<const Key&, T&, iterator> key_value_iterator;

    // STL style
    iterator begin() { detach(); return iterator(d->m.begin()); }
    const_iterator begin() const { if (!d) return const_iterator(); return const_iterator(d->m.cbegin()); }
    const_iterator constBegin() const { return begin(); }
    const_iterator cbegin() const { return begin(); }
    iterator end() { detach(); return iterator(d->m.end()); }
    const_iterator end() const { if (!d) return const_iterator(); return const_iterator(d->m.end()); }
    const_iterator constEnd() const { return end(); }
    const_iterator cend() const { return end(); }
    key_iterator keyBegin() const { return key_iterator(begin()); }
    key_iterator keyEnd() const { return key_iterator(end()); }
    key_value_iterator keyValueBegin() { return key_value_iterator(begin()); }
    key_value_iterator keyValueEnd() { return key_value_iterator(end()); }
    const_key_value_iterator keyValueBegin() const { return const_key_value_iterator(begin()); }
    const_key_value_iterator constKeyValueBegin() const { return const_key_value_iterator(begin()); }
    const_key_value_iterator keyValueEnd() const { return const_key_value_iterator(end()); }
    const_key_value_iterator constKeyValueEnd() const { return const_key_value_iterator(end()); }

    iterator erase(const_iterator it)
    {
        return erase(it, std::next(it));
    }

    iterator erase(const_iterator afirst, const_iterator alast)
    {
        if (!d)
            return iterator();

        if (!d.isShared())
            return iterator(d->m.erase(afirst.i, alast.i));

        auto result = d->erase(afirst.i, alast.i);
        d.reset(result.data);
        return iterator(result.it);
    }

    // more Qt
    typedef iterator Iterator;
    typedef const_iterator ConstIterator;

    iterator find(const Key &key)
    {
        detach();
        return iterator(d->m.find(key));
    }

    const_iterator find(const Key &key) const
    {
        if (!d)
            return const_iterator();
        return const_iterator(d->m.find(key));
    }

    const_iterator constFind(const Key &key) const
    {
        return find(key);
    }

    iterator lowerBound(const Key &key)
    {
        detach();
        return iterator(d->m.lower_bound(key));
    }

    const_iterator lowerBound(const Key &key) const
    {
        if (!d)
            return const_iterator();
        return const_iterator(d->m.lower_bound(key));
    }

    iterator upperBound(const Key &key)
    {
        detach();
        return iterator(d->m.upper_bound(key));
    }

    const_iterator upperBound(const Key &key) const
    {
        if (!d)
            return const_iterator();
        return const_iterator(d->m.upper_bound(key));
    }

    iterator insert(const Key &key, const T &value)
    {
        // TODO: improve. In case of assignment, why copying first?
        detach();
        return iterator(d->m.insert_or_assign(key, value).first);
    }

    iterator insert(const_iterator pos, const Key &key, const T &value)
    {
        // TODO: improve. In case of assignment, why copying first?
        auto posDistance = d ? std::distance(d->m.cbegin(), pos.i) : 0;
        detach();
        auto detachedPos = std::next(d->m.cbegin(), posDistance);
        return iterator(d->m.insert_or_assign(detachedPos, key, value));
    }

    void insert(const QMap<Key, T> &map)
    {
        // TODO: improve. In case of assignment, why copying first?
        if (map.isEmpty())
            return;

        detach();

#ifdef __cpp_lib_node_extract
        auto copy = map.d->m;
        copy.merge(std::move(d->m));
        d->m = std::move(copy);
#else
        // this is a std::copy, but we can't use std::inserter (need insert_or_assign...).
        // copy in reverse order, trying to make effective use of insertionHint.
        auto insertionHint = d->m.end();
        auto mapIt = map.d->m.crbegin();
        auto end = map.d->m.crend();
        for (; mapIt != end; ++mapIt)
            insertionHint = d->m.insert_or_assign(insertionHint, mapIt->first, mapIt->second);
#endif
    }

    void insert(QMap<Key, T> &&map)
    {
        if (!map.d || map.d->m.empty())
            return;

        if (map.d.isShared()) {
            // fall back to a regular copy
            insert(map);
            return;
        }

        detach();

#ifdef __cpp_lib_node_extract
        map.d->m.merge(std::move(d->m));
        *this = std::move(map);
#else
        // same as above
        auto insertionHint = d->m.end();
        auto mapIt = map.d->m.crbegin();
        auto end = map.d->m.crend();
        for (; mapIt != end; ++mapIt)
            insertionHint = d->m.insert_or_assign(insertionHint, std::move(mapIt->first), std::move(mapIt->second));
#endif
    }

    // STL compatibility
    inline bool empty() const
    {
        return isEmpty();
    }

    QPair<iterator, iterator> equal_range(const Key &akey)
    {
        detach();
        auto result = d->m.equal_range(akey);
        return {iterator(result.first), iterator(result.second)};
    }

    QPair<const_iterator, const_iterator> equal_range(const Key &akey) const
    {
        if (!d)
            return {};
        auto result = d->m.equal_range(akey);
        return {const_iterator(result.first), const_iterator(result.second)};
    }
};

Q_DECLARE_ASSOCIATIVE_ITERATOR(Map)
Q_DECLARE_MUTABLE_ASSOCIATIVE_ITERATOR(Map)

template <typename Key, typename T, typename Predicate>
qsizetype erase_if(QMap<Key, T> &map, Predicate pred)
{
    return QtPrivate::associative_erase_if(map, pred);
}

//
// QMultiMap
//

template <class Key, class T>
class QMultiMap
{
    using Map = std::multimap<Key, T>;
    using MapData = QMapData<Map>;
    QtPrivate::QExplicitlySharedDataPointerV2<MapData> d;

public:
    using key_type = Key;
    using mapped_type = T;
    using difference_type = qptrdiff;
    using size_type = qsizetype;

    QMultiMap() = default;

    // implicitly generated special member functions are OK!

    QMultiMap(std::initializer_list<std::pair<Key,T>> list)
    {
        for (auto &p : list)
            insert(p.first, p.second);
    }

    void swap(QMultiMap<Key, T> &other) noexcept
    {
        qSwap(d, other.d);
    }

    explicit QMultiMap(const QMap<Key, T> &other)
        : d(other.isEmpty() ? nullptr : new MapData)
    {
        if (d) {
            Q_ASSERT(other.d);
            d->m.insert(other.d->m.begin(),
                        other.d->m.end());
        }
    }

    explicit QMultiMap(QMap<Key, T> &&other)
        : d(other.isEmpty() ? nullptr : new MapData)
    {
        if (d) {
            Q_ASSERT(other.d);
            if (other.d.isShared()) {
                d->m.insert(other.d->m.begin(),
                            other.d->m.end());
            } else {
#ifdef __cpp_lib_node_extract
                d->m.merge(std::move(other.d->m));
#else
                d->m.insert(std::make_move_iterator(other.d->m.begin()),
                            std::make_move_iterator(other.d->m.end()));
#endif
            }
        }
    }

    explicit QMultiMap(const std::multimap<Key, T> &other)
        : d(other.empty() ? nullptr : new MapData(other))
    {
    }

    explicit QMultiMap(std::multimap<Key, T> &&other)
        : d(other.empty() ? nullptr : new MapData(std::move(other)))
    {
    }

    // CHANGE: return type
    Q_DECL_DEPRECATED_X("Use toStdMultiMap instead")
    std::multimap<Key, T> toStdMap() const
    {
        return toStdMultiMap();
    }

    std::multimap<Key, T> toStdMultiMap() const &
    {
        if (d)
            return d->m;
        return {};
    }

    std::multimap<Key, T> toStdMultiMap() &&
    {
        if (d) {
            if (d.isShared())
                return d->m;
            else
                return std::move(d->m);
        }

        return {};
    }

    template <typename AKey = Key, typename AT = T> friend
    QTypeTraits::compare_eq_result<AKey, AT> operator==(const QMultiMap &lhs, const QMultiMap &rhs)
    {
        if (lhs.d == rhs.d)
            return true;
        if (!lhs.d)
            return rhs == lhs;
        Q_ASSERT(lhs.d);
        return rhs.d ? (lhs.d->m == rhs.d->m) : lhs.d->m.empty();
    }

    template <typename AKey = Key, typename AT = T> friend
    QTypeTraits::compare_eq_result<AKey, AT> operator!=(const QMultiMap &lhs, const QMultiMap &rhs)
    {
        return !(lhs == rhs);
    }
    // TODO: add the other comparison operators; std::multimap has them.

    size_type size() const { return d ? size_type(d->m.size()) : size_type(0); }

    bool isEmpty() const { return d ? d->m.empty() : true; }

    void detach()
    {
        if (d)
            d.detach();
        else
            d.reset(new MapData);
    }

    bool isDetached() const noexcept
    {
        return d ? !d.isShared() : false; // false makes little sense, but that's shared_null's behavior...
    }

    bool isSharedWith(const QMultiMap<Key, T> &other) const noexcept
    {
        return d == other.d; // also this makes little sense?
    }

    void clear()
    {
        if (!d)
            return;

        if (!d.isShared())
            d->m.clear();
        else
            d.reset();
    }

    size_type remove(const Key &key)
    {
        if (!d)
            return 0;

        if (!d.isShared())
            return size_type(d->m.erase(key));

        MapData *newData = new MapData;
        size_type result = newData->copyIfNotEquivalentTo(d->m, key);

        d.reset(newData);

        return result;
    }

    size_type remove(const Key &key, const T &value)
    {
        if (!d)
            return 0;

        // TODO: improve. Copy over only the elements not to be removed.
        detach();

        // key and value may belong to this map. As such, we need to copy
        // them to ensure they stay valid througout the iteration below
        // (which may destroy them)
        const Key keyCopy = key;
        const T valueCopy = value;

        size_type result = 0;
        const auto &keyCompare = d->m.key_comp();

        auto i = d->m.find(keyCopy);
        const auto e = d->m.end();

        while (i != e && !keyCompare(keyCopy, i->first)) {
            if (i->second == valueCopy) {
                i = d->m.erase(i);
                ++result;
            } else {
                ++i;
            }
        }

        return result;
    }

    template <typename Predicate>
    size_type removeIf(Predicate pred)
    {
        return QtPrivate::associative_erase_if(*this, pred);
    }

    T take(const Key &key)
    {
        if (!d)
            return T();

        // TODO: improve. There is no need of copying all the
        // elements (the one to be removed can be skipped).
        detach();

        auto i = d->m.find(key);
        if (i != d->m.end()) {
            T result(std::move(i->second));
            d->m.erase(i);
            return result;
        }
        return T();
    }

    bool contains(const Key &key) const
    {
        if (!d)
            return false;
        auto i = d->m.find(key);
        return i != d->m.end();
    }

    bool contains(const Key &key, const T &value) const
    {
        return find(key, value) != end();
    }

    Key key(const T &value, const Key &defaultKey = Key()) const
    {
        if (!d)
            return defaultKey;

        return d->key(value, defaultKey);
    }

    T value(const Key &key, const T &defaultValue = T()) const
    {
        if (!d)
            return defaultValue;
        const auto i = d->m.find(key);
        if (i != d->m.cend())
            return i->second;
        return defaultValue;
    }

    QList<Key> keys() const
    {
        if (!d)
            return {};
        return d->keys();
    }

    QList<Key> keys(const T &value) const
    {
        if (!d)
            return {};
        return d->keys(value);
    }

    QList<Key> uniqueKeys() const
    {
        QList<Key> result;
        if (!d)
            return result;

        result.reserve(size());

        std::unique_copy(keyBegin(), keyEnd(),
                         std::back_inserter(result));

        result.shrink_to_fit();
        return result;
    }

    QList<T> values() const
    {
        if (!d)
            return {};
        return d->values();
    }

    QList<T> values(const Key &key) const
    {
        QList<T> result;
        const auto range = equal_range(key);
        result.reserve(std::distance(range.first, range.second));
        std::copy(range.first, range.second, std::back_inserter(result));
        return result;
    }

    size_type count(const Key &key) const
    {
        if (!d)
            return 0;
        return d->count(key);
    }

    size_type count(const Key &key, const T &value) const
    {
        if (!d)
            return 0;

        // TODO: improve; no need of scanning the equal_range twice.
        auto range = d->m.equal_range(key);

        return size_type(std::count_if(range.first,
                                       range.second,
                                       MapData::valueIsEqualTo(value)));
    }

    inline const Key &firstKey() const { Q_ASSERT(!isEmpty()); return constBegin().key(); }
    inline const Key &lastKey() const { Q_ASSERT(!isEmpty()); return std::next(constEnd(), -1).key(); }

    inline T &first() { Q_ASSERT(!isEmpty()); return *begin(); }
    inline const T &first() const { Q_ASSERT(!isEmpty()); return *constBegin(); }
    inline T &last() { Q_ASSERT(!isEmpty()); return *std::next(end(), -1); }
    inline const T &last() const { Q_ASSERT(!isEmpty()); return *std::next(constEnd(), -1); }

    class const_iterator;

    class iterator
    {
        friend class QMultiMap<Key, T>;
        friend class const_iterator;

        typename Map::iterator i;
        explicit iterator(typename Map::iterator it) : i(it) {}
    public:
        using iterator_category = std::bidirectional_iterator_tag;
        using difference_type = qptrdiff;
        using value_type = T;
        using pointer = T *;
        using reference = T &;

        iterator() = default;

        const Key &key() const { return i->first; }
        T &value() const { return i->second; }
        T &operator*() const { return i->second; }
        T *operator->() const { return &i->second; }
        friend bool operator==(const iterator &lhs, const iterator &rhs) { return lhs.i == rhs.i; }
        friend bool operator!=(const iterator &lhs, const iterator &rhs) { return lhs.i != rhs.i; }

        iterator &operator++()
        {
            ++i;
            return *this;
        }
        iterator operator++(int)
        {
            iterator r = *this;
            ++i;
            return r;
        }
        iterator &operator--()
        {
            --i;
            return *this;
        }
        iterator operator--(int)
        {
            iterator r = *this;
            --i;
            return r;
        }
    };

    class const_iterator
    {
        friend class QMultiMap<Key, T>;
        typename Map::const_iterator i;
        explicit const_iterator(typename Map::const_iterator it) : i(it) {}

    public:
        using iterator_category = std::bidirectional_iterator_tag;
        using difference_type = qptrdiff;
        using value_type = T;
        using pointer = const T *;
        using reference = const T &;

        const_iterator() = default;
        Q_IMPLICIT const_iterator(const iterator &o) : i(o.i) {}

        const Key &key() const { return i->first; }
        const T &value() const { return i->second; }
        const T &operator*() const { return i->second; }
        const T *operator->() const { return &i->second; }
        friend bool operator==(const const_iterator &lhs, const const_iterator &rhs) { return lhs.i == rhs.i; }
        friend bool operator!=(const const_iterator &lhs, const const_iterator &rhs) { return lhs.i != rhs.i; }

        const_iterator &operator++()
        {
            ++i;
            return *this;
        }
        const_iterator operator++(int)
        {
            const_iterator r = *this;
            ++i;
            return r;
        }
        const_iterator &operator--()
        {
            --i;
            return *this;
        }
        const_iterator operator--(int)
        {
            const_iterator r = *this;
            --i;
            return r;
        }
    };

    class key_iterator
    {
        const_iterator i;

    public:
        typedef typename const_iterator::iterator_category iterator_category;
        typedef typename const_iterator::difference_type difference_type;
        typedef Key value_type;
        typedef const Key *pointer;
        typedef const Key &reference;

        key_iterator() = default;
        explicit key_iterator(const_iterator o) : i(o) { }

        const Key &operator*() const { return i.key(); }
        const Key *operator->() const { return &i.key(); }
        bool operator==(key_iterator o) const { return i == o.i; }
        bool operator!=(key_iterator o) const { return i != o.i; }

        inline key_iterator &operator++() { ++i; return *this; }
        inline key_iterator operator++(int) { return key_iterator(i++);}
        inline key_iterator &operator--() { --i; return *this; }
        inline key_iterator operator--(int) { return key_iterator(i--); }
        const_iterator base() const { return i; }
    };

    typedef QKeyValueIterator<const Key&, const T&, const_iterator> const_key_value_iterator;
    typedef QKeyValueIterator<const Key&, T&, iterator> key_value_iterator;

    // STL style
    iterator begin() { detach(); return iterator(d->m.begin()); }
    const_iterator begin() const { if (!d) return const_iterator(); return const_iterator(d->m.cbegin()); }
    const_iterator constBegin() const { return begin(); }
    const_iterator cbegin() const { return begin(); }
    iterator end() { detach(); return iterator(d->m.end()); }
    const_iterator end() const { if (!d) return const_iterator(); return const_iterator(d->m.end()); }
    const_iterator constEnd() const { return end(); }
    const_iterator cend() const { return end(); }
    key_iterator keyBegin() const { return key_iterator(begin()); }
    key_iterator keyEnd() const { return key_iterator(end()); }
    key_value_iterator keyValueBegin() { return key_value_iterator(begin()); }
    key_value_iterator keyValueEnd() { return key_value_iterator(end()); }
    const_key_value_iterator keyValueBegin() const { return const_key_value_iterator(begin()); }
    const_key_value_iterator constKeyValueBegin() const { return const_key_value_iterator(begin()); }
    const_key_value_iterator keyValueEnd() const { return const_key_value_iterator(end()); }
    const_key_value_iterator constKeyValueEnd() const { return const_key_value_iterator(end()); }

    iterator erase(const_iterator it)
    {
        return erase(it, std::next(it));
    }

    iterator erase(const_iterator afirst, const_iterator alast)
    {
        if (!d)
            return iterator();

        if (!d.isShared())
            return iterator(d->m.erase(afirst.i, alast.i));

        auto result = d->erase(afirst.i, alast.i);
        d.reset(result.data);
        return iterator(result.it);
    }

    // more Qt
    typedef iterator Iterator;
    typedef const_iterator ConstIterator;

    size_type count() const
    {
        return size();
    }

    iterator find(const Key &key)
    {
        detach();
        return iterator(d->m.find(key));
    }

    const_iterator find(const Key &key) const
    {
        if (!d)
            return const_iterator();
        return const_iterator(d->m.find(key));
    }

    const_iterator constFind(const Key &key) const
    {
        return find(key);
    }

    iterator find(const Key &key, const T &value)
    {
        detach();

        auto range = d->m.equal_range(key);
        auto i = std::find_if(range.first, range.second,
                              MapData::valueIsEqualTo(value));

        if (i != range.second)
            return iterator(i);
        return iterator(d->m.end());
    }

    const_iterator find(const Key &key, const T &value) const
    {
        if (!d)
            return const_iterator();

        auto range = d->m.equal_range(key);
        auto i = std::find_if(range.first, range.second,
                              MapData::valueIsEqualTo(value));

        if (i != range.second)
            return const_iterator(i);
        return const_iterator(d->m.end());
    }

    const_iterator constFind(const Key &key, const T &value) const
    {
        return find(key, value);
    }

    iterator lowerBound(const Key &key)
    {
        detach();
        return iterator(d->m.lower_bound(key));
    }

    const_iterator lowerBound(const Key &key) const
    {
        if (!d)
            return const_iterator();
        return const_iterator(d->m.lower_bound(key));
    }

    iterator upperBound(const Key &key)
    {
        detach();
        return iterator(d->m.upper_bound(key));
    }

    const_iterator upperBound(const Key &key) const
    {
        if (!d)
            return const_iterator();
        return const_iterator(d->m.upper_bound(key));
    }

    iterator insert(const Key &key, const T &value)
    {
        detach();
        // note that std::multimap inserts at the end of an equal_range for a key,
        // QMultiMap at the beginning.
        auto i = d->m.lower_bound(key);
        return iterator(d->m.insert(i, {key, value}));
    }

    iterator insert(const_iterator pos, const Key &key, const T &value)
    {
        auto posDistance = d ? std::distance(d->m.cbegin(), pos.i) : 0;
        detach();
        auto detachedPos = std::next(d->m.cbegin(), posDistance);
        return iterator(d->m.insert(detachedPos, {key, value}));
    }

#if QT_DEPRECATED_SINCE(6, 0)
    QT_DEPRECATED_VERSION_X_6_0("Use insert() instead")
    iterator insertMulti(const Key &key, const T &value)
    {
        return insert(key, value);
    }
    QT_DEPRECATED_VERSION_X_6_0("Use insert() instead")
    iterator insertMulti(const_iterator pos, const Key &key, const T &value)
    {
        return insert(pos, key, value);
    }

    QT_DEPRECATED_VERSION_X_6_0("Use unite() instead")
    void insert(const QMultiMap<Key, T> &map)
    {
        unite(map);
    }

    QT_DEPRECATED_VERSION_X_6_0("Use unite() instead")
    void insert(QMultiMap<Key, T> &&map)
    {
        unite(std::move(map));
    }
#endif

    iterator replace(const Key &key, const T &value)
    {
        // TODO: improve. No need of copying and then overwriting.
        detach();

        // Similarly, improve here (e.g. lower_bound and hinted insert);
        // there's no insert_or_assign on multimaps
        auto i = d->m.find(key);
        if (i != d->m.end())
            i->second = value;
        else
            i = d->m.insert({key, value});

        return iterator(i);
    }

    // STL compatibility
    inline bool empty() const { return isEmpty(); }

    QPair<iterator, iterator> equal_range(const Key &akey)
    {
        detach();
        auto result = d->m.equal_range(akey);
        return {iterator(result.first), iterator(result.second)};
    }

    QPair<const_iterator, const_iterator> equal_range(const Key &akey) const
    {
        if (!d)
            return {};
        auto result = d->m.equal_range(akey);
        return {const_iterator(result.first), const_iterator(result.second)};
    }

    QMultiMap &unite(const QMultiMap &other)
    {
        if (other.isEmpty())
            return *this;

        detach();

        auto copy = other.d->m;
#ifdef __cpp_lib_node_extract
        copy.merge(std::move(d->m));
#else
        copy.insert(std::make_move_iterator(d->m.begin()),
                    std::make_move_iterator(d->m.end()));
#endif
        d->m = std::move(copy);
        return *this;
    }

    QMultiMap &unite(QMultiMap<Key, T> &&other)
    {
        if (!other.d || other.d->m.empty())
            return *this;

        if (other.d.isShared()) {
            // fall back to a regular copy
            unite(other);
            return *this;
        }

        detach();

#ifdef __cpp_lib_node_extract
        other.d->m.merge(std::move(d->m));
#else
        other.d->m.insert(std::make_move_iterator(d->m.begin()),
                          std::make_move_iterator(d->m.end()));
#endif
        *this = std::move(other);
        return *this;
    }
};

Q_DECLARE_ASSOCIATIVE_ITERATOR(MultiMap)
Q_DECLARE_MUTABLE_ASSOCIATIVE_ITERATOR(MultiMap)

template <typename Key, typename T>
QMultiMap<Key, T> operator+(const QMultiMap<Key, T> &lhs, const QMultiMap<Key, T> &rhs)
{
    auto result = lhs;
    result += rhs;
    return result;
}

template <typename Key, typename T>
QMultiMap<Key, T> operator+=(QMultiMap<Key, T> &lhs, const QMultiMap<Key, T> &rhs)
{
    return lhs.unite(rhs);
}

template <typename Key, typename T, typename Predicate>
qsizetype erase_if(QMultiMap<Key, T> &map, Predicate pred)
{
    return QtPrivate::associative_erase_if(map, pred);
}

QT_END_NAMESPACE

#endif // QMAP_H
