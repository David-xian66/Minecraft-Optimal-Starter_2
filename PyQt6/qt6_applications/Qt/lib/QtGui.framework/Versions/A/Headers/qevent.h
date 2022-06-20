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

#ifndef QEVENT_H
#define QEVENT_H

#include <QtGui/qtguiglobal.h>

#include <QtCore/qcoreevent.h>
#include <QtCore/qiodevice.h>
#include <QtCore/qlist.h>
#include <QtCore/qnamespace.h>
#include <QtCore/qpointer.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qvariant.h>
#include <QtGui/qeventpoint.h>
#include <QtGui/qpointingdevice.h>
#include <QtGui/qregion.h>
#include <QtGui/qwindowdefs.h>

#if QT_CONFIG(shortcut)
#  include <QtGui/qkeysequence.h>
#endif

QT_BEGIN_NAMESPACE

class QFile;
class QAction;
class QMouseEvent;
class QPointerEvent;
class QScreen;
class QTabletEvent;
class QTouchEvent;
#if QT_CONFIG(gestures)
class QGesture;
#endif

class Q_GUI_EXPORT QInputEvent : public QEvent
{
    Q_EVENT_DISABLE_COPY(QInputEvent);
public:
    explicit QInputEvent(Type type, const QInputDevice *m_dev, Qt::KeyboardModifiers modifiers = Qt::NoModifier);
    ~QInputEvent();
    QInputEvent *clone() const override { return new QInputEvent(*this); }

    const QInputDevice *device() const { return m_dev; }
    QInputDevice::DeviceType deviceType() const { return m_dev ? m_dev->type() : QInputDevice::DeviceType::Unknown; }
    inline Qt::KeyboardModifiers modifiers() const { return m_modState; }
    inline void setModifiers(Qt::KeyboardModifiers modifiers) { m_modState = modifiers; }
    inline quint64 timestamp() const { return m_timeStamp; }
    virtual void setTimestamp(quint64 timestamp) { m_timeStamp = timestamp; }

protected:
    QInputEvent(Type type, PointerEventTag, const QInputDevice *dev, Qt::KeyboardModifiers modifiers = Qt::NoModifier);
    QInputEvent(Type type, SinglePointEventTag, const QInputDevice *dev, Qt::KeyboardModifiers modifiers = Qt::NoModifier);

    const QInputDevice *m_dev = nullptr;
    quint64 m_timeStamp = 0;
    Qt::KeyboardModifiers m_modState = Qt::NoModifier;
    // fill up to the closest 8-byte aligned size: 48
    quint32 m_reserved = 0;
};

class Q_GUI_EXPORT QPointerEvent : public QInputEvent
{
    Q_EVENT_DISABLE_COPY(QPointerEvent);
public:
    explicit QPointerEvent(Type type, const QPointingDevice *dev,
                           Qt::KeyboardModifiers modifiers = Qt::NoModifier, const QList<QEventPoint> &points = {});
    ~QPointerEvent();

    QPointerEvent *clone() const override { return new QPointerEvent(*this); }

    const QPointingDevice *pointingDevice() const;
    QPointingDevice::PointerType pointerType() const {
        return pointingDevice() ? pointingDevice()->pointerType() : QPointingDevice::PointerType::Unknown;
    }
    void setTimestamp(quint64 timestamp) override;
    qsizetype pointCount() const { return m_points.count(); }
    QEventPoint &point(qsizetype i) { return m_points[i]; }
    const QList<QEventPoint> &points() const { return m_points; }
    QEventPoint *pointById(int id);
    bool allPointsGrabbed() const;
    virtual bool isBeginEvent() const { return false; }
    virtual bool isUpdateEvent() const { return false; }
    virtual bool isEndEvent() const { return false; }
    bool allPointsAccepted() const;
    virtual void setAccepted(bool accepted) override;
    QObject *exclusiveGrabber(const QEventPoint &point) const;
    void setExclusiveGrabber(const QEventPoint &point, QObject *exclusiveGrabber);
    QList<QPointer <QObject>> passiveGrabbers(const QEventPoint &point) const;
    void clearPassiveGrabbers(const QEventPoint &point);
    bool addPassiveGrabber(const QEventPoint &point, QObject *grabber);
    bool removePassiveGrabber(const QEventPoint &point, QObject *grabber);

protected:
    QPointerEvent(Type type, SinglePointEventTag, const QInputDevice *dev, Qt::KeyboardModifiers modifiers = Qt::NoModifier);

    QList<QEventPoint> m_points;
};

class Q_GUI_EXPORT QSinglePointEvent : public QPointerEvent
{
    Q_GADGET
    Q_PROPERTY(QObject *exclusivePointGrabber READ exclusivePointGrabber WRITE setExclusivePointGrabber)

    Q_EVENT_DISABLE_COPY(QSinglePointEvent);
public:
    inline Qt::MouseButton button() const { return m_button; }
    inline Qt::MouseButtons buttons() const { return m_mouseState; }

    inline QPointF position() const
    { Q_ASSERT(!m_points.isEmpty()); return m_points.first().position(); }
    inline QPointF scenePosition() const
    { Q_ASSERT(!m_points.isEmpty()); return m_points.first().scenePosition(); }
    inline QPointF globalPosition() const
    { Q_ASSERT(!m_points.isEmpty()); return m_points.first().globalPosition(); }

    bool isBeginEvent() const override;
    bool isUpdateEvent() const override;
    bool isEndEvent() const override;

