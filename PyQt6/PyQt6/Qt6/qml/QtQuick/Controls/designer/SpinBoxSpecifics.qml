/****************************************************************************
**
** Copyright (C) 2017 The Qt Company Ltd.
** Contact: https://www.qt.io/licensing/
**
** This file is part of the Qt Quick Controls 2 module of the Qt Toolkit.
**
** $QT_BEGIN_LICENSE:LGPL$
** Commercial License Usage
** Licensees holding valid commercial Qt licenses may use this file in
** accordance with the commercial license agreement provided with the
** Software or, alternatively, in accordance with the terms contained in
** a written agreement between you and The Qt Company. For licensing terms
** and conditions see https://www.qt.io/terms-conditions. For further
** information use the contact form at https://www.qt.io/contact-us.
**
** GNU Lesser General Public License Usage
** Alternatively, this file may be used under the terms of the GNU Lesser
** General Public License version 3 as published by the Free Software
** Foundation and appearing in the file LICENSE.LGPL3 included in the
** packaging of this file. Please review the following information to
** ensure the GNU Lesser General Public License version 3 requirements
** will be met: https://www.gnu.org/licenses/lgpl-3.0.html.
**
** GNU General Public License Usage
** Alternatively, this file may be used under the terms of the GNU
** General Public License version 2.0 or (at your option) the GNU General
** Public license version 3 or any later version approved by the KDE Free
** Qt Foundation. The licenses are as published by the Free Software
** Foundation and appearing in the file LICENSE.GPL2 and LICENSE.GPL3
** included in the packaging of this file. Please review the following
** information to ensure the GNU General Public License requirements will
** be met: https://www.gnu.org/licenses/gpl-2.0.html and
** https://www.gnu.org/licenses/gpl-3.0.html.
**
** $QT_END_LICENSE$
**
****************************************************************************/

import QtQuick
import HelperWidgets
import QtQuick.Layouts

Column {
    width: parent.width

    Section {
        width: parent.width
        caption: qsTr("SpinBox")

        SectionLayout {
            Label {
                text: qsTr("Value")
                tooltip: qsTr("The current value of the spinbox.")
            }
            SecondColumnLayout {
                SpinBox {
                    minimumValue: Math.min(backendValues.from.value, backendValues.to.value)
                    maximumValue: Math.max(backendValues.from.value, backendValues.to.value)
                    decimals: 2
                    backendValue: backendValues.value
                    Layout.fillWidth: true
                }
            }

            Label {
                text: qsTr("From")
                tooltip: qsTr("The starting value of the spinbox range.")
            }
            SecondColumnLayout {
                SpinBox {
                    maximumValue: 9999999
                    minimumValue: -9999999
                    decimals: 2
                    backendValue: backendValues.from
                    Layout.fillWidth: true
                }
            }

            Label {
                text: qsTr("To")
                tooltip: qsTr("The ending value of the spinbox range.")
            }
            SecondColumnLayout {
                SpinBox {
                    maximumValue: 9999999
                    minimumValue: -9999999
                    decimals: 2
                    backendValue: backendValues.to
                    Layout.fillWidth: true
                }
            }

            Label {
                text: qsTr("Step Size")
                tooltip: qsTr("The step size of the spinbox.")
            }
            SecondColumnLayout {
                SpinBox {
                    maximumValue: 9999999
                    minimumValue: -9999999
                    decimals: 2
                    backendValue: backendValues.stepSize
                    Layout.fillWidth: true
                }
            }

            Label {
                text: qsTr("Editable")
                tooltip: qsTr("Whether the spinbox is editable.")
            }
            SecondColumnLayout {
                CheckBox {
                    text: backendValues.editable.valueToString
                    backendValue: backendValues.editable
                    Layout.fillWidth: true
                }
            }

            Label {
                text: qsTr("Wrap")
                tooltip: qsTr("Whether the spinbox wraps.")
            }
            SecondColumnLayout {
                CheckBox {
                    text: backendValues.wrap.valueToString
                    backendValue: backendValues.wrap
                    Layout.fillWidth: true
                }
            }
        }
    }

    ControlSection {
        width: parent.width
    }

    FontSection {
        width: parent.width
    }

    PaddingSection {
        width: parent.width
    }
}
