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
    caption: qsTr("Particle Sprite Sequence")
    width: parent.width

    SectionLayout {
        PropertyLabel {
            text: qsTr("Frame Count")
            tooltip: qsTr("This property defines the amount of image frames in sprite.")
        }
        SecondColumnLayout {
            SpinBox {
                minimumValue: 0
                maximumValue: 999999
                decimals: 0
                backendValue: backendValues.frameCount
                implicitWidth: StudioTheme.Values.twoControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Frame Index")
            tooltip: qsTr("This property defines the initial index of the frame.")
        }

        SecondColumnLayout {
            SpinBox {
                minimumValue: 0
                maximumValue: 999999
                decimals: 0
                backendValue: backendValues.frameIndex
                implicitWidth: StudioTheme.Values.twoControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Interpolate")
            tooltip: qsTr("This property defines if the sprites are interpolated (blended) between frames to make the animation appear smoother.")
        }

        SecondColumnLayout {
            CheckBox {
                id: interpolateCheckBox
                text: backendValues.interpolate.valueToString
                backendValue: backendValues.interpolate
                implicitWidth: StudioTheme.Values.twoControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Duration")
            tooltip: qsTr("This property defines the duration in milliseconds how long it takes for the sprite sequence to animate.")
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
                minimumValue: -999999
                maximumValue: 999999
                decimals: 0
                backendValue: backendValues.durationVariation
                implicitWidth: StudioTheme.Values.twoControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Random Start")
            tooltip: qsTr("This property defines if the animation should start from a random frame between 0 and frameCount - 1.")
        }

        SecondColumnLayout {
            CheckBox {
                id: randomStartCheckBox
                text: backendValues.randomStart.valueToString
                backendValue: backendValues.randomStart
                implicitWidth: StudioTheme.Values.twoControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Animation Direction")
            tooltip: qsTr("This property defines the animation direction of the sequence.")
        }

        SecondColumnLayout {
            ComboBox {
                scope: "SpriteSequence3D"
                model: ["Normal", "Reverse", "Alternate", "AlternateReverse", "SingleFrame"]
                backendValue: backendValues.animationDirection
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }
    }
}
