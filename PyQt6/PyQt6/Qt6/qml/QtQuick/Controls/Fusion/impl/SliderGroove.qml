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
    id: groove

    property Item control
    property real offset
    property real progress
    property real visualProgress

    x: control.horizontal ? 0 : (control.availableWidth - width) / 2
    y: control.horizontal ? (control.availableHeight - height) / 2 : 0

    implicitWidth: control.horizontal ? 160 : 5
    implicitHeight: control.horizontal ? 5 : 160
    width: control.horizontal ? control.availableWidth : implicitWidth
    height: control.horizontal ? implicitHeight : control.availableHeight

    radius: 2
    border.color: Fusion.outline(control.palette)
    scale: control.horizontal && control.mirrored ? -1 : 1

    gradient: Gradient {
        GradientStop {
            position: 0
            color: Qt.darker(Fusion.grooveColor(groove.control.palette), 1.1)
        }
        GradientStop {
            position: 1
            color: Qt.lighter(Fusion.grooveColor(groove.control.palette), 1.1)
        }
    }

    Rectangle {
        x: groove.control.horizontal ? groove.offset * parent.width : 0
        y: groove.control.horizontal ? 0 : groove.visualProgress * parent.height
        width: groove.control.horizontal ? groove.progress * parent.width - groove.offset * parent.width : 5
        height: groove.control.horizontal ? 5 : groove.progress * parent.height - groove.offset * parent.height

        radius: 2
        border.color: Qt.darker(Fusion.highlightedOutline(groove.control.palette), 1.1)

        gradient: Gradient {
            GradientStop {
                position: 0
                color: Fusion.highlight(groove.control.palette)
            }
            GradientStop {
                position: 1
                color: Qt.lighter(Fusion.highlight(groove.control.palette), 1.2)
            }
        }
    }
}
