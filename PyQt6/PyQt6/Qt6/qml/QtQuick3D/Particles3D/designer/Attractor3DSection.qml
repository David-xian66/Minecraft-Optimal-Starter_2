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
    caption: qsTr("Particle Attractor")
    width: parent.width

    SectionLayout {
        PropertyLabel {
            text: qsTr("Position Variation")
            tooltip: qsTr("This property defines the variation on attract position.")
        }

        SecondColumnLayout {
            SpinBox {
                minimumValue: -9999999
                maximumValue: 9999999
                decimals: 2
                backendValue: backendValues.positionVariation_x
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
                backendValue: backendValues.positionVariation_y
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
                backendValue: backendValues.positionVariation_z
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
            text: qsTr("Shape")
            tooltip: qsTr("This property defines a ParticleAbstractShape3D for particles attraction.")
        }

        SecondColumnLayout {
            IdComboBox {
                typeFilter: "QQuick3DParticleAbstractShape"
                backendValue: backendValues.shape
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Duration")
            tooltip: qsTr("This property defines the duration in milliseconds how long it takes for particles to reach the attaction position.")
        }

        SecondColumnLayout {
            SpinBox {
                minimumValue: -1
                maximumValue: 999999
                decimals: 0
                backendValue: backendValues.duration
                implicitWidth: StudioTheme.Values.twoControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Duration Variation")
            tooltip: qsTr("This property defines the duration variation in milliseconds.")
        }

        SecondColumnLayout {
            SpinBox {
                minimumValue: 0
                maximumValue: 999999
                decimals: 0
                backendValue: backendValues.durationVariation
                implicitWidth: StudioTheme.Values.twoControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Hide At End")
            tooltip: qsTr("This property defines if the particle should disappear when it reaches the attractor.")
        }

        SecondColumnLayout {
            CheckBox {
                text: backendValues.hideAtEnd.valueToString
                backendValue: backendValues.hideAtEnd
                implicitWidth: StudioTheme.Values.twoControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Use Cached Positions")
            tooltip: qsTr("This property defines if the attractor caches possible positions within its shape. Cached positions give less random results but are better for performance.")
        }

        SecondColumnLayout {
            CheckBox {
                text: backendValues.useCachedPositions.valueToString
                backendValue: backendValues.useCachedPositions
                implicitWidth: StudioTheme.Values.twoControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Positions Amount")
            tooltip: qsTr("This property defines the amount of possible positions stored within the attractor shape.")
        }

        SecondColumnLayout {
            SpinBox {
                minimumValue: 0
                maximumValue: 999999
                decimals: 0
                backendValue: backendValues.positionsAmount
                implicitWidth: StudioTheme.Values.twoControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }
        }
    }
}
