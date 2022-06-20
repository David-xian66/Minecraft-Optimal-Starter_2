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
    caption: qsTr("Sprite Particle")
    width: parent.width

    SectionLayout {
        PropertyLabel {
            text: qsTr("Blend Mode")
            tooltip: qsTr("This property defines the blending mode used for rendering the particles.")
        }

        SecondColumnLayout {
            ComboBox {
                scope: "SpriteParticle3D"
                model: ["SourceOver", "Screen", "Multiply"]
                backendValue: backendValues.blendMode
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Sprite")
            tooltip: qsTr("This property defines the Texture used for the particles.")
        }

        SecondColumnLayout {
            IdComboBox {
                typeFilter: "QtQuick3D.Texture"
                backendValue: backendValues.sprite
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Sprite Sequence")
            tooltip: qsTr("This property defines the sprite sequence properties for the particle.")
        }

        SecondColumnLayout {
            IdComboBox {
                typeFilter: "QtQuick3D.Particles3D.SpriteSequence3D"
                backendValue: backendValues.spriteSequence
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Billboard")
            tooltip: qsTr("This property defines if the particle texture should always be aligned face towards the screen.")
        }

        SecondColumnLayout {
            CheckBox {
                id: billboardCheckBox
                text: backendValues.billboard.valueToString
                backendValue: backendValues.billboard
                implicitWidth: StudioTheme.Values.twoControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Particle Scale")
            tooltip: qsTr("This property defines the scale multiplier of the particles.")
        }

        SecondColumnLayout {
            SpinBox {
                minimumValue: -999999
                maximumValue: 999999
                decimals: 2
                backendValue: backendValues.particleScale
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Color Table")
            tooltip: qsTr("This property defines the Texture used for coloring the particles.")
        }

        SecondColumnLayout {
            IdComboBox {
                typeFilter: "QtQuick3D.Texture"
                backendValue: backendValues.colorTable
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Lights")
            tooltip: qsTr("This property defines the lights used for the particles.")
            Layout.alignment: Qt.AlignTop
            Layout.topMargin: 5
        }

        SecondColumnLayout {
            EditableListView {
                backendValue: backendValues.lights
                model: backendValues.lights.expressionAsList
                Layout.fillWidth: true
                typeFilter: "QtQuick3D.Light"
                onAdd: function(value) { backendValues.lights.idListAdd(value) }
                onRemove: function(idx) { backendValues.lights.idListRemove(idx) }
                onReplace: function (idx, value) { backendValues.lights.idListReplace(idx, value) }
            }
            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Offset")
        }

        SecondColumnLayout {
            SpinBox {
                maximumValue: 999999
                minimumValue: -999999
                decimals: 2
                stepSize: 0.1
                backendValue: backendValues.offsetX
                implicitWidth: StudioTheme.Values.twoControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            Spacer { implicitWidth: StudioTheme.Values.controlLabelGap }

            ControlLabel {
                text: "Offset X"
                tooltip: qsTr("Offsets the X coordinate.")
            }

            Spacer { implicitWidth: StudioTheme.Values.controlGap }

            SpinBox {
                maximumValue: 999999
                minimumValue: -999999
                decimals: 2
                stepSize: 0.1
                backendValue: backendValues.offsetY
                implicitWidth: StudioTheme.Values.twoControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            Spacer { implicitWidth: StudioTheme.Values.controlLabelGap }

            ControlLabel {
                text: "Offset Y"
                tooltip: qsTr("Offsets the Y coordinate.")
            }

            ExpandingSpacer {}
        }
    }
}