    QObject *exclusivePointGrabber() const
    { return QPointerEvent::exclusiveGrabber(points().first()); }
    void setExclusivePointGrabber(QObject *exclusiveGrabber)
    { QPointerEvent::setExclusiveGrabber(points().first(), exclusiveGrabber); }

    QSinglePointEvent *clone() const override { return new QSinglePointEvent(*this); }

protected:
    QSinglePointEvent(Type type, const QPointingDevice *dev, const QEventPoint &point,
                      Qt::MouseButton button, Qt::MouseButtons buttons,
                      Qt::KeyboardModifiers modifiers, Qt::MouseEventSource source);
    QSinglePointEvent(Type type, const QPointingDevice *dev, const QPointF &localPos,
                      const QPointF &scenePos, const QPointF &globalPos,
                      Qt::MouseButton button, Qt::MouseButtons buttons,
                      Qt::KeyboardModifiers modifiers,
                      Qt::MouseEventSource source = Qt::MouseEventNotSynthesized);

    Qt::MouseButton m_button = Qt::NoButton;
    Qt::MouseButtons m_mouseState = Qt::NoButton;
    Qt::MouseEventSource m_source;
    /*
        Fill up to the next 8-byte aligned size: 88
        We have 32bits left, use some for QSinglePointEvent subclasses so that
        we don't end up with gaps.
    */
    // split this in two quint16; with a quint32, MSVC would 32-bit align it
    quint16 m_reserved;
    quint16 m_reserved2  : 11;
    // for QMouseEvent
    quint16 m_doubleClick : 1;
    // for QWheelEvent
    quint16 m_phase : 3;
    quint16 m_invertedScrolling : 1;
};

class Q_GUI_EXPORT QEnterEvent : public QSinglePointEvent
{
    Q_EVENT_DISABLE_COPY(QEnterEvent);
public:
    QEnterEvent(const QPointF &localPos, const QPointF &scenePos, const QPointF &globalPos,
                const QPointingDevice *device = QPointingDevice::primaryPointingDevice());
    ~QEnterEvent();

    QEnterEvent *clone() const override { return new QEnterEvent(*this); }

#if QT_DEPRECATED_SINCE(6, 0)
#ifndef QT_NO_INTEGER_EVENT_COORDINATES
    QT_DEPRECATED_VERSION_X_6_0("Use position()")
    inline QPoint pos() const { return position().toPoint(); }
    QT_DEPRECATED_VERSION_X_6_0("Use globalPosition()")
    inline QPoint globalPos() const { return globalPosition().toPoint(); }
    QT_DEPRECATED_VERSION_X_6_0("Use position()")
    inline int x() const { return qRound(position().x()); }
    QT_DEPRECATED_VERSION_X_6_0("Use position()")
    inline int y() const { return qRound(position().y()); }
    QT_DEPRECATED_VERSION_X_6_0("Use globalPosition()")
    inline int globalX() const { return qRound(globalPosition().x()); }
    QT_DEPRECATED_VERSION_X_6_0("Use globalPosition()")
    inline int globalY() const { return qRound(globalPosition().y()); }
#endif
    QT_DEPRECATED_VERSION_X_6_0("Use position()")
    QPointF localPos() const { return position(); }
    QT_DEPRECATED_VERSION_X_6_0("Use scenePosition()")
    QPointF windowPos() const { return scenePosition(); }
    QT_DEPRECATED_VERSION_X_6_0("Use globalPosition()")
    QPointF screenPos() const { return globalPosition(); }
#endif // QT_DEPRECATED_SINCE(6, 0)
};

class Q_GUI_EXPORT QMouseEvent : public QSinglePointEvent
{
    Q_EVENT_DISABLE_COPY(QMouseEvent);
public:
    QMouseEvent(Type type, const QPointF &localPos, Qt::MouseButton button,
                Qt::MouseButtons buttons, Qt::KeyboardModifiers modifiers,
                const QPointingDevice *device = QPointingDevice::primaryPointingDevice());
    QMouseEvent(Type type, const QPointF &localPos, const QPointF &globalPos,
                Qt::MouseButton button, Qt::MouseButtons buttons,
                Qt::KeyboardModifiers modifiers,
                const QPointingDevice *device = QPointingDevice::primaryPointingDevice());
    QMouseEvent(Type type, const QPointF &localPos, const QPointF &scenePos, const QPointF &globalPos,
                Qt::MouseButton button, Qt::MouseButtons buttons,
                Qt::KeyboardModifiers modifiers,
                const QPointingDevice *device = QPointingDevice::primaryPointingDevice());
    QMouseEvent(Type type, const QPointF &localPos, const QPointF &scenePos, const QPointF &globalPos,
                Qt::MouseButton button, Qt::MouseButtons buttons,
                Qt::KeyboardModifiers modifiers, Qt::MouseEventSource source,
                const QPointingDevice *device = QPointingDevice::primaryPointingDevice());
    ~QMouseEvent();

