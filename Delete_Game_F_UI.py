# Form implementation generated from reading ui file '/Users/xyj/.npm/ssh/UI/UI/Delete_Game_F_UI.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Delete_Game_F_UI_J(object):
    def setupUi(self, Delete_Game_F_UI_J):
        Delete_Game_F_UI_J.setObjectName("Delete_Game_F_UI_J")
        Delete_Game_F_UI_J.resize(622, 127)
        Delete_Game_F_UI_J.setMinimumSize(QtCore.QSize(622, 127))
        Delete_Game_F_UI_J.setMaximumSize(QtCore.QSize(622, 127))
        Delete_Game_F_UI_J.setStyleSheet("QDialog{background-color: rgb(255, 255, 255);}\n"
"#pushButton{border:2px solid rgba(235, 235, 235,0);height:25px;border-radius:5px;}\n"
"#pushButton::hover{background-color: rgb(192, 192, 192);}\n"
"#pushButton::pressed{background-color: rgb(169, 169, 169);}\n"
"\n"
"#pushButton_2{background-color: rgba(255, 255, 255, 0);}\n"
"\n"
"#pushButton_3{border:2px solid rgba(235, 235, 235,0);height:25px;border-radius:5px;}\n"
"#pushButton_3::hover{background-color: rgb(192, 192, 192);}\n"
"#pushButton_3::pressed{background-color: rgb(169, 169, 169);}")
        self.gridLayout = QtWidgets.QGridLayout(Delete_Game_F_UI_J)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(Delete_Game_F_UI_J)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton.setStyleSheet("font-size: 14px;")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 4, 1, 3)
        self.label_2 = QtWidgets.QLabel(Delete_Game_F_UI_J)
        self.label_2.setStyleSheet("font-size: 16px;")
        self.label_2.setIndent(2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 6)
        self.pushButton_2 = QtWidgets.QPushButton(Delete_Game_F_UI_J)
        self.pushButton_2.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_2.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        MOS_catalogue_picture_trash_red_png = os.path.join("picture", "trash_red.png")
        icon.addPixmap(QtGui.QPixmap(MOS_catalogue_picture_trash_red_png), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 2, 1)
        spacerItem = QtWidgets.QSpacerItem(434, 27, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 3)
        self.label = QtWidgets.QLabel(Delete_Game_F_UI_J)
        self.label.setStyleSheet("font-size: 14px;")
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 6)
        self.pushButton_3 = QtWidgets.QPushButton(Delete_Game_F_UI_J)
        self.pushButton_3.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 3, 1, 1)

        self.retranslateUi(Delete_Game_F_UI_J)
        QtCore.QMetaObject.connectSlotsByName(Delete_Game_F_UI_J)

    def retranslateUi(self, Delete_Game_F_UI_J):
        _translate = QtCore.QCoreApplication.translate
        Delete_Game_F_UI_J.setWindowTitle(_translate("Delete_Game_F_UI_J", "Dialog"))
        self.pushButton.setText(_translate("Delete_Game_F_UI_J", "确定"))
        self.label_2.setText(_translate("Delete_Game_F_UI_J", "警告"))
        self.label.setText(_translate("Delete_Game_F_UI_J", "您确定要删除游戏文件夹吗 这将不会显示在您的游戏列表中 您可以重新添加"))
        self.pushButton_3.setText(_translate("Delete_Game_F_UI_J", "取消"))