/****************************************************************************
**
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

#ifndef QSIZE_H
#define QSIZE_H

#include <QtCore/qnamespace.h>
#include <QtCore/qhashfunctions.h>
#include <QtCore/qmargins.h>

#if defined(Q_OS_DARWIN) || defined(Q_QDOC)
struct CGSize;
#endif

QT_BEGIN_NAMESPACE


class Q_CORE_EXPORT QSize
{
public:
    constexpr QSize() noexcept;
    constexpr QSize(int w, int h) noexcept;

    constexpr inline bool isNull() const noexcept;
    constexpr inline bool isEmpty() const noexcept;
    constexpr inline bool isValid() const noexcept;

    constexpr inline int width() const noexcept;
    constexpr inline int height() const noexcept;
    constexpr inline void setWidth(int w) noexcept;
    constexpr inline void setHeight(int h) noexcept;
    void transpose() noexcept;
    [[nodiscard]] constexpr inline QSize transposed() const noexcept;

    inline void scale(int w, int h, Qt::AspectRatioMode mode) noexcept;
    inline void scale(const QSize &s, Qt::AspectRatioMode mode) noexcept;
    [[nodiscard]] QSize scaled(int w, int h, Qt::AspectRatioMode mode) const noexcept;
    [[nodiscard]] QSize scaled(const QSize &s, Qt::AspectRatioMode mode) const noexcept;

    [[nodiscard]] constexpr inline QSize expandedTo(const QSize &) const noexcept;
    [[nodiscard]] constexpr inline QSize boundedTo(const QSize &) const noexcept;

    [[nodiscard]] constexpr QSize grownBy(QMargins m) const noexcept
    { return {width() + m.left() + m.right(), height() + m.top() + m.bottom()}; }
    [[nodiscard]] constexpr QSize shrunkBy(QMargins m) const noexcept
    { return {width() - m.left() - m.right(), height() - m.top() - m.bottom()}; }

    constexpr inline int &rwidth() noexcept;
    constexpr inline int &rheight() noexcept;

    constexpr inline QSize &operator+=(const QSize &) noexcept;
    constexpr inline QSize &operator-=(const QSize &) noexcept;
    constexpr inline QSize &operator*=(qreal c) noexcept;
    inline QSize &operator/=(qreal c);

    friend inline constexpr bool operator==(const QSize &s1, const QSize &s2) noexcept
    { return s1.wd == s2.wd && s1.ht == s2.ht; }
    friend inline constexpr bool operator!=(const QSize &s1, const QSize &s2) noexcept
    { return s1.wd != s2.wd || s1.ht != s2.ht; }
    friend inline constexpr QSize operator+(const QSize &s1, const QSize &s2) noexcept
    { return QSize(s1.wd + s2.wd, s1.ht + s2.ht); }
    friend inline constexpr QSize operator-(const QSize &s1, const QSize &s2) noexcept
    { return QSize(s1.wd - s2.wd, s1.ht - s2.ht); }
    friend inline constexpr QSize operator*(const QSize &s, qreal c) noexcept
    { return QSize(qRound(s.wd * c), qRound(s.ht * c)); }
    friend inline constexpr QSize operator*(qreal c, const QSize &s) noexcept
    { return s * c; }
    friend inline QSize operator/(const QSize &s, qreal c)
    { Q_ASSERT(!qFuzzyIsNull(c)); return QSize(qRound(s.wd / c), qRound(s.ht / c)); }
    friend inline constexpr size_t qHash(const QSize &, size_t) noexcept;

#if defined(Q_OS_DARWIN) || defined(Q_QDOC)
    [[nodiscard]] CGSize toCGSize() const noexcept;
#endif

private:
    int wd;
    int ht;
};
Q_DECLARE_TYPEINFO(QSize, Q_RELOCATABLE_TYPE);

/*****************************************************************************
  QSize stream functions
 *****************************************************************************/

#ifndef QT_NO_DATASTREAM
Q_CORE_EXPORT QDataStream &operator<<(QDataStream &, const QSize &);
Q_CORE_EXPORT QDataStream &operator>>(QDataStream &, QSize &);
#endif


/*****************************************************************************
  QSize inline functions
 *****************************************************************************/

constexpr inline QSize::QSize() noexcept : wd(-1), ht(-1) {}

constexpr inline QSize::QSize(int w, int h) noexcept : wd(w), ht(h) {}

constexpr inline bool QSize::isNull() const noexcept
{ return wd == 0 && ht == 0; }

constexpr inline bool QSize::isEmpty() const noexcept
{ return wd < 1 || ht < 1; }

constexpr inline bool QSize::isValid() const noexcept
{ return wd >= 0 && ht >= 0; }

constexpr inline int QSize::width() const noexcept
{ return wd; }

constexpr inline int QSize::height() const noexcept
{ return ht; }

constexpr inline void QSize::setWidth(int w) noexcept
{ wd = w; }

