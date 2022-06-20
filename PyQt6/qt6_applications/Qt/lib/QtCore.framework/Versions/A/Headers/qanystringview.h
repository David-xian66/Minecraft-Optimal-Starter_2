/****************************************************************************
**
** Copyright (C) 2020 Klarälvdalens Datakonsult AB, a KDAB Group company, info@kdab.com, author Marc Mutz <marc.mutz@kdab.com>
** Contact: http://www.qt.io/licensing/
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
#ifndef QANYSTRINGVIEW_H
#define QANYSTRINGVIEW_H

#include <QtCore/qstringview.h>
#include <QtCore/qutf8stringview.h>

#ifdef __cpp_impl_three_way_comparison
#include <compare>
#endif
#include <limits>

QT_BEGIN_NAMESPACE

template <typename, typename> class QStringBuilder;

class QAnyStringView
{
public:
    typedef qptrdiff difference_type;
    typedef qsizetype size_type;
private:
    template <typename Char>
    using if_compatible_char = std::enable_if_t<std::disjunction_v<
        QtPrivate::IsCompatibleCharType<Char>,
        QtPrivate::IsCompatibleChar8Type<Char>
    >, bool>;

    template <typename Pointer>
    using if_compatible_pointer = std::enable_if_t<std::disjunction_v<
        QtPrivate::IsCompatiblePointer<Pointer>,
        QtPrivate::IsCompatiblePointer8<Pointer>
    >, bool>;


    template <typename T>
    using if_compatible_container = std::enable_if_t<std::disjunction_v<
        QtPrivate::IsContainerCompatibleWithQStringView<T>,
        QtPrivate::IsContainerCompatibleWithQUtf8StringView<T>
    >, bool>;

    // confirm we don't make an accidental copy constructor:
    static_assert(QtPrivate::IsContainerCompatibleWithQStringView<QAnyStringView>::value == false);
    static_assert(QtPrivate::IsContainerCompatibleWithQUtf8StringView<QAnyStringView>::value == false);

    template <typename Char>
    static constexpr std::size_t encodeType(qsizetype sz) noexcept
    {
        // only deals with Utf8 and Utf16 - there's only one way to create
        // a Latin1 string, and that ctor deals with the tag itself
        Q_ASSERT(sz >= 0);
        Q_ASSERT(sz <= qsizetype(SizeMask));
        return std::size_t(sz) | uint(sizeof(Char) == sizeof(char16_t)) * Tag::Utf16;
    }

    template <typename Char>
    static qsizetype lengthHelperPointer(const Char *str) noexcept
    {
#if defined(Q_CC_GNU) && !defined(Q_CC_CLANG) && !defined(Q_CC_INTEL)
        if (__builtin_constant_p(*str)) {
            qsizetype result = 0;
            while (*str++ != u'\0')
                ++result;
            return result;
        }
#endif
        if constexpr (sizeof(Char) == sizeof(char16_t))
            return QtPrivate::qustrlen(reinterpret_cast<const char16_t*>(str));
        else
            return qsizetype(strlen(reinterpret_cast<const char*>(str)));
    }

    template <typename Container>
    static constexpr qsizetype lengthHelperContainer(const Container &c) noexcept
    {
        return qsizetype(std::size(c));
    }

    template <typename Char, size_t N>
    static constexpr qsizetype lengthHelperContainer(const Char (&str)[N]) noexcept
    {
        const auto it = std::char_traits<Char>::find(str, N, Char(0));
        const auto end = it ? it : std::next(str, N);
        return qsizetype(std::distance(str, end));
    }

    static QChar toQChar(char ch) noexcept { return toQChar(QLatin1Char{ch}); } // we don't handle UTF-8 multibytes
    static QChar toQChar(QChar ch) noexcept { return ch; }
    static QChar toQChar(QLatin1Char ch) noexcept { return ch; }

    explicit constexpr QAnyStringView(const void *d, qsizetype n, std::size_t sizeAndType) noexcept
        : m_data{d}, m_size{std::size_t(n) | (sizeAndType & TypeMask)} {}
public:
    constexpr QAnyStringView() noexcept
        : m_data{nullptr}, m_size{0} {}
    constexpr QAnyStringView(std::nullptr_t) noexcept
        : QAnyStringView() {}

    template <typename Char, if_compatible_char<Char> = true>
    constexpr QAnyStringView(const Char *str, qsizetype len)
        : m_data{str},
          m_size{encodeType<Char>((Q_ASSERT(len >= 0), Q_ASSERT(str || !len), len))} {}

    template <typename Char, if_compatible_char<Char> = true>
    constexpr QAnyStringView(const Char *f, const Char *l)
        : QAnyStringView(f, l - f) {}

#ifdef Q_CLANG_QDOC
    template <typename Char, size_t N>
    constexpr QAnyStringView(const Char (&array)[N]) noexcept;

    template <typename Char>
    constexpr QAnyStringView(const Char *str) noexcept;
#else

    template <typename Pointer, if_compatible_pointer<Pointer> = true>
    constexpr QAnyStringView(const Pointer &str) noexcept
        : QAnyStringView{str, str ? lengthHelperPointer(str) : 0} {}
#endif

    // defined in qstring.h
    inline QAnyStringView(const QByteArray &str) noexcept; // TODO: Should we have this at all? Remove?
    inline QAnyStringView(const QString &str) noexcept;
    inline constexpr QAnyStringView(QLatin1String str) noexcept;

    // defined in qstringbuilder.h
    template <typename A, typename B>
    inline QAnyStringView(const QStringBuilder<A, B> &expr,
                          typename QStringBuilder<A, B>::ConvertTo &&capacity = {});

    template <typename Container, if_compatible_container<Container> = true>
    constexpr QAnyStringView(const Container &c) noexcept
        : QAnyStringView(std::data(c), lengthHelperContainer(c)) {}

    template <typename Char, if_compatible_char<Char> = true>
    constexpr QAnyStringView(const Char &c) noexcept
        : QAnyStringView{&c, 1} {}
    constexpr QAnyStringView(const QChar &c) noexcept
        : QAnyStringView{&c, 1} {}

    template <typename Char, typename Container = decltype(QChar::fromUcs4(U'x')),
              std::enable_if_t<std::is_same_v<Char, char32_t>, bool> = true>
    constexpr QAnyStringView(Char c, Container &&capacity = {})
        : QAnyStringView(capacity = QChar::fromUcs4(c)) {}

    constexpr QAnyStringView(QStringView v) noexcept
        : QAnyStringView(std::data(v), lengthHelperContainer(v)) {}

    template <bool UseChar8T>
    constexpr QAnyStringView(QBasicUtf8StringView<UseChar8T> v) noexcept
        : QAnyStringView(std::data(v), lengthHelperContainer(v)) {}

    template <typename Char, size_t Size, if_compatible_char<Char> = true>
    [[nodiscard]] constexpr static QAnyStringView fromArray(const Char (&string)[Size]) noexcept
    { return QAnyStringView(string, Size); }

    // defined in qstring.h:
    template <typename Visitor>
    inline constexpr decltype(auto) visit(Visitor &&v) const;

    [[nodiscard]] inline QString toString() const; // defined in qstring.h

    [[nodiscard]] constexpr qsizetype size() const noexcept { return qsizetype(m_size & SizeMask); }
    [[nodiscard]] constexpr const void *data() const noexcept { return m_data; }

    [[nodiscard]] Q_CORE_EXPORT static int compare(QAnyStringView lhs, QAnyStringView rhs, Qt::CaseSensitivity cs = Qt::CaseSensitive) noexcept;
    [[nodiscard]] Q_CORE_EXPORT static bool equal(QAnyStringView lhs, QAnyStringView rhs) noexcept;

    //
    // STL compatibility API:
    //
    [[nodiscard]] constexpr QChar front() const; // NOT noexcept!
    [[nodiscard]] constexpr QChar back() const; // NOT noexcept!
    [[nodiscard]] constexpr bool empty() const noexcept { return size() == 0; }
    [[nodiscard]] constexpr qsizetype size_bytes() const noexcept
    { return size() * charSize(); }

    //
    // Qt compatibility API:
    //
    [[nodiscard]] constexpr bool isNull() const noexcept { return !m_data; }
    [[nodiscard]] constexpr bool isEmpty() const noexcept { return empty(); }
#if QT_DEPRECATED_SINCE(6, 0)
    [[nodiscard]]
    Q_DECL_DEPRECATED_X("Use size() and port callers to qsizetype.")
    constexpr int length() const /* not nothrow! */
    { return Q_ASSERT(int(size()) == size()), int(size()); }
