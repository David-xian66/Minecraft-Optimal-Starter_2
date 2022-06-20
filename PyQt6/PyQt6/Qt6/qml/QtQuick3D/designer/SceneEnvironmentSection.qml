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

Column {
    width: parent.width

    Section {
        width: parent.width
        caption: qsTr("Scene Environment")

        SectionLayout {
            PropertyLabel {
                text: qsTr("Clear Color")
                tooltip: qsTr("This property defines which color will be used to clear the viewport when using SceneEnvironment.Color for the backgroundMode property.")
            }

            ColorEditor {
                backendValue: backendValues.clearColor
                supportGradient: false
            }

            PropertyLabel {
                text: qsTr("Background Mode")
                tooltip: qsTr("Controls if and how the background of the scene should be cleared.")
            }

            SecondColumnLayout {
                ComboBox {
                    scope: "SceneEnvironment"
                    model: ["Transparent", "Unspecified", "Color", "SkyBox"]
                    backendValue: backendValues.backgroundMode
                    implicitWidth: StudioTheme.Values.singleControlColumnWidth
                                   + StudioTheme.Values.actionIndicatorWidth
                }

                ExpandingSpacer {}
            }

            PropertyLabel {
                text: qsTr("Enable Depth Test")
                tooltip: qsTr("Enables depth testing. Disable to optimize render speed for layers with mostly transparent objects.")
            }

            SecondColumnLayout {
                CheckBox {
                    text: backendValues.depthTestEnabled.valueToString
                    backendValue: backendValues.depthTestEnabled
                    implicitWidth: StudioTheme.Values.twoControlColumnWidth
                                   + StudioTheme.Values.actionIndicatorWidth
                }

                ExpandingSpacer {}
            }

            PropertyLabel {
                text: qsTr("Enable Depth Prepass")
                tooltip: qsTr("Draw depth buffer as a separate pass. Disable to optimize render speed for layers with low depth complexity.")
            }

            SecondColumnLayout {
                CheckBox {
                    text: backendValues.depthPrePassEnabled.valueToString
                    backendValue: backendValues.depthPrePassEnabled
                    implicitWidth: StudioTheme.Values.twoControlColumnWidth
                                   + StudioTheme.Values.actionIndicatorWidth
                }

                ExpandingSpacer {}
            }

            PropertyLabel {
                text: qsTr("Effect")
                tooltip: qsTr("A post-processing effect applied to this scene.")
                Layout.alignment: Qt.AlignTop
                Layout.topMargin: 5
            }

            SecondColumnLayout {
                EditableListView {
                    backendValue: backendValues.effects
                    model: backendValues.effects.expressionAsList
                    Layout.fillWidth: true
                    typeFilter: "QtQuick3D.Effect"

                    onAdd: function(value) { backendValues.effects.idListAdd(value) }
                    onRemove: function(idx) { backendValues.effects.idListRemove(idx) }
                    onReplace: function (idx, value) { backendValues.effects.idListReplace(idx, value) }
                }

                ExpandingSpacer {}
            }

            PropertyLabel {
                text: qsTr("Tonemap Mode")
                tooltip: qsTr("This property defines how colors are tonemapped before rendering.")
            }

            SecondColumnLayout {
                ComboBox {
                    scope: "SceneEnvironment"
                    model: ["TonemapModeNone", "TonemapModeLinear", "TonemapModeAces", "TonemapModeHejlDawson", "TonemapModeFilmic"]
                    backendValue: backendValues.tonemapMode
                    implicitWidth: StudioTheme.Values.singleControlColumnWidth
                                   + StudioTheme.Values.actionIndicatorWidth
                }

                ExpandingSpacer {}
            }
        }
    }

    Section {
        width: parent.width
        caption: qsTr("Antialiasing")

        SectionLayout {
            PropertyLabel {
                text: qsTr("Antialiasing Mode")
                tooltip: qsTr("Sets the antialiasing mode applied to the scene.")
            }

            SecondColumnLayout {
                ComboBox {
                    scope: "SceneEnvironment"
                    model: ["NoAA", "SSAA", "MSAA", "ProgressiveAA"]
                    backendValue: backendValues.antialiasingMode
                    implicitWidth: StudioTheme.Values.singleControlColumnWidth
                                   + StudioTheme.Values.actionIndicatorWidth
                }

                ExpandingSpacer {}
            }

            PropertyLabel {
                text: qsTr("Antialiasing Quality")
                tooltip: qsTr("Sets the level of antialiasing applied to the scene.")
            }

            SecondColumnLayout {
                ComboBox {
                    scope: "SceneEnvironment"
                    model: ["Medium", "High", "VeryHigh"]
                    backendValue: backendValues.antialiasingQuality
                    implicitWidth: StudioTheme.Values.singleControlColumnWidth
                                   + StudioTheme.Values.actionIndicatorWidth
                }

                ExpandingSpacer {}
            }

            PropertyLabel {
                text: qsTr("Temporal AA")
                tooltip: qsTr("Enables temporal antialiasing using camera jittering and frame blending.")
            }

            SecondColumnLayout {
                CheckBox {
                    text: backendValues.temporalAAEnabled.valueToString
                    backendValue: backendValues.temporalAAEnabled
                    implicitWidth: StudioTheme.Values.twoControlColumnWidth
                                   + StudioTheme.Values.actionIndicatorWidth
                }

                ExpandingSpacer {}
            }

            PropertyLabel {
                text: qsTr("Temporal AA Strength")
                tooltip: qsTr("Sets the amount of temporal antialiasing applied.")
            }

            SecondColumnLayout {
                SpinBox {
                    minimumValue: 0.01
                    maximumValue: 2.0
                    decimals: 2
                    stepSize: 0.1
                    backendValue: backendValues.temporalAAStrength
                    implicitWidth: StudioTheme.Values.twoControlColumnWidth
                                   + StudioTheme.Values.actionIndicatorWidth
                }

                ExpandingSpacer {}
            }
        }
    }

    Section {
        width: parent.width
        caption: qsTr("Ambient Occlusion")

        SectionLayout {
            PropertyLabel {
                text: qsTr("Strength")
                tooltip: qsTr("This property defines the amount of ambient occulusion applied.")
            }

            SecondColumnLayout {
                SpinBox {
                    minimumValue: 0
                    maximumValue: 100
                    decimals: 2
                    backendValue: backendValues.aoStrength
                    implicitWidth: StudioTheme.Values.singleControlColumnWidth
                                   + StudioTheme.Values.actionIndicatorWidth
                }

                ExpandingSpacer {}
            }

            PropertyLabel {
                text: qsTr("Distance")
                tooltip: qsTr("This property defines roughly how far ambient occlusion shadows spread away from objects.")
            }

            SecondColumnLayout {
                SpinBox {
                    minimumValue: 0
                    maximumValue: 9999999
                    decimals: 2
                    backendValue: backendValues.aoDistance
                    implicitWidth: StudioTheme.Values.singleControlColumnWidth
                                   + StudioTheme.Values.actionIndicatorWidth
                }

                ExpandingSpacer {}
            }

            PropertyLabel {
                text: qsTr("Softness")
                tooltip: qsTr("This property how smooth the edges of the ambient occlusion shading are.")
            }

            SecondColumnLayout {
                SpinBox {
                    minimumValue: 0
                    maximumValue: 50
                    decimals: 2
                    backendValue: backendValues.aoSoftness
                    implicitWidth: StudioTheme.Values.singleControlColumnWidth
                                   + StudioTheme.Values.actionIndicatorWidth
                }

                ExpandingSpacer {}
            }

            PropertyLabel {
                text: qsTr("Sample Rate")
                tooltip: qsTr("This property defines ambient occlusion quality (more shades of gray) at the expense of performance.")
            }

            SecondColumnLayout {
                SpinBox {
                    minimumValue: 2
                    maximumValue: 4
                    decimals: 0
                    backendValue: backendValues.aoSampleRate
                    implicitWidth: StudioTheme.Values.singleControlColumnWidth
                                   + StudioTheme.Values.actionIndicatorWidth
                }

                ExpandingSpacer {}
            }

            PropertyLabel {
                text: qsTr("Bias")
                tooltip: qsTr("This property defines a cutoff distance preventing objects from exhibiting ambient occlusion at close distances.")
            }

            SecondColumnLayout {
                SpinBox {
                    minimumValue: 0
                    maximumValue: 9999999
                    decimals: 2
                    backendValue: backendValues.aoBias
                    implicitWidth: StudioTheme.Values.singleControlColumnWidth
                                   + StudioTheme.Values.actionIndicatorWidth
                }

                ExpandingSpacer {}
            }

            PropertyLabel {
                text: qsTr("Dither")
                tooltip: qsTr("When this property is enabled it scatters the edges of the ambient occlusion shadow bands to improve smoothness.")
            }

            SecondColumnLayout {
                CheckBox {
                    id: aoDitherCheckBox
                    text: backendValues.aoDither.valueToString
                    backendValue: backendValues.aoDither
                    implicitWidth: StudioTheme.Values.twoControlColumnWidth
                                   + StudioTheme.Values.actionIndicatorWidth
                }

                ExpandingSpacer {}
            }
        }
    }

    Section {
        width: parent.width
        caption: qsTr("Light Probe")

        SectionLayout {
            PropertyLabel {
                text: qsTr("Image")
                tooltip: qsTr("This property defines an image, to use to light the scene, either instead of or in addition to standard lights.")
            }

            SecondColumnLayout {
                IdComboBox {
                    typeFilter: "QtQuick3D.Texture"
                    backendValue: backendValues.lightProbe
                    implicitWidth: StudioTheme.Values.singleControlColumnWidth
                                   + StudioTheme.Values.actionIndicatorWidth
                }

                ExpandingSpacer {}
            }

            PropertyLabel {
                text: qsTr("Exposure")
                tooltip: qsTr("This property modifies the amount of light emitted by the light probe.")
            }

            SecondColumnLayout {
                SpinBox {
                    minimumValue: 0
                    maximumValue: 9999999
                    decimals: 2
                    backendValue: backendValues.probeExposure
                    implicitWidth: StudioTheme.Values.singleControlColumnWidth
                                   + StudioTheme.Values.actionIndicatorWidth
                }

                ExpandingSpacer {}
            }

            PropertyLabel {
                text: qsTr("Horizon")
                tooltip: qsTr("This property when defined with increasing values adds darkness (black) to the bottom half of the environment, forcing the lighting to come predominantly from the top of the image.")
            }

            SecondColumnLayout {
                SpinBox {
                    minimumValue: 1
                    maximumValue: 0
                    decimals: 2
                    backendValue: backendValues.probeHorizon
                    implicitWidth: StudioTheme.Values.singleControlColumnWidth
                                   + StudioTheme.Values.actionIndicatorWidth
                }

                ExpandingSpacer {}
            }

            PropertyLabel {
                text: qsTr("Orientation")
                tooltip: qsTr("This property when defines the orientation of the light probe. Orientation is defined in terms of euler angles in degrees over the x, y, and z axes.")
            }

            SecondColumnLayout {
                SpinBox {
                    implicitWidth: StudioTheme.Values.singleControlColumnWidth
                                   + StudioTheme.Values.actionIndicatorWidth
                    minimumValue: -9999999
                    maximumValue: 9999999
                    decimals: 2
                    backendValue: backendValues.probeOrientation_x
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
                    implicitWidth: StudioTheme.Values.singleControlColumnWidth
                                   + StudioTheme.Values.actionIndicatorWidth
                    minimumValue: -9999999
                    maximumValue: 9999999
                    decimals: 2
                    backendValue: backendValues.probeOrientation_y
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
                    implicitWidth: StudioTheme.Values.singleControlColumnWidth
                                   + StudioTheme.Values.actionIndicatorWidth
                    minimumValue: -9999999
                    maximumValue: 9999999
                    decimals: 2
                    backendValue: backendValues.probeOrientation_z
                }

                Spacer { implicitWidth: StudioTheme.Values.controlLabelGap }

                ControlLabel {
                    text: "Z"
                    color: StudioTheme.Values.theme3DAxisZColor
                }

                ExpandingSpacer {}
            }
        }
    }
}
