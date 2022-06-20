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

#ifndef QPOINTER_H
#define QPOINTER_H

#include <QtCore/qsharedpointer.h>
#include <QtCore/qtypeinfo.h>

#ifndef QT_NO_QOBJECT

QT_BEGIN_NAMESPACE

class QVariant;

template <class T>
class QPointer
{
    static_assert(!std::is_pointer<T>::value, "QPointer's template type must not be a pointer type");

    using QObjectType =
        typename std::conditional<std::is_const<T>::value, const QObject, QObject>::type;
    QWeakPointer<QObjectType> wp;
public:
    QPointer() = default;
    inline QPointer(T *p) : wp(p, true) { }
    // compiler-generated copy/move ctor/assignment operators are fine!
    // compiler-generated dtor is fine!

#ifdef Q_QDOC
    // Stop qdoc from complaining about missing function
    ~QPointer();
#endif

    inline void swap(QPointer &other) noexcept { wp.swap(other.wp); }

    inline QPointer<T> &operator=(T* p)
    { wp.assign(static_cast<QObjectType*>(p)); return *this; }

    inline T* data() const
    { return static_cast<T*>(wp.internalData()); }
    inline T* get() const
    { return data(); }
    inline T* operator->() const
    { return data(); }
    inline T& operator*() const
    { return *data(); }
    inline operator T*() const
    { return data(); }

    inline bool isNull() const
    { return wp.isNull(); }

    inline void clear()
    { wp.clear(); }

#define DECLARE_COMPARE_SET(T1, A1, T2, A2) \
    friend bool operator==(T1, T2) \
    { return A1 == A2; } \
    friend bool operator!=(T1, T2) \
    { return A1 != A2; }

#define DECLARE_TEMPLATE_COMPARE_SET(T1, A1, T2, A2) \
    template <typename X> \
    friend bool operator==(T1, T2) noexcept \
    { return A1 == A2; } \
    template <typename X> \
    friend bool operator!=(T1, T2) noexcept \
    { return A1 != A2; }

    DECLARE_TEMPLATE_COMPARE_SET(const QPointer &p1, p1.data(), const QPointer<X> &p2, p2.data())
    DECLARE_TEMPLATE_COMPARE_SET(const QPointer &p1, p1.data(), X *ptr, ptr)
    DECLARE_TEMPLATE_COMPARE_SET(X *ptr, ptr, const QPointer &p2, p2.data())
    DECLARE_COMPARE_SET(const QPointer &p1, p1.data(), std::nullptr_t, nullptr)
    DECLARE_COMPARE_SET(std::nullptr_t, nullptr, const QPointer &p2, p2.data())
#undef DECLARE_COMPARE_SET
#undef DECLARE_TEMPLATE_COMPARE_SET
};
template <class T> Q_DECLARE_TYPEINFO_BODY(QPointer<T>, Q_RELOCATABLE_TYPE);

template<typename T>
QPointer<T>
qPointerFromVariant(const QVariant &variant)
{
    const auto wp = QtSharedPointer::weakPointerFromVariant_internal(variant);
    return QPointer<T>{qobject_cast<T*>(QtPrivate::EnableInternalData::internalData(wp))};
}

template <class T>
inline void swap(QPointer<T> &p1, QPointer<T> &p2) noexcept
{ p1.swap(p2); }

QT_END_NAMESPACE

#endif // QT_NO_QOBJECT

#endif // QPOINTER_H
