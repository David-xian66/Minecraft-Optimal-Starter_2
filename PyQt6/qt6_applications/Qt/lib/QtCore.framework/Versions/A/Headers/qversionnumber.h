/****************************************************************************
**
** Copyright (C) 2016 The Qt Company Ltd.
** Copyright (C) 2016 Intel Corporation.
** Copyright (C) 2014 Keith Gardner <kreios4004@gmail.com>
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

#ifndef QVERSIONNUMBER_H
#define QVERSIONNUMBER_H

#include <QtCore/qlist.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qnamespace.h>
#include <QtCore/qstring.h>
#include <QtCore/qtypeinfo.h>
#include <limits>

QT_BEGIN_NAMESPACE

class QVersionNumber;
Q_CORE_EXPORT size_t qHash(const QVersionNumber &key, size_t seed = 0);

#ifndef QT_NO_DATASTREAM
Q_CORE_EXPORT QDataStream &operator<<(QDataStream &out, const QVersionNumber &version);
Q_CORE_EXPORT QDataStream &operator>>(QDataStream &in, QVersionNumber &version);
#endif

class QVersionNumber
{
    /*
     * QVersionNumber stores small values inline, without memory allocation.
     * We do that by setting the LSB in the pointer that would otherwise hold
     * the longer form of the segments.
     * The constants below help us deal with the permutations for 32- and 64-bit,
     * little- and big-endian architectures.
     */
    enum {
        // in little-endian, inline_segments[0] is shared with the pointer's LSB, while
        // in big-endian, it's inline_segments[7]
        InlineSegmentMarker = Q_BYTE_ORDER == Q_LITTLE_ENDIAN ? 0 : sizeof(void *) - 1,
        InlineSegmentStartIdx = !InlineSegmentMarker, // 0 for BE, 1 for LE
        InlineSegmentCount = sizeof(void *) - 1
    };
    static_assert(InlineSegmentCount >= 3);   // at least major, minor, micro

    struct SegmentStorage
    {
        // Note: we alias the use of dummy and inline_segments in the use of the
        // union below. This is undefined behavior in C++98, but most compilers implement
        // the C++11 behavior. The one known exception is older versions of Sun Studio.
        union {
            quintptr dummy;
            qint8 inline_segments[sizeof(void *)];
            QList<int> *pointer_segments;
        };

        // set the InlineSegmentMarker and set length to zero
        SegmentStorage() noexcept : dummy(1) {}

        SegmentStorage(const QList<int> &seg)
        {
            if (dataFitsInline(seg.begin(), seg.size()))
                setInlineData(seg.begin(), seg.size());
            else
                pointer_segments = new QList<int>(seg);
        }

        SegmentStorage(const SegmentStorage &other)
        {
            if (other.isUsingPointer())
                pointer_segments = new QList<int>(*other.pointer_segments);
            else
                dummy = other.dummy;
        }

        SegmentStorage &operator=(const SegmentStorage &other)
        {
            if (isUsingPointer() && other.isUsingPointer()) {
                *pointer_segments = *other.pointer_segments;
            } else if (other.isUsingPointer()) {
                pointer_segments = new QList<int>(*other.pointer_segments);
            } else {
                if (isUsingPointer())
                    delete pointer_segments;
                dummy = other.dummy;
            }
            return *this;
        }

        SegmentStorage(SegmentStorage &&other) noexcept
            : dummy(other.dummy)
        {
            other.dummy = 1;
        }

        QT_MOVE_ASSIGNMENT_OPERATOR_IMPL_VIA_PURE_SWAP(SegmentStorage)

        void swap(SegmentStorage &other) noexcept
        {
            qSwap(dummy, other.dummy);
        }

        explicit SegmentStorage(QList<int> &&seg)
        {
            if (dataFitsInline(seg.begin(), seg.size()))
                setInlineData(seg.begin(), seg.size());
            else
                pointer_segments = new QList<int>(std::move(seg));
        }
        SegmentStorage(std::initializer_list<int> args)
        {
            if (dataFitsInline(args.begin(), int(args.size()))) {
                setInlineData(args.begin(), int(args.size()));
            } else {
                pointer_segments = new QList<int>(args);
            }
        }

        ~SegmentStorage() { if (isUsingPointer()) delete pointer_segments; }

        bool isUsingPointer() const noexcept
        { return (inline_segments[InlineSegmentMarker] & 1) == 0; }

        int size() const noexcept
        { return isUsingPointer() ? pointer_segments->size() : (inline_segments[InlineSegmentMarker] >> 1); }

        void setInlineSize(int len)
        { inline_segments[InlineSegmentMarker] = qint8(1 + 2 * len); }

        void resize(int len)
        {
            if (isUsingPointer())
                pointer_segments->resize(len);
            else
                setInlineSize(len);
        }

        int at(int index) const
        {
            return isUsingPointer() ?
                        pointer_segments->at(index) :
                        inline_segments[InlineSegmentStartIdx + index];
        }

        void setSegments(int len, int maj, int min = 0, int mic = 0)
        {
            if (maj == qint8(maj) && min == qint8(min) && mic == qint8(mic)) {
                int data[] = { maj, min, mic };
                setInlineData(data, len);
            } else {
                setVector(len, maj, min, mic);
            }
        }

    private:
        static bool dataFitsInline(const int *data, int len)
        {
            if (len > InlineSegmentCount)
                return false;
            for (int i = 0; i < len; ++i)
                if (data[i] != qint8(data[i]))
                    return false;
            return true;
        }
        void setInlineData(const int *data, int len)
        {
            dummy = 1 + len * 2;
#if Q_BYTE_ORDER == Q_LITTLE_ENDIAN
            for (int i = 0; i < len; ++i)
                dummy |= quintptr(data[i] & 0xFF) << (8 * (i + 1));
#elif Q_BYTE_ORDER == Q_BIG_ENDIAN
            for (int i = 0; i < len; ++i)
                dummy |= quintptr(data[i] & 0xFF) << (8 * (sizeof(void *) - i - 1));
#else
            // the code above is equivalent to:
            setInlineSize(len);
            for (int i = 0; i < len; ++i)
                inline_segments[InlineSegmentStartIdx + i] = data[i] & 0xFF;
#endif
        }

        Q_CORE_EXPORT void setVector(int len, int maj, int min, int mic);
    } m_segments;

