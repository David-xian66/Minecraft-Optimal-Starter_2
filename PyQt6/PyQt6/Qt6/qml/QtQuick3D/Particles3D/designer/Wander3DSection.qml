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
        caption: qsTr("Particle Wander")
        width: parent.width

        SectionLayout {
            PropertyLabel {
                text: qsTr("Fade In Duration")
                tooltip: qsTr("This property defines the duration in milliseconds for fading in the affector.")
            }

            SecondColumnLayout {
                SpinBox {
                    minimumValue: 0
                    maximumValue: 999999
                    decimals: 0
                    backendValue: backendValues.fadeInDuration
                    implicitWidth: StudioTheme.Values.twoControlColumnWidth
                                   + StudioTheme.Values.actionIndicatorWidth
                }

                ExpandingSpacer {}
            }

            PropertyLabel {
                text: qsTr("Fade Out Duration")
                tooltip: qsTr("This property defines the duration in milliseconds for fading out the affector.")
            }

            SecondColumnLayout {
                SpinBox {
                    minimumValue: 0
                    maximumValue: 999999
                    decimals: 0
                    backendValue: backendValues.fadeOutDuration
                    implicitWidth: StudioTheme.Values.twoControlColumnWidth
                                   + StudioTheme.Values.actionIndicatorWidth
                }

                ExpandingSpacer {}
            }
        }
    }

    Section {
        width: parent.width
        caption: qsTr("Global")

        ColumnLayout {
            spacing: StudioTheme.Values.transform3DSectionSpacing

            SectionLayout {
                PropertyLabel {
                    text: qsTr("Amount")
                    tooltip: qsTr("This property defines how long distance each particle moves at the ends of curves.")
                }

                SecondColumnLayout {
                    SpinBox {
                        minimumValue: -9999999
                        maximumValue: 9999999
                        decimals: 2
                        backendValue: backendValues.globalAmount_x
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
                        backendValue: backendValues.globalAmount_y
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
                        backendValue: backendValues.globalAmount_z
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
            }

            SectionLayout {
                PropertyLabel {
                    text: qsTr("Pace")
                    tooltip: qsTr("This property defines the pace (frequency) each particle wanders in curves per second.")
                }

                SecondColumnLayout {
                    SpinBox {
                        minimumValue: -9999999
                        maximumValue: 9999999
                        decimals: 2
                        stepSize: 0.01
                        backendValue: backendValues.globalPace_x
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
                        stepSize: 0.01
                        backendValue: backendValues.globalPace_y
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
                        stepSize: 0.01
                        backendValue: backendValues.globalPace_z
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
            }

            SectionLayout {
                PropertyLabel {
                    text: qsTr("Pace Start")
                    tooltip: qsTr("This property defines the starting point for the pace (frequency).")
                }

                SecondColumnLayout {
                    SpinBox {
                        minimumValue: -9999999
                        maximumValue: 9999999
                        decimals: 2
                        stepSize: 0.01
                        backendValue: backendValues.globalPaceStart_x
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
                        stepSize: 0.01
                        backendValue: backendValues.globalPaceStart_y
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
                        stepSize: 0.01
                        backendValue: backendValues.globalPaceStart_z
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
            }
        }
    }
    Section {
        width: parent.width
        caption: qsTr("Unique")

        ColumnLayout {
            spacing: StudioTheme.Values.transform3DSectionSpacing

            SectionLayout {
                PropertyLabel {
                    text: qsTr("Amount")
                    tooltip: qsTr("This property defines the unique distance each particle moves at the ends of curves.")
                }

                SecondColumnLayout {
                    SpinBox {
                        minimumValue: -9999999
                        maximumValue: 9999999
                        decimals: 2
                        backendValue: backendValues.uniqueAmount_x
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
                        backendValue: backendValues.uniqueAmount_y
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
                        backendValue: backendValues.uniqueAmount_z
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
                    text: qsTr("Amount Variation")
                    tooltip: qsTr("This property defines variation for uniqueAmount between 0.0 and 1.0.")
                }

                SecondColumnLayout {
                    SpinBox {
                        minimumValue: 0
                        maximumValue: 1
                        decimals: 2
                        stepSize: 0.01
                        backendValue: backendValues.uniqueAmountVariation
                        implicitWidth: StudioTheme.Values.twoControlColumnWidth
                                       + StudioTheme.Values.actionIndicatorWidth
                    }

                    ExpandingSpacer {}
                }
            }

            SectionLayout {
                PropertyLabel {
                    text: qsTr("Pace")
                    tooltip: qsTr("This property defines the unique pace (frequency) each particle wanders in curves per second.")
                }

                SecondColumnLayout {
                    SpinBox {
                        minimumValue: -9999999
                        maximumValue: 9999999
                        decimals: 2
                        stepSize: 0.01
                        backendValue: backendValues.uniquePace_x
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
                        stepSize: 0.01
                        backendValue: backendValues.uniquePace_y
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
                        stepSize: 0.01
                        backendValue: backendValues.uniquePace_z
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
                    text: qsTr("Pace Variation")
                    tooltip: qsTr("This property defines the unique pace (frequency) variation for each particle between 0.0 and 1.0.")
                }

                SecondColumnLayout {
                    SpinBox {
                        minimumValue: 0
                        maximumValue: 1
                        decimals: 2
                        stepSize: 0.01
                        backendValue: backendValues.uniquePaceVariation
                        implicitWidth: StudioTheme.Values.twoControlColumnWidth
                                       + StudioTheme.Values.actionIndicatorWidth
                    }

                    ExpandingSpacer {}
                }
            }
        }
    }

}