#endif

private:
    [[nodiscard]] friend inline bool operator==(QAnyStringView lhs, QAnyStringView rhs) noexcept
    { return QAnyStringView::equal(lhs, rhs); }
    [[nodiscard]] friend inline bool operator!=(QAnyStringView lhs, QAnyStringView rhs) noexcept
    { return !QAnyStringView::equal(lhs, rhs); }

#if defined(__cpp_impl_three_way_comparison) && !defined(Q_QDOC)
    [[nodiscard]] friend inline auto operator<=>(QAnyStringView lhs, QAnyStringView rhs) noexcept
    { return QAnyStringView::compare(lhs, rhs) <=> 0; }
#else
    [[nodiscard]] friend inline bool operator<=(QAnyStringView lhs, QAnyStringView rhs) noexcept
    { return QAnyStringView::compare(lhs, rhs) <= 0; }
    [[nodiscard]] friend inline bool operator>=(QAnyStringView lhs, QAnyStringView rhs) noexcept
    { return QAnyStringView::compare(lhs, rhs) >= 0; }
    [[nodiscard]] friend inline bool operator<(QAnyStringView lhs, QAnyStringView rhs) noexcept
    { return QAnyStringView::compare(lhs, rhs) < 0; }
    [[nodiscard]] friend inline bool operator>(QAnyStringView lhs, QAnyStringView rhs) noexcept
    { return QAnyStringView::compare(lhs, rhs) > 0; }
