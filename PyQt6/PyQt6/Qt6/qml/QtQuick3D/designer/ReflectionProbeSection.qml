/****************************************************************************
**
** Copyright (C) 2021 The Qt Company Ltd.
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

Section {
    caption: qsTr("Reflection Probe")

    SectionLayout {
        PropertyLabel {
            text: qsTr("Box Size")
            tooltip: qsTr("Sets the reflection probe box size.")
        }

        SecondColumnLayout {
            SpinBox {
                minimumValue: 0
                maximumValue: 9999999
                decimals: 2
                backendValue: backendValues.boxSize_x
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            Spacer { implicitWidth: StudioTheme.Values.controlLabelGap }

            ControlLabel {
                text: "box size x"
                color: StudioTheme.Values.theme3DAxisXColor
            }

            ExpandingSpacer {}
        }

        PropertyLabel {}

        SecondColumnLayout {
            SpinBox {
                minimumValue: 0
                maximumValue: 9999999
                decimals: 2
                backendValue: backendValues.boxSize_y
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            Spacer { implicitWidth: StudioTheme.Values.controlLabelGap }

            ControlLabel {
                text: "box size y"
                color: StudioTheme.Values.theme3DAxisYColor
            }

            ExpandingSpacer {}
        }

        PropertyLabel {}

        SecondColumnLayout {
            SpinBox {
                minimumValue: 0
                maximumValue: 9999999
                decimals: 2
                backendValue: backendValues.boxSize_z
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            Spacer { implicitWidth: StudioTheme.Values.controlLabelGap }

            ControlLabel {
                text: "box size z"
                color: StudioTheme.Values.theme3DAxisZColor
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Parallax Correction")
            tooltip: qsTr("Reflection maps are considered to be at infinite distance by default. This is unsuitable for indoor area as it produces parallax issues.\nSetting this property to true, corrects the cubemap by taking the camera position and the box's dimension into account")
        }

        SecondColumnLayout {
            CheckBox {
                text: backendValues.parallaxCorrection.valueToString
                backendValue: backendValues.parallaxCorrection
                implicitWidth: StudioTheme.Values.twoControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Clear Color")
            tooltip: qsTr("The property defines the color that will be used to clear the reflection map.")
        }

        ColorEditor {
            backendValue: backendValues.clearColor
            supportGradient: false
        }

        PropertyLabel {
            text: qsTr("Reflection Map Quality")
            tooltip: qsTr("Sets the quality of the reflection map.")
        }

        SecondColumnLayout {
            ComboBox {
                scope: "ReflectionProbe"
                model: ["VeryLow", "Low", "Medium", "High", "VeryHigh"]
                backendValue: backendValues.quality
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Refresh Mode")
            tooltip: qsTr("Sets how often the reflection map will be updated.")
        }

        SecondColumnLayout {
            ComboBox {
                scope: "ReflectionProbe"
                model: ["FirstFrame", "EveryFrame"]
                backendValue: backendValues.refreshMode
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Time Slicing")
            tooltip: qsTr("Sets how often the faces of the reflection cube map are updated.")
        }

        SecondColumnLayout {
            ComboBox {
                scope: "ReflectionProbe"
                model: ["None", "AllFacesAtOnce", "IndividualFaces"]
                backendValue: backendValues.timeSlicing
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }
    }
}
