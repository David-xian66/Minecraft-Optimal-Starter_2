/****************************************************************************
**
** Copyright (C) 2021 The Qt Company Ltd.
** Contact: https://www.qt.io/licensing/
**
** This file is part of the Qt Quick Dialogs module of the Qt Toolkit.
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

import QtQuick
import QtQuick.Controls
import QtQuick.Controls.impl as ControlsImpl
import QtQuick.Dialogs.quickimpl as DialogsQuickImpl

DialogsQuickImpl.FileDialogDelegate {
    id: control

    implicitWidth: Math.max(implicitBackgroundWidth + leftInset + rightInset,
                            implicitContentWidth + leftPadding + rightPadding)
    implicitHeight: Math.max(implicitBackgroundHeight + topInset + bottomInset,
                             implicitContentHeight + topPadding + bottomPadding,
                             implicitIndicatorHeight + topPadding + bottomPadding)

    padding: 12
    spacing: 8
    topPadding: 0
    bottomPadding: 0

    file: fileUrl

    icon.width: 16
    icon.height: 16
    icon.color: highlighted ? palette.highlightedText : palette.text
    icon.source: "qrc:/qt-project.org/imports/QtQuick/Dialogs/quickimpl/images/folder-icon-round.png"

    // We don't use index here, but in C++. Since we're using required
    // properties, the index context property will not be injected, so we can't
    // use its QQmlContext to access it.
    required property int index
    required property string fileName
    required property url fileUrl
    required property date fileModified

    contentItem: FolderDialogDelegateLabel {
        delegate: control
        fileDetailRowTextColor: Qt.lighter(control.icon.color)
    }

    background: Rectangle {
        implicitWidth: 100
        implicitHeight: 40
        visible: control.down || control.highlighted || control.visualFocus
        color: Color.blend(control.down ? control.palette.midlight : control.palette.light,
                                          control.palette.highlight, control.highlighted ? 0.15 : 0.0)
    }
}