    QMouseEvent *clone() const override { return new QMouseEvent(*this); }

#ifndef QT_NO_INTEGER_EVENT_COORDINATES
    inline QPoint pos() const { return position().toPoint(); }
#endif
#if QT_DEPRECATED_SINCE(6, 0)
#ifndef QT_NO_INTEGER_EVENT_COORDINATES
    QT_DEPRECATED_VERSION_X_6_0("Use globalPosition()")
    inline QPoint globalPos() const { return globalPosition().toPoint(); }
    QT_DEPRECATED_VERSION_X_6_0("Use position()")
    inline int x() const { return qRound(position().x()); }
    QT_DEPRECATED_VERSION_X_6_0("Use position()")
    inline int y() const { return qRound(position().y()); }
    QT_DEPRECATED_VERSION_X_6_0("Use globalPosition()")
    inline int globalX() const { return qRound(globalPosition().x()); }
    QT_DEPRECATED_VERSION_X_6_0("Use globalPosition()")
    inline int globalY() const { return qRound(globalPosition().y()); }
#endif // QT_NO_INTEGER_EVENT_COORDINATES
    QT_DEPRECATED_VERSION_X_6_0("Use position()")
    QPointF localPos() const { return position(); }
    QT_DEPRECATED_VERSION_X_6_0("Use scenePosition()")
    QPointF windowPos() const { return scenePosition(); }
    QT_DEPRECATED_VERSION_X_6_0("Use globalPosition()")
    QPointF screenPos() const { return globalPosition(); }
    Qt::MouseEventSource source() const;
    Qt::MouseEventFlags flags() const;
#endif // QT_DEPRECATED_SINCE(6, 0)
};

class Q_GUI_EXPORT QHoverEvent : public QSinglePointEvent
{
    Q_EVENT_DISABLE_COPY(QHoverEvent);
public:
    QHoverEvent(Type type, const QPointF &pos, const QPointF &oldPos,
                Qt::KeyboardModifiers modifiers = Qt::NoModifier,
                const QPointingDevice *device = QPointingDevice::primaryPointingDevice());
    ~QHoverEvent();

    QHoverEvent *clone() const override { return new QHoverEvent(*this); }

#if QT_DEPRECATED_SINCE(6, 0)
#ifndef QT_NO_INTEGER_EVENT_COORDINATES
    QT_DEPRECATED_VERSION_X_6_0("Use position()")
    inline QPoint pos() const { return position().toPoint(); }
#endif

    QT_DEPRECATED_VERSION_X_6_0("Use position()")
    inline QPointF posF() const { return position(); }
#endif // QT_DEPRECATED_SINCE(6, 0)

    bool isUpdateEvent() const override  { return true; }

    // TODO deprecate when we figure out an actual replacement (point history?)
    inline QPoint oldPos() const { return m_oldPos.toPoint(); }
    inline QPointF oldPosF() const { return m_oldPos; }

protected:
    QPointF m_oldPos; // TODO remove?
};

#if QT_CONFIG(wheelevent)
class Q_GUI_EXPORT QWheelEvent : public QSinglePointEvent
{
    Q_GADGET
    Q_PROPERTY(const QPointingDevice *device READ pointingDevice)
    Q_PROPERTY(QPoint pixelDelta READ pixelDelta)
    Q_PROPERTY(QPoint angleDelta READ angleDelta)
    Q_PROPERTY(Qt::ScrollPhase phase READ phase)
    Q_PROPERTY(bool inverted READ inverted)

    Q_EVENT_DISABLE_COPY(QWheelEvent);
public:
    enum { DefaultDeltasPerStep = 120 };

    QWheelEvent(const QPointF &pos, const QPointF &globalPos, QPoint pixelDelta, QPoint angleDelta,
                Qt::MouseButtons buttons, Qt::KeyboardModifiers modifiers, Qt::ScrollPhase phase,
                bool inverted, Qt::MouseEventSource source = Qt::MouseEventNotSynthesized,
                const QPointingDevice *device = QPointingDevice::primaryPointingDevice());
    ~QWheelEvent();

    QWheelEvent *clone() const override { return new QWheelEvent(*this); }

    inline QPoint pixelDelta() const { return m_pixelDelta; }
    inline QPoint angleDelta() const { return m_angleDelta; }

    inline Qt::ScrollPhase phase() const { return Qt::ScrollPhase(m_phase); }
    inline bool inverted() const { return m_invertedScrolling; }
    inline bool isInverted() const { return m_invertedScrolling; }
    inline bool hasPixelDelta() const { return !m_pixelDelta.isNull(); }

    bool isBeginEvent() const override;
    bool isUpdateEvent() const override;
    bool isEndEvent() const override;
    Qt::MouseEventSource source() const { return Qt::MouseEventSource(m_source); }

protected:
    QPoint m_pixelDelta;
    QPoint m_angleDelta;
};
#endif

#if QT_CONFIG(tabletevent)
class Q_GUI_EXPORT QTabletEvent : public QSinglePointEvent
{
    Q_EVENT_DISABLE_COPY(QTabletEvent);
public:
    QTabletEvent(Type t, const QPointingDevice *device,
                 const QPointF &pos, const QPointF &globalPos,
                 qreal pressure, float xTilt, float yTilt,
                 float tangentialPressure, qreal rotation, float z,
                 Qt::KeyboardModifiers keyState,
                 Qt::MouseButton button, Qt::MouseButtons buttons);
    ~QTabletEvent();

    QTabletEvent *clone() const override { return new QTabletEvent(*this); }

#if QT_DEPRECATED_SINCE(6, 0)
    QT_DEPRECATED_VERSION_X_6_0("Use position()")
    inline QPoint pos() const { return position().toPoint(); }
    QT_DEPRECATED_VERSION_X_6_0("Use globalPosition()")
    inline QPoint globalPos() const { return globalPosition().toPoint(); }

