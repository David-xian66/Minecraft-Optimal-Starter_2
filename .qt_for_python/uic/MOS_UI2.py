# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MOS_UI2.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFontComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QProgressBar, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTextBrowser,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)
import img_rc

class Ui_MOS(object):
    def setupUi(self, MOS):
        if not MOS.objectName():
            MOS.setObjectName(u"MOS")
        MOS.setWindowModality(Qt.NonModal)
        MOS.resize(1000, 533)
        MOS.setMinimumSize(QSize(1000, 533))
        icon = QIcon()
        icon.addFile(u"../picture/ico.png", QSize(), QIcon.Normal, QIcon.Off)
        MOS.setWindowIcon(icon)
        MOS.setStyleSheet(u"")
        self.centralwidget = QWidget(MOS)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgba(255, 255, 255,0);")
        self.gridLayout_13 = QGridLayout(self.centralwidget)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setHorizontalSpacing(0)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_mos_right = QStackedWidget(self.centralwidget)
        self.stackedWidget_mos_right.setObjectName(u"stackedWidget_mos_right")
        self.stackedWidget_mos_right.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.page_gonggao = QWidget()
        self.page_gonggao.setObjectName(u"page_gonggao")
        self.page_gonggao.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.page_gonggao)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(12, -1, -1, -1)
        self.scrollArea_page_gonggao = QScrollArea(self.page_gonggao)
        self.scrollArea_page_gonggao.setObjectName(u"scrollArea_page_gonggao")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.scrollArea_page_gonggao.sizePolicy().hasHeightForWidth())
        self.scrollArea_page_gonggao.setSizePolicy(sizePolicy)
        self.scrollArea_page_gonggao.setMinimumSize(QSize(790, 0))
        self.scrollArea_page_gonggao.setStyleSheet(u"border-style:none;background-color: rgb(255, 255, 255);")
        self.scrollArea_page_gonggao.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 808, 509))
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.gridLayout_16 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.widget_scrollArea_page_gonggao_left = QWidget(self.scrollAreaWidgetContents)
        self.widget_scrollArea_page_gonggao_left.setObjectName(u"widget_scrollArea_page_gonggao_left")
        self.widget_scrollArea_page_gonggao_left.setMinimumSize(QSize(399, 509))
        self.widget_scrollArea_page_gonggao_left.setStyleSheet(u"QWidget{border:2px solid rgb(0, 150, 255);border-radius:15px;}\n"
"QLabel{border-style:none;}")
        self.gridLayout_5 = QGridLayout(self.widget_scrollArea_page_gonggao_left)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(0)
        self.gridLayout_5.setContentsMargins(10, -1, 10, -1)
        self.stackedWidget_gonggao = QStackedWidget(self.widget_scrollArea_page_gonggao_left)
        self.stackedWidget_gonggao.setObjectName(u"stackedWidget_gonggao")
        self.stackedWidget_gonggao.setStyleSheet(u"border-style:none;")
        self.stackedWidget_gonggao.setFrameShape(QFrame.NoFrame)
        self.stackedWidget_gonggao.setLineWidth(2)
        self.page_gonggao_jiazai = QWidget()
        self.page_gonggao_jiazai.setObjectName(u"page_gonggao_jiazai")
        self.page_gonggao_jiazai.setStyleSheet(u"QTextBrowser{border-style:none;background-color: rgba(255, 255, 255, 0);}")
        self.gridLayout_20 = QGridLayout(self.page_gonggao_jiazai)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.textBrowser_gonggao_left_txt = QTextBrowser(self.page_gonggao_jiazai)
        self.textBrowser_gonggao_left_txt.setObjectName(u"textBrowser_gonggao_left_txt")
        self.textBrowser_gonggao_left_txt.setStyleSheet(u"")

        self.gridLayout_20.addWidget(self.textBrowser_gonggao_left_txt, 0, 0, 1, 1)

        self.stackedWidget_gonggao.addWidget(self.page_gonggao_jiazai)
        self.page_gonggao_jiazai_ing = QWidget()
        self.page_gonggao_jiazai_ing.setObjectName(u"page_gonggao_jiazai_ing")
        self.page_gonggao_jiazai_ing.setStyleSheet(u"QProgressBar{\n"
"	text-align: center;border-style:none;border-radius:7px;background-color: rgba(0, 150, 255, 10);height:15px;color: rgb(66, 66, 66);\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius:7px;\n"
"	background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(53, 244, 252, 255), stop:1 rgba(222, 255, 255, 255));\n"
"}\n"
"QLabel{color: rgb(0, 150, 255);}")
        self.gridLayout_21 = QGridLayout(self.page_gonggao_jiazai_ing)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_21.addItem(self.verticalSpacer_6, 0, 0, 1, 1)

        self.label_2 = QLabel(self.page_gonggao_jiazai_ing)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-size: 13px;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.label_2, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(40, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_21.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.progressBar_2 = QProgressBar(self.page_gonggao_jiazai_ing)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setStyleSheet(u"font-size: 13px;")
        self.progressBar_2.setMinimum(0)
        self.progressBar_2.setMaximum(100)
        self.progressBar_2.setValue(25)
        self.progressBar_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.progressBar_2.setTextVisible(True)
        self.progressBar_2.setOrientation(Qt.Horizontal)
        self.progressBar_2.setInvertedAppearance(False)
        self.progressBar_2.setTextDirection(QProgressBar.TopToBottom)

        self.gridLayout_21.addWidget(self.progressBar_2, 2, 0, 1, 1)

        self.stackedWidget_gonggao.addWidget(self.page_gonggao_jiazai_ing)

        self.gridLayout_5.addWidget(self.stackedWidget_gonggao, 2, 0, 1, 2)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_11, 3, 0, 1, 1)

        self.line_7 = QFrame(self.widget_scrollArea_page_gonggao_left)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setLayoutDirection(Qt.LeftToRight)
        self.line_7.setAutoFillBackground(False)
        self.line_7.setStyleSheet(u"background-color: rgb(169, 169, 169);border:none;")
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.line_7.setLineWidth(1)
        self.line_7.setFrameShape(QFrame.HLine)

        self.gridLayout_5.addWidget(self.line_7, 1, 0, 1, 2)

        self.label_gonggao_left_txt = QLabel(self.widget_scrollArea_page_gonggao_left)
        self.label_gonggao_left_txt.setObjectName(u"label_gonggao_left_txt")
        self.label_gonggao_left_txt.setStyleSheet(u"font-size: 14px;")
        self.label_gonggao_left_txt.setAlignment(Qt.AlignCenter)
        self.label_gonggao_left_txt.setWordWrap(True)

        self.gridLayout_5.addWidget(self.label_gonggao_left_txt, 0, 0, 1, 1)


        self.gridLayout_16.addWidget(self.widget_scrollArea_page_gonggao_left, 0, 0, 1, 1)

        self.widget_scrollArea_page_gonggao_right = QWidget(self.scrollAreaWidgetContents)
        self.widget_scrollArea_page_gonggao_right.setObjectName(u"widget_scrollArea_page_gonggao_right")
        self.widget_scrollArea_page_gonggao_right.setMinimumSize(QSize(399, 509))
        self.widget_scrollArea_page_gonggao_right.setStyleSheet(u"QWidget{border:2px solid rgb(0, 150, 255);border-radius:15px;}\n"
"QLabel{border-style:none;}\n"
"QProgressBar{\n"
"	text-align: center;border-style:none;border-radius:7px;background-color: rgba(0, 150, 255, 10);height:15px;color: rgb(66, 66, 66);\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius:7px;\n"
"	background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(53, 244, 252, 255), stop:1 rgba(222, 255, 255, 255));\n"
"}")
        self.gridLayout_28 = QGridLayout(self.widget_scrollArea_page_gonggao_right)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.label__gonggao_right_txt = QLabel(self.widget_scrollArea_page_gonggao_right)
        self.label__gonggao_right_txt.setObjectName(u"label__gonggao_right_txt")
        self.label__gonggao_right_txt.setStyleSheet(u"font-size: 14px;")
        self.label__gonggao_right_txt.setAlignment(Qt.AlignCenter)
        self.label__gonggao_right_txt.setWordWrap(True)

        self.gridLayout_28.addWidget(self.label__gonggao_right_txt, 0, 0, 1, 1)

        self.line_8 = QFrame(self.widget_scrollArea_page_gonggao_right)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setStyleSheet(u"background-color: rgb(169, 169, 169);border:none;")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout_28.addWidget(self.line_8, 1, 0, 1, 1)

        self.widget_scrollArea_page_gonggao_statring = QWidget(self.widget_scrollArea_page_gonggao_right)
        self.widget_scrollArea_page_gonggao_statring.setObjectName(u"widget_scrollArea_page_gonggao_statring")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_scrollArea_page_gonggao_statring.sizePolicy().hasHeightForWidth())
        self.widget_scrollArea_page_gonggao_statring.setSizePolicy(sizePolicy1)
        self.widget_scrollArea_page_gonggao_statring.setStyleSheet(u"border-style:none;")
        self.gridLayout_2 = QGridLayout(self.widget_scrollArea_page_gonggao_statring)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.progressBar = QProgressBar(self.widget_scrollArea_page_gonggao_statring)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"font-size: 13px;")
        self.progressBar.setMinimum(0)
        self.progressBar.setValue(0)

        self.gridLayout_2.addWidget(self.progressBar, 2, 0, 1, 5)

        self.verticalSpacer_4 = QSpacerItem(10, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 0, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(10, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 0, 4, 2, 1)

        self.label_3 = QLabel(self.widget_scrollArea_page_gonggao_statring)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"border-style:none;background-color: rgba(255, 255, 255, 0);")
        self.label_3.setPixmap(QPixmap(u"../../../Desktop/MOS/picture/loading_3.gif"))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_3, 0, 1, 2, 3)

        self.label_7 = QLabel(self.widget_scrollArea_page_gonggao_statring)
        self.label_7.setObjectName(u"label_7")
        font = QFont()
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"font-size: 13px;")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 5)


        self.gridLayout_28.addWidget(self.widget_scrollArea_page_gonggao_statring, 2, 0, 1, 1)

        self.widget_9 = QWidget(self.widget_scrollArea_page_gonggao_right)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy2)
        self.widget_9.setStyleSheet(u"QWidget{border-style:none;}\n"
"QPushButton{border:2px solid rgb(192, 192, 192);border-radius:8px;}\n"
"#pushButton__gonggao_start{border:2px solid rgb(0, 150, 255);height:25px;border-radius:8px;}\n"
"#pushButton__gonggao_start::hover{color: rgb(0, 150, 255,100);}\n"
"#pushButton__gonggao_start::pressed{background-color: rgba(0, 150, 255, 50);}\n"
"\n"
"QComboBox {\n"
"    border: 2px solid rgb(169, 169, 169); /* border: \u5bbd\u5ea6 \u7ebf\u7c7b\u578b \u989c\u8272 */\n"
"    height:25px;\n"
"    /*background-color: rgba(0, 150, 255, 150);*/\n"
"    background-color: rgba(214, 214, 214,100);\n"
"    border-radius:8px;\n"
"}\n"
"\n"
"/*\u4e0b\u62c9\u6846\u7684\u6837\u5f0f*/\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    outline: 0px solid gray;  /*\u53d6\u6d88\u9009\u4e2d\u865a\u7ebf*/\n"
"    border: 1px solid rgb(31, 156, 255);\n"
"    color: rgb(66, 66, 66);\n"
"    background-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(0, 150, 255);\n"
"    border-radius:5px;\n"
"    height:35px;\n"
" "
                        "   border:None;\n"
"}\n"
"/*\u9009\u4e2d\u6bcf\u4e00\u9879\u7684\u5b57\u4f53\u989c\u8272\u548c\u80cc\u666f\u989c\u8272*/\n"
"QComboBox::item:selected \n"
"{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 150, 255);\n"
"    border-radius:5px;\n"
"}\n"
"/*\u53f3\u8fb9*/\n"
"QComboBox::drop-down{border: 2px solid rgba(0, 150, 255,0);}\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(:/img/picture/back_blue_down.png);\n"
"    width: 25px;\n"
"    height: 35px;\n"
"    right:6px;\n"
"    border-left: 2px solid rgb(192, 192, 192);\n"
"    border-right: 1px solid rgba(214, 214, 214,0);\n"
"}\n"
"QComboBox::down-arrow:on\n"
"{\n"
"    image: url(:/img/picture/back_blue_up.png);\n"
"    width: 25px;\n"
"    height: 35px;\n"
"    right:6px;\n"
"    border-left: 2px solid rgb(192, 192, 192);\n"
"    border-right: 1px solid rgba(214, 214, 214,0);\n"
"}\n"
"/*QComboBox::down-arrow::hover{}*\n"
"\n"
"/* QComboBox\u4e2d\u7684\u5782\u76f4\u6eda\u52a8\u6761 */\n"
"QComboBox QAbstractScrollArea QScrollBar"
                        ":vertical {\n"
"    width: 10px;\n"
"    height: 8px;\n"
"    background-color: rgb(255, 64, 255);   /* \u7a7a\u767d\u533a\u57df\u7684\u80cc\u666f\u8272*/\n"
"    border-style:none;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical {\n"
"    border-radius: 5px;   /* \u5706\u89d2 */\n"
"    background: rgb(160,160,160);   /* \u5c0f\u65b9\u5757\u7684\u80cc\u666f\u8272\u6df1\u7070lightblue */\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical:hover {\n"
"    background: rgb(255, 255, 255);   /* \u8d8a\u8fc7\u5c0f\u65b9\u5757\u7684\u80cc\u666f\u8272*/\n"
"}")
        self.gridLayout_6 = QGridLayout(self.widget_9)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(5)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_16 = QPushButton(self.widget_9)
        self.pushButton_16.setObjectName(u"pushButton_16")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy3)
        self.pushButton_16.setMinimumSize(QSize(183, 29))
        self.pushButton_16.setStyleSheet(u"font-size: 14px;")

        self.gridLayout_6.addWidget(self.pushButton_16, 0, 0, 1, 1)

        self.pushButton_17 = QPushButton(self.widget_9)
        self.pushButton_17.setObjectName(u"pushButton_17")
        sizePolicy3.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy3)
        self.pushButton_17.setMinimumSize(QSize(183, 29))
        self.pushButton_17.setStyleSheet(u"font-size: 14px;")

        self.gridLayout_6.addWidget(self.pushButton_17, 0, 1, 1, 1)

        self.comboBox_gonggao_right = QComboBox(self.widget_9)
        self.comboBox_gonggao_right.setObjectName(u"comboBox_gonggao_right")
        sizePolicy3.setHeightForWidth(self.comboBox_gonggao_right.sizePolicy().hasHeightForWidth())
        self.comboBox_gonggao_right.setSizePolicy(sizePolicy3)
        self.comboBox_gonggao_right.setMinimumSize(QSize(183, 29))
        self.comboBox_gonggao_right.setMouseTracking(False)
        self.comboBox_gonggao_right.setStyleSheet(u"font-size: 14px;")
        self.comboBox_gonggao_right.setEditable(False)
        self.comboBox_gonggao_right.setMaxVisibleItems(15)
        self.comboBox_gonggao_right.setMaxCount(2147483647)
        self.comboBox_gonggao_right.setMinimumContentsLength(0)
        self.comboBox_gonggao_right.setDuplicatesEnabled(False)
        self.comboBox_gonggao_right.setFrame(True)
        self.comboBox_gonggao_right.setModelColumn(0)

        self.gridLayout_6.addWidget(self.comboBox_gonggao_right, 1, 0, 1, 1)

        self.pushButton__gonggao_start = QPushButton(self.widget_9)
        self.pushButton__gonggao_start.setObjectName(u"pushButton__gonggao_start")
        sizePolicy3.setHeightForWidth(self.pushButton__gonggao_start.sizePolicy().hasHeightForWidth())
        self.pushButton__gonggao_start.setSizePolicy(sizePolicy3)
        self.pushButton__gonggao_start.setMinimumSize(QSize(183, 29))
        self.pushButton__gonggao_start.setStyleSheet(u"font-size: 14px;")

        self.gridLayout_6.addWidget(self.pushButton__gonggao_start, 1, 1, 1, 1)


        self.gridLayout_28.addWidget(self.widget_9, 3, 0, 1, 1)


        self.gridLayout_16.addWidget(self.widget_scrollArea_page_gonggao_right, 0, 1, 1, 1)

        self.scrollArea_page_gonggao.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea_page_gonggao)

        self.stackedWidget_mos_right.addWidget(self.page_gonggao)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.page_8.setStyleSheet(u"QLabel{border-style:none;color:rgb(33, 33, 33);background-color: rgba(255, 255, 255, 0);}")
        self.gridLayout_50 = QGridLayout(self.page_8)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.gridLayout_50.setVerticalSpacing(0)
        self.gridLayout_50.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_mos_right_2 = QStackedWidget(self.page_8)
        self.stackedWidget_mos_right_2.setObjectName(u"stackedWidget_mos_right_2")
        self.stackedWidget_mos_right_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 128);")
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.page_12.setStyleSheet(u"#pushButton_35\n"
"{\n"
"	width:30px;border-radius: 13px;background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"#pushButton_35::hover\n"
"{\n"
"	border-radius: 13px;\n"
"	background-color: rgba(192, 192, 192, 128);\n"
"}\n"
"#pushButton_35::pressed\n"
"{\n"
"	background-color: rgba(0, 150, 255, 51);\n"
"}\n"
"#pushButton_41\n"
"{\n"
"	width:30px;border-radius: 13px;background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"#pushButton_41::hover\n"
"{\n"
"	border-radius: 13px;\n"
"	background-color: rgba(192, 192, 192, 128);\n"
"}\n"
"#pushButton_41::pressed\n"
"{\n"
"	background-color: rgba(0, 150, 255, 51);\n"
"}")
        self.gridLayout_33 = QGridLayout(self.page_12)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_33.setHorizontalSpacing(0)
        self.gridLayout_33.setContentsMargins(5, 0, 5, 5)
        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_33.addItem(self.horizontalSpacer_40, 1, 3, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(805, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_33.addItem(self.horizontalSpacer_20, 0, 0, 1, 4)

        self.line_11 = QFrame(self.page_12)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setStyleSheet(u"color:rgb(214, 214, 214)")
        self.line_11.setFrameShadow(QFrame.Plain)
        self.line_11.setMidLineWidth(1)
        self.line_11.setFrameShape(QFrame.HLine)

        self.gridLayout_33.addWidget(self.line_11, 2, 0, 1, 4)

        self.label_24 = QLabel(self.page_12)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"font-size: 17px;")
        self.label_24.setIndent(8)
        self.label_24.setOpenExternalLinks(False)

        self.gridLayout_33.addWidget(self.label_24, 1, 1, 1, 1)

        self.widget_20 = QWidget(self.page_12)
        self.widget_20.setObjectName(u"widget_20")
        self.gridLayout_55 = QGridLayout(self.widget_20)
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.gridLayout_55.setHorizontalSpacing(4)
        self.gridLayout_55.setContentsMargins(0, 0, 0, 0)
        self.line_16 = QFrame(self.widget_20)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setStyleSheet(u"border-style:none;background-color: rgba(66, 66, 66,200);")
        self.line_16.setFrameShape(QFrame.VLine)
        self.line_16.setFrameShadow(QFrame.Sunken)

        self.gridLayout_55.addWidget(self.line_16, 0, 1, 1, 1)

        self.widget_7 = QWidget(self.widget_20)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMaximumSize(QSize(185, 16777215))
        self.widget_7.setStyleSheet(u"#listWidget{border-style:none;}\n"
"QListView::item {\n"
"    height: 30px;\n"
"	padding: 10px;\n"
"	border-left: 3px solid rgba(214, 214, 214,0);\n"
"}\n"
"QListView::item:hover {\n"
"	border-left: 3px solid rgb(214, 214, 214);\n"
"	background-color: transparent;\n"
"}\n"
"QListView::item:selected {\n"
"	background-color: transparent;\n"
"	color: black;\n"
"	border-left: 3px solid rgb(0, 150, 255);\n"
"}\n"
"QPushButton\n"
"{\n"
"	border-radius: 2px;background-color: rgba(255, 255, 255, 0);border-style:none;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	border-radius: 2px;\n"
"	background-color: rgba(192, 192, 192, 128);\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: rgba(0, 150, 255, 51);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget_7)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.listWidget = QListWidget(self.widget_7)
        icon1 = QIcon()
        icon1.addFile(u"../picture/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem = QListWidgetItem(self.listWidget)
        __qlistwidgetitem.setIcon(icon1);
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u"font-size: 15px;")
        self.listWidget.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.listWidget)

        self.pushButton_38 = QPushButton(self.widget_7)
        self.pushButton_38.setObjectName(u"pushButton_38")
        self.pushButton_38.setMinimumSize(QSize(0, 30))
        self.pushButton_38.setStyleSheet(u"font-size: 13px;")
        icon2 = QIcon()
        icon2.addFile(u"../picture/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_38.setIcon(icon2)

        self.verticalLayout.addWidget(self.pushButton_38)

        self.pushButton_36 = QPushButton(self.widget_7)
        self.pushButton_36.setObjectName(u"pushButton_36")
        self.pushButton_36.setMinimumSize(QSize(0, 30))
        self.pushButton_36.setStyleSheet(u"font-size: 13px;")
        icon3 = QIcon()
        icon3.addFile(u"../picture/folder_add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_36.setIcon(icon3)

        self.verticalLayout.addWidget(self.pushButton_36)

        self.pushButton_37 = QPushButton(self.widget_7)
        self.pushButton_37.setObjectName(u"pushButton_37")
        self.pushButton_37.setMinimumSize(QSize(0, 30))
        self.pushButton_37.setStyleSheet(u"font-size: 13px;")
        icon4 = QIcon()
        icon4.addFile(u"../picture/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_37.setIcon(icon4)

        self.verticalLayout.addWidget(self.pushButton_37)


        self.gridLayout_55.addWidget(self.widget_7, 0, 0, 1, 1)

        self.widget_6 = QWidget(self.widget_20)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout_52 = QGridLayout(self.widget_6)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.gridLayout_52.setHorizontalSpacing(0)
        self.gridLayout_52.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_5 = QStackedWidget(self.widget_6)
        self.stackedWidget_5.setObjectName(u"stackedWidget_5")
        self.stackedWidget_5.setStyleSheet(u"")
        self.page_21 = QWidget()
        self.page_21.setObjectName(u"page_21")
        self.page_21.setStyleSheet(u"#listWidget_2{border-style:none;}\n"
"QListView::item {\n"
"    height: 25px;\n"
"	padding: 8px;\n"
"	border-left: 3px solid rgba(214, 214, 214,0);\n"
"}\n"
"QListView::item:hover {\n"
"	border-left: 3px solid rgb(214, 214, 214);\n"
"	background-color: transparent;\n"
"}\n"
"QListView::item:selected {\n"
"	background-color: transparent;\n"
"	color: black;\n"
"	background-color: rgb(235, 235, 235);\n"
"	border-left: 3px solid rgb(0, 150, 255);\n"
"}")
        self.gridLayout_51 = QGridLayout(self.page_21)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.gridLayout_51.setContentsMargins(0, 0, 0, 0)
        self.listWidget_2 = QListWidget(self.page_21)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setStyleSheet(u"font-size: 14px;")

        self.gridLayout_51.addWidget(self.listWidget_2, 0, 0, 1, 1)

        self.stackedWidget_5.addWidget(self.page_21)
        self.page_25 = QWidget()
        self.page_25.setObjectName(u"page_25")
        self.page_25.setStyleSheet(u"#label_43{border-style:none;color:rgb(33, 33, 33);background-color: rgba(255, 255, 255, 0);}")
        self.gridLayout_22 = QGridLayout(self.page_25)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.widget_22 = QWidget(self.page_25)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setStyleSheet(u"QWidget{border-radius: 15px;background-color: rgb(249, 249, 249);}\n"
"QLineEdit{border-radius: 10px;border:2px solid rgb(192, 192, 192);background-color: rgb(255, 255, 255);}\n"
"QLineEdit::focus{border:2px solid rgb(0, 250, 146);}")
        self.gridLayout_58 = QGridLayout(self.widget_22)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.label_44 = QLabel(self.widget_22)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setStyleSheet(u"font-size: 14px;")
        self.label_44.setAlignment(Qt.AlignCenter)

        self.gridLayout_58.addWidget(self.label_44, 0, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.widget_22)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 28))
        self.lineEdit_4.setStyleSheet(u"font-size: 14px;")
        self.lineEdit_4.setDragEnabled(False)
        self.lineEdit_4.setReadOnly(False)

        self.gridLayout_58.addWidget(self.lineEdit_4, 0, 1, 1, 1)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_58.addItem(self.horizontalSpacer_38, 1, 0, 1, 1)

        self.label_47 = QLabel(self.widget_22)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"font-size: 14px;")
        self.label_47.setAlignment(Qt.AlignCenter)

        self.gridLayout_58.addWidget(self.label_47, 1, 1, 1, 1)


        self.gridLayout_22.addWidget(self.widget_22, 2, 0, 1, 4)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_22.addItem(self.verticalSpacer_14, 5, 0, 1, 4)

        self.label_43 = QLabel(self.page_25)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setStyleSheet(u"font-size: 17px;")
        self.label_43.setLineWidth(1)
        self.label_43.setIndent(4)
        self.label_43.setOpenExternalLinks(False)

        self.gridLayout_22.addWidget(self.label_43, 0, 1, 1, 1)

        self.widget_21 = QWidget(self.page_25)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setStyleSheet(u"QWidget{border-radius: 15px;background-color: rgb(249, 249, 249);}\n"
"QPushButton{border-radius: 10px;border:2px solid rgb(192, 192, 192);background-color: rgb(255, 255, 255);}\n"
"QPushButton::hover{background-color: rgb(118, 214, 255);border:2px solid rgb(128, 217, 255);color: rgb(255, 255, 255);}")
        self.gridLayout_57 = QGridLayout(self.widget_21)
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.label_45 = QLabel(self.widget_21)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font)
        self.label_45.setStyleSheet(u"font-size: 14px;")
        self.label_45.setAlignment(Qt.AlignCenter)
        self.label_45.setWordWrap(False)
        self.label_45.setOpenExternalLinks(False)

        self.gridLayout_57.addWidget(self.label_45, 0, 0, 2, 1)

        self.label_48 = QLabel(self.widget_21)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setStyleSheet(u"font-size: 14px;")
        self.label_48.setAlignment(Qt.AlignCenter)

        self.gridLayout_57.addWidget(self.label_48, 2, 0, 1, 1)

        self.pushButton_42 = QPushButton(self.widget_21)
        self.pushButton_42.setObjectName(u"pushButton_42")
        self.pushButton_42.setMinimumSize(QSize(0, 28))
        self.pushButton_42.setStyleSheet(u"font-size: 14px;")
        self.pushButton_42.setIcon(icon1)

        self.gridLayout_57.addWidget(self.pushButton_42, 0, 2, 2, 1)

        self.label_46 = QLabel(self.widget_21)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"font-size: 13px;")
        self.label_46.setAlignment(Qt.AlignCenter)

        self.gridLayout_57.addWidget(self.label_46, 2, 2, 1, 1)


        self.gridLayout_22.addWidget(self.widget_21, 1, 0, 1, 4)

        self.pushButton_41 = QPushButton(self.page_25)
        self.pushButton_41.setObjectName(u"pushButton_41")
        self.pushButton_41.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u"../picture/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_41.setIcon(icon5)
        self.pushButton_41.setIconSize(QSize(27, 30))
        self.pushButton_41.setAutoDefault(False)
        self.pushButton_41.setFlat(False)

        self.gridLayout_22.addWidget(self.pushButton_41, 0, 0, 1, 1)

        self.widget_3 = QWidget(self.page_25)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setEnabled(False)
        self.widget_3.setMinimumSize(QSize(602, 44))
        self.widget_3.setStyleSheet(u"QWiget{background-color: rgba(255, 255, 255, 0);}\n"
"QPushButton\n"
"{\n"
"	border-radius: 10px;border:2px solid rgb(115, 250, 121);background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	color: rgb(115, 250, 121);\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: rgb(115, 250, 121);color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:disabled{\n"
"	/*\u7981\u7528*/\n"
"	border-radius: 10px;border:2px solid rgb(214, 214, 214);background-color: rgb(255, 255, 255);\n"
"}")
        self.gridLayout_27 = QGridLayout(self.widget_3)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_17, 1, 3, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_21, 1, 1, 1, 1)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_22, 1, 2, 1, 1)

        self.pushButton_18 = QPushButton(self.widget_3)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setEnabled(False)
        self.pushButton_18.setMinimumSize(QSize(0, 28))
        font1 = QFont()
        font1.setBold(False)
        font1.setKerning(True)
        self.pushButton_18.setFont(font1)
        self.pushButton_18.setStyleSheet(u"font-size: 14px;")
        self.pushButton_18.setIconSize(QSize(16, 16))
        self.pushButton_18.setChecked(False)
        self.pushButton_18.setAutoRepeat(False)
        self.pushButton_18.setAutoExclusive(False)
        self.pushButton_18.setAutoDefault(False)

        self.gridLayout_27.addWidget(self.pushButton_18, 0, 1, 1, 2)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_18, 1, 0, 1, 1)


        self.gridLayout_22.addWidget(self.widget_3, 3, 0, 1, 4)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_37, 0, 3, 1, 1)

        self.stackedWidget_5.addWidget(self.page_25)
        self.page_22 = QWidget()
        self.page_22.setObjectName(u"page_22")
        self.page_22.setStyleSheet(u"QLineEdit{height:23px;border-radius:8px;border:2px solid rgb(192, 192, 192);}\n"
"#pushButton_39{height:23px;border-radius:8px;border:2px solid rgb(192, 192, 192);}\n"
"#pushButton_40{height:30px;background-color: rgba(255, 255, 255,0);border-radius:7px;border:2px solid rgb(255, 59, 0);height:27px;}\n"
"#pushButton_40::hover{color: rgb(255, 59, 0)}\n"
"#pushButton_40::pressed{background-color: rgba(255, 0, 0, 100);}")
        self.gridLayout_53 = QGridLayout(self.page_22)
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.gridLayout_53.setContentsMargins(0, 0, 0, 0)
        self.pushButton_40 = QPushButton(self.page_22)
        self.pushButton_40.setObjectName(u"pushButton_40")
        self.pushButton_40.setFont(font)
        self.pushButton_40.setStyleSheet(u"font-size: 13px;")
        icon6 = QIcon()
        icon6.addFile(u"../picture/trash_red.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_40.setIcon(icon6)
        self.pushButton_40.setIconSize(QSize(20, 20))
        self.pushButton_40.setCheckable(False)

        self.gridLayout_53.addWidget(self.pushButton_40, 4, 1, 1, 2)

        self.lineEdit_3 = QLineEdit(self.page_22)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet(u"font-size: 13px;")

        self.gridLayout_53.addWidget(self.lineEdit_3, 1, 0, 1, 2)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_53.addItem(self.horizontalSpacer_33, 6, 0, 1, 2)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_53.addItem(self.horizontalSpacer_36, 0, 0, 1, 4)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_53.addItem(self.horizontalSpacer_35, 3, 0, 1, 4)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_53.addItem(self.horizontalSpacer_34, 6, 2, 1, 2)

        self.pushButton_39 = QPushButton(self.page_22)
        self.pushButton_39.setObjectName(u"pushButton_39")
        self.pushButton_39.setFont(font)
        self.pushButton_39.setStyleSheet(u"font-size: 14px;")

        self.gridLayout_53.addWidget(self.pushButton_39, 1, 2, 1, 2)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_53.addItem(self.verticalSpacer_18, 5, 0, 1, 4)

        self.stackedWidget_5.addWidget(self.page_22)
        self.page_23 = QWidget()
        self.page_23.setObjectName(u"page_23")
        self.gridLayout_54 = QGridLayout(self.page_23)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.gridLayout_54.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.page_23)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setPixmap(QPixmap(u"../picture/loading.gif"))
        self.label_26.setScaledContents(False)
        self.label_26.setAlignment(Qt.AlignCenter)
        self.label_26.setWordWrap(False)

        self.gridLayout_54.addWidget(self.label_26, 0, 2, 1, 1)

        self.stackedWidget_5.addWidget(self.page_23)

        self.gridLayout_52.addWidget(self.stackedWidget_5, 0, 0, 1, 1)


        self.gridLayout_55.addWidget(self.widget_6, 0, 2, 1, 1)


        self.gridLayout_33.addWidget(self.widget_20, 3, 0, 1, 4)

        self.pushButton_35 = QPushButton(self.page_12)
        self.pushButton_35.setObjectName(u"pushButton_35")
        self.pushButton_35.setStyleSheet(u"")
        self.pushButton_35.setIcon(icon5)
        self.pushButton_35.setIconSize(QSize(27, 30))

        self.gridLayout_33.addWidget(self.pushButton_35, 1, 0, 1, 1)

        self.stackedWidget_mos_right_2.addWidget(self.page_12)

        self.gridLayout_50.addWidget(self.stackedWidget_mos_right_2, 0, 0, 1, 1)

        self.stackedWidget_mos_right.addWidget(self.page_8)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"QLabel{border-style:none;color:rgb(33, 33, 33);background-color: rgba(255, 255, 255, 0);}")
        self.gridLayout_7 = QGridLayout(self.page_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(5, 0, 5, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_3, 4, 0, 1, 2)

        self.label_9 = QLabel(self.page_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font-size: 17px;")
        self.label_9.setIndent(10)

        self.gridLayout_7.addWidget(self.label_9, 1, 0, 1, 1)

        self.line = QFrame(self.page_2)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"color:rgb(214, 214, 214)")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QFrame.HLine)

        self.gridLayout_7.addWidget(self.line, 2, 0, 1, 2)

        self.widget_5 = QWidget(self.page_2)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"QWidget{border-radius:10px;border:2px solid rgb(0, 150, 255);}\n"
"QLabel{border-style:none;color:rgb(0, 150, 255);}")
        self.gridLayout_8 = QGridLayout(self.widget_5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(12, -1, -1, -1)
        self.label_8 = QLabel(self.widget_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font-size: 13px;")

        self.gridLayout_8.addWidget(self.label_8, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.widget_5, 3, 0, 1, 2)

        self.horizontalSpacer_3 = QSpacerItem(49, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.stackedWidget_mos_right.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        font2 = QFont()
        font2.setPointSize(13)
        self.page_3.setFont(font2)
        self.page_3.setStyleSheet(u"QLabel{border-style:none;color:rgb(33, 33, 33);background-color: rgba(255, 255, 255, 0);}\n"
"QComboBox {\n"
"    border: 2px solid rgb(169, 169, 169); /* border: \u5bbd\u5ea6 \u7ebf\u7c7b\u578b \u989c\u8272 */\n"
"    height:25px;\n"
"    /*background-color: rgba(0, 150, 255, 150);*/\n"
"    background-color: rgba(214, 214, 214,100);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"/*\u4e0b\u62c9\u6846\u7684\u6837\u5f0f*/\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    outline: 0px solid gray;  /*\u53d6\u6d88\u9009\u4e2d\u865a\u7ebf*/\n"
"    border: 1px solid rgb(31, 156, 255);\n"
"    color: rgb(66, 66, 66);\n"
"    background-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(0, 150, 255);\n"
"    border-radius:5px;\n"
"    height:35px;\n"
"    border:None;\n"
"}\n"
"/*\u9009\u4e2d\u6bcf\u4e00\u9879\u7684\u5b57\u4f53\u989c\u8272\u548c\u80cc\u666f\u989c\u8272*/\n"
"QComboBox::item:selected \n"
"{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 150, 255);\n"
"    border-radius:5px"
                        ";\n"
"}\n"
"/*\u53f3\u8fb9*/\n"
"QComboBox::drop-down{border: 2px solid rgba(0, 150, 255,0);}\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(:/img/picture/back_blue_down.png);\n"
"    width: 25px;\n"
"    height: 35px;\n"
"    right:6px;\n"
"    border-left: 2px solid rgb(192, 192, 192);\n"
"    border-right: 1px solid rgba(214, 214, 214,0);\n"
"}\n"
"QComboBox::down-arrow:on\n"
"{\n"
"    image: url(:/img/picture/back_blue_up.png);\n"
"    width: 25px;\n"
"    height: 35px;\n"
"    right:6px;\n"
"    border-left: 2px solid rgb(192, 192, 192);\n"
"    border-right: 1px solid rgba(214, 214, 214,0);\n"
"}\n"
"/*QComboBox::down-arrow::hover{}*\n"
"\n"
"/* QComboBox\u4e2d\u7684\u5782\u76f4\u6eda\u52a8\u6761 */\n"
"QComboBox QAbstractScrollArea QScrollBar:vertical {\n"
"    width: 10px;\n"
"    height: 8px;\n"
"    background-color: rgb(255, 64, 255);   /* \u7a7a\u767d\u533a\u57df\u7684\u80cc\u666f\u8272*/\n"
"    border-style:none;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical {\n"
""
                        "    border-radius: 5px;   /* \u5706\u89d2 */\n"
"    background: rgb(160,160,160);   /* \u5c0f\u65b9\u5757\u7684\u80cc\u666f\u8272\u6df1\u7070lightblue */\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical:hover {\n"
"    background: rgb(255, 255, 255);   /* \u8d8a\u8fc7\u5c0f\u65b9\u5757\u7684\u80cc\u666f\u8272*/\n"
"}")
        self.gridLayout = QGridLayout(self.page_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.line_3 = QFrame(self.page_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"color:rgb(214, 214, 214)")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setMidLineWidth(1)
        self.line_3.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line_3, 3, 0, 1, 2)

        self.label_10 = QLabel(self.page_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font-size: 17px;")
        self.label_10.setIndent(10)

        self.gridLayout.addWidget(self.label_10, 1, 0, 2, 1)

        self.comboBox_2 = QComboBox(self.page_3)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setStyleSheet(u"font-size: 14px;")

        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 2, 1)

        self.horizontalSpacer_4 = QSpacerItem(832, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 0, 1, 2)

        self.stackedWidget_2 = QStackedWidget(self.page_3)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.page_9.setStyleSheet(u"\n"
"QTreeWidget::item {\n"
"    height: 40px;\n"
"}")
        self.gridLayout_9 = QGridLayout(self.page_9)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.treeWidget = QTreeWidget(self.page_9)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setStyleSheet(u"font-size: 13px;")
        self.treeWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.treeWidget.setDragDropOverwriteMode(False)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setUniformRowHeights(True)
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setAllColumnsShowFocus(False)
        self.treeWidget.setWordWrap(False)
        self.treeWidget.setHeaderHidden(False)
        self.treeWidget.setColumnCount(2)

        self.gridLayout_9.addWidget(self.treeWidget, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.page_9)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.page_10.setStyleSheet(u"#lineEdit{height:25px;border-radius: 5px;border:2px solid rgb(169, 169, 169);color: rgb(0, 0, 0);}\n"
"#pushButton_2{height:25px;border-radius: 5px;width:70px;border:2px solid rgb(169, 169, 169);}")
        self.gridLayout_26 = QGridLayout(self.page_10)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.widget_2 = QWidget(self.page_10)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QWidget{border-radius: 23px;border:2px solid rgb(0, 150, 255);}\n"
"QLabel{border-style:none;}\n"
"QComboBox {\n"
"    border: 2px solid rgb(169, 169, 169); /* border: \u5bbd\u5ea6 \u7ebf\u7c7b\u578b \u989c\u8272 */\n"
"    height:25px;\n"
"    /*background-color: rgba(0, 150, 255, 150);*/\n"
"    background-color: rgba(214, 214, 214,100);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"/*\u4e0b\u62c9\u6846\u7684\u6837\u5f0f*/\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    outline: 0px solid gray;  /*\u53d6\u6d88\u9009\u4e2d\u865a\u7ebf*/\n"
"    border: 1px solid rgb(31, 156, 255);\n"
"    color: rgb(66, 66, 66);\n"
"    background-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(0, 150, 255);\n"
"    border-radius:5px;\n"
"    height:35px;\n"
"    border:None;\n"
"}\n"
"/*\u9009\u4e2d\u6bcf\u4e00\u9879\u7684\u5b57\u4f53\u989c\u8272\u548c\u80cc\u666f\u989c\u8272*/\n"
"QComboBox::item:selected \n"
"{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 150, 255);\n"
"    border-radiu"
                        "s:5px;\n"
"}\n"
"/*\u53f3\u8fb9*/\n"
"QComboBox::drop-down{border: 2px solid rgba(0, 150, 255,0);}\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(:/img/picture/back_blue_down.png);\n"
"    width: 25px;\n"
"    height: 35px;\n"
"    right:6px;\n"
"    border-left: 2px solid rgb(192, 192, 192);\n"
"    border-right: 1px solid rgba(214, 214, 214,0);\n"
"}\n"
"QComboBox::down-arrow:on\n"
"{\n"
"    image: url(:/img/picture/back_blue_up.png);\n"
"    width: 25px;\n"
"    height: 35px;\n"
"    right:6px;\n"
"    border-left: 2px solid rgb(192, 192, 192);\n"
"    border-right: 1px solid rgba(214, 214, 214,0);\n"
"}\n"
"/*QComboBox::down-arrow::hover{}*\n"
"\n"
"/* QComboBox\u4e2d\u7684\u5782\u76f4\u6eda\u52a8\u6761 */\n"
"QComboBox QAbstractScrollArea QScrollBar:vertical {\n"
"    width: 10px;\n"
"    height: 8px;\n"
"    background-color: rgb(255, 64, 255);   /* \u7a7a\u767d\u533a\u57df\u7684\u80cc\u666f\u8272*/\n"
"    border-style:none;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical {"
                        "\n"
"    border-radius: 5px;   /* \u5706\u89d2 */\n"
"    background: rgb(160,160,160);   /* \u5c0f\u65b9\u5757\u7684\u80cc\u666f\u8272\u6df1\u7070lightblue */\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical:hover {\n"
"    background: rgb(255, 255, 255);   /* \u8d8a\u8fc7\u5c0f\u65b9\u5757\u7684\u80cc\u666f\u8272*/\n"
"}")
        self.gridLayout_25 = QGridLayout(self.widget_2)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.horizontalSpacer_15 = QSpacerItem(199, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_15, 0, 2, 1, 2)

        self.pushButton_8 = QPushButton(self.widget_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"border-style:none;width:50px;height:50px;border-radius: 23px;background-color: rgba(235, 235, 235, 0);")
        icon7 = QIcon()
        icon7.addFile(u"../picture/quilt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon7)
        self.pushButton_8.setIconSize(QSize(50, 50))

        self.gridLayout_25.addWidget(self.pushButton_8, 3, 0, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_13, 2, 2, 1, 2)

        self.comboBox_5 = QComboBox(self.widget_2)
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setMinimumSize(QSize(120, 25))
        self.comboBox_5.setStyleSheet(u"font-size: 13px;")

        self.gridLayout_25.addWidget(self.comboBox_5, 2, 5, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_14, 1, 2, 1, 2)

        self.label_21 = QLabel(self.widget_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"font-size: 15px;")

        self.gridLayout_25.addWidget(self.label_21, 3, 1, 1, 1)

        self.label_20 = QLabel(self.widget_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"font-size: 15px;")

        self.gridLayout_25.addWidget(self.label_20, 2, 1, 1, 1)

        self.pushButton_13 = QPushButton(self.widget_2)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setStyleSheet(u"border-style:none;width:50px;height:50px;border-radius: 23px;background-color: rgba(235, 235, 235, 0);")
        icon8 = QIcon()
        icon8.addFile(u"../picture/loading.gif", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_13.setIcon(icon8)
        self.pushButton_13.setIconSize(QSize(40, 40))

        self.gridLayout_25.addWidget(self.pushButton_13, 1, 4, 1, 1)

        self.pushButton_14 = QPushButton(self.widget_2)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setStyleSheet(u"border-style:none;width:50px;height:50px;border-radius: 23px;background-color: rgba(235, 235, 235, 0);")
        self.pushButton_14.setIcon(icon8)
        self.pushButton_14.setIconSize(QSize(40, 40))

        self.gridLayout_25.addWidget(self.pushButton_14, 2, 4, 1, 1)

        self.pushButton_5 = QPushButton(self.widget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"border-style:none;width:50px;height:50px;border-radius: 23px;background-color: rgba(235, 235, 235, 0);")
        icon9 = QIcon()
        icon9.addFile(u"../picture/forge.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon9)
        self.pushButton_5.setIconSize(QSize(50, 50))

        self.gridLayout_25.addWidget(self.pushButton_5, 0, 0, 1, 1)

        self.label_11 = QLabel(self.widget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font-size: 15px;")

        self.gridLayout_25.addWidget(self.label_11, 0, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.widget_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"border-style:none;width:50px;height:50px;border-radius: 23px;background-color: rgba(235, 235, 235, 0);")
        icon10 = QIcon()
        icon10.addFile(u"../picture/optifine.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon10)
        self.pushButton_7.setIconSize(QSize(50, 50))

        self.gridLayout_25.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_15 = QPushButton(self.widget_2)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setStyleSheet(u"border-style:none;width:50px;height:50px;border-radius: 23px;background-color: rgba(235, 235, 235, 0);")
        self.pushButton_15.setIcon(icon8)
        self.pushButton_15.setIconSize(QSize(40, 40))

        self.gridLayout_25.addWidget(self.pushButton_15, 3, 4, 1, 1)

        self.comboBox_6 = QComboBox(self.widget_2)
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setMinimumSize(QSize(120, 25))
        self.comboBox_6.setStyleSheet(u"font-size: 13px;")

        self.gridLayout_25.addWidget(self.comboBox_6, 3, 5, 1, 1)

        self.label_19 = QLabel(self.widget_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"font-size: 15px;")

        self.gridLayout_25.addWidget(self.label_19, 1, 1, 1, 1)

        self.comboBox_3 = QComboBox(self.widget_2)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(210, 25))
        self.comboBox_3.setStyleSheet(u"font-size: 13px;")

        self.gridLayout_25.addWidget(self.comboBox_3, 0, 5, 1, 1)

        self.pushButton_6 = QPushButton(self.widget_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"border-style:none;width:50px;height:50px;border-radius: 23px;background-color: rgba(235, 235, 235, 0);")
        icon11 = QIcon()
        icon11.addFile(u"../picture/fabric.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon11)
        self.pushButton_6.setIconSize(QSize(50, 50))

        self.gridLayout_25.addWidget(self.pushButton_6, 1, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.widget_2)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setStyleSheet(u"border-style:none;width:50px;height:50px;border-radius: 23px;background-color: rgba(235, 235, 235, 0);")
        self.pushButton_12.setIcon(icon8)
        self.pushButton_12.setIconSize(QSize(40, 40))

        self.gridLayout_25.addWidget(self.pushButton_12, 0, 4, 1, 1)

        self.comboBox_4 = QComboBox(self.widget_2)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMinimumSize(QSize(120, 25))
        self.comboBox_4.setStyleSheet(u"font-size: 13px;")

        self.gridLayout_25.addWidget(self.comboBox_4, 1, 5, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_12, 3, 2, 1, 1)


        self.gridLayout_26.addWidget(self.widget_2, 0, 0, 1, 3)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_16, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.page_10)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"font-size: 13px;")
        self.lineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_26.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.page_10)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"font-size: 13px;")

        self.gridLayout_26.addWidget(self.pushButton_2, 1, 2, 1, 1)

        self.stackedWidget_2.addWidget(self.page_10)

        self.gridLayout.addWidget(self.stackedWidget_2, 4, 0, 1, 2)

        self.stackedWidget_mos_right.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_3 = QGridLayout(self.page_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 0, 5, 0)
        self.horizontalSpacer_5 = QSpacerItem(832, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 0, 0, 1, 1)

        self.label_12 = QLabel(self.page_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"font-size: 17px;")
        self.label_12.setIndent(10)

        self.gridLayout_3.addWidget(self.label_12, 1, 0, 1, 1)

        self.line_4 = QFrame(self.page_4)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"color:rgb(214, 214, 214)")
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setMidLineWidth(1)
        self.line_4.setFrameShape(QFrame.HLine)

        self.gridLayout_3.addWidget(self.line_4, 2, 0, 1, 1)

        self.widget_8 = QWidget(self.page_4)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"QWidget{border-radius:10px;border:2px solid rgb(0, 150, 255);}\n"
"QLabel{border-style:none;color:rgb(0, 150, 255);}")
        self.gridLayout_10 = QGridLayout(self.widget_8)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(12, -1, -1, -1)
        self.label_13 = QLabel(self.widget_8)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"font-size: 13px;")

        self.gridLayout_10.addWidget(self.label_13, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_8, 3, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(832, 393, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_7, 4, 0, 1, 1)

        self.stackedWidget_mos_right.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setStyleSheet(u"QLabel{border-style:none;color:rgb(33, 33, 33);background-color: rgba(255, 255, 255, 0);}\n"
"QComboBox {\n"
"    border: 2px solid rgb(169, 169, 169); /* border: \u5bbd\u5ea6 \u7ebf\u7c7b\u578b \u989c\u8272 */\n"
"    height:25px;\n"
"    /*background-color: rgba(0, 150, 255, 150);*/\n"
"    background-color: rgba(214, 214, 214,100);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"/*\u4e0b\u62c9\u6846\u7684\u6837\u5f0f*/\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    outline: 0px solid gray;  /*\u53d6\u6d88\u9009\u4e2d\u865a\u7ebf*/\n"
"    border: 1px solid rgb(31, 156, 255);\n"
"    color: rgb(66, 66, 66);\n"
"    background-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(0, 150, 255);\n"
"    border-radius:5px;\n"
"    height:35px;\n"
"    border:None;\n"
"}\n"
"/*\u9009\u4e2d\u6bcf\u4e00\u9879\u7684\u5b57\u4f53\u989c\u8272\u548c\u80cc\u666f\u989c\u8272*/\n"
"QComboBox::item:selected \n"
"{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 150, 255);\n"
"    border-radius:5px"
                        ";\n"
"}\n"
"/*\u53f3\u8fb9*/\n"
"QComboBox::drop-down{border: 2px solid rgba(0, 150, 255,0);}\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(:/img/picture/back_blue_down.png);\n"
"    width: 25px;\n"
"    height: 35px;\n"
"    right:6px;\n"
"    border-left: 2px solid rgb(192, 192, 192);\n"
"    border-right: 1px solid rgba(214, 214, 214,0);\n"
"}\n"
"QComboBox::down-arrow:on\n"
"{\n"
"    image: url(:/img/picture/back_blue_up.png);\n"
"    width: 25px;\n"
"    height: 35px;\n"
"    right:6px;\n"
"    border-left: 2px solid rgb(192, 192, 192);\n"
"    border-right: 1px solid rgba(214, 214, 214,0);\n"
"}\n"
"/*QComboBox::down-arrow::hover{}*\n"
"\n"
"/* QComboBox\u4e2d\u7684\u5782\u76f4\u6eda\u52a8\u6761 */\n"
"QComboBox QAbstractScrollArea QScrollBar:vertical {\n"
"    width: 10px;\n"
"    height: 8px;\n"
"    background-color: rgb(255, 64, 255);   /* \u7a7a\u767d\u533a\u57df\u7684\u80cc\u666f\u8272*/\n"
"    border-style:none;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical {\n"
""
                        "    border-radius: 5px;   /* \u5706\u89d2 */\n"
"    background: rgb(160,160,160);   /* \u5c0f\u65b9\u5757\u7684\u80cc\u666f\u8272\u6df1\u7070lightblue */\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical:hover {\n"
"    background: rgb(255, 255, 255);   /* \u8d8a\u8fc7\u5c0f\u65b9\u5757\u7684\u80cc\u666f\u8272*/\n"
"}")
        self.gridLayout_15 = QGridLayout(self.page_5)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(5, 0, 5, 0)
        self.horizontalSpacer_6 = QSpacerItem(832, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_6, 0, 0, 1, 2)

        self.line_5 = QFrame(self.page_5)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"color:rgb(214, 214, 214)")
        self.line_5.setFrameShadow(QFrame.Plain)
        self.line_5.setMidLineWidth(1)
        self.line_5.setFrameShape(QFrame.HLine)

        self.gridLayout_15.addWidget(self.line_5, 2, 0, 1, 2)

        self.label_15 = QLabel(self.page_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"font-size: 17px;")
        self.label_15.setIndent(10)

        self.gridLayout_15.addWidget(self.label_15, 1, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.page_5)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.gridLayout_11 = QGridLayout(self.page)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"border-style:none;background-color: rgba(255, 255, 255, 0);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 822, 456))
        self.scrollAreaWidgetContents_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.gridLayout_23 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.widget = QWidget(self.scrollAreaWidgetContents_2)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget{background-color: rgba(255, 255, 255, 0);border-radius:15px;border: 2px solid rgb(0, 150, 255);}\n"
"QLabel{border-style:none;}\n"
"#label_6{text-decoration: underline;}\n"
"QComboBox {\n"
"	border: 2px solid rgb(192, 192, 192); /* border: \u5bbd\u5ea6 \u7ebf\u7c7b\u578b \u989c\u8272 */\n"
"	height:27px;\n"
"	background-color: rgba(235, 235, 235, 128);\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"/*\u4e0b\u62c9\u6846\u7684\u6837\u5f0f*/\n"
"QComboBox QAbstractItemView \n"
"{\n"
"    outline: 0px solid gray;  /*\u53d6\u6d88\u9009\u4e2d\u865a\u7ebf*/\n"
"    border: 1px solid rgb(31, 156, 255);\n"
"    color: rgb(66, 66, 66);\n"
"    background-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(0, 150, 255);\n"
"	border-radius:5px;\n"
"	height:150px;\n"
"}\n"
" /*\u9009\u4e2d\u6bcf\u4e00\u9879\u9ad8\u5ea6*/\n"
"QComboBox QAbstractItemView::item\n"
"{ \n"
"	height: 25px;\n"
"	border-radius:5px;\n"
" }\n"
"/*\u9009\u4e2d\u6bcf\u4e00\u9879\u7684\u5b57\u4f53\u989c\u8272\u548c\u80cc\u666f\u989c\u8272"
                        "*/\n"
