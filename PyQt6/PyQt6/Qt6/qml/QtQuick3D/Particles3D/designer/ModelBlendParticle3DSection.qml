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
    caption: qsTr("Model Blend Particle")
    width: parent.width

    SectionLayout {
        PropertyLabel {
            text: qsTr("Delegate")
            tooltip: qsTr("The delegate provides a template defining the model for the ModelBlendParticle3D.")
        }

        SecondColumnLayout {
            IdComboBox {
                typeFilter: "Component"
                backendValue: backendValues.delegate
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("End Node")
            tooltip: qsTr("This property holds the node that specifies the transformation for the model at the end of particle effect.")
        }

        SecondColumnLayout {
            IdComboBox {
                typeFilter: "QtQuick3D.Node"
                backendValue: backendValues.endNode
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Model Blend Mode")
            tooltip: qsTr("This property holds blending mode for the particle effect.")
        }

        SecondColumnLayout {
            ComboBox {
                scope: "ModelBlendParticle3D"
                model: ["Explode", "Construct", "Transfer"]
                backendValue: backendValues.modelBlendMode
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("End Time")
            tooltip: qsTr("This property holds the end time of the particle in milliseconds.")
        }

        SecondColumnLayout {
            SpinBox {
                minimumValue: 0
                maximumValue: 999999
                decimals: 0
                backendValue: backendValues.endTime
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Activation Node")
            tooltip: qsTr("This property holds a node that activates particles.")
        }

        SecondColumnLayout {
            IdComboBox {
                typeFilter: "QtQuick3D.Node"
                backendValue: backendValues.activationNode
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Emit Mode")
            tooltip: qsTr("This property holds emit mode of the particles.")
        }

        SecondColumnLayout {
            ComboBox {
                id: randomCheckBox
                model: ["Sequential", "Random", "Activation"]
                backendValue: backendValues.emitMode
                implicitWidth: StudioTheme.Values.twoControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }
    }

}
