# Form implementation generated from reading ui file '/Users/xyj/.npm/ssh/UI/UI/MC_Dowmloader_UI.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MOS_D_MC_Dialog(object):
    def setupUi(self, MOS_D_MC_Dialog):
        MOS_D_MC_Dialog.setObjectName("MOS_D_MC_Dialog")
        MOS_D_MC_Dialog.resize(561, 249)
        MOS_D_MC_Dialog.setStyleSheet("QDialog{background-color: rgb(255, 255, 255);}\n"
"\n"
"QScrollArea{border-style:none;}\n"
"QPushButton{border:2px solid rgba(235, 235, 235,0);height:25px;border-radius:5px;}\n"
"QPushButton::hover{background-color: rgb(192, 192, 192);}\n"
"QPushButton::pressed{background-color: rgb(169, 169, 169);}")
        self.gridLayout_2 = QtWidgets.QGridLayout(MOS_D_MC_Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton = QtWidgets.QPushButton(MOS_D_MC_Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(150, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(MOS_D_MC_Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(MOS_D_MC_Dialog)
        self.scrollArea.setStyleSheet("QScrollArea{border-style:none;background-color: rgba(255, 255, 255, 0);}\n"
"QPushButton{border:2px solid rgba(235, 235, 235,0);height:25px;border-radius:5px;}\n"
"QPushButton::hover{background-color: rgb(192, 192, 192);}\n"
"QPushButton::pressed{background-color: rgb(169, 169, 169);}\n"
"\n"
"QProgressBar{\n"
"    text-align: center;border-style:none;border-radius:5px;background-color: rgb(235, 235, 235);height:3px;color: rgb(66, 66, 66);\n"
"}\n"
"QProgressBar::chunk{\n"
"    border-radius:5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(64, 183, 255, 255), stop:1 rgba(67, 146, 255, 255));\n"
"}\n"
"\n"
"QScrollArea{border-style:none;background-color: rgba(255, 255, 255, 0);}\n"
"/*设置垂直滚动条基本样式*/\n"
"QScrollBar:vertical\n"
"{\n"
"    width:8px;\n"
"    background:rgba(0,0,0,0%);\n"
"    margin:0px,0px,0px,0px;\n"
"    padding-top:9px;   /*留出9px给上面和下面的箭头*/\n"
"    padding-bottom:9px;\n"
"}\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    width:8px;\n"
"    background: rgb(214, 214, 214);\n"
"    border-radius:3px;   /*滚动条两端变成椭圆*/\n"
"    min-height:;\n"
"}\n"
"QScrollBar::handle:vertical:hover\n"
"{\n"
"    width:8px;\n"
"    background:rgb(192, 192, 192);   /* 鼠标放到滚动条上的时候，颜色变深*/\n"
"    border-radius:4px;\n"
"    min-height:;\n"
"}\n"
"QScrollBar::add-line:vertical   /*这个应该是设置下箭头的，3.png就是箭头*/\n"
"{\n"
"    height:9px;width:8px;\n"
"    border-image:url(:/img/picture/caret-down_1.png);\n"
"    subcontrol-position:bottom;\n"
"}\n"
"QScrollBar::sub-line:vertical   /*设置上箭头*/\n"
"{\n"
"    height:9px;width:8px;\n"
"    border-image:url(:/img/picture/caret-up_1.png);\n"
"    subcontrol-position:top;\n"
"}\n"
"QScrollBar::add-line:vertical:hover   /*当鼠标放到下箭头上的时候*/\n"
"{\n"
"    height:9px;width:8px;\n"
"    border-image:url(:/img/picture/caret-down.png);\n"
"    subcontrol-position:bottom;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover  /*当鼠标放到下箭头上的时候*/\n"
"{\n"
"    height:9px;width:8px;\n"
"    border-image:url(:/img/picture/caret-up.png);\n"
"    subcontrol-position:top;\n"
"}\n"
"QScrollBar::sub-page:vertical,QScrollBar::add-page:vertical   /*当滚动条滚动的时候，上面的部分和下面的部分*/\n"
"{\n"
"    background: rgba(235, 235, 235,150);\n"
"    border-radius:4px;\n"
"}\n"
"QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical   /*当滚动条滚动的时候，上面的部分和下面的部分*/\n"
"{\n"
"    background: rgba(235, 235, 235,150);\n"
"    border-radius:4px;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 537, 172))
        self.scrollAreaWidgetContents.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 3)
        self.progressBar = QtWidgets.QProgressBar(self.scrollAreaWidgetContents)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(110)
        self.progressBar.setProperty("value", 50)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 3)
        self.progressBar_2 = QtWidgets.QProgressBar(self.scrollAreaWidgetContents)
        self.progressBar_2.setProperty("value", 5)
        self.progressBar_2.setTextVisible(False)
        self.progressBar_2.setInvertedAppearance(False)
        self.progressBar_2.setObjectName("progressBar_2")
        self.gridLayout.addWidget(self.progressBar_2, 4, 0, 1, 3)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 3)
        self.progressBar_3 = QtWidgets.QProgressBar(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_3.sizePolicy().hasHeightForWidth())
        self.progressBar_3.setSizePolicy(sizePolicy)
        self.progressBar_3.setProperty("value", 5)
        self.progressBar_3.setTextVisible(False)
        self.progressBar_3.setInvertedAppearance(False)
        self.progressBar_3.setObjectName("progressBar_3")
        self.gridLayout.addWidget(self.progressBar_3, 6, 0, 1, 3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 2)
        self.label = QtWidgets.QLabel(MOS_D_MC_Dialog)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)

        self.retranslateUi(MOS_D_MC_Dialog)
        QtCore.QMetaObject.connectSlotsByName(MOS_D_MC_Dialog)

    def retranslateUi(self, MOS_D_MC_Dialog):
        _translate = QtCore.QCoreApplication.translate
        MOS_D_MC_Dialog.setWindowTitle(_translate("MOS_D_MC_Dialog", "Dialog"))
        self.pushButton.setText(_translate("MOS_D_MC_Dialog", "取消"))
        self.label_5.setText(_translate("MOS_D_MC_Dialog", "0 MB/S - 正在准备下载"))
        self.label_2.setText(_translate("MOS_D_MC_Dialog", "下载主文件"))
        self.label_4.setText(_translate("MOS_D_MC_Dialog", "安装游戏"))
        self.label_3.setText(_translate("MOS_D_MC_Dialog", "下载资源库"))
        self.label.setText(_translate("MOS_D_MC_Dialog", "安装游戏"))
