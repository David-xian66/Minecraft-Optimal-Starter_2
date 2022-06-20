/****************************************************************************
**
** Copyright (C) 2016 The Qt Company Ltd.
** Contact: https://www.qt.io/licensing/
**
** This file is part of the QtQuick module of the Qt Toolkit.
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

#ifndef QQUICKWINDOW_H
#define QQUICKWINDOW_H

#include <QtQuick/qtquickglobal.h>
#include <QtQuick/qsgrendererinterface.h>

#include <QtCore/qmetatype.h>
#include <QtGui/qwindow.h>
#include <QtGui/qevent.h>
#include <QtQml/qqml.h>
#include <QtQml/qqmldebug.h>

QT_BEGIN_NAMESPACE

class QRunnable;
class QQuickItem;
class QSGTexture;
class QInputMethodEvent;
class QQuickWindowPrivate;
class QQuickWindowAttached;
class QQmlIncubationController;
class QInputMethodEvent;
class QQuickCloseEvent;
class QQuickRenderControl;
class QSGRectangleNode;
class QSGImageNode;
class QSGNinePatchNode;
class QQuickRenderTarget;
class QQuickGraphicsDevice;
class QQuickGraphicsConfiguration;

class Q_QUICK_EXPORT QQuickWindow : public QWindow
{
    Q_OBJECT
    Q_PRIVATE_PROPERTY(QQuickWindow::d_func(), QQmlListProperty<QObject> data READ data DESIGNABLE false)
    Q_PROPERTY(QColor color READ color WRITE setColor NOTIFY colorChanged)
    Q_PROPERTY(QQuickItem* contentItem READ contentItem CONSTANT)
    Q_PROPERTY(QQuickItem* activeFocusItem READ activeFocusItem NOTIFY activeFocusItemChanged REVISION(2, 1))
    QDOC_PROPERTY(QWindow* transientParent READ transientParent WRITE setTransientParent NOTIFY transientParentChanged)
    Q_CLASSINFO("DefaultProperty", "data")
    Q_DECLARE_PRIVATE(QQuickWindow)

    QML_NAMED_ELEMENT(Window)
    QML_ADDED_IN_VERSION(2, 0)
    QML_REMOVED_IN_VERSION(2, 1)
public:
    enum CreateTextureOption {
        TextureHasAlphaChannel  = 0x0001,
        TextureHasMipmaps       = 0x0002,
        TextureOwnsGLTexture    = 0x0004,
        TextureCanUseAtlas      = 0x0008,
        TextureIsOpaque         = 0x0010
    };

    enum RenderStage {
        BeforeSynchronizingStage,
        AfterSynchronizingStage,
        BeforeRenderingStage,
        AfterRenderingStage,
        AfterSwapStage,
        NoStage
    };

    Q_DECLARE_FLAGS(CreateTextureOptions, CreateTextureOption)
    Q_FLAG(CreateTextureOptions)

    enum SceneGraphError {
        ContextNotAvailable = 1
    };
    Q_ENUM(SceneGraphError)

    enum TextRenderType {
        QtTextRendering,
        NativeTextRendering
    };
    Q_ENUM(TextRenderType)

    explicit QQuickWindow(QWindow *parent = nullptr);
    explicit QQuickWindow(QQuickRenderControl *renderControl);

    ~QQuickWindow() override;

    QQuickItem *contentItem() const;

    QQuickItem *activeFocusItem() const;
    QObject *focusObject() const override;

    QQuickItem *mouseGrabberItem() const;

    QImage grabWindow();

    void setRenderTarget(const QQuickRenderTarget &target);
    QQuickRenderTarget renderTarget() const;

    struct GraphicsStateInfo {
        int currentFrameSlot;
        int framesInFlight;
    };
    const GraphicsStateInfo &graphicsStateInfo();
    void beginExternalCommands();
    void endExternalCommands();
    QQmlIncubationController *incubationController() const;

#if QT_CONFIG(accessibility)
    QAccessibleInterface *accessibleRoot() const override;
#endif

    // Scene graph specific functions
    QSGTexture *createTextureFromImage(const QImage &image) const;
    QSGTexture *createTextureFromImage(const QImage &image, CreateTextureOptions options) const;

    void setColor(const QColor &color);
    QColor color() const;

    static bool hasDefaultAlphaBuffer();
    static void setDefaultAlphaBuffer(bool useAlpha);

    void setPersistentGraphics(bool persistent);
    bool isPersistentGraphics() const;

    void setPersistentSceneGraph(bool persistent);
    bool isPersistentSceneGraph() const;

    bool isSceneGraphInitialized() const;

    void scheduleRenderJob(QRunnable *job, RenderStage schedule);

    qreal effectiveDevicePixelRatio() const;

    QSGRendererInterface *rendererInterface() const;

    static void setGraphicsApi(QSGRendererInterface::GraphicsApi api);
    static QSGRendererInterface::GraphicsApi graphicsApi();

    static void setSceneGraphBackend(const QString &backend);
    static QString sceneGraphBackend();

    void setGraphicsDevice(const QQuickGraphicsDevice &device);
    QQuickGraphicsDevice graphicsDevice() const;

    void setGraphicsConfiguration(const QQuickGraphicsConfiguration &config);
    QQuickGraphicsConfiguration graphicsConfiguration() const;

    QSGRectangleNode *createRectangleNode() const;
    QSGImageNode *createImageNode() const;
    QSGNinePatchNode *createNinePatchNode() const;

    static TextRenderType textRenderType();
    static void setTextRenderType(TextRenderType renderType);

Q_SIGNALS:
    void frameSwapped();
    void sceneGraphInitialized();
    void sceneGraphInvalidated();
    void beforeSynchronizing();
    Q_REVISION(2, 2) void afterSynchronizing();
    void beforeRendering();
    void afterRendering();
    Q_REVISION(2, 2) void afterAnimating();
    Q_REVISION(2, 2) void sceneGraphAboutToStop();

    Q_REVISION(2, 1) void closing(QQuickCloseEvent *close);
    void colorChanged(const QColor &);
    Q_REVISION(2, 1) void activeFocusItemChanged();
    Q_REVISION(2, 2) void sceneGraphError(QQuickWindow::SceneGraphError error, const QString &message);

    Q_REVISION(2, 14) void beforeRenderPassRecording();
    Q_REVISION(2, 14) void afterRenderPassRecording();

    Q_REVISION(6, 0) void paletteChanged();
    Q_REVISION(6, 0) void paletteCreated();

    Q_REVISION(6, 0) void beforeFrameBegin();
    Q_REVISION(6, 0) void afterFrameEnd();

public Q_SLOTS:
    void update();
    void releaseResources();

protected:
    QQuickWindow(QQuickWindowPrivate &dd, QWindow *parent = nullptr);
    QQuickWindow(QQuickWindowPrivate &dd, QQuickRenderControl *control);

    void exposeEvent(QExposeEvent *) override;
    void resizeEvent(QResizeEvent *) override;

    void showEvent(QShowEvent *) override;
    void hideEvent(QHideEvent *) override;
    void closeEvent(QCloseEvent *) override;

    void focusInEvent(QFocusEvent *) override;
    void focusOutEvent(QFocusEvent *) override;

    bool event(QEvent *) override;

    // These overrides are no longer normal entry points for
    // input events, but kept in case legacy code calls them.
    void keyPressEvent(QKeyEvent *) override;
    void keyReleaseEvent(QKeyEvent *) override;
    void mousePressEvent(QMouseEvent *) override;
    void mouseReleaseEvent(QMouseEvent *) override;
    void mouseDoubleClickEvent(QMouseEvent *) override;
    void mouseMoveEvent(QMouseEvent *) override;
#if QT_CONFIG(wheelevent)
    void wheelEvent(QWheelEvent *) override;
#endif
#if QT_CONFIG(tabletevent)
    void tabletEvent(QTabletEvent *) override;
#endif

private Q_SLOTS:
    void maybeUpdate();
    void cleanupSceneGraph();
    void physicalDpiChanged();
    void handleScreenChanged(QScreen *screen);
    void setTransientParent_helper(QQuickWindow *window);
    void runJobsAfterSwap();
    void handleApplicationStateChanged(Qt::ApplicationState state);
private:
    friend class QQuickItem;
    friend class QQuickWidget;
    friend class QQuickRenderControl;
    friend class QQuickAnimatorController;
    friend class QQuickWidgetPrivate;
    friend class QQuickDeliveryAgentPrivate;
    Q_DISABLE_COPY(QQuickWindow)
};

#ifndef QT_NO_DEBUG_STREAM
QDebug Q_QUICK_EXPORT operator<<(QDebug debug, const QQuickWindow *item);
#endif

QT_END_NAMESPACE

Q_DECLARE_METATYPE(QQuickWindow *)

#endif // QQUICKWINDOW_H

