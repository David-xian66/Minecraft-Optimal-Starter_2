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
    caption: qsTr("Model")

    SectionLayout {
        id: tessellationSection

        PropertyLabel {
            text: qsTr("Source")
            tooltip: qsTr("Defines the location of the mesh file containing the geometry of this model.")
        }

        SecondColumnLayout {
            UrlChooser {
                id: sourceUrlChooser
                backendValue: backendValues.source
                filter: "*.mesh"
                defaultItems: ["#Rectangle" ,"#Sphere" ,"#Cube" ,"#Cone" ,"#Cylinder"]
            }

            ExpandingSpacer {}
        }

        function hasTessellationMode(mode) {
            if (tessellationModeComboBox.backendValue.valueToString !== "" &&
                tessellationModeComboBox.backendValue.valueToString !== mode)
                return false

            if (tessellationModeComboBox.backendValue.enumeration !== "" &&
                tessellationModeComboBox.backendValue.enumeration !== mode)
                return false

            return true
        }

        PropertyLabel {
            text: qsTr("Casts Shadows")
            tooltip: qsTr("Enables the geometry of this model to be rendered to the shadow maps.")
        }

        SecondColumnLayout {
            CheckBox {
                text: backendValues.castsShadows.valueToString
                backendValue: backendValues.castsShadows
                implicitWidth: StudioTheme.Values.twoControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Receives Shadows")
            tooltip: qsTr("Enables the geometry of this model to receive shadows.")
        }

        SecondColumnLayout {
            CheckBox {
                text: backendValues.receivesShadows.valueToString
                backendValue: backendValues.receivesShadows
                implicitWidth: StudioTheme.Values.twoControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Receives Reflections")
            tooltip: qsTr("Enables the geometry of this model to receive reflections from the nearest reflection probe. The model must be inside at least one reflection probe to start receiving reflections.")
        }

        SecondColumnLayout {
            CheckBox {
                text: backendValues.receivesReflections.valueToString
                backendValue: backendValues.receivesReflections
                implicitWidth: StudioTheme.Values.twoControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Pickable")
            tooltip: qsTr("Controls whether the model is pickable or not.")
        }

        SecondColumnLayout {
            CheckBox {
                text: backendValues.pickable.valueToString
                backendValue: backendValues.pickable
                implicitWidth: StudioTheme.Values.twoControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Materials")
            Layout.alignment: Qt.AlignTop
            Layout.topMargin: 5
        }

        SecondColumnLayout {
            EditableListView {
                backendValue: backendValues.materials
                model: backendValues.materials.expressionAsList
                Layout.fillWidth: true

                onAdd: function(value) { backendValues.materials.idListAdd(value) }
                onRemove: function(idx) { backendValues.materials.idListRemove(idx) }
                onReplace: function (idx, value) { backendValues.materials.idListReplace(idx, value) }
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Geometry")
            tooltip: qsTr("Specify a custom geometry for the model")
        }

        SecondColumnLayout {
            IdComboBox {
                id: geometryComboBox
                typeFilter: "QtQuick3D.Geometry"
                backendValue: backendValues.geometry
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth

                Connections {
                    target: geometryComboBox.backendValue
                    function onExpressionChanged() {
                        if (geometryComboBox.backendValue.expression !== "" &&
                                sourceUrlChooser.backendValue.expression !== "")
                            sourceUrlChooser.backendValue.resetValue()
                    }
                }
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Instancing")
            tooltip: qsTr("If this property is set, the model will not be rendered normally. Instead, a number of instances of the model will be rendered, as defined by the instance table.")
        }

        SecondColumnLayout {
            IdComboBox {
                typeFilter: "QtQuick3D.Instancing"
                backendValue: backendValues.instancing
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Instance Root")
            tooltip: qsTr("This property defines the origin of the instance’s coordinate system.")
        }

        SecondColumnLayout {
            IdComboBox {
                typeFilter: "QtQuick3D.Node"
                backendValue: backendValues.instanceRoot
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Skeleton")
            tooltip: qsTr("Contains the skeleton for the model.")
        }

        SecondColumnLayout {
            IdComboBox {
                typeFilter: "QtQuick3D.Skeleton"
                backendValue: backendValues.skeleton
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Morph Targets")
            tooltip: qsTr("This property contains a list of MorphTargets used to render the provided geometry.")
            Layout.alignment: Qt.AlignTop
            Layout.topMargin: 5
        }

        SecondColumnLayout {
            EditableListView {
                backendValue: backendValues.morphTargets
                model: backendValues.morphTargets.expressionAsList
                Layout.fillWidth: true
                typeFilter: "QtQuick3D.MorphTarget"

                onAdd: function(value) { backendValues.morphTargets.idListAdd(value) }
                onRemove: function(idx) { backendValues.morphTargets.idListRemove(idx) }
                onReplace: function (idx, value) { backendValues.morphTargets.idListReplace(idx, value) }
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Depth Bias")
            tooltip: qsTr("Holds the depth bias of the model.")
        }

        SecondColumnLayout {
            SpinBox {
                minimumValue: -9999999
                maximumValue: 9999999
                decimals: 0
                backendValue: backendValues.depthBias
                implicitWidth: StudioTheme.Values.twoControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }
    }
}