public:
    inline QVersionNumber() noexcept
        : m_segments()
    {}
    inline explicit QVersionNumber(const QList<int> &seg) : m_segments(seg) { }

    // compiler-generated copy/move ctor/assignment operators and the destructor are ok

    explicit QVersionNumber(QList<int> &&seg) : m_segments(std::move(seg)) { }

    inline QVersionNumber(std::initializer_list<int> args)
        : m_segments(args)
    {}

    inline explicit QVersionNumber(int maj)
    { m_segments.setSegments(1, maj); }

    inline explicit QVersionNumber(int maj, int min)
    { m_segments.setSegments(2, maj, min); }

    inline explicit QVersionNumber(int maj, int min, int mic)
    { m_segments.setSegments(3, maj, min, mic); }

    [[nodiscard]] inline bool isNull() const noexcept
    { return segmentCount() == 0; }

    [[nodiscard]] inline bool isNormalized() const noexcept
    { return isNull() || segmentAt(segmentCount() - 1) != 0; }

    [[nodiscard]] inline int majorVersion() const noexcept
    { return segmentAt(0); }

    [[nodiscard]] inline int minorVersion() const noexcept
    { return segmentAt(1); }

    [[nodiscard]] inline int microVersion() const noexcept
    { return segmentAt(2); }

    [[nodiscard]] Q_CORE_EXPORT QVersionNumber normalized() const;

    [[nodiscard]] Q_CORE_EXPORT QList<int> segments() const;

    [[nodiscard]] inline int segmentAt(int index) const noexcept
    { return (m_segments.size() > index) ? m_segments.at(index) : 0; }

    [[nodiscard]] inline int segmentCount() const noexcept
    { return m_segments.size(); }

    [[nodiscard]] Q_CORE_EXPORT bool isPrefixOf(const QVersionNumber &other) const noexcept;

    [[nodiscard]] Q_CORE_EXPORT static int compare(const QVersionNumber &v1, const QVersionNumber &v2) noexcept;

    [[nodiscard]] Q_CORE_EXPORT static Q_DECL_PURE_FUNCTION QVersionNumber commonPrefix(const QVersionNumber &v1, const QVersionNumber &v2);

    [[nodiscard]] Q_CORE_EXPORT QString toString() const;
#if QT_STRINGVIEW_LEVEL < 2
    [[nodiscard]] Q_CORE_EXPORT static Q_DECL_PURE_FUNCTION QVersionNumber fromString(const QString &string, int *suffixIndex = nullptr);