"QComboBox QAbstractItemView::item:selected \n"
"{\n"
"    color: rgb(31,163,246);\n"
"	background-color: rgb(0, 150, 255);\n"
"	border-radius:5px;\n"
"}\n"
"/*QComboBox::down-arrow\n"
"\u662f \u53f3\u9762\u90a3\u4e2a \n"
"*/\n"
"\n"
"\n"
"\n"
"/* QComboBox\u4e2d\u7684\u5782\u76f4\u6eda\u52a8\u6761 */\n"
"QComboBox QAbstractScrollArea QScrollBar:vertical {\n"
"	width: 10px;\n"
"	height: 8px;\n"
"	background-color: #d0d2d4;   /* \u7a7a\u767d\u533a\u57df\u7684\u80cc\u666f\u8272*/\n"
"	border-style:none;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical {\n"
"    border-radius: 5px;   /* \u5706\u89d2 */\n"
"    background: rgb(160,160,160);   /* \u5c0f\u65b9\u5757\u7684\u80cc\u666f\u8272\u6df1\u7070lightblue */\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical:hover {\n"
"    background: rgb(255, 255, 255);   /* \u8d8a\u8fc7\u5c0f\u65b9\u5757\u7684\u80cc\u666f\u8272*/\n"
"}\n"
"\n"
"QPushButton{height:30px;background-color: rgba(255, 255, 255,0);border-radius:7p"
                        "x;border:2px solid rgb(255, 59, 0);}\n"