    QT_DEPRECATED_VERSION_X_6_0("Use position()")
    inline const QPointF posF() const { return position(); }
    QT_DEPRECATED_VERSION_X_6_0("Use globalPosition()")
    inline const QPointF globalPosF() const { return globalPosition(); }
    QT_DEPRECATED_VERSION_X_6_0("Use position().x()")
    inline int x() const { return qRound(position().x()); }
    QT_DEPRECATED_VERSION_X_6_0("Use position().y()")
    inline int y() const { return qRound(position().y()); }
    QT_DEPRECATED_VERSION_X_6_0("Use globalPosition().x()")
    inline int globalX() const { return qRound(globalPosition().x()); }
    QT_DEPRECATED_VERSION_X_6_0("Use globalPosition().y()")
    inline int globalY() const { return qRound(globalPosition().y()); }
    QT_DEPRECATED_VERSION_X_6_0("use globalPosition().x()")
    inline qreal hiResGlobalX() const { return globalPosition().x(); }
    QT_DEPRECATED_VERSION_X_6_0("use globalPosition().y()")
    inline qreal hiResGlobalY() const { return globalPosition().y(); }
    QT_DEPRECATED_VERSION_X_6_0("use pointingDevice().uniqueId()")
    inline qint64 uniqueId() const { return pointingDevice() ? pointingDevice()->uniqueId().numericId() : -1; }
#endif
    inline qreal pressure() const { Q_ASSERT(!points().isEmpty()); return points().first().pressure(); }
    inline qreal rotation() const { Q_ASSERT(!points().isEmpty()); return points().first().rotation(); }
    inline qreal z() const { return m_z; }
    inline qreal tangentialPressure() const { return m_tangential; }
    inline qreal xTilt() const { return m_xTilt; }
    inline qreal yTilt() const { return m_yTilt; }

protected:
    float m_tangential;
    float m_xTilt;
    float m_yTilt;
    float m_z;
};
#endif // QT_CONFIG(tabletevent)

#if QT_CONFIG(gestures)
class Q_GUI_EXPORT QNativeGestureEvent : public QSinglePointEvent
{
    Q_EVENT_DISABLE_COPY(QNativeGestureEvent);
public:
    QNativeGestureEvent(Qt::NativeGestureType type, const QPointingDevice *dev, const QPointF &localPos, const QPointF &scenePos,
                        const QPointF &globalPos, qreal value, quint64 sequenceId, quint64 intArgument);
    ~QNativeGestureEvent();

    QNativeGestureEvent *clone() const override { return new QNativeGestureEvent(*this); }

    Qt::NativeGestureType gestureType() const { return m_gestureType; }
    qreal value() const { return m_realValue; }

#if QT_DEPRECATED_SINCE(6, 0)
#ifndef QT_NO_INTEGER_EVENT_COORDINATES
    QT_DEPRECATED_VERSION_X_6_0("Use position().toPoint()")
    inline const QPoint pos() const { return position().toPoint(); }
    QT_DEPRECATED_VERSION_X_6_0("Use globalPosition().toPoint()")
    inline const QPoint globalPos() const { return globalPosition().toPoint(); }
#endif
    QT_DEPRECATED_VERSION_X_6_0("Use position()")
    QPointF localPos() const { return position(); }
    QT_DEPRECATED_VERSION_X_6_0("Use scenePosition()")
    QPointF windowPos() const { return scenePosition(); }
    QT_DEPRECATED_VERSION_X_6_0("Use globalPosition()")
    QPointF screenPos() const { return globalPosition(); }
#endif

protected:
    quint64 m_sequenceId;
    quint64 m_intValue;
    qreal m_realValue;
    Qt::NativeGestureType m_gestureType;
    quint32 m_reserved;
};
#endif // QT_CONFIG(gestures)

class Q_GUI_EXPORT QKeyEvent : public QInputEvent
{
    Q_EVENT_DISABLE_COPY(QKeyEvent);
public:
    QKeyEvent(Type type, int key, Qt::KeyboardModifiers modifiers, const QString& text = QString(),
              bool autorep = false, quint16 count = 1);
    QKeyEvent(Type type, int key, Qt::KeyboardModifiers modifiers,
              quint32 nativeScanCode, quint32 nativeVirtualKey, quint32 nativeModifiers,
              const QString &text = QString(), bool autorep = false, quint16 count = 1,
              const QInputDevice *device = QInputDevice::primaryKeyboard());
    ~QKeyEvent();

    QKeyEvent *clone() const override { return new QKeyEvent(*this); }

    int key() const { return m_key; }
#if QT_CONFIG(shortcut)
    bool matches(QKeySequence::StandardKey key) const;
#endif
    Qt::KeyboardModifiers modifiers() const;
    QKeyCombination keyCombination() const
    {
        return QKeyCombination(modifiers(), Qt::Key(m_key));
    }
    inline QString text() const { return m_text; }
    inline bool isAutoRepeat() const { return m_autoRepeat; }
    inline int count() const { return int(m_count); }

    inline quint32 nativeScanCode() const { return m_scanCode; }
    inline quint32 nativeVirtualKey() const { return m_virtualKey; }
    inline quint32 nativeModifiers() const { return m_nativeModifiers; }

#if QT_CONFIG(shortcut)
    friend inline bool operator==(QKeyEvent *e, QKeySequence::StandardKey key)
    { return (e ? e->matches(key) : false); }
    friend inline bool operator==(QKeySequence::StandardKey key, QKeyEvent *e)
    { return (e ? e->matches(key) : false); }
#endif // QT_CONFIG(shortcut)

protected:
    QString m_text;
    int m_key;
    quint32 m_scanCode;
    quint32 m_virtualKey;
    quint32 m_nativeModifiers;
    quint16 m_count      : 15;
    quint16 m_autoRepeat : 1;
};


