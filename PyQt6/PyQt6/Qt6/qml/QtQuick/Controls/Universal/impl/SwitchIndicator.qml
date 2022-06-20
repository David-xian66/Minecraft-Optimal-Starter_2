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
import QtQuick.Controls.Universal

Item {
    id: indicator
    implicitWidth: 44
    implicitHeight: 20

    property T.AbstractButton control

    Rectangle {
        width: parent.width
        height: parent.height

        radius: 10
        color: !indicator.control.enabled ? "transparent" :
                indicator.control.pressed ? indicator.control.Universal.baseMediumColor :
                indicator.control.checked ? indicator.control.Universal.accent : "transparent"
        border.color: !indicator.control.enabled ? indicator.control.Universal.baseLowColor :
                       indicator.control.checked && !indicator.control.pressed ? indicator.control.Universal.accent :
                       indicator.control.hovered && !indicator.control.checked && !indicator.control.pressed ? indicator.control.Universal.baseHighColor : indicator.control.Universal.baseMediumColor
        opacity: indicator.control.hovered && indicator.control.checked && !indicator.control.pressed ? (indicator.control.Universal.theme === Universal.Light ? 0.7 : 0.9) : 1.0
        border.width: 2
    }

    Rectangle {
        width: 10
        height: 10
        radius: 5

        color: !indicator.control.enabled ? indicator.control.Universal.baseLowColor :
                indicator.control.pressed || indicator.control.checked ? indicator.control.Universal.chromeWhiteColor :
                indicator.control.hovered && !indicator.control.checked ? indicator.control.Universal.baseHighColor : indicator.control.Universal.baseMediumHighColor

        x: Math.max(5, Math.min(parent.width - width - 5,
                                indicator.control.visualPosition * parent.width - (width / 2)))
        y: (parent.height - height) / 2

        Behavior on x {
            enabled: !indicator.control.pressed
            SmoothedAnimation { velocity: 200 }
        }
    }
}