"QPushButton::hover{color: rgb(255, 59, 0)}\n"
"QPushButton::pressed{background-color: rgba(255, 0, 0, 100);}")
        self.gridLayout_24 = QGridLayout(self.widget)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.pushButton_11 = QPushButton(self.widget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy4)
        self.pushButton_11.setMinimumSize(QSize(0, 0))
        self.pushButton_11.setSizeIncrement(QSize(0, 0))
        self.pushButton_11.setBaseSize(QSize(0, 0))
        self.pushButton_11.setStyleSheet(u"font-size: 14px;")
        self.pushButton_11.setIconSize(QSize(16, 16))

        self.gridLayout_24.addWidget(self.pushButton_11, 1, 3, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font-size: 13px;")
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.gridLayout_24.addWidget(self.label_4, 0, 0, 2, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        font3 = QFont()
        font3.setItalic(True)
        font3.setUnderline(True)
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"font-size: 14px;")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_24.addWidget(self.label_6, 1, 1, 1, 2)

        self.fontComboBox = QFontComboBox(self.widget)
        self.fontComboBox.setObjectName(u"fontComboBox")
        self.fontComboBox.setStyleSheet(u"font-size: 14px;")
        self.fontComboBox.setEditable(True)
        self.fontComboBox.setCurrentIndex(0)
        self.fontComboBox.setMaxVisibleItems(20)
        self.fontComboBox.setDuplicatesEnabled(False)

        self.gridLayout_24.addWidget(self.fontComboBox, 0, 1, 1, 3)


        self.gridLayout_23.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_4 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"QWidget{background-color: rgba(255, 255, 255, 0);border-radius:15px;border: 2px solid rgb(0, 150, 255);}\n"
"QLabel{border-style:none;}\n"
"QComboBox {\n"
"	border: 2px solid rgb(192, 192, 192); /* border: \u5bbd\u5ea6 \u7ebf\u7c7b\u578b \u989c\u8272 */\n"
"	height:27px;\n"
"	background-color: rgba(235, 235, 235, 128);\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"/*\u4e0b\u62c9\u6846\u7684\u6837\u5f0f*/\n"
"QComboBox QAbstractItemView \n"
"{\n"
"    outline: 0px solid gray;  /*\u53d6\u6d88\u9009\u4e2d\u865a\u7ebf*/\n"
"    border: 1px solid rgb(31, 156, 255);\n"
"    color: rgb(66, 66, 66);\n"
"    background-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(0, 150, 255);\n"
"	border-radius:5px;\n"
"	height:150px;\n"
"}\n"
" /*\u9009\u4e2d\u6bcf\u4e00\u9879\u9ad8\u5ea6*/\n"
"QComboBox QAbstractItemView::item\n"
"{ \n"
"	height: 25px;\n"
"	border-radius:5px;\n"
" }\n"
"/*\u9009\u4e2d\u6bcf\u4e00\u9879\u7684\u5b57\u4f53\u989c\u8272\u548c\u80cc\u666f\u989c\u8272*/\n"
"QComboBox QAbstractItemView::item"
                        ":selected \n"
"{\n"
"    color: rgb(31,163,246);\n"
"	background-color: rgb(0, 150, 255);\n"
"	border-radius:5px;\n"
"}\n"
"/*QComboBox::down-arrow\n"
"\u662f \u53f3\u9762\u90a3\u4e2a \n"
"*/\n"
"\n"
"\n"
"\n"
"/* QComboBox\u4e2d\u7684\u5782\u76f4\u6eda\u52a8\u6761 */\n"
"QComboBox QAbstractScrollArea QScrollBar:vertical {\n"
"	width: 10px;\n"
"	height: 8px;\n"
"	background-color: #d0d2d4;   /* \u7a7a\u767d\u533a\u57df\u7684\u80cc\u666f\u8272*/\n"
"	border-style:none;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical {\n"
"    border-radius: 5px;   /* \u5706\u89d2 */\n"
"    background: rgb(160,160,160);   /* \u5c0f\u65b9\u5757\u7684\u80cc\u666f\u8272\u6df1\u7070lightblue */\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical:hover {\n"
"    background: rgb(255, 255, 255);   /* \u8d8a\u8fc7\u5c0f\u65b9\u5757\u7684\u80cc\u666f\u8272*/\n"
"}\n"
"\n"
"#pushButton_20{height:30px;background-color: rgba(255, 255, 255,0);border-radius:7px;border:2px solid rgb(255, 59, 0);}\n"
""
                        "#pushButton_20::hover{color: rgb(255, 59, 0)}\n"
"#pushButton_20::pressed{background-color: rgba(255, 0, 0, 100);}\n"
"\n"
"#pushButton_19{height:30px;background-color: rgba(255, 255, 255,0);border-radius:7px;border:2px solid rgb(0, 250, 146);color: rgb(33, 33, 33);}\n"
"#pushButton_19::hover{color: rgb(0, 250, 146);}\n"
"#pushButton_19::pressed{background-color: rgb(128, 255, 202);color: rgb(255, 255, 255);}\n"
"\n"
"/*\u7981\u7528*/\n"
"#pushButton_20:disabled{border-radius: 7px;border:2px solid rgb(214, 214, 214);}\n"
"\n"
"QRadioButton{border-style:none;}")
        self.gridLayout_29 = QGridLayout(self.widget_4)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.pushButton_19 = QPushButton(self.widget_4)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setStyleSheet(u"font-size: 14px;")

        self.gridLayout_29.addWidget(self.pushButton_19, 1, 1, 1, 2)

        self.label_5 = QLabel(self.widget_4)
        self.label_5.setObjectName(u"label_5")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy5)
        self.label_5.setStyleSheet(u"font-size: 13px;")
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.gridLayout_29.addWidget(self.label_5, 1, 0, 2, 1)

        self.radioButton = QRadioButton(self.widget_4)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setLayoutDirection(Qt.LeftToRight)
        self.radioButton.setStyleSheet(u"font-size: 13px;")
        self.radioButton.setChecked(True)
        self.radioButton.setAutoRepeat(False)

        self.gridLayout_29.addWidget(self.radioButton, 2, 1, 1, 1)

        self.pushButton_20 = QPushButton(self.widget_4)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setEnabled(False)
        self.pushButton_20.setStyleSheet(u"font-size: 14px;")

        self.gridLayout_29.addWidget(self.pushButton_20, 2, 2, 1, 1)


        self.gridLayout_23.addWidget(self.widget_4, 1, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_23.addItem(self.verticalSpacer_8, 2, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_11.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.gridLayout_32 = QGridLayout(self.page_7)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setHorizontalSpacing(-1)
        self.gridLayout_32.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.page_7)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"border-style:none;background-color: rgba(255, 255, 255, 0);")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 245, 829))
        self.scrollAreaWidgetContents_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.gridLayout_30 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.widget_15 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setStyleSheet(u"QWidget{background-color: rgba(255, 255, 255, 0);border-radius:15px;border: 2px solid rgb(0, 150, 255);}\n"
"QLabel{border-style:none;}\n"
"#label_6{text-decoration: underline;}\n"
"QComboBox {\n"
"	border: 2px solid rgb(192, 192, 192); /* border: \u5bbd\u5ea6 \u7ebf\u7c7b\u578b \u989c\u8272 */\n"
"	height:27px;\n"
"	background-color: rgba(235, 235, 235, 128);\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"/*\u4e0b\u62c9\u6846\u7684\u6837\u5f0f*/\n"
"QComboBox QAbstractItemView \n"
"{\n"
"    outline: 0px solid gray;  /*\u53d6\u6d88\u9009\u4e2d\u865a\u7ebf*/\n"
"    border: 1px solid rgb(31, 156, 255);\n"
"    color: rgb(66, 66, 66);\n"
"    background-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(0, 150, 255);\n"
"	border-radius:5px;\n"
"	height:150px;\n"
"}\n"
" /*\u9009\u4e2d\u6bcf\u4e00\u9879\u9ad8\u5ea6*/\n"
"QComboBox QAbstractItemView::item\n"
"{ \n"
"	height: 25px;\n"
"	border-radius:5px;\n"
" }\n"
"/*\u9009\u4e2d\u6bcf\u4e00\u9879\u7684\u5b57\u4f53\u989c\u8272\u548c\u80cc\u666f\u989c\u8272"
                        "*/\n"
"QComboBox QAbstractItemView::item:selected \n"
"{\n"
"    color: rgb(31,163,246);\n"
"	background-color: rgb(0, 150, 255);\n"
"	border-radius:5px;\n"
"}\n"
"/*QComboBox::down-arrow\n"
"\u662f \u53f3\u9762\u90a3\u4e2a \n"
"*/\n"
"\n"
"\n"
"\n"
"/* QComboBox\u4e2d\u7684\u5782\u76f4\u6eda\u52a8\u6761 */\n"
"QComboBox QAbstractScrollArea QScrollBar:vertical {\n"
"	width: 10px;\n"
"	height: 8px;\n"
"	background-color: #d0d2d4;   /* \u7a7a\u767d\u533a\u57df\u7684\u80cc\u666f\u8272*/\n"
"	border-style:none;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical {\n"
"    border-radius: 5px;   /* \u5706\u89d2 */\n"
"    background: rgb(160,160,160);   /* \u5c0f\u65b9\u5757\u7684\u80cc\u666f\u8272\u6df1\u7070lightblue */\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical:hover {\n"
"    background: rgb(255, 255, 255);   /* \u8d8a\u8fc7\u5c0f\u65b9\u5757\u7684\u80cc\u666f\u8272*/\n"
"}\n"
"\n"
"QPushButton{height:30px;background-color: rgba(255, 255, 255,0);border-radius:7p"
                        "x;border:2px solid rgb(255, 59, 0);}\n"
"QPushButton::hover{color: rgb(255, 59, 0)}\n"
"QPushButton::pressed{background-color: rgba(255, 0, 0, 100);}")
        self.gridLayout_31 = QGridLayout(self.widget_15)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.label_14 = QLabel(self.widget_15)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"font-size: 13px;")
        self.label_14.setScaledContents(False)
        self.label_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_14.setWordWrap(True)
        self.label_14.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.gridLayout_31.addWidget(self.label_14, 0, 0, 3, 1)

        self.comboBox_7 = QComboBox(self.widget_15)
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.gridLayout_31.addWidget(self.comboBox_7, 0, 2, 2, 1)

        self.pushButton_21 = QPushButton(self.widget_15)
        self.pushButton_21.setObjectName(u"pushButton_21")
        sizePolicy4.setHeightForWidth(self.pushButton_21.sizePolicy().hasHeightForWidth())
        self.pushButton_21.setSizePolicy(sizePolicy4)
        self.pushButton_21.setMinimumSize(QSize(0, 0))
        self.pushButton_21.setSizeIncrement(QSize(0, 0))
        self.pushButton_21.setBaseSize(QSize(0, 0))
        self.pushButton_21.setFont(font)
        self.pushButton_21.setStyleSheet(u"font-size: 14px;")
        self.pushButton_21.setIconSize(QSize(16, 16))

        self.gridLayout_31.addWidget(self.pushButton_21, 2, 2, 1, 1)


        self.gridLayout_30.addWidget(self.widget_15, 0, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 282, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_30.addItem(self.verticalSpacer_9, 1, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_32.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_7)

        self.gridLayout_15.addWidget(self.stackedWidget, 3, 0, 1, 2)

        self.comboBox = QComboBox(self.page_5)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"font-size: 14px;")

        self.gridLayout_15.addWidget(self.comboBox, 1, 1, 1, 1)

        self.stackedWidget_mos_right.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.page_6.setStyleSheet(u"QLabel{border-style:none;color:rgb(33, 33, 33);background-color: rgba(255, 255, 255, 0);}")
        self.gridLayout_14 = QGridLayout(self.page_6)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.widget_10 = QWidget(self.page_6)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.gridLayout_19 = QGridLayout(self.widget_10)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.widget_13 = QWidget(self.widget_10)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setStyleSheet(u"QWidget{border-radius:15px;border:2px solid rgba(0, 150, 255, 230);}\n"
"QLabel{border-style:none;}")
        self.verticalLayout_3 = QVBoxLayout(self.widget_13)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.widget_13)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size: 13px;")

        self.verticalLayout_3.addWidget(self.label)

        self.widget_11 = QWidget(self.widget_13)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setStyleSheet(u"border-style:none;background-color: rgb(235, 235, 235);border-radius:15px;")
        self.gridLayout_12 = QGridLayout(self.widget_11)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setHorizontalSpacing(7)
        self.pushButton = QPushButton(self.widget_11)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"border-style:none;")
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(40, 40))

        self.gridLayout_12.addWidget(self.pushButton, 1, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(34, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_8, 1, 2, 1, 1)

        self.label_16 = QLabel(self.widget_11)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"font-size: 13px;")

        self.gridLayout_12.addWidget(self.label_16, 1, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.widget_13)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setStyleSheet(u"QWidget{border-style:none;background-color: rgb(235, 235, 235);border-radius:15px;}\n"
"#pushButton_3{width:120px;height:30px;background-color: rgba(255, 255, 255,0);border-radius:7px;border:2px solid rgb(0, 150, 255);}\n"
"#pushButton_3::hover{background-color: rgb(255, 255, 255);}\n"
"#pushButton_3::pressed{background-color: rgba(0, 150, 255, 51);}")
        self.gridLayout_17 = QGridLayout(self.widget_12)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setHorizontalSpacing(7)
        self.label_18 = QLabel(self.widget_12)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"font-size: 13px;")

        self.gridLayout_17.addWidget(self.label_18, 0, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(34, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_9, 0, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.widget_12)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"border-style:none;")
        icon12 = QIcon()
        icon12.addFile(u"../picture/david.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon12)
        self.pushButton_4.setIconSize(QSize(40, 40))

        self.gridLayout_17.addWidget(self.pushButton_4, 0, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.widget_12)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"font-size: 13px;")

        self.gridLayout_17.addWidget(self.pushButton_3, 0, 3, 1, 1)


        self.verticalLayout_3.addWidget(self.widget_12)

        self.widget_14 = QWidget(self.widget_13)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setStyleSheet(u"QWidget{border-style:none;background-color: rgb(235, 235, 235);border-radius:15px;}\n"
"#pushButton_10{width:120px;height:30px;background-color: rgba(255, 255, 255,0);border-radius:7px;border:2px solid rgb(0, 150, 255);}\n"
"#pushButton_10::hover{background-color: rgb(255, 255, 255);}\n"
"#pushButton_10::pressed{background-color: rgba(0, 150, 255, 51);}")
        self.gridLayout_18 = QGridLayout(self.widget_14)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setHorizontalSpacing(2)
        self.gridLayout_18.setVerticalSpacing(6)
        self.horizontalSpacer_10 = QSpacerItem(34, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_10, 0, 3, 1, 1)

        self.label_25 = QLabel(self.widget_14)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_18.addWidget(self.label_25, 0, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.widget_14)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"border-style:none;")
        icon13 = QIcon()
        icon13.addFile(u"../picture/heimnad.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon13)
        self.pushButton_9.setIconSize(QSize(40, 40))

        self.gridLayout_18.addWidget(self.pushButton_9, 0, 0, 1, 1)

        self.label_22 = QLabel(self.widget_14)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"font-size: 13px;")

        self.gridLayout_18.addWidget(self.label_22, 0, 2, 1, 1)

        self.pushButton_10 = QPushButton(self.widget_14)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"font-size: 13px;")

        self.gridLayout_18.addWidget(self.pushButton_10, 0, 4, 1, 1)


        self.verticalLayout_3.addWidget(self.widget_14)


        self.gridLayout_19.addWidget(self.widget_13, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(796, 368, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_19.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.gridLayout_14.addWidget(self.widget_10, 3, 0, 1, 2)

        self.line_6 = QFrame(self.page_6)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setStyleSheet(u"color:rgb(214, 214, 214)")
        self.line_6.setFrameShadow(QFrame.Plain)
        self.line_6.setMidLineWidth(1)
        self.line_6.setFrameShape(QFrame.HLine)

        self.gridLayout_14.addWidget(self.line_6, 2, 0, 1, 2)

        self.horizontalSpacer_7 = QSpacerItem(832, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_7, 0, 0, 1, 2)

        self.label_17 = QLabel(self.page_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)
        self.label_17.setStyleSheet(u"font-size: 17px;")
        self.label_17.setIndent(10)

        self.gridLayout_14.addWidget(self.label_17, 1, 0, 1, 2)

        self.stackedWidget_mos_right.addWidget(self.page_6)

        self.gridLayout_13.addWidget(self.stackedWidget_mos_right, 0, 1, 1, 1)

        self.widget_mos_left = QWidget(self.centralwidget)
        self.widget_mos_left.setObjectName(u"widget_mos_left")
        sizePolicy1.setHeightForWidth(self.widget_mos_left.sizePolicy().hasHeightForWidth())
        self.widget_mos_left.setSizePolicy(sizePolicy1)
        font4 = QFont()
        font4.setPointSize(15)
        self.widget_mos_left.setFont(font4)
        self.widget_mos_left.setAutoFillBackground(False)
        self.widget_mos_left.setStyleSheet(u"QWidget\n"
"{\n"
"	background-color: rgb(231, 230, 228);\n"
"}\n"
"#widget_mos_left_top\n"
"{\n"
"	background-color: rgb(231, 230, 228);\n"
"	border-style:none;\n"
"	border-radius:15px;\n"
"}\n"
"#widget_mos_left_top::hover\n"
"{\n"
"	background-color: rgba(0, 150, 255, 51);\n"
"}\n"
"#widget_mos_left_top::pressed\n"
"{\n"
"	background-color: rgba(0, 150, 255, 51);\n"
"}\n"
"QPushButton\n"
"{\n"
"	color: blue;\n"
"	height:35px;\n"
"	color: rgb(0, 150, 255);\n"
"	background-position: left;\n"
"	text-align: left;\n"
"	padding-right:15px;\n"
"	padding-left:5px;\n"
"	border-style:none;\n"
"	border-radius:8px;\n"
"	border:2px solid rgba(229, 228, 226,0);\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	background-color: rgb(192, 192, 192);\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"	border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"#pushButton_home\n"
"{\n"
"	color: blue;\n"
"	height:35px;\n"
"	color: rgb(0, 150, 255);\n"
"	background-position: left;\n"
"	text-align: left;\n"
"	padding-right:15px;\n"
"	padding-left:5px;\n"
"	"
                        "border-style:none;\n"
"	border-radius:8px;\n"
"	border:2px solid rgba(229, 228, 226,0);background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_home::hover\n"
"{\n"
"	background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_home::pressed\n"
"{\n"
"	border:2px solid rgb(0, 150, 255);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.widget_mos_left)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, -1, 9, -1)
        self.widget_mos_left_top = QWidget(self.widget_mos_left)
        self.widget_mos_left_top.setObjectName(u"widget_mos_left_top")
        self.widget_mos_left_top.setStyleSheet(u"#label_mos_left_top_user{background-color: rgba(255, 255, 255, 0);}\n"
"#label_mos_left_top_add{background-color: rgba(255, 255, 255, 0);}\n"
"QWidget\n"
"{\n"
"	background-color: rgb(231, 230, 228);\n"
"	border-style:none;\n"
"	border-radius:15px;\n"
"}\n"
"QWidget::hover\n"
"{\n"
"	background-color: rgba(0, 150, 255, 51);\n"
"}\n"
"QWidget::pressed\n"
"{\n"
"	background-color: rgba(0, 150, 255, 51);\n"
"}\n"
"QPushButton\n"
"{\n"
"	background-position: left;\n"
"	text-align: left;\n"
"	padding-right:0px;\n"
"	padding-left:0px;\n"
"}\n"
"")
        self.gridLayout_4 = QGridLayout(self.widget_mos_left_top)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_mos_left_top_add = QLabel(self.widget_mos_left_top)
        self.label_mos_left_top_add.setObjectName(u"label_mos_left_top_add")
        self.label_mos_left_top_add.setStyleSheet(u"font-size: 13px;")

        self.gridLayout_4.addWidget(self.label_mos_left_top_add, 1, 1, 1, 1)

        self.pushButton_mos_left_top = QPushButton(self.widget_mos_left_top)
        self.pushButton_mos_left_top.setObjectName(u"pushButton_mos_left_top")
        self.pushButton_mos_left_top.setStyleSheet(u"width:50px;height:50px;border-radius: 23px;background-color: rgba(255, 255, 255, 0);")
        self.pushButton_mos_left_top.setIcon(icon)
        self.pushButton_mos_left_top.setIconSize(QSize(50, 50))

        self.gridLayout_4.addWidget(self.pushButton_mos_left_top, 0, 0, 2, 1)

        self.label_mos_left_top_user = QLabel(self.widget_mos_left_top)
        self.label_mos_left_top_user.setObjectName(u"label_mos_left_top_user")
        self.label_mos_left_top_user.setStyleSheet(u"font-size: 13px;")

        self.gridLayout_4.addWidget(self.label_mos_left_top_user, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.widget_mos_left_top)

        self.line_2 = QFrame(self.widget_mos_left)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.pushButton_home = QPushButton(self.widget_mos_left)
        self.pushButton_home.setObjectName(u"pushButton_home")
        self.pushButton_home.setMinimumSize(QSize(150, 0))
        self.pushButton_home.setFocusPolicy(Qt.TabFocus)
        self.pushButton_home.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_home.setStyleSheet(u"font-size: 15px;")
        icon14 = QIcon()
        icon14.addFile(u"../picture/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_home.setIcon(icon14)
        self.pushButton_home.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.pushButton_home)

        self.pushButton_lianji = QPushButton(self.widget_mos_left)
        self.pushButton_lianji.setObjectName(u"pushButton_lianji")
        self.pushButton_lianji.setMinimumSize(QSize(150, 0))
        self.pushButton_lianji.setStyleSheet(u"font-size: 15px;")
        icon15 = QIcon()
        icon15.addFile(u"../picture/online.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_lianji.setIcon(icon15)
        self.pushButton_lianji.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.pushButton_lianji)

        self.pushButton_xiazai = QPushButton(self.widget_mos_left)
        self.pushButton_xiazai.setObjectName(u"pushButton_xiazai")
        self.pushButton_xiazai.setMinimumSize(QSize(150, 0))
        self.pushButton_xiazai.setStyleSheet(u"font-size: 15px;")
        icon16 = QIcon()
        icon16.addFile(u"../picture/download.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_xiazai.setIcon(icon16)
        self.pushButton_xiazai.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.pushButton_xiazai)

        self.pushButton_music = QPushButton(self.widget_mos_left)
        self.pushButton_music.setObjectName(u"pushButton_music")
        self.pushButton_music.setMinimumSize(QSize(150, 0))
        self.pushButton_music.setStyleSheet(u"font-size: 15px;")
        icon17 = QIcon()
        icon17.addFile(u"../picture/music.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_music.setIcon(icon17)
        self.pushButton_music.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.pushButton_music)

        self.pushButton_shezhi = QPushButton(self.widget_mos_left)
        self.pushButton_shezhi.setObjectName(u"pushButton_shezhi")
        self.pushButton_shezhi.setMinimumSize(QSize(150, 0))
        self.pushButton_shezhi.setStyleSheet(u"font-size: 15px;")
        self.pushButton_shezhi.setIcon(icon2)
        self.pushButton_shezhi.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.pushButton_shezhi)

        self.pushButton_about = QPushButton(self.widget_mos_left)
        self.pushButton_about.setObjectName(u"pushButton_about")
        self.pushButton_about.setMinimumSize(QSize(150, 0))
        self.pushButton_about.setStyleSheet(u"font-size: 15px;")
        icon18 = QIcon()
        icon18.addFile(u"../picture/about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_about.setIcon(icon18)
        self.pushButton_about.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.pushButton_about)

        self.verticalSpacer_11 = QSpacerItem(20, 184, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_11)

        self.label_mosll = QLabel(self.widget_mos_left)
        self.label_mosll.setObjectName(u"label_mosll")
        self.label_mosll.setStyleSheet(u"color: rgb(0, 150, 255);font-size: 17px;font: 75 17pt \"Yuanti SC\";background-color: rgba(240, 239, 238,0);")
        self.label_mosll.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_mosll)


        self.gridLayout_13.addWidget(self.widget_mos_left, 0, 0, 1, 1)

        MOS.setCentralWidget(self.centralwidget)

        self.retranslateUi(MOS)

        self.stackedWidget_mos_right.setCurrentIndex(0)
        self.stackedWidget_gonggao.setCurrentIndex(1)
        self.comboBox_gonggao_right.setCurrentIndex(-1)
        self.stackedWidget_mos_right_2.setCurrentIndex(0)
        self.stackedWidget_5.setCurrentIndex(0)
        self.pushButton_41.setDefault(False)
        self.pushButton_18.setDefault(False)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MOS)
    # setupUi

    def retranslateUi(self, MOS):
        MOS.setWindowTitle(QCoreApplication.translate("MOS", u"MOS ll \u542f\u52a8\u5668", None))
        self.label_2.setText(QCoreApplication.translate("MOS", u"\u6b63\u5728\u52a0\u8f7d\n"
"\n"
"\u5f53\u524d\u6b65\u9aa4\uff1a\u4e0b\u8f7d\u516c\u544a\u2026\u2026\u8bf7\u7a0d\u540e\n"
"", None))
        self.label_gonggao_left_txt.setText(QCoreApplication.translate("MOS", u"<html><head/><body><p>\u5b98\u65b9\u516c\u544a <span style=\" color:#55f976;\">\u2022\u6b63\u5728\u52a0\u8f7d\u4e2d</span></p></body></html>", None))
        self.label__gonggao_right_txt.setText(QCoreApplication.translate("MOS", u"<html><head/><body><p>\u542f\u52a8\u6e38\u620f <span style=\" color:#0096ff;\">\u2022\u7b49\u5f85\u542f\u52a8</span></p></body></html>", None))
        self.label_3.setText("")
        self.label_7.setText(QCoreApplication.translate("MOS", u"\u542f\u52a8\u541b\uff1a\u5f85\u547d\u4e2d\u2026\u2026", None))
        self.pushButton_16.setText(QCoreApplication.translate("MOS", u"\u7248\u672c\u5217\u8868", None))
        self.pushButton_17.setText(QCoreApplication.translate("MOS", u"\u7248\u672c\u8bbe\u7f6e", None))
        self.pushButton__gonggao_start.setText(QCoreApplication.translate("MOS", u"\u542f\u52a8\u6e38\u620f", None))
        self.label_24.setText(QCoreApplication.translate("MOS", u"\u7248\u672c\u5217\u8868", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MOS", u"\u9ed8\u8ba4\u76ee\u5f55", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.pushButton_38.setText(QCoreApplication.translate("MOS", u"\u7248\u672c\u8bbe\u7f6e", None))
        self.pushButton_36.setText(QCoreApplication.translate("MOS", u"\u6dfb\u52a0\u7248\u672c\u6587\u4ef6\u5939", None))
        self.pushButton_37.setText(QCoreApplication.translate("MOS", u"\u5b89\u88c5\u6574\u5408\u5305", None))
        self.label_44.setText(QCoreApplication.translate("MOS", u"\u76ee\u5f55\u540d\u79f0\uff1a", None))
        self.lineEdit_4.setInputMask("")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MOS", u"\u8bf7\u8f93\u5165\u76ee\u5f55\u540d", None))
        self.label_47.setText(QCoreApplication.translate("MOS", u"* \u76ee\u5f55\u540d\u76f8\u5f53\u4e8e\u7ed9 \u6e38\u620f\u76ee\u5f55\u8d77\u4e86\u4e2a\u540d\u5b57", None))
        self.label_43.setText(QCoreApplication.translate("MOS", u"\u6dfb\u52a0\u6e38\u620f\u76ee\u5f55", None))
        self.label_45.setText(QCoreApplication.translate("MOS", u"\u9009\u62e9\u76ee\u5f55\uff1a", None))
        self.label_48.setText(QCoreApplication.translate("MOS", u"\u9009\u62e9\u7684\u8def\u5f84\uff1a", None))
        self.pushButton_42.setText(QCoreApplication.translate("MOS", u"\u9009\u62e9\u2026\u2026", None))
        self.label_46.setText(QCoreApplication.translate("MOS", u"\u8bf7\u5148\u9009\u62e9\u4e00\u4e2a\u76ee\u5f55", None))
        self.pushButton_41.setText("")
        self.pushButton_18.setText(QCoreApplication.translate("MOS", u"\u786e\u5b9a\u6dfb\u52a0", None))
        self.pushButton_40.setText(QCoreApplication.translate("MOS", u"\u5220\u9664\u6e38\u620f\u6587\u4ef6\u5939", None))
        self.pushButton_39.setText(QCoreApplication.translate("MOS", u"\u91cd\u547d\u540d\u7248\u672c\u6587\u4ef6\u5939", None))
        self.label_26.setText("")
        self.pushButton_35.setText("")
        self.label_9.setText(QCoreApplication.translate("MOS", u"\u8054\u673a\u6a21\u5757", None))
        self.label_8.setText(QCoreApplication.translate("MOS", u"\u8054\u673a\u6a21\u5757\u6b63\u5728\u5f00\u53d1\u4e2d\u2026\u2026\n"
"\u4e0d\u8981\u7740\u6025\u5566 \u4f60\u7684\u8d5e\u52a9\u5c31\u662f\u6211\u66f4\u65b0\u7684\u52a8\u529b\uff01\u563b\u563b\uff5e", None))
        self.label_10.setText(QCoreApplication.translate("MOS", u"\u4e0b\u8f7d", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MOS", u"\u6e38\u620f\u4e0b\u8f7d", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MOS", u"Mod\u4e0b\u8f7d", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MOS", u"\u6574\u5408\u5305\u4e0b\u8f7d", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MOS", u"\u4e16\u754c\u4e0b\u8f7d", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MOS", u"\u4e0b\u8f7d/\u5b89\u88c5/\u5df2\u5b8c\u6210", None))

        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MOS", u"\u79cd\u7c7b", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MOS", u"\u7248\u672c\u5217\u8868", None));
        self.pushButton_8.setText("")
        self.label_21.setText(QCoreApplication.translate("MOS", u"Quilt\n"
"\u6a21\u7ec4\u52a0\u8f7d\u5668", None))
        self.label_20.setText(QCoreApplication.translate("MOS", u"Optifine\n"
"\u9ad8\u6e05\u4fee\u590d", None))
        self.pushButton_13.setText("")
        self.pushButton_14.setText("")
        self.pushButton_5.setText("")
        self.label_11.setText(QCoreApplication.translate("MOS", u"Forge\n"
"\u6a21\u7ec4\u52a0\u8f7d\u5668", None))
        self.pushButton_7.setText("")
        self.pushButton_15.setText("")
        self.label_19.setText(QCoreApplication.translate("MOS", u"Fabric\n"
"\u6a21\u7ec4\u52a0\u8f7d\u5668", None))
        self.pushButton_6.setText("")
        self.pushButton_12.setText("")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MOS", u"\u7248\u672c\u540d", None))
        self.pushButton_2.setText(QCoreApplication.translate("MOS", u"\u5b89\u88c5", None))
        self.label_12.setText(QCoreApplication.translate("MOS", u"\u97f3\u4e50", None))
        self.label_13.setText(QCoreApplication.translate("MOS", u"\u97f3\u4e50 \u6b63\u5728\u5f00\u53d1\u4e2d\u2026\u2026\n"
"\u4e0d\u8981\u7740\u6025\u5566 \u4f60\u7684\u8d5e\u52a9\u5c31\u662f\u6211\u66f4\u65b0\u7684\u52a8\u529b\uff01\u563b\u563b\uff5e", None))
        self.label_15.setText(QCoreApplication.translate("MOS", u"\u8bbe\u7f6e", None))
        self.pushButton_11.setText(QCoreApplication.translate("MOS", u"\u6062\u590d\u9ed8\u8ba4", None))
        self.label_4.setText(QCoreApplication.translate("MOS", u"<html><head/><body style=\"line-height:1px;\"><p style=\"line-height:1px;\"><span style=\" font-size:20pt;\">\u542f\u52a8\u5668\u5b57\u4f53</span></p><p  style=\"line-height:1px;\">\u5728\u8fd9\u91cc \u4f60\u53ef\u4ee5\u81ea\u5b9a\u4e49\u542f\u52a8\u5668\u5b57\u4f53 \u6709\u7684\u5b57\u4f53\u76f8\u5dee\u5f88\u5c0f\uff0c\u5bfc\u81f4\u6709\u4eba\u53ef\u80fd\u8ba4\u4e3a<span style=\" font-style:italic;line-height:1px;\">\u5b57\u4f53\u6ca1\u6709\u66f4\u6539</span>\uff0c\u5176\u5b9e\u4e0d\u662f\u7684</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MOS", u"Hello Minecraft Optimal Starter 2 !", None))
        self.pushButton_19.setText(QCoreApplication.translate("MOS", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.label_5.setText(QCoreApplication.translate("MOS", u"<html><head/><body><p><span style=\" font-size:20pt;\">\u542f\u52a8\u5668\u66f4\u65b0</span></p><p>\u5728\u8fd9\u91cc \u4f60\u53ef\u4ee5\u66f4\u65b0\u542f\u52a8\u5668</p><p>\u4f60\u53ef\u4ee5\u5728\u201c\u5173\u4e8e\u201d\u4e2d\u67e5\u770b\u5f53\u524d\u7248\u672c</p></body></html>", None))
        self.radioButton.setText(QCoreApplication.translate("MOS", u"\u81ea\u52a8\u4e3a\u60a8\u68c0\u67e5\u66f4\u65b0", None))
        self.pushButton_20.setText(QCoreApplication.translate("MOS", u"\u5f00\u59cb\u66f4\u65b0", None))
        self.label_14.setText(QCoreApplication.translate("MOS", u"<html><head/><body><p><span style=\" font-size:20pt;\">Java\u8bbe\u7f6e</span></p><p>\u5728\u8fd9\u91cc \u4f60\u53ef\u4ee5\u8bbe\u7f6e\u542f\u52a8\u6e38\u620f\u65f6\u4f7f\u7528\u7684Java \u5efa\u8bae\u9009\u62e9 <span style=\" font-style:italic;\">\u8ba9MOS\u4e3a\u60a8\u81ea\u52a8\u9009\u62e9</span></p><p>\u6ce8\u610f\uff1a<span style=\" font-weight:600;\">\u4e0d\u8981\u4f7f\u7528</span><span style=\" font-weight:600; font-style:italic;\">\u7f51\u6613\u542f\u52a8\u5668</span><span style=\" font-weight:600;\">\u7684Java \u3001</span><span style=\" font-weight:600; font-style:italic;\">1.17</span><span style=\" font-weight:600;\">\u53ca\u4ee5\u4e0a\u7248\u672c\u9700\u7528</span><span style=\" font-weight:600; font-style:italic;\">Java16</span><span style=\" font-weight:600;\">\u53ca\u4ee5\u4e0a\u7248\u672c 1.17\u4e00\u4e0b\u9700\u7528Java8</span></p></body></html>", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("MOS", u"\u8ba9MOS\u81ea\u52a8\u4e3a\u60a8\u9009\u62e9", None))

        self.pushButton_21.setText(QCoreApplication.translate("MOS", u"\u6062\u590d\u9ed8\u8ba4", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MOS", u"\u542f\u52a8\u5668\u8bbe\u7f6e", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MOS", u"\u5168\u5c40\u6e38\u620f\u8bbe\u7f6e", None))

        self.label.setText(QCoreApplication.translate("MOS", u"\u5173\u4e8e\uff1a", None))
        self.pushButton.setText("")
        self.label_16.setText(QCoreApplication.translate("MOS", u"MOS\u542f\u52a8\u5668\n"
"\u7248\u672cV2.0.5-alpha", None))
        self.label_18.setText(QCoreApplication.translate("MOS", u"MOS\u552f\u4e00\u5f00\u53d1\u8005 David", None))
        self.pushButton_4.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MOS", u"\u8d5e\u52a9\u4f5c\u8005", None))
        self.label_25.setText("")
        self.pushButton_9.setText("")
        self.label_22.setText(QCoreApplication.translate("MOS", u"MOS\u7f51\u7ad9\u652f\u6301\u3001\u6d4b\u8bd5\u5c0f\u7ec4\u8d1f\u8d23\u4eba HeimNad", None))
        self.pushButton_10.setText(QCoreApplication.translate("MOS", u"\u6253\u5f00\u535a\u5ba2", None))
        self.label_17.setText(QCoreApplication.translate("MOS", u"\u5173\u4e8e", None))
        self.label_mos_left_top_add.setText(QCoreApplication.translate("MOS", u"\u70b9\u51fb\u6dfb\u52a0", None))
        self.pushButton_mos_left_top.setText("")
        self.label_mos_left_top_user.setText(QCoreApplication.translate("MOS", u"\u65e0\u7528\u6237", None))
        self.pushButton_home.setText(QCoreApplication.translate("MOS", u"\u4e3b\u9875", None))
        self.pushButton_lianji.setText(QCoreApplication.translate("MOS", u"\u8054\u673a", None))
        self.pushButton_xiazai.setText(QCoreApplication.translate("MOS", u"\u4e0b\u8f7d", None))
        self.pushButton_music.setText(QCoreApplication.translate("MOS", u"\u97f3\u4e50", None))
        self.pushButton_shezhi.setText(QCoreApplication.translate("MOS", u"\u8bbe\u7f6e", None))
        self.pushButton_about.setText(QCoreApplication.translate("MOS", u"\u5173\u4e8e", None))
        self.label_mosll.setText(QCoreApplication.translate("MOS", u"MOS II", None))
    # retranslateUi