class Q_GUI_EXPORT QFocusEvent : public QEvent
{
    Q_EVENT_DISABLE_COPY(QFocusEvent);
public:
    explicit QFocusEvent(Type type, Qt::FocusReason reason=Qt::OtherFocusReason);
    ~QFocusEvent();

    QFocusEvent *clone() const override { return new QFocusEvent(*this); }

    inline bool gotFocus() const { return type() == FocusIn; }
    inline bool lostFocus() const { return type() == FocusOut; }

    Qt::FocusReason reason() const;

private:
    Qt::FocusReason m_reason;
};


class Q_GUI_EXPORT QPaintEvent : public QEvent
{
    Q_EVENT_DISABLE_COPY(QPaintEvent);
public:
    explicit QPaintEvent(const QRegion& paintRegion);
    explicit QPaintEvent(const QRect &paintRect);
    ~QPaintEvent();

    QPaintEvent *clone() const override { return new QPaintEvent(*this); }

    inline const QRect &rect() const { return m_rect; }
    inline const QRegion &region() const { return m_region; }

protected:
    QRect m_rect;
    QRegion m_region;
    bool m_erased;
};

class Q_GUI_EXPORT QMoveEvent : public QEvent
{
    Q_EVENT_DISABLE_COPY(QMoveEvent);
public:
    QMoveEvent(const QPoint &pos, const QPoint &oldPos);
    ~QMoveEvent();

    QMoveEvent *clone() const override { return new QMoveEvent(*this); }

    inline const QPoint &pos() const { return m_pos; }
    inline const QPoint &oldPos() const { return m_oldPos;}
protected:
    QPoint m_pos, m_oldPos;
    friend class QApplication;
};

class Q_GUI_EXPORT QExposeEvent : public QEvent
{
    Q_EVENT_DISABLE_COPY(QExposeEvent);
public:
    explicit QExposeEvent(const QRegion &m_region);
    ~QExposeEvent();

    QExposeEvent *clone() const override { return new QExposeEvent(*this); }

#if QT_DEPRECATED_SINCE(6, 0)
    QT_DEPRECATED_VERSION_X_6_0("Handle QPaintEvent instead")
    inline const QRegion &region() const { return m_region; }
#endif

protected:
    QRegion m_region;
};

class Q_GUI_EXPORT QPlatformSurfaceEvent : public QEvent
{
    Q_EVENT_DISABLE_COPY(QPlatformSurfaceEvent);
public:
    enum SurfaceEventType {
        SurfaceCreated,
        SurfaceAboutToBeDestroyed
    };

    explicit QPlatformSurfaceEvent(SurfaceEventType surfaceEventType);
    ~QPlatformSurfaceEvent();

    QPlatformSurfaceEvent *clone() const override { return new QPlatformSurfaceEvent(*this); }

    inline SurfaceEventType surfaceEventType() const { return m_surfaceEventType; }

protected:
    SurfaceEventType m_surfaceEventType;
};

class Q_GUI_EXPORT QResizeEvent : public QEvent
{
    Q_EVENT_DISABLE_COPY(QResizeEvent);
public:
    QResizeEvent(const QSize &size, const QSize &oldSize);
    ~QResizeEvent();

    QResizeEvent *clone() const override { return new QResizeEvent(*this); }

    inline const QSize &size() const { return m_size; }
    inline const QSize &oldSize()const { return m_oldSize;}
protected:
    QSize m_size, m_oldSize;
    friend class QApplication;
};


class Q_GUI_EXPORT QCloseEvent : public QEvent
{
    Q_EVENT_DISABLE_COPY(QCloseEvent);
public:
    QCloseEvent();
    ~QCloseEvent();
};


class Q_GUI_EXPORT QIconDragEvent : public QEvent
{
    Q_EVENT_DISABLE_COPY(QIconDragEvent);
public:
    QIconDragEvent();
    ~QIconDragEvent();
};


class Q_GUI_EXPORT QShowEvent : public QEvent
{
    Q_EVENT_DISABLE_COPY(QShowEvent);
public:
    QShowEvent();
    ~QShowEvent();
};


class Q_GUI_EXPORT QHideEvent : public QEvent
{
    Q_EVENT_DISABLE_COPY(QHideEvent);
public:
    QHideEvent();
    ~QHideEvent();
};

#ifndef QT_NO_CONTEXTMENU
class Q_GUI_EXPORT QContextMenuEvent : public QInputEvent
{
    Q_EVENT_DISABLE_COPY(QContextMenuEvent);
public:
    enum Reason { Mouse, Keyboard, Other };

    QContextMenuEvent(Reason reason, const QPoint &pos, const QPoint &globalPos,
                      Qt::KeyboardModifiers modifiers = Qt::NoModifier);
    QContextMenuEvent(Reason reason, const QPoint &pos);
    ~QContextMenuEvent();

    QContextMenuEvent *clone() const override { return new QContextMenuEvent(*this); }

    inline int x() const { return m_pos.x(); }
    inline int y() const { return m_pos.y(); }
    inline int globalX() const { return m_globalPos.x(); }
    inline int globalY() const { return m_globalPos.y(); }

