/****************************************************************************
**
** Copyright (C) 2017 The Qt Company Ltd.
** Contact: https://www.qt.io/licensing/
**
** This file is part of the Qt Quick Controls 2 module of the Qt Toolkit.
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
import QtQuick.Controls.impl
import QtQuick.Controls.Fusion
import QtQuick.Controls.Fusion.impl

Rectangle {
    id: indicator

    property Item control
    readonly property color pressedColor: Fusion.mergedColors(control.palette.base, control.palette.windowText, 85)
    readonly property color checkMarkColor: Qt.darker(control.palette.text, 1.2)

    implicitWidth: 14
    implicitHeight: 14

    radius: width / 2
    color: control.down ? indicator.pressedColor : control.palette.base
    border.color: control.visualFocus ? Fusion.highlightedOutline(control.palette)
                                      : Qt.darker(control.palette.window, 1.5)

    Rectangle {
        y: 1
        width: parent.width
        height: parent.height - 1
        radius: width / 2
        color: "transparent"
        border.color: Fusion.topShadow
        visible: indicator.control.enabled && !indicator.control.down
    }

    Rectangle {
        x: (parent.width - width) / 2
        y: (parent.height - height) / 2
        width: parent.width / 2.32
        height: parent.height / 2.32
        radius: width / 2
        color: Color.transparent(indicator.checkMarkColor, 180 / 255)
        border.color: Color.transparent(indicator.checkMarkColor, 200 / 255)
        visible: indicator.control.checked
    }
}
