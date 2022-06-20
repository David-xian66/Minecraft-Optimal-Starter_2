/****************************************************************************
**
** Copyright (C) 2020 The Qt Company Ltd.
** Contact: https://www.qt.io/licensing/
**
** This file is part of the QtGui module of the Qt Toolkit.
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

#ifndef QPOINTINGDEVICE_H
#define QPOINTINGDEVICE_H

#include <QtGui/qtguiglobal.h>
#include <QtCore/qobject.h>
#include <QtGui/qinputdevice.h>

QT_BEGIN_NAMESPACE

class QDebug;
class QEventPoint;
class QPointerEvent;
class QPointingDevicePrivate;
class QPointerEvent;
class QScreen;

class Q_GUI_EXPORT QPointingDeviceUniqueId
{
    Q_GADGET
    Q_PROPERTY(qint64 numericId READ numericId CONSTANT)
public:
    Q_ALWAYS_INLINE
    constexpr QPointingDeviceUniqueId() noexcept : m_numericId(-1) {}
    // compiler-generated copy/move ctor/assignment operators are ok!
    // compiler-generated dtor is ok!

    static QPointingDeviceUniqueId fromNumericId(qint64 id);

    Q_ALWAYS_INLINE constexpr bool isValid() const noexcept { return m_numericId != -1; }
    qint64 numericId() const noexcept;

private:
    friend bool operator==(QPointingDeviceUniqueId lhs, QPointingDeviceUniqueId rhs) noexcept
    { return lhs.numericId() == rhs.numericId(); }
    friend bool operator!=(QPointingDeviceUniqueId lhs, QPointingDeviceUniqueId rhs) noexcept
    { return lhs.numericId() != rhs.numericId(); }

    // TODO: for TUIO 2, or any other type of complex token ID, an internal
    // array (or hash) can be added to hold additional properties.
    // In this case, m_numericId will then turn into an index into that array (or hash).
    qint64 m_numericId;
};
Q_DECLARE_TYPEINFO(QPointingDeviceUniqueId, Q_RELOCATABLE_TYPE);

Q_GUI_EXPORT size_t qHash(QPointingDeviceUniqueId key, size_t seed = 0) noexcept;

class Q_GUI_EXPORT QPointingDevice : public QInputDevice
{
    Q_OBJECT
    Q_DECLARE_PRIVATE(QPointingDevice)
    Q_PROPERTY(PointerType pointerType READ pointerType CONSTANT)
    Q_PROPERTY(int maximumPoints READ maximumPoints CONSTANT)
    Q_PROPERTY(int buttonCount READ buttonCount CONSTANT)
    Q_PROPERTY(QPointingDeviceUniqueId uniqueId READ uniqueId CONSTANT)

public:
    enum class PointerType {
        Unknown = 0,
        Generic = 0x0001,   // mouse or similar
        Finger = 0x0002,    // touchscreen or pad
        Pen = 0x0004,       // stylus on a tablet
        Eraser = 0x0008,    // eraser end of a stylus
        Cursor = 0x0010,    // digitizer with crosshairs
        AllPointerTypes = 0x7FFF
    };
    Q_DECLARE_FLAGS(PointerTypes, PointerType)
    Q_FLAG(PointerTypes)

    enum GrabTransition {
        GrabPassive = 0x01,
        UngrabPassive = 0x02,
        CancelGrabPassive = 0x03,
        OverrideGrabPassive = 0x04,
        GrabExclusive = 0x10,
        UngrabExclusive = 0x20,
        CancelGrabExclusive = 0x30,
    };
    Q_ENUM(GrabTransition)

    QPointingDevice(QObject *parent = nullptr);
    ~QPointingDevice();
    QPointingDevice(const QString &name, qint64 systemId, QInputDevice::DeviceType devType,
                    PointerType pType, Capabilities caps, int maxPoints, int buttonCount,
                    const QString &seatName = QString(),
                    QPointingDeviceUniqueId uniqueId = QPointingDeviceUniqueId(),
                    QObject *parent = nullptr);

#if QT_DEPRECATED_SINCE(6, 0)
    QT_DEPRECATED_VERSION_X_6_0("Use the constructor")
    void setType(DeviceType devType);
    QT_DEPRECATED_VERSION_X_6_0("Use the constructor")
    void setCapabilities(QInputDevice::Capabilities caps);
    QT_DEPRECATED_VERSION_X_6_0("Use the constructor")
    void setMaximumTouchPoints(int c);
#endif

    PointerType pointerType() const;
    int maximumPoints() const;
    int buttonCount() const;
    QPointingDeviceUniqueId uniqueId() const;

    static const QPointingDevice *primaryPointingDevice(const QString& seatName = QString());

    bool operator==(const QPointingDevice &other) const;

Q_SIGNALS:
    void grabChanged(QObject *grabber, GrabTransition transition, const QPointerEvent *event, const QEventPoint &point) const;

protected:
    QPointingDevice(QPointingDevicePrivate &d, QObject *parent);

    Q_DISABLE_COPY_MOVE(QPointingDevice)
};

Q_DECLARE_OPERATORS_FOR_FLAGS(QPointingDevice::PointerTypes)

#ifndef QT_NO_DEBUG_STREAM
Q_GUI_EXPORT QDebug operator<<(QDebug, const QPointingDevice *);
#endif

//typedef QPointingDevice QTouchDevice; // Qt 5 source compatibility if we need it? or could be "using"

QT_END_NAMESPACE

#endif // QPOINTINGDEVICE_H
