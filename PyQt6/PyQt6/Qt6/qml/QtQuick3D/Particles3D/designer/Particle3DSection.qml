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
    caption: qsTr("Particle")
    width: parent.width

    SectionLayout {
        PropertyLabel {
            text: qsTr("Max Amount")
            tooltip: qsTr("This property defines the maximum amount of particles that can exist at the same time.")
        }

        SecondColumnLayout {
            SpinBox {
                minimumValue: 0
                maximumValue: 999999
                decimals: 0
                backendValue: backendValues.maxAmount
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Color")
            tooltip: qsTr("This property defines the base color that is used for colorizing the particles.")
        }

        ColorEditor {
            backendValue: backendValues.color
            supportGradient: false
        }

        PropertyLabel {
            text: qsTr("Color Variation")
            tooltip: qsTr("This property defines the color variation that is used for colorizing the particles.")
        }

        SecondColumnLayout {
            SpinBox {
                minimumValue: 0
                maximumValue: 1
                decimals: 2
                stepSize: 0.01
                backendValue: backendValues.colorVariation_x
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            Spacer { implicitWidth: StudioTheme.Values.controlLabelGap }

            ControlLabel {
                text: "X"
                color: StudioTheme.Values.theme3DAxisXColor
            }

            ExpandingSpacer {}
        }

        PropertyLabel {}

        SecondColumnLayout {
            SpinBox {
                minimumValue: 0
                maximumValue: 1
                decimals: 2
                stepSize: 0.01
                backendValue: backendValues.colorVariation_y
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            Spacer { implicitWidth: StudioTheme.Values.controlLabelGap }

            ControlLabel {
                text: "Y"
                color: StudioTheme.Values.theme3DAxisYColor
            }

            ExpandingSpacer {}
        }

        PropertyLabel {}

        SecondColumnLayout {
            SpinBox {
                minimumValue: 0
                maximumValue: 1
                decimals: 2
                stepSize: 0.01
                backendValue: backendValues.colorVariation_z
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            Spacer { implicitWidth: StudioTheme.Values.controlLabelGap }

            ControlLabel {
                text: "Z"
                color: StudioTheme.Values.theme3DAxisZColor
            }

            ExpandingSpacer {}
        }

        PropertyLabel {}

        SecondColumnLayout {
            SpinBox {
                minimumValue: -9999999
                maximumValue: 9999999
                decimals: 2
                backendValue: backendValues.colorVariation_w
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            Spacer { implicitWidth: StudioTheme.Values.controlLabelGap }

            ControlLabel {
                text: "W"
                color: StudioTheme.Values.themeTextColor // TODO theme3DAxisWColor
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Unified Color Variation")
            tooltip: qsTr("This property defines if the colorVariation should be applied uniformly for all the color channels.")
        }

        SecondColumnLayout {
            CheckBox {
                id: unifiedColorVariationCheckBox
                text: backendValues.unifiedColorVariation.valueToString
                backendValue: backendValues.unifiedColorVariation
                implicitWidth: StudioTheme.Values.twoControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Fade In Effect")
            tooltip: qsTr("This property defines the fading effect used when the particles appear.")
        }

        SecondColumnLayout {
            ComboBox {
                scope: "Particle3D"
                model: ["FadeNone", "FadeOpacity", "FadeScale"]
                backendValue: backendValues.fadeInEffect
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Fade Out Effect")
            tooltip: qsTr("This property defines the fading effect used when the particles reach their lifeSpan and disappear.")
        }

        SecondColumnLayout {
            ComboBox {
                scope: "Particle3D"
                model: ["FadeNone", "FadeOpacity", "FadeScale"]
                backendValue: backendValues.fadeOutEffect
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Fade In Duration")
            tooltip: qsTr("This property defines the duration in milliseconds for the fading in effect.")
        }
        SecondColumnLayout {
            SpinBox {
                minimumValue: 0
                maximumValue: 999999
                decimals: 0
                backendValue: backendValues.fadeInDuration
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Fade Out Duration")
            tooltip: qsTr("This property defines the duration in milliseconds for the fading out effect.")
        }

        SecondColumnLayout {
            SpinBox {
                minimumValue: 0
                maximumValue: 999999
                decimals: 0
                backendValue: backendValues.fadeOutDuration
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Align Mode")
            tooltip: qsTr("This property defines the align mode used for the particles. Particle alignment means the direction that particles face.")
        }

        SecondColumnLayout {
            ComboBox {
                scope: "Particle3D"
                model: ["AlignNone", "AlignTowardsTarget", "AlignTowardsStartVelocity"]
                backendValue: backendValues.alignMode
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Align Target Position")
            tooltip: qsTr("This property defines the position particles are aligned to. This property has effect only when the alignMode is set to Particle3D.AlignTowardsTarget.")
        }

        SecondColumnLayout {
            SpinBox {
                minimumValue: -9999999
                maximumValue: 9999999
                decimals: 2
                backendValue: backendValues.alignTargetPosition_x
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            Spacer { implicitWidth: StudioTheme.Values.controlLabelGap }

            ControlLabel {
                text: "X"
                color: StudioTheme.Values.theme3DAxisXColor
            }

            ExpandingSpacer {}
        }

        PropertyLabel {}

        SecondColumnLayout {
            SpinBox {
                minimumValue: -9999999
                maximumValue: 9999999
                decimals: 2
                backendValue: backendValues.alignTargetPosition_y
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            Spacer { implicitWidth: StudioTheme.Values.controlLabelGap }

            ControlLabel {
                text: "Y"
                color: StudioTheme.Values.theme3DAxisYColor
            }

            ExpandingSpacer {}
        }

        PropertyLabel {}

        SecondColumnLayout {
            SpinBox {
                minimumValue: -9999999
                maximumValue: 9999999
                decimals: 2
                backendValue: backendValues.alignTargetPosition_z
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            Spacer { implicitWidth: StudioTheme.Values.controlLabelGap }

            ControlLabel {
                text: "Z"
                color: StudioTheme.Values.theme3DAxisZColor
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Has Transparency")
            tooltip: qsTr("This property defines if the particle has any transparency and should be blended with the background.")
        }

        SecondColumnLayout {
            CheckBox {
                id: hasTransparencyCheckBox
                text: backendValues.hasTransparency.valueToString
                backendValue: backendValues.hasTransparency
                implicitWidth: StudioTheme.Values.twoControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Sort Mode")
            tooltip: qsTr("This property defines the sort mode used for the particles.")
        }

        SecondColumnLayout {
            ComboBox {
                scope: "Particle3D"
                model: ["SortNone", "SortNewest", "SortOldest", "SortDistance"]
                backendValue: backendValues.sortMode
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }
    }
}
