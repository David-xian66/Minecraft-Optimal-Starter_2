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

#ifndef QOPENGLCONTEXT_PLATFORM_H
#define QOPENGLCONTEXT_PLATFORM_H

#ifndef QT_NO_OPENGL

#include <QtGui/qtguiglobal.h>
#include <QtGui/qopenglcontext.h>
#include <QtGui/qwindowdefs.h>

#if defined(Q_OS_MACOS)
Q_FORWARD_DECLARE_OBJC_CLASS(NSOpenGLContext);
#endif

#if defined(Q_OS_LINUX)
struct __GLXcontextRec; typedef struct __GLXcontextRec *GLXContext;
#endif
#if QT_CONFIG(egl)
typedef void *EGLContext;
typedef void *EGLDisplay;
#endif

#if !defined(Q_OS_MACOS) && defined(Q_CLANG_QDOC)
typedef void *NSOpenGLContext;
#endif

QT_BEGIN_NAMESPACE

namespace QNativeInterface {

#if defined(Q_OS_MACOS) || defined(Q_CLANG_QDOC)
struct Q_GUI_EXPORT QCocoaGLContext
{
    QT_DECLARE_NATIVE_INTERFACE(QCocoaGLContext)
    static QOpenGLContext *fromNative(QT_IGNORE_DEPRECATIONS(NSOpenGLContext) *context, QOpenGLContext *shareContext = nullptr);
    virtual QT_IGNORE_DEPRECATIONS(NSOpenGLContext) *nativeContext() const = 0;
};
#endif

#if defined(Q_OS_WIN) || defined(Q_CLANG_QDOC)
struct Q_GUI_EXPORT QWGLContext
{
    QT_DECLARE_NATIVE_INTERFACE(QWGLContext)
    static HMODULE openGLModuleHandle();
    static QOpenGLContext *fromNative(HGLRC context, HWND window, QOpenGLContext *shareContext = nullptr);
    virtual HGLRC nativeContext() const = 0;
};
#endif

#if defined(Q_OS_LINUX) || defined(Q_CLANG_QDOC)
struct Q_GUI_EXPORT QGLXContext
{
    QT_DECLARE_NATIVE_INTERFACE(QGLXContext)
    static QOpenGLContext *fromNative(GLXContext configBasedContext, QOpenGLContext *shareContext = nullptr);
    static QOpenGLContext *fromNative(GLXContext visualBasedContext, void *visualInfo, QOpenGLContext *shareContext = nullptr);
    virtual GLXContext nativeContext() const = 0;
};
#endif

#if QT_CONFIG(egl) || defined(Q_CLANG_QDOC)
struct Q_GUI_EXPORT QEGLContext
{
    QT_DECLARE_NATIVE_INTERFACE(QEGLContext)
    static QOpenGLContext *fromNative(EGLContext context, EGLDisplay display, QOpenGLContext *shareContext = nullptr);
    virtual EGLContext nativeContext() const = 0;
};
#endif

} // QNativeInterface

QT_END_NAMESPACE

#endif // QT_NO_OPENGL

#endif // QOPENGLCONTEXT_PLATFORM_H