#endif
    [[nodiscard]] Q_CORE_EXPORT static Q_DECL_PURE_FUNCTION QVersionNumber fromString(QLatin1String string, int *suffixIndex = nullptr);
    [[nodiscard]] Q_CORE_EXPORT static Q_DECL_PURE_FUNCTION QVersionNumber fromString(QStringView string, int *suffixIndex = nullptr);

    [[nodiscard]] friend bool operator> (const QVersionNumber &lhs, const QVersionNumber &rhs) noexcept
    { return compare(lhs, rhs) > 0; }

    [[nodiscard]] friend bool operator>=(const QVersionNumber &lhs, const QVersionNumber &rhs) noexcept
    { return compare(lhs, rhs) >= 0; }

    [[nodiscard]] friend bool operator< (const QVersionNumber &lhs, const QVersionNumber &rhs) noexcept
    { return compare(lhs, rhs) < 0; }

    [[nodiscard]] friend bool operator<=(const QVersionNumber &lhs, const QVersionNumber &rhs) noexcept
    { return compare(lhs, rhs) <= 0; }

    [[nodiscard]] friend bool operator==(const QVersionNumber &lhs, const QVersionNumber &rhs) noexcept
    { return compare(lhs, rhs) == 0; }

    [[nodiscard]] friend bool operator!=(const QVersionNumber &lhs, const QVersionNumber &rhs) noexcept
    { return compare(lhs, rhs) != 0; }


private:
#ifndef QT_NO_DATASTREAM
    friend Q_CORE_EXPORT QDataStream& operator>>(QDataStream &in, QVersionNumber &version);
#endif
    friend Q_CORE_EXPORT size_t qHash(const QVersionNumber &key, size_t seed);
};

Q_DECLARE_TYPEINFO(QVersionNumber, Q_RELOCATABLE_TYPE);

#ifndef QT_NO_DEBUG_STREAM
Q_CORE_EXPORT QDebug operator<<(QDebug, const QVersionNumber &version);
#endif

class QTypeRevision;
Q_CORE_EXPORT size_t qHash(const QTypeRevision &key, size_t seed = 0);

#ifndef QT_NO_DATASTREAM
Q_CORE_EXPORT QDataStream& operator<<(QDataStream &out, const QTypeRevision &revision);
Q_CORE_EXPORT QDataStream& operator>>(QDataStream &in, QTypeRevision &revision);
#endif

class QTypeRevision
{
public:
    template<typename Integer>
    using if_valid_segment_type = typename std::enable_if<
            std::is_integral<Integer>::value, bool>::type;

    template<typename Integer>
    using if_valid_value_type = typename std::enable_if<
            std::is_integral<Integer>::value
            && (sizeof(Integer) > sizeof(quint16)
                || (sizeof(Integer) == sizeof(quint16)
                    && !std::is_signed<Integer>::value)), bool>::type;

    template<typename Integer, if_valid_segment_type<Integer> = true>
    static constexpr bool isValidSegment(Integer segment)
    {
        // using extra parentheses around max to avoid expanding it if it is a macro
        return segment >= Integer(0)
                && ((std::numeric_limits<Integer>::max)() < Integer(SegmentUnknown)
                    || segment < Integer(SegmentUnknown));
    }

    template<typename Major, typename Minor,
             if_valid_segment_type<Major> = true,
             if_valid_segment_type<Minor> = true>
    static constexpr QTypeRevision fromVersion(Major majorVersion, Minor minorVersion)
    {
        return Q_ASSERT(isValidSegment(majorVersion)),
               Q_ASSERT(isValidSegment(minorVersion)),
               QTypeRevision(quint8(majorVersion), quint8(minorVersion));
    }

    template<typename Major, if_valid_segment_type<Major> = true>
    static constexpr QTypeRevision fromMajorVersion(Major majorVersion)
    {
        return Q_ASSERT(isValidSegment(majorVersion)),
               QTypeRevision(quint8(majorVersion), SegmentUnknown);
    }

    template<typename Minor, if_valid_segment_type<Minor> = true>
    static constexpr QTypeRevision fromMinorVersion(Minor minorVersion)
    {
        return Q_ASSERT(isValidSegment(minorVersion)),
               QTypeRevision(SegmentUnknown, quint8(minorVersion));
    }