constexpr inline void QSize::setHeight(int h) noexcept
{ ht = h; }

constexpr inline QSize QSize::transposed() const noexcept
{ return QSize(ht, wd); }

inline void QSize::scale(int w, int h, Qt::AspectRatioMode mode) noexcept
{ scale(QSize(w, h), mode); }

inline void QSize::scale(const QSize &s, Qt::AspectRatioMode mode) noexcept
{ *this = scaled(s, mode); }

inline QSize QSize::scaled(int w, int h, Qt::AspectRatioMode mode) const noexcept
{ return scaled(QSize(w, h), mode); }

constexpr inline int &QSize::rwidth() noexcept
{ return wd; }

constexpr inline int &QSize::rheight() noexcept
{ return ht; }

constexpr inline QSize &QSize::operator+=(const QSize &s) noexcept
{
    wd += s.wd;
    ht += s.ht;
    return *this;
}

constexpr inline QSize &QSize::operator-=(const QSize &s) noexcept
{
    wd -= s.wd;
    ht -= s.ht;
    return *this;
}

constexpr inline QSize &QSize::operator*=(qreal c) noexcept
{
    wd = qRound(wd * c);
    ht = qRound(ht * c);
    return *this;
}

constexpr inline size_t qHash(const QSize &s, size_t seed = 0) noexcept
{ return qHashMulti(seed, s.wd, s.ht); }

inline QSize &QSize::operator/=(qreal c)
{
    Q_ASSERT(!qFuzzyIsNull(c));
    wd = qRound(wd / c);
    ht = qRound(ht / c);
    return *this;
}

constexpr inline QSize QSize::expandedTo(const QSize & otherSize) const noexcept
{
    return QSize(qMax(wd,otherSize.wd), qMax(ht,otherSize.ht));
}

constexpr inline QSize QSize::boundedTo(const QSize & otherSize) const noexcept
{
    return QSize(qMin(wd,otherSize.wd), qMin(ht,otherSize.ht));
}

#ifndef QT_NO_DEBUG_STREAM
Q_CORE_EXPORT QDebug operator<<(QDebug, const QSize &);
#endif


class Q_CORE_EXPORT QSizeF
{
public:
    constexpr QSizeF() noexcept;
    constexpr QSizeF(const QSize &sz) noexcept;
    constexpr QSizeF(qreal w, qreal h) noexcept;

    inline bool isNull() const noexcept;
    constexpr inline bool isEmpty() const noexcept;
    constexpr inline bool isValid() const noexcept;

    constexpr inline qreal width() const noexcept;
    constexpr inline qreal height() const noexcept;
    constexpr inline void setWidth(qreal w) noexcept;
    constexpr inline void setHeight(qreal h) noexcept;
    void transpose() noexcept;
    [[nodiscard]] constexpr inline QSizeF transposed() const noexcept;

    inline void scale(qreal w, qreal h, Qt::AspectRatioMode mode) noexcept;
    inline void scale(const QSizeF &s, Qt::AspectRatioMode mode) noexcept;
    [[nodiscard]] QSizeF scaled(qreal w, qreal h, Qt::AspectRatioMode mode) const noexcept;
    [[nodiscard]] QSizeF scaled(const QSizeF &s, Qt::AspectRatioMode mode) const noexcept;

    [[nodiscard]] constexpr inline QSizeF expandedTo(const QSizeF &) const noexcept;
    [[nodiscard]] constexpr inline QSizeF boundedTo(const QSizeF &) const noexcept;

    [[nodiscard]] constexpr QSizeF grownBy(QMarginsF m) const noexcept
    { return {width() + m.left() + m.right(), height() + m.top() + m.bottom()}; }
    [[nodiscard]] constexpr QSizeF shrunkBy(QMarginsF m) const noexcept
    { return {width() - m.left() - m.right(), height() - m.top() - m.bottom()}; }

    constexpr inline qreal &rwidth() noexcept;
    constexpr inline qreal &rheight() noexcept;

    constexpr inline QSizeF &operator+=(const QSizeF &) noexcept;
    constexpr inline QSizeF &operator-=(const QSizeF &) noexcept;
    constexpr inline QSizeF &operator*=(qreal c) noexcept;
    inline QSizeF &operator/=(qreal c);