    inline const QPoint& pos() const { return m_pos; }
    inline const QPoint& globalPos() const { return m_globalPos; }

    inline Reason reason() const { return Reason(m_reason); }

protected:
    QPoint m_pos;
    QPoint m_globalPos;
    uint m_reason : 8;
};
#endif // QT_NO_CONTEXTMENU

#ifndef QT_NO_INPUTMETHOD
class Q_GUI_EXPORT QInputMethodEvent : public QEvent
{
    Q_EVENT_DISABLE_COPY(QInputMethodEvent);
public:
    enum AttributeType {
       TextFormat,
       Cursor,
       Language,
       Ruby,
       Selection
    };
    class Attribute {
    public:
        Attribute(AttributeType typ, int s, int l, QVariant val) : type(typ), start(s), length(l), value(std::move(val)) {}
        Attribute(AttributeType typ, int s, int l) : type(typ), start(s), length(l), value() {}

        AttributeType type;
        int start;
        int length;
        QVariant value;
    };
    QInputMethodEvent();
    QInputMethodEvent(const QString &preeditText, const QList<Attribute> &attributes);
    ~QInputMethodEvent();

    QInputMethodEvent *clone() const override { return new QInputMethodEvent(*this); }

    void setCommitString(const QString &commitString, int replaceFrom = 0, int replaceLength = 0);
    inline const QList<Attribute> &attributes() const { return m_attributes; }
    inline const QString &preeditString() const { return m_preedit; }

    inline const QString &commitString() const { return m_commit; }
    inline int replacementStart() const { return m_replacementStart; }
    inline int replacementLength() const { return m_replacementLength; }

    inline friend bool operator==(const QInputMethodEvent::Attribute &lhs,
                                  const QInputMethodEvent::Attribute &rhs)
    {
        return lhs.type == rhs.type && lhs.start == rhs.start
                && lhs.length == rhs.length && lhs.value == rhs.value;
    }

    inline friend bool operator!=(const QInputMethodEvent::Attribute &lhs,
                                  const QInputMethodEvent::Attribute &rhs)
    {
        return !(lhs == rhs);
    }

private:
    QString m_preedit;
    QString m_commit;
    QList<Attribute> m_attributes;
    int m_replacementStart;
    int m_replacementLength;
};
Q_DECLARE_TYPEINFO(QInputMethodEvent::Attribute, Q_RELOCATABLE_TYPE);

class Q_GUI_EXPORT QInputMethodQueryEvent : public QEvent
{
    Q_EVENT_DISABLE_COPY(QInputMethodQueryEvent);
public:
    explicit QInputMethodQueryEvent(Qt::InputMethodQueries queries);
    ~QInputMethodQueryEvent();

    QInputMethodQueryEvent *clone() const override { return new QInputMethodQueryEvent(*this); }

    Qt::InputMethodQueries queries() const { return m_queries; }

    void setValue(Qt::InputMethodQuery query, const QVariant &value);
    QVariant value(Qt::InputMethodQuery query) const;
private:
    Qt::InputMethodQueries m_queries;
    struct QueryPair {
        Qt::InputMethodQuery query;
        QVariant value;
    };
    friend QTypeInfo<QueryPair>;
    QList<QueryPair> m_values;
};
Q_DECLARE_TYPEINFO(QInputMethodQueryEvent::QueryPair, Q_RELOCATABLE_TYPE);

#endif // QT_NO_INPUTMETHOD

#if QT_CONFIG(draganddrop)

class QMimeData;

class Q_GUI_EXPORT QDropEvent : public QEvent
{
    Q_EVENT_DISABLE_COPY(QDropEvent);
public:
    QDropEvent(const QPointF& pos, Qt::DropActions actions, const QMimeData *data,
               Qt::MouseButtons buttons, Qt::KeyboardModifiers modifiers, Type type = Drop);
    ~QDropEvent();

    QDropEvent *clone() const override { return new QDropEvent(*this); }

#if QT_DEPRECATED_SINCE(6, 0)
    QT_DEPRECATED_VERSION_X_6_0("Use position().toPoint()")
    inline QPoint pos() const { return position().toPoint(); }
    QT_DEPRECATED_VERSION_X_6_0("Use position()")
    inline QPointF posF() const { return position(); }
    QT_DEPRECATED_VERSION_X_6_0("Use buttons()")
    inline Qt::MouseButtons mouseButtons() const { return buttons(); }
    QT_DEPRECATED_VERSION_X_6_0("Use modifiers()")
    inline Qt::KeyboardModifiers keyboardModifiers() const { return modifiers(); }
#endif // QT_DEPRECATED_SINCE(6, 0)

    QPointF position() const { return m_pos; }
    inline Qt::MouseButtons buttons() const { return m_mouseState; }
    inline Qt::KeyboardModifiers modifiers() const { return m_modState; }

    inline Qt::DropActions possibleActions() const { return m_actions; }
    inline Qt::DropAction proposedAction() const { return m_defaultAction; }
    inline void acceptProposedAction() { m_dropAction = m_defaultAction; accept(); }

    inline Qt::DropAction dropAction() const { return m_dropAction; }
    void setDropAction(Qt::DropAction action);

    QObject* source() const;
    inline const QMimeData *mimeData() const { return m_data; }

protected:
    friend class QApplication;
    QPointF m_pos;
    Qt::MouseButtons m_mouseState;
    Qt::KeyboardModifiers m_modState;
    Qt::DropActions m_actions;
    Qt::DropAction m_dropAction;
    Qt::DropAction m_defaultAction;
    const QMimeData *m_data;
};