    template<typename Integer, if_valid_value_type<Integer> = true>
    static constexpr QTypeRevision fromEncodedVersion(Integer value)
    {
        return Q_ASSERT((value & ~Integer(0xffff)) == Integer(0)),
               QTypeRevision((value & Integer(0xff00)) >> 8, value & Integer(0xff));
    }

    static constexpr QTypeRevision zero() { return QTypeRevision(0, 0); }

    constexpr QTypeRevision() = default;

    constexpr bool hasMajorVersion() const { return m_majorVersion != SegmentUnknown; }
    constexpr quint8 majorVersion() const { return m_majorVersion; }

    constexpr bool hasMinorVersion() const { return m_minorVersion != SegmentUnknown; }
    constexpr quint8 minorVersion() const { return m_minorVersion; }

    constexpr bool isValid() const { return hasMajorVersion() || hasMinorVersion(); }

    template<typename Integer, if_valid_value_type<Integer> = true>
    constexpr Integer toEncodedVersion() const
    {
        return Integer(m_majorVersion << 8) | Integer(m_minorVersion);
    }

    [[nodiscard]] friend constexpr bool operator==(QTypeRevision lhs, QTypeRevision rhs)
    {
        return lhs.toEncodedVersion<quint16>() == rhs.toEncodedVersion<quint16>();
    }

    [[nodiscard]] friend constexpr bool operator!=(QTypeRevision lhs, QTypeRevision rhs)
    {
        return lhs.toEncodedVersion<quint16>() != rhs.toEncodedVersion<quint16>();
    }

    [[nodiscard]] friend constexpr bool operator<(QTypeRevision lhs, QTypeRevision rhs)
    {
        return (!lhs.hasMajorVersion() && rhs.hasMajorVersion())
                // non-0 major > unspecified major > major 0
                ? rhs.majorVersion() != 0
                : ((lhs.hasMajorVersion() && !rhs.hasMajorVersion())
                // major 0 < unspecified major < non-0 major
                ? lhs.majorVersion() == 0
                : (lhs.majorVersion() != rhs.majorVersion()
                    // both majors specified and non-0
                    ? lhs.majorVersion() < rhs.majorVersion()
                    : ((!lhs.hasMinorVersion() && rhs.hasMinorVersion())
                        // non-0 minor > unspecified minor > minor 0
                        ? rhs.minorVersion() != 0
                        : ((lhs.hasMinorVersion() && !rhs.hasMinorVersion())
                            // minor 0 < unspecified minor < non-0 minor
                            ? lhs.minorVersion() == 0
                            // both minors specified and non-0
                            : lhs.minorVersion() < rhs.minorVersion()))));
    }

    [[nodiscard]] friend constexpr bool operator>(QTypeRevision lhs, QTypeRevision rhs)
    {
        return lhs != rhs && !(lhs < rhs);
    }

    [[nodiscard]] friend constexpr bool operator<=(QTypeRevision lhs, QTypeRevision rhs)
    {
        return lhs == rhs || lhs < rhs;
    }

    [[nodiscard]] friend constexpr bool operator>=(QTypeRevision lhs, QTypeRevision rhs)
    {
        return lhs == rhs || !(lhs < rhs);
    }

private:
    enum { SegmentUnknown = 0xff };

#if Q_BYTE_ORDER == Q_LITTLE_ENDIAN
    constexpr QTypeRevision(quint8 major, quint8 minor)
        : m_minorVersion(minor), m_majorVersion(major) {}

    quint8 m_minorVersion = SegmentUnknown;
    quint8 m_majorVersion = SegmentUnknown;
#else
    constexpr QTypeRevision(quint8 major, quint8 minor)
        : m_majorVersion(major), m_minorVersion(minor) {}

    quint8 m_majorVersion = SegmentUnknown;
    quint8 m_minorVersion = SegmentUnknown;
#endif
};

static_assert(sizeof(QTypeRevision) == 2);
Q_DECLARE_TYPEINFO(QTypeRevision, Q_RELOCATABLE_TYPE);

#ifndef QT_NO_DEBUG_STREAM
Q_CORE_EXPORT QDebug operator<<(QDebug, const QTypeRevision &revision);
#endif

QT_END_NAMESPACE

Q_DECLARE_METATYPE(QVersionNumber)
Q_DECLARE_METATYPE(QTypeRevision)

#endif // QVERSIONNUMBER_H