#endif

    // TODO: Optimize by inverting and storing the flags in the low bits and
    //       the size in the high.
    static_assert(std::is_same_v<std::size_t, size_t>);
    static_assert(sizeof(size_t) == sizeof(qsizetype));
    static constexpr size_t SizeMask = (std::numeric_limits<size_t>::max)() / 4;
    static constexpr size_t Latin1Flag = SizeMask + 1;
    static constexpr size_t TwoByteCodePointFlag = Latin1Flag << 1;
    static constexpr size_t TypeMask = (std::numeric_limits<size_t>::max)() & ~SizeMask;
    static_assert(TypeMask == (Latin1Flag|TwoByteCodePointFlag));
    // HI HI LO LO ...
    //  0  0 SZ SZ  Utf8
    //  0  1 SZ SZ  Latin1
    //  1  0 SZ SZ  Utf16
    //  1  1 SZ SZ  Unused
    //  ^  ^ latin1
    //  | sizeof code-point == 2
    enum Tag : size_t {
        Utf8     = 0,
        Latin1   = Latin1Flag,
        Utf16    = TwoByteCodePointFlag,
        Unused   = TypeMask,
    };
    [[nodiscard]] constexpr Tag tag() const noexcept { return Tag{m_size & TypeMask}; }
    [[nodiscard]] constexpr bool isUtf16() const noexcept { return tag() == Tag::Utf16; }
    [[nodiscard]] constexpr bool isUtf8() const noexcept { return tag() == Tag::Utf8; }
    [[nodiscard]] constexpr bool isLatin1() const noexcept { return tag() == Tag::Latin1; }
    [[nodiscard]] constexpr QStringView asStringView() const
    { return Q_ASSERT(isUtf16()), QStringView{m_data_utf16, size()}; }
    [[nodiscard]] constexpr q_no_char8_t::QUtf8StringView asUtf8StringView() const
    { return Q_ASSERT(isUtf8()), q_no_char8_t::QUtf8StringView{m_data_utf8, size()}; }
    [[nodiscard]] inline constexpr QLatin1String asLatin1StringView() const;
    [[nodiscard]] constexpr size_t charSize() const noexcept { return isUtf16() ? 2 : 1; }
    Q_ALWAYS_INLINE constexpr void verify(qsizetype pos, qsizetype n = 0) const
    {
        Q_ASSERT(pos >= 0);
        Q_ASSERT(pos <= size());
        Q_ASSERT(n >= 0);
        Q_ASSERT(n <= size() - pos);
    }
    union {
        const void *m_data;
        const char *m_data_utf8;
        const char16_t *m_data_utf16;
    };
    size_t m_size;
};
Q_DECLARE_TYPEINFO(QAnyStringView, Q_PRIMITIVE_TYPE);

template <typename QStringLike, std::enable_if_t<std::disjunction_v<
        std::is_same<QStringLike, QString>,
        std::is_same<QStringLike, QByteArray>
    >, bool> = true>
[[nodiscard]] inline QAnyStringView qToAnyStringViewIgnoringNull(const QStringLike &s) noexcept
{ return QAnyStringView(s.data(), s.size()); }

QT_END_NAMESPACE

#endif /* QANYSTRINGVIEW_H */