class Q_GUI_EXPORT QDragMoveEvent : public QDropEvent
{
    Q_EVENT_DISABLE_COPY(QDragMoveEvent);
public:
    QDragMoveEvent(const QPoint &pos, Qt::DropActions actions, const QMimeData *data,
                   Qt::MouseButtons buttons, Qt::KeyboardModifiers modifiers, Type type = DragMove);
    ~QDragMoveEvent();

    QDragMoveEvent *clone() const override { return new QDragMoveEvent(*this); }

    inline QRect answerRect() const { return m_rect; }

    inline void accept() { QDropEvent::accept(); }
    inline void ignore() { QDropEvent::ignore(); }

    inline void accept(const QRect & r) { accept(); m_rect = r; }
    inline void ignore(const QRect & r) { ignore(); m_rect = r; }

protected:
    QRect m_rect;
};


class Q_GUI_EXPORT QDragEnterEvent : public QDragMoveEvent
{
    Q_EVENT_DISABLE_COPY(QDragEnterEvent);
public:
    QDragEnterEvent(const QPoint &pos, Qt::DropActions actions, const QMimeData *data,
                    Qt::MouseButtons buttons, Qt::KeyboardModifiers modifiers);
    ~QDragEnterEvent();
};


class Q_GUI_EXPORT QDragLeaveEvent : public QEvent
{
    Q_EVENT_DISABLE_COPY(QDragLeaveEvent);
public:
    QDragLeaveEvent();
    ~QDragLeaveEvent();
};
#endif // QT_CONFIG(draganddrop)


class Q_GUI_EXPORT QHelpEvent : public QEvent
{
    Q_EVENT_DISABLE_COPY(QHelpEvent);
public:
    QHelpEvent(Type type, const QPoint &pos, const QPoint &globalPos);
    ~QHelpEvent();

    QHelpEvent *clone() const override { return new QHelpEvent(*this); }

    inline int x() const { return m_pos.x(); }
    inline int y() const { return m_pos.y(); }
    inline int globalX() const { return m_globalPos.x(); }
    inline int globalY() const { return m_globalPos.y(); }

    inline const QPoint& pos()  const { return m_pos; }
    inline const QPoint& globalPos() const { return m_globalPos; }

private:
    QPoint m_pos;
    QPoint m_globalPos;
};

#ifndef QT_NO_STATUSTIP
class Q_GUI_EXPORT QStatusTipEvent : public QEvent
{
    Q_EVENT_DISABLE_COPY(QStatusTipEvent);
public:
    explicit QStatusTipEvent(const QString &tip);
    ~QStatusTipEvent();

    QStatusTipEvent *clone() const override { return new QStatusTipEvent(*this); }

    inline QString tip() const { return m_tip; }
private:
    QString m_tip;
};
#endif

#if QT_CONFIG(whatsthis)
class Q_GUI_EXPORT QWhatsThisClickedEvent : public QEvent
{
    Q_EVENT_DISABLE_COPY(QWhatsThisClickedEvent);
public:
    explicit QWhatsThisClickedEvent(const QString &href);
    ~QWhatsThisClickedEvent();

    QWhatsThisClickedEvent *clone() const override { return new QWhatsThisClickedEvent(*this); }

    inline QString href() const { return m_href; }
private:
    QString m_href;
};
#endif

#if QT_CONFIG(action)
class Q_GUI_EXPORT QActionEvent : public QEvent
{
    Q_EVENT_DISABLE_COPY(QActionEvent);
public:
    QActionEvent(int type, QAction *action, QAction *before = nullptr);
    ~QActionEvent();

    QActionEvent *clone() const override { return new QActionEvent(*this); }

    inline QAction *action() const { return m_action; }
    inline QAction *before() const { return m_before; }
private:
    QAction *m_action;
    QAction *m_before;
};
#endif // QT_CONFIG(action)

class Q_GUI_EXPORT QFileOpenEvent : public QEvent
{
    Q_EVENT_DISABLE_COPY(QFileOpenEvent);
public:
    explicit QFileOpenEvent(const QString &file);
    explicit QFileOpenEvent(const QUrl &url);
    ~QFileOpenEvent();

    QFileOpenEvent *clone() const override { return new QFileOpenEvent(*this); }

    inline QString file() const { return m_file; }
    QUrl url() const { return m_url; }
    bool openFile(QFile &file, QIODevice::OpenMode flags) const;
private:
    QString m_file;
    QUrl m_url;
};

#ifndef QT_NO_TOOLBAR
class Q_GUI_EXPORT QToolBarChangeEvent : public QEvent
{
    Q_EVENT_DISABLE_COPY(QToolBarChangeEvent);
public:
    explicit QToolBarChangeEvent(bool t);
    ~QToolBarChangeEvent();

    QToolBarChangeEvent *clone() const override { return new QToolBarChangeEvent(*this); }

    inline bool toggle() const { return m_toggle; }
private:
    bool m_toggle;
};
#endif

#if QT_CONFIG(shortcut)
class Q_GUI_EXPORT QShortcutEvent : public QEvent
{
    Q_EVENT_DISABLE_COPY(QShortcutEvent);
public:
    QShortcutEvent(const QKeySequence &key, int id, bool ambiguous = false);
    ~QShortcutEvent();

    QShortcutEvent *clone() const override { return new QShortcutEvent(*this); }

