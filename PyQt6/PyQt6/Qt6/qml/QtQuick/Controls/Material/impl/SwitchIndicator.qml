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
import QtQuick.Controls.Material
import QtQuick.Controls.Material.impl

Item {
    id: indicator
    implicitWidth: 38
    implicitHeight: 32

    property T.AbstractButton control
    property alias handle: handle

    Material.elevation: 1

    Rectangle {
        width: parent.width
        height: 14
        radius: height / 2
        y: parent.height / 2 - height / 2
        color: indicator.control.enabled ? (indicator.control.checked ? indicator.control.Material.switchCheckedTrackColor : indicator.control.Material.switchUncheckedTrackColor)
                               : indicator.control.Material.switchDisabledTrackColor
    }

    Rectangle {
        id: handle
        x: Math.max(0, Math.min(parent.width - width, indicator.control.visualPosition * parent.width - (width / 2)))
        y: (parent.height - height) / 2
        width: 20
        height: 20
        radius: width / 2
        color: indicator.control.enabled ? (indicator.control.checked ? indicator.control.Material.switchCheckedHandleColor : indicator.control.Material.switchUncheckedHandleColor)
                               : indicator.control.Material.switchDisabledHandleColor

        Behavior on x {
            enabled: !indicator.control.pressed
            SmoothedAnimation {
                duration: 300
            }
        }
        layer.enabled: indicator.Material.elevation > 0
        layer.effect: ElevationEffect {
            elevation: indicator.Material.elevation
        }
    }
}