    QT_WARNING_PUSH
    QT_WARNING_DISABLE_FLOAT_COMPARE
    friend constexpr inline bool operator==(const QSizeF &s1, const QSizeF &s2)
    {
        return ((!s1.wd || !s2.wd) ? qFuzzyIsNull(s1.wd - s2.wd) : qFuzzyCompare(s1.wd, s2.wd))
            && ((!s1.ht || !s2.ht) ? qFuzzyIsNull(s1.ht - s2.ht) : qFuzzyCompare(s1.ht, s2.ht));
    }
    QT_WARNING_POP
    friend constexpr inline bool operator!=(const QSizeF &s1, const QSizeF &s2)
    { return !(s1 == s2); }
    friend constexpr inline QSizeF operator+(const QSizeF &s1, const QSizeF &s2) noexcept
    { return QSizeF(s1.wd + s2.wd, s1.ht + s2.ht); }
    friend constexpr inline QSizeF operator-(const QSizeF &s1, const QSizeF &s2) noexcept
    { return QSizeF(s1.wd - s2.wd, s1.ht - s2.ht); }
    friend constexpr inline QSizeF operator*(const QSizeF &s, qreal c) noexcept
    { return QSizeF(s.wd * c, s.ht * c); }
    friend constexpr inline QSizeF operator*(qreal c, const QSizeF &s) noexcept
    { return s * c; }
    friend inline QSizeF operator/(const QSizeF &s, qreal c)
    { Q_ASSERT(!qFuzzyIsNull(c)); return QSizeF(s.wd / c, s.ht / c); }

    constexpr inline QSize toSize() const noexcept;

#if defined(Q_OS_DARWIN) || defined(Q_QDOC)
    [[nodiscard]] static QSizeF fromCGSize(CGSize size) noexcept;
    [[nodiscard]] CGSize toCGSize() const noexcept;
#endif

private:
    qreal wd;
    qreal ht;
};
Q_DECLARE_TYPEINFO(QSizeF, Q_RELOCATABLE_TYPE);


/*****************************************************************************
  QSizeF stream functions
 *****************************************************************************/

#ifndef QT_NO_DATASTREAM
Q_CORE_EXPORT QDataStream &operator<<(QDataStream &, const QSizeF &);
Q_CORE_EXPORT QDataStream &operator>>(QDataStream &, QSizeF &);
#endif


/*****************************************************************************
  QSizeF inline functions
 *****************************************************************************/

constexpr inline QSizeF::QSizeF() noexcept : wd(-1.), ht(-1.) {}

constexpr inline QSizeF::QSizeF(const QSize &sz) noexcept : wd(sz.width()), ht(sz.height()) {}

constexpr inline QSizeF::QSizeF(qreal w, qreal h) noexcept : wd(w), ht(h) {}

inline bool QSizeF::isNull() const noexcept
{ return qIsNull(wd) && qIsNull(ht); }

constexpr inline bool QSizeF::isEmpty() const noexcept
{ return wd <= 0. || ht <= 0.; }

constexpr inline bool QSizeF::isValid() const noexcept
{ return wd >= 0. && ht >= 0.; }

constexpr inline qreal QSizeF::width() const noexcept
{ return wd; }

constexpr inline qreal QSizeF::height() const noexcept
{ return ht; }

constexpr inline void QSizeF::setWidth(qreal w) noexcept
{ wd = w; }

constexpr inline void QSizeF::setHeight(qreal h) noexcept
{ ht = h; }

constexpr inline QSizeF QSizeF::transposed() const noexcept
{ return QSizeF(ht, wd); }

inline void QSizeF::scale(qreal w, qreal h, Qt::AspectRatioMode mode) noexcept
{ scale(QSizeF(w, h), mode); }

inline void QSizeF::scale(const QSizeF &s, Qt::AspectRatioMode mode) noexcept
{ *this = scaled(s, mode); }

inline QSizeF QSizeF::scaled(qreal w, qreal h, Qt::AspectRatioMode mode) const noexcept
{ return scaled(QSizeF(w, h), mode); }

constexpr inline qreal &QSizeF::rwidth() noexcept
{ return wd; }

constexpr inline qreal &QSizeF::rheight() noexcept
{ return ht; }

constexpr inline QSizeF &QSizeF::operator+=(const QSizeF &s) noexcept
{
    wd += s.wd;
    ht += s.ht;
    return *this;
}

constexpr inline QSizeF &QSizeF::operator-=(const QSizeF &s) noexcept
{
    wd -= s.wd;
    ht -= s.ht;
    return *this;
}

constexpr inline QSizeF &QSizeF::operator*=(qreal c) noexcept
{
    wd *= c;
    ht *= c;
    return *this;
}

inline QSizeF &QSizeF::operator/=(qreal c)
{
    Q_ASSERT(!qFuzzyIsNull(c));
    wd = wd / c;
    ht = ht / c;
    return *this;
}

constexpr inline QSizeF QSizeF::expandedTo(const QSizeF &otherSize) const noexcept
{
    return QSizeF(qMax(wd, otherSize.wd), qMax(ht, otherSize.ht));
}

constexpr inline QSizeF QSizeF::boundedTo(const QSizeF &otherSize) const noexcept
{
    return QSizeF(qMin(wd, otherSize.wd), qMin(ht, otherSize.ht));
}

constexpr inline QSize QSizeF::toSize() const noexcept
{
    return QSize(qRound(wd), qRound(ht));
}

#ifndef QT_NO_DEBUG_STREAM
Q_CORE_EXPORT QDebug operator<<(QDebug, const QSizeF &);
#endif

QT_END_NAMESPACE

#endif // QSIZE_H
