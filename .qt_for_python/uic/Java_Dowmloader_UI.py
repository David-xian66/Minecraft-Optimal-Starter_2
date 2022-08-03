# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Java_Dowmloader_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QProgressBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import Java_Dowmloader_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(568, 255)
        Dialog.setMinimumSize(QSize(568, 255))
        Dialog.setMaximumSize(QSize(568, 255))
        Dialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea{border-style:none;}\n"
"QPushButton{border:2px solid rgba(235, 235, 235,0);height:25px;border-radius:5px;}\n"
"QPushButton::hover{background-color: rgb(192, 192, 192);}\n"
"QPushButton::pressed{background-color: rgb(169, 169, 169);}\n"
"\n"
"QProgressBar{\n"
"	text-align: center;border-style:none;border-radius:5px;background-color: rgb(235, 235, 235);height:3px;color: rgb(66, 66, 66);\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius:5px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(64, 183, 255, 255), stop:1 rgba(67, 146, 255, 255));\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 544, 207))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 2)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.pushButton = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setMaximumSize(QSize(150, 30))

        self.gridLayout.addWidget(self.pushButton, 5, 1, 1, 1)

        self.progressBar = QProgressBar(self.scrollAreaWidgetContents)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(110)
        self.progressBar.setValue(50)
        self.progressBar.setTextVisible(False)

        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 2)

        self.progressBar_2 = QProgressBar(self.scrollAreaWidgetContents)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setValue(5)
        self.progressBar_2.setTextVisible(False)
        self.progressBar_2.setInvertedAppearance(False)

        self.gridLayout.addWidget(self.progressBar_2, 3, 0, 1, 2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u6b63\u5728\u4e0b\u8f7dJava", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u4e0b\u8f7dJava", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u914d\u7f6eJava", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"0 MB/S - \u6b63\u5728\u51c6\u5907\u4e0b\u8f7d", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
    # retranslateUi

