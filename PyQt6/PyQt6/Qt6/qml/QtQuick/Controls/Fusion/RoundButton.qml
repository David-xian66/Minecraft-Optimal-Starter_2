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
import QtQuick.Templates as T
import QtQuick.Controls.impl
import QtQuick.Controls.Fusion
import QtQuick.Controls.Fusion.impl

T.RoundButton {
    id: control

    implicitWidth: Math.max(implicitBackgroundWidth + leftInset + rightInset,
                            implicitContentWidth + leftPadding + rightPadding)
    implicitHeight: Math.max(implicitBackgroundHeight + topInset + bottomInset,
                             implicitContentHeight + topPadding + bottomPadding)

    padding: 6
    spacing: 6

    icon.width: 16
    icon.height: 16

    contentItem: IconLabel {
        spacing: control.spacing
        mirrored: control.mirrored
        display: control.display

        icon: control.icon
        text: control.text
        font: control.font
        color: control.palette.buttonText
    }

    background: Rectangle {
        implicitWidth: 32
        implicitHeight: 32
        visible: !control.flat || control.down || control.checked

        gradient: Gradient {
            GradientStop {
                position: 0
                color: control.down || control.checked ? Fusion.buttonColor(control.palette, control.highlighted, control.down || control.checked, control.hovered)
                                                       : Fusion.gradientStart(Fusion.buttonColor(control.palette, control.highlighted, control.down, control.hovered))
            }
            GradientStop {
                position: 1
                color: control.down || control.checked ? Fusion.buttonColor(control.palette, control.highlighted, control.down || control.checked, control.hovered)
                                                       : Fusion.gradientStop(Fusion.buttonColor(control.palette, control.highlighted, control.down, control.hovered))
            }
        }

        radius: control.radius
        border.color: Fusion.buttonOutline(control.palette, control.highlighted || control.visualFocus, control.enabled)

        Rectangle {
            x: 1; y: 1
            width: parent.width - 2
            height: parent.height - 2
            border.color: Fusion.innerContrastLine
            color: "transparent"
            radius: control.radius
        }
    }
}
