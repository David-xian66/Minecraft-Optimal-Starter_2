# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Java_Dowmloader_OK_UI.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QWidget)
import Java_Dowmloader_rc

class Ui_Dialog_2(object):
    def setupUi(self, Dialog_2):
        if not Dialog_2.objectName():
            Dialog_2.setObjectName(u"Dialog_2")
        Dialog_2.resize(505, 120)
        Dialog_2.setMinimumSize(QSize(505, 120))
        Dialog_2.setMaximumSize(QSize(505, 120))
        Dialog_2.setStyleSheet(u"QDialog{background-color: rgb(255, 255, 255);}\n"
"#pushButton{border:2px solid rgba(235, 235, 235,0);height:25px;border-radius:5px;}\n"
"#pushButton::hover{background-color: rgb(192, 192, 192);}\n"
"#pushButton::pressed{background-color: rgb(169, 169, 169);}\n"
"\n"
"#pushButton_2{background-color: rgba(255, 255, 255, 0);}")
        self.gridLayout = QGridLayout(Dialog_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(Dialog_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 30))
        self.pushButton.setStyleSheet(u"font-size: 14px;")

        self.gridLayout.addWidget(self.pushButton, 2, 3, 1, 1)

        self.label_2 = QLabel(Dialog_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-size: 16px;")
        self.label_2.setMargin(0)
        self.label_2.setIndent(2)

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 2)

        self.label = QLabel(Dialog_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size: 14px;")

        self.gridLayout.addWidget(self.label, 1, 2, 1, 2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 1, 1, 2)

        self.pushButton_2 = QPushButton(Dialog_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(50, 50))
        self.pushButton_2.setMaximumSize(QSize(50, 50))
        icon = QIcon()
        icon.addFile(u":/ing/OK.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(40, 40))

        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 2, 1)


        self.retranslateUi(Dialog_2)

        QMetaObject.connectSlotsByName(Dialog_2)
    # setupUi

    def retranslateUi(self, Dialog_2):
        Dialog_2.setWindowTitle(QCoreApplication.translate("Dialog_2", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog_2", u"\u597d\u7684", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_2", u"\u63d0\u793a", None))
        self.label.setText(QCoreApplication.translate("Dialog_2", u"\u4e0b\u8f7d&\u914d\u7f6eJava\u5b8c\u6210", None))
        self.pushButton_2.setText("")
    # retranslateUi