    inline const QKeySequence &key() const { return m_sequence; }
    inline int shortcutId() const { return m_shortcutId; }
    inline bool isAmbiguous() const { return m_ambiguous; }
protected:
    QKeySequence m_sequence;
    int  m_shortcutId;
    bool m_ambiguous;
};
#endif

class Q_GUI_EXPORT QWindowStateChangeEvent: public QEvent
{
    Q_EVENT_DISABLE_COPY(QWindowStateChangeEvent);
public:
    explicit QWindowStateChangeEvent(Qt::WindowStates oldState, bool isOverride = false);
    ~QWindowStateChangeEvent();

    QWindowStateChangeEvent *clone() const override { return new QWindowStateChangeEvent(*this); }

    inline Qt::WindowStates oldState() const { return m_oldStates; }
    bool isOverride() const;

private:
    Qt::WindowStates m_oldStates;
    bool m_override;
};

#ifndef QT_NO_DEBUG_STREAM
Q_GUI_EXPORT QDebug operator<<(QDebug, const QEvent *);
#endif

class Q_GUI_EXPORT QTouchEvent : public QPointerEvent
{
    Q_EVENT_DISABLE_COPY(QTouchEvent);
public:
    using TouchPoint = QEventPoint; // source compat

    explicit QTouchEvent(QEvent::Type eventType,
                         const QPointingDevice *device = nullptr,
                         Qt::KeyboardModifiers modifiers = Qt::NoModifier,
                         const QList<QEventPoint> &touchPoints = {});
#if QT_DEPRECATED_SINCE(6, 0)
    QT_DEPRECATED_VERSION_X_6_0("Use another constructor")
    explicit QTouchEvent(QEvent::Type eventType,
                         const QPointingDevice *device,
                         Qt::KeyboardModifiers modifiers,
                         QEventPoint::States touchPointStates,
                         const QList<QEventPoint> &touchPoints = {});
#endif
    ~QTouchEvent();

    QTouchEvent *clone() const override { return new QTouchEvent(*this); }

    inline QObject *target() const { return m_target; }
    inline QEventPoint::States touchPointStates() const { return m_touchPointStates; }
#if QT_DEPRECATED_SINCE(6, 0)
    QT_DEPRECATED_VERSION_X_6_0("Use points()")
    const QList<QEventPoint> &touchPoints() const { return points(); }
#endif
    bool isBeginEvent() const override;
    bool isUpdateEvent() const override;
    bool isEndEvent() const override;

protected:
    QObject *m_target = nullptr;
    QEventPoint::States m_touchPointStates = QEventPoint::State::Unknown;
    quint32 m_reserved : 24;
};

class Q_GUI_EXPORT QScrollPrepareEvent : public QEvent
{
    Q_EVENT_DISABLE_COPY(QScrollPrepareEvent);
public:
    explicit QScrollPrepareEvent(const QPointF &startPos);
    ~QScrollPrepareEvent();

    QScrollPrepareEvent *clone() const override { return new QScrollPrepareEvent(*this); }

    QPointF startPos() const { return m_startPos; }

    QSizeF viewportSize() const { return m_viewportSize; }
    QRectF contentPosRange() const { return m_contentPosRange; }
    QPointF contentPos() const { return m_contentPos; }

    void setViewportSize(const QSizeF &size);
    void setContentPosRange(const QRectF &rect);
    void setContentPos(const QPointF &pos);

private:
    QRectF m_contentPosRange;
    QSizeF m_viewportSize;
    QPointF m_startPos;
    QPointF m_contentPos;
};


class Q_GUI_EXPORT QScrollEvent : public QEvent
{
    Q_EVENT_DISABLE_COPY(QScrollEvent);
public:
    enum ScrollState
    {
        ScrollStarted,
        ScrollUpdated,
        ScrollFinished
    };

    QScrollEvent(const QPointF &contentPos, const QPointF &overshoot, ScrollState scrollState);
    ~QScrollEvent();

    QScrollEvent *clone() const override { return new QScrollEvent(*this); }

    QPointF contentPos() const { return m_contentPos; }
    QPointF overshootDistance() const { return m_overshoot; }
    ScrollState scrollState() const { return m_state; }

private:
    QPointF m_contentPos;
    QPointF m_overshoot;
    QScrollEvent::ScrollState m_state;
};

class Q_GUI_EXPORT QScreenOrientationChangeEvent : public QEvent
{
    Q_EVENT_DISABLE_COPY(QScreenOrientationChangeEvent);
public:
    QScreenOrientationChangeEvent(QScreen *screen, Qt::ScreenOrientation orientation);
    ~QScreenOrientationChangeEvent();

    QScreenOrientationChangeEvent *clone() const override { return new QScreenOrientationChangeEvent(*this); }

    QScreen *screen() const { return m_screen; }
    Qt::ScreenOrientation orientation() const { return m_orientation; }

private:
    QScreen *m_screen;
    Qt::ScreenOrientation m_orientation;
};

class Q_GUI_EXPORT QApplicationStateChangeEvent : public QEvent
{
    Q_EVENT_DISABLE_COPY(QApplicationStateChangeEvent);
public:
    explicit QApplicationStateChangeEvent(Qt::ApplicationState state);

    QApplicationStateChangeEvent *clone() const override { return new QApplicationStateChangeEvent(*this); }

    Qt::ApplicationState applicationState() const { return m_applicationState; }

private:
    Qt::ApplicationState m_applicationState;
};

QT_END_NAMESPACE

#endif // QEVENT_H
