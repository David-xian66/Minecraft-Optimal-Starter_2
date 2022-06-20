/****************************************************************************
**
** Copyright (C) 2022 The Qt Company Ltd.
** Contact: https://www.qt.io/licensing/
**
** This file is part of Qt Quick 3D.
**
** $QT_BEGIN_LICENSE:GPL$
** Commercial License Usage
** Licensees holding valid commercial Qt licenses may use this file in
** accordance with the commercial license agreement provided with the
** Software or, alternatively, in accordance with the terms contained in
** a written agreement between you and The Qt Company. For licensing terms
** and conditions see https://www.qt.io/terms-conditions. For further
** information use the contact form at https://www.qt.io/contact-us.
**
** GNU General Public License Usage
** Alternatively, this file may be used under the terms of the GNU
** General Public License version 3 or (at your option) any later version
** approved by the KDE Free Qt Foundation. The licenses are as published by
** the Free Software Foundation and appearing in the file LICENSE.GPL3
** included in the packaging of this file. Please review the following
** information to ensure the GNU General Public License requirements will
** be met: https://www.gnu.org/licenses/gpl-3.0.html.
**
** $QT_END_LICENSE$
**
****************************************************************************/

import QtQuick 2.15
import QtQuick.Layouts 1.15
import HelperWidgets 2.0
import StudioTheme 1.0 as StudioTheme

Column {
    width: parent.width

    Section {
        width: parent.width
        caption: qsTr("Axis Helper")

        SectionLayout {
            PropertyLabel {
                text: qsTr("Axis Lines")
                tooltip: qsTr("Show colored axis indicator lines.")
            }

            SecondColumnLayout {
                CheckBox {
                    text: qsTr("Enabled")
                    backendValue: backendValues.enableAxisLines
                    implicitWidth: StudioTheme.Values.twoControlColumnWidth
                                   + StudioTheme.Values.actionIndicatorWidth
                }

                ExpandingSpacer {}
            }

            PropertyLabel {
                text: qsTr("XY Grid")
                tooltip: qsTr("Show grid on XY plane.")
            }

            SecondColumnLayout {
                CheckBox {
                    text: qsTr("Enabled")
                    backendValue: backendValues.enableXYGrid
                    implicitWidth: StudioTheme.Values.twoControlColumnWidth
                                   + StudioTheme.Values.actionIndicatorWidth
                }

                ExpandingSpacer {}
            }

            PropertyLabel {
                text: qsTr("XZ Grid")
                tooltip: qsTr("Show grid on XZ plane.")
            }

            SecondColumnLayout {
                CheckBox {
                    text: qsTr("Enabled")
                    backendValue: backendValues.enableXZGrid
                    implicitWidth: StudioTheme.Values.twoControlColumnWidth
                                   + StudioTheme.Values.actionIndicatorWidth
                }

                ExpandingSpacer {}
            }


            PropertyLabel {
                text: qsTr("YZ Grid")
                tooltip: qsTr("Show grid on YZ plane.")
            }

            SecondColumnLayout {
                CheckBox {
                    text: qsTr("Enabled")
                    backendValue: backendValues.enableYZGrid
                    implicitWidth: StudioTheme.Values.twoControlColumnWidth
                                   + StudioTheme.Values.actionIndicatorWidth
                }

                ExpandingSpacer {}
            }

            PropertyLabel {
                text: qsTr("Grid Opacity")
                tooltip: qsTr("Sets the opacity of the visible grids.")
            }

            SecondColumnLayout {
                SpinBox {
                    minimumValue: 0
                    maximumValue: 1
                    decimals: 2
                    stepSize: 0.1
                    backendValue: backendValues.gridOpacity
                    implicitWidth: StudioTheme.Values.twoControlColumnWidth
                                   + StudioTheme.Values.actionIndicatorWidth
                }

                ExpandingSpacer {}
            }

            PropertyLabel {
                text: qsTr("Grid Color")
            }

            ColorEditor {
                backendValue: backendValues.gridColor
                supportGradient: false
            }
        }
    }
}
