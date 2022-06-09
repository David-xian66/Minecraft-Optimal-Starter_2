# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MOS_UI.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHeaderView, QLabel, QMainWindow, QProgressBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QTextBrowser, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)
import img_rc

class Ui_MOS(object):
    def setupUi(self, MOS):
        if not MOS.objectName():
            MOS.setObjectName(u"MOS")
        MOS.setWindowModality(Qt.NonModal)
        MOS.resize(1000, 533)
        MOS.setMinimumSize(QSize(1000, 533))
        MOS.setStyleSheet(u"QMainWindow{\n"
"	border-radius:15px;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.centralwidget = QWidget(MOS)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgba(255, 255, 255,100);")
        self.gridLayout_13 = QGridLayout(self.centralwidget)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setHorizontalSpacing(0)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.widget_mos_left = QWidget(self.centralwidget)
        self.widget_mos_left.setObjectName(u"widget_mos_left")
        self.widget_mos_left.setAutoFillBackground(False)
        self.widget_mos_left.setStyleSheet(u"QWidget\n"
"{\n"
"	background-color: rgba(231, 230, 228,100);\n"
"	border-bottom-left-radius:15px;\n"
"	border-top-left-radius:15px;\n"
"}\n"
"#pushButton_about\n"
"{\n"
"	color: blue;\n"
"	height:35px;\n"
"	color: rgb(0, 150, 255);\n"
"	background-position: left;\n"
"	text-align: left;\n"
"	padding-right:10px;\n"
"	padding-left:3px;\n"
"	font-size: 15px;\n"
"	border-style:none;\n"
"	border-radius:8px;\n"
"	border:2px solid rgb(229, 228, 226);\n"
"}\n"
"#pushButton_about::hover\n"
"{\n"
"	background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_about::pressed\n"
"{\n"
"	border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_xiazai\n"
"{\n"
"	color: blue;\n"
"	height:35px;\n"
"	color: rgb(0, 150, 255);\n"
"	background-position: left;\n"
"	text-align: left;\n"
"	padding-right:10px;\n"
"	padding-left:3px;\n"
"	font-size: 15px;\n"
"	border-style:none;\n"
"	border-radius:8px;\n"
"	border:2px solid rgb(229, 228, 226);\n"
"}\n"
"#pushButton_xiazai::hover\n"
"{\n"
"	background-color: rgb(192, 192, 192);"
                        "\n"
"}\n"
"#pushButton_xiazai::pressed\n"
"{\n"
"	border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_shezhi\n"
"{\n"
"	color: blue;\n"
"	height:35px;\n"
"	color: rgb(0, 150, 255);\n"
"	background-position: left;\n"
"	text-align: left;\n"
"	padding-right:10px;\n"
"	padding-left:3px;\n"
"	font-size: 15px;\n"
"	border-style:none;\n"
"	border-radius:8px;\n"
"	border:2px solid rgb(229, 228, 226);\n"
"}\n"
"#pushButton_shezhi::hover\n"
"{\n"
"	background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_shezhi::pressed\n"
"{\n"
"	border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_music\n"
"{\n"
"	color: blue;\n"
"	height:35px;\n"
"	color: rgb(0, 150, 255);\n"
"	background-position: left;\n"
"	text-align: left;\n"
"	padding-right:10px;\n"
"	padding-left:3px;\n"
"	font-size: 15px;\n"
"	border-style:none;\n"
"	border-radius:8px;\n"
"	border:2px solid rgb(229, 228, 226);\n"
"}\n"
"#pushButton_music::hover\n"
"{\n"
"	background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_music::pressed"
                        "\n"
"{\n"
"	border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_lianji\n"
"{\n"
"	color: blue;\n"
"	height:35px;\n"
"	color: rgb(0, 150, 255);\n"
"	background-position: left;\n"
"	text-align: left;\n"
"	padding-right:10px;\n"
"	padding-left:3px;\n"
"	font-size: 15px;\n"
"	border-style:none;\n"
"	border-radius:8px;\n"
"	border:2px solid rgb(229, 228, 226);\n"
"}\n"
"#pushButton_lianji::hover\n"
"{\n"
"	background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_lianji::pressed\n"
"{\n"
"	border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"\n"
"#pushButton_home\n"
"{\n"
"	color: blue;\n"
"	height:35px;\n"
"	color: rgb(0, 150, 255);\n"
"	background-position: left;\n"
"	text-align: left;\n"
"	padding-right:10px;\n"
"	padding-left:3px;\n"
"	font-size: 15px;\n"
"	border-style:none;\n"
"	border-radius:8px;\n"
"	border:2px solid rgb(229, 228, 226);background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_home::hover\n"
"{\n"
"	background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_home::pressed\n"
""
                        "{\n"
"	border:2px solid rgb(0, 150, 255);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.widget_mos_left)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_mos_left_top = QWidget(self.widget_mos_left)
        self.widget_mos_left_top.setObjectName(u"widget_mos_left_top")
        self.widget_mos_left_top.setStyleSheet(u"QWidget\n"
"{\n"
"	background-color: rgba(231, 230, 228,100);\n"
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
"")
        self.gridLayout_4 = QGridLayout(self.widget_mos_left_top)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_mos_left_top_user = QLabel(self.widget_mos_left_top)
        self.label_mos_left_top_user.setObjectName(u"label_mos_left_top_user")
        self.label_mos_left_top_user.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_4.addWidget(self.label_mos_left_top_user, 0, 1, 1, 1)

        self.pushButton_mos_left_top = QPushButton(self.widget_mos_left_top)
        self.pushButton_mos_left_top.setObjectName(u"pushButton_mos_left_top")
        self.pushButton_mos_left_top.setStyleSheet(u"width:50px;height:50px;border-radius: 23px;background-color: rgba(255, 255, 255, 0);")
        icon = QIcon()
        icon.addFile(u"../picture/ico.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_mos_left_top.setIcon(icon)
        self.pushButton_mos_left_top.setIconSize(QSize(50, 50))

        self.gridLayout_4.addWidget(self.pushButton_mos_left_top, 0, 0, 2, 1)

        self.label_mos_left_top_add = QLabel(self.widget_mos_left_top)
        self.label_mos_left_top_add.setObjectName(u"label_mos_left_top_add")
        self.label_mos_left_top_add.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_4.addWidget(self.label_mos_left_top_add, 1, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.widget_mos_left_top)

        self.line_2 = QFrame(self.widget_mos_left)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.pushButton_home = QPushButton(self.widget_mos_left)
        self.pushButton_home.setObjectName(u"pushButton_home")
        self.pushButton_home.setFocusPolicy(Qt.TabFocus)
        self.pushButton_home.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_home.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"../picture/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_home.setIcon(icon1)
        self.pushButton_home.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.pushButton_home)

        self.pushButton_lianji = QPushButton(self.widget_mos_left)
        self.pushButton_lianji.setObjectName(u"pushButton_lianji")
        self.pushButton_lianji.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"../picture/online.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_lianji.setIcon(icon2)
        self.pushButton_lianji.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.pushButton_lianji)

        self.pushButton_xiazai = QPushButton(self.widget_mos_left)
        self.pushButton_xiazai.setObjectName(u"pushButton_xiazai")
        self.pushButton_xiazai.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"../picture/download.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_xiazai.setIcon(icon3)
        self.pushButton_xiazai.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.pushButton_xiazai)

        self.pushButton_music = QPushButton(self.widget_mos_left)
        self.pushButton_music.setObjectName(u"pushButton_music")
        self.pushButton_music.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"../picture/music.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_music.setIcon(icon4)
        self.pushButton_music.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.pushButton_music)

        self.pushButton_shezhi = QPushButton(self.widget_mos_left)
        self.pushButton_shezhi.setObjectName(u"pushButton_shezhi")
        self.pushButton_shezhi.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u"../picture/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_shezhi.setIcon(icon5)
        self.pushButton_shezhi.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.pushButton_shezhi)

        self.pushButton_about = QPushButton(self.widget_mos_left)
        self.pushButton_about.setObjectName(u"pushButton_about")
        self.pushButton_about.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u"../picture/about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_about.setIcon(icon6)
        self.pushButton_about.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.pushButton_about)

        self.verticalSpacer_11 = QSpacerItem(20, 184, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_11)

        self.label_mosll = QLabel(self.widget_mos_left)
        self.label_mosll.setObjectName(u"label_mosll")
        self.label_mosll.setStyleSheet(u"color: rgb(0, 150, 255);font-size: 17px;font: 75 17pt \"Yuanti SC\";background-color: rgb(240, 239, 238,0);")
        self.label_mosll.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_mosll)


        self.gridLayout_13.addWidget(self.widget_mos_left, 0, 0, 1, 1)

        self.stackedWidget_mos_right = QStackedWidget(self.centralwidget)
        self.stackedWidget_mos_right.setObjectName(u"stackedWidget_mos_right")
        self.stackedWidget_mos_right.setStyleSheet(u"background-color: rgba(255, 255, 255, 128);")
        self.page_gonggao = QWidget()
        self.page_gonggao.setObjectName(u"page_gonggao")
        self.page_gonggao.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.page_gonggao)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea_page_gonggao = QScrollArea(self.page_gonggao)
        self.scrollArea_page_gonggao.setObjectName(u"scrollArea_page_gonggao")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.scrollArea_page_gonggao.sizePolicy().hasHeightForWidth())
        self.scrollArea_page_gonggao.setSizePolicy(sizePolicy)
        self.scrollArea_page_gonggao.setMinimumSize(QSize(790, 0))
        self.scrollArea_page_gonggao.setStyleSheet(u"border-style:none;background-color: rgba(255, 255, 255, 128);")
        self.scrollArea_page_gonggao.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 811, 509))
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.gridLayout_16 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.widget_scrollArea_page_gonggao_left = QWidget(self.scrollAreaWidgetContents)
        self.widget_scrollArea_page_gonggao_left.setObjectName(u"widget_scrollArea_page_gonggao_left")
        self.widget_scrollArea_page_gonggao_left.setStyleSheet(u"border:2px solid rgb(0, 150, 255);border-radius:15px;")
        self.gridLayout_5 = QGridLayout(self.widget_scrollArea_page_gonggao_left)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_gonggao_left_txt = QLabel(self.widget_scrollArea_page_gonggao_left)
        self.label_gonggao_left_txt.setObjectName(u"label_gonggao_left_txt")
        self.label_gonggao_left_txt.setStyleSheet(u"border-style:none;\n"
"font: 13pt \"PingFang SC\";")
        self.label_gonggao_left_txt.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_gonggao_left_txt, 0, 0, 1, 1)

        self.stackedWidget_gonggao = QStackedWidget(self.widget_scrollArea_page_gonggao_left)
        self.stackedWidget_gonggao.setObjectName(u"stackedWidget_gonggao")
        self.stackedWidget_gonggao.setStyleSheet(u"border-style:none;")
        self.page_gonggao_jiazai = QWidget()
        self.page_gonggao_jiazai.setObjectName(u"page_gonggao_jiazai")
        self.gridLayout_20 = QGridLayout(self.page_gonggao_jiazai)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.textBrowser_gonggao_left_txt = QTextBrowser(self.page_gonggao_jiazai)
        self.textBrowser_gonggao_left_txt.setObjectName(u"textBrowser_gonggao_left_txt")
        self.textBrowser_gonggao_left_txt.setStyleSheet(u"border-style:none;")

        self.gridLayout_20.addWidget(self.textBrowser_gonggao_left_txt, 0, 0, 1, 1)

        self.stackedWidget_gonggao.addWidget(self.page_gonggao_jiazai)
        self.page_gonggao_jiazai_ing = QWidget()
        self.page_gonggao_jiazai_ing.setObjectName(u"page_gonggao_jiazai_ing")
        self.page_gonggao_jiazai_ing.setStyleSheet(u"QProgressBar{\n"
"	text-align: center;\n"
"	border-style:none;\n"
"	border-radius:7px;\n"
"	color: rgb(33, 33, 33);\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius:7px;\n"
"	background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(53, 244, 252, 255), stop:1 rgba(222, 255, 255, 255));\n"
"}")
        self.gridLayout_21 = QGridLayout(self.page_gonggao_jiazai_ing)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.page_gonggao_jiazai_ing)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(0, 150, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.label_2, 1, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_21.addItem(self.verticalSpacer_6, 0, 0, 1, 1)

        self.progressBar_2 = QProgressBar(self.page_gonggao_jiazai_ing)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setStyleSheet(u"background-color: rgba(0, 150, 255, 10);height:15px;")
        self.progressBar_2.setMinimum(0)
        self.progressBar_2.setMaximum(100)
        self.progressBar_2.setValue(25)
        self.progressBar_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.progressBar_2.setOrientation(Qt.Horizontal)
        self.progressBar_2.setInvertedAppearance(False)
        self.progressBar_2.setTextDirection(QProgressBar.TopToBottom)

        self.gridLayout_21.addWidget(self.progressBar_2, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_21.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.stackedWidget_gonggao.addWidget(self.page_gonggao_jiazai_ing)

        self.gridLayout_5.addWidget(self.stackedWidget_gonggao, 1, 0, 1, 1)


        self.gridLayout_16.addWidget(self.widget_scrollArea_page_gonggao_left, 0, 0, 1, 1)

        self.widget_scrollArea_page_gonggao_right = QWidget(self.scrollAreaWidgetContents)
        self.widget_scrollArea_page_gonggao_right.setObjectName(u"widget_scrollArea_page_gonggao_right")
        self.widget_scrollArea_page_gonggao_right.setStyleSheet(u"QWidget  {\n"
"	border:2px solid rgb(0, 150, 255);border-radius:15px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 2px solid rgb(235, 235, 235); /* border: \u5bbd\u5ea6 \u7ebf\u7c7b\u578b \u989c\u8272 */\n"
"    border-radius: 3px;\n"
"	height:25px;\n"
"	font-size: 14px;\n"
"	background-color: rgba(0, 150, 255, 77);\n"
"	border-radius:10px;\n"
"}\n"
"/*QComboBox::down-arrow\n"
"\u662f \u53f3\u9762\u90a3\u4e2a \n"
"*/\n"
"QProgressBar{\n"
"	text-align: center;\n"
"	border-style:none;\n"
"	border-radius:7px;\n"
"	color: rgb(33, 33, 33);\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius:7px;\n"
"	background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 224, 249, 255), stop:1 rgba(212, 255, 255, 255));\n"
"}")
        self.gridLayout_6 = QGridLayout(self.widget_scrollArea_page_gonggao_right)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.widget_scrollArea_page_gonggao_statring = QWidget(self.widget_scrollArea_page_gonggao_right)
        self.widget_scrollArea_page_gonggao_statring.setObjectName(u"widget_scrollArea_page_gonggao_statring")
        self.widget_scrollArea_page_gonggao_statring.setStyleSheet(u"border-style:none;")
        self.gridLayout_2 = QGridLayout(self.widget_scrollArea_page_gonggao_statring)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.widget_scrollArea_page_gonggao_statring)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"border-style:none;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_3, 0, 1, 2, 3)

        self.label_7 = QLabel(self.widget_scrollArea_page_gonggao_statring)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_7, 3, 1, 1, 3)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 0, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 0, 4, 2, 1)

        self.progressBar = QProgressBar(self.widget_scrollArea_page_gonggao_statring)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"background-color: rgba(0, 150, 255, 10);height:15px;")
        self.progressBar.setValue(0)

        self.gridLayout_2.addWidget(self.progressBar, 2, 0, 1, 5)


        self.gridLayout_6.addWidget(self.widget_scrollArea_page_gonggao_statring, 1, 0, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_2, 3, 1, 1, 1)

        self.pushButton__gonggao_start = QPushButton(self.widget_scrollArea_page_gonggao_right)
        self.pushButton__gonggao_start.setObjectName(u"pushButton__gonggao_start")
        self.pushButton__gonggao_start.setStyleSheet(u"border-radius:8px;")

        self.gridLayout_6.addWidget(self.pushButton__gonggao_start, 2, 1, 1, 1)

        self.comboBox_gonggao_right = QComboBox(self.widget_scrollArea_page_gonggao_right)
        self.comboBox_gonggao_right.setObjectName(u"comboBox_gonggao_right")

        self.gridLayout_6.addWidget(self.comboBox_gonggao_right, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.label__gonggao_right_txt = QLabel(self.widget_scrollArea_page_gonggao_right)
        self.label__gonggao_right_txt.setObjectName(u"label__gonggao_right_txt")
        self.label__gonggao_right_txt.setStyleSheet(u"border-style:none;")
        self.label__gonggao_right_txt.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label__gonggao_right_txt, 0, 0, 1, 2)


        self.gridLayout_16.addWidget(self.widget_scrollArea_page_gonggao_right, 0, 1, 1, 1)

        self.scrollArea_page_gonggao.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea_page_gonggao)

        self.stackedWidget_mos_right.addWidget(self.page_gonggao)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_7 = QGridLayout(self.page_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(49, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.label_9 = QLabel(self.page_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"border-style:none;color:rgb(33, 33, 33);font-size: 17px;background-color: rgba(255, 255, 255, 0);")
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
        self.widget_5.setStyleSheet(u"border-radius:10px;border:2px solid rgb(0, 150, 255);")
        self.gridLayout_8 = QGridLayout(self.widget_5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(12, -1, -1, -1)
        self.label_8 = QLabel(self.widget_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"border-style:none;color:rgb(0, 150, 255);")

        self.gridLayout_8.addWidget(self.label_8, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.widget_5, 3, 0, 1, 2)

        self.verticalSpacer_3 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_3, 4, 0, 1, 2)

        self.stackedWidget_mos_right.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"QComboBox {\n"
"    border: 2px solid rgb(235, 235, 235); /* border: \u5bbd\u5ea6 \u7ebf\u7c7b\u578b \u989c\u8272 */\n"
"    border-radius: 3px;\n"
"	height:25px;\n"
"	font-size: 14px;\n"
"	background-color: rgba(0, 150, 255, 77);\n"
"	border-radius:10px;\n"
"}\n"
"/*QComboBox::down-arrow\n"
"\u662f \u53f3\u9762\u90a3\u4e2a \n"
"*/")
        self.gridLayout = QGridLayout(self.page_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.comboBox_2 = QComboBox(self.page_3)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 2, 1)

        self.line_3 = QFrame(self.page_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"color:rgb(214, 214, 214)")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setMidLineWidth(1)
        self.line_3.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line_3, 3, 0, 1, 2)

        self.horizontalSpacer_4 = QSpacerItem(832, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 0, 1, 2)

        self.stackedWidget_2 = QStackedWidget(self.page_3)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.page_9.setStyleSheet(u"QAbstractItemView::item {\n"
"    min-height: 110px;\n"
"    min-width: 40px; \n"
"}")
        self.gridLayout_9 = QGridLayout(self.page_9)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.treeWidget = QTreeWidget(self.page_9)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setStyleSheet(u"")
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setUniformRowHeights(False)

        self.gridLayout_9.addWidget(self.treeWidget, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.page_9)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.pushButton_5 = QPushButton(self.page_10)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(40, 50, 113, 32))
        self.label_11 = QLabel(self.page_10)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(200, 70, 171, 16))
        self.comboBox_3 = QComboBox(self.page_10)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(410, 50, 91, 32))
        self.comboBox_4 = QComboBox(self.page_10)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setGeometry(QRect(450, 180, 91, 32))
        self.label_19 = QLabel(self.page_10)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(240, 200, 171, 16))
        self.pushButton_6 = QPushButton(self.page_10)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(80, 180, 113, 32))
        self.comboBox_5 = QComboBox(self.page_10)
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setGeometry(QRect(440, 280, 91, 32))
        self.label_20 = QLabel(self.page_10)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(230, 300, 171, 16))
        self.pushButton_7 = QPushButton(self.page_10)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(70, 280, 113, 32))
        self.comboBox_6 = QComboBox(self.page_10)
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setGeometry(QRect(460, 360, 91, 32))
        self.label_21 = QLabel(self.page_10)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(250, 380, 171, 16))
        self.pushButton_8 = QPushButton(self.page_10)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(90, 360, 113, 32))
        self.stackedWidget_2.addWidget(self.page_10)

        self.gridLayout.addWidget(self.stackedWidget_2, 4, 0, 1, 2)

        self.label_10 = QLabel(self.page_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"border-style:none;color:rgb(33, 33, 33);font-size: 17px;background-color: rgba(255, 255, 255, 0);")
        self.label_10.setIndent(10)

        self.gridLayout.addWidget(self.label_10, 1, 0, 2, 1)

        self.stackedWidget_mos_right.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_3 = QGridLayout(self.page_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(832, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 0, 0, 1, 1)

        self.label_12 = QLabel(self.page_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"border-style:none;color:rgb(33, 33, 33);font-size: 17px;background-color: rgba(255, 255, 255, 0);")
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
        self.widget_8.setStyleSheet(u"border-radius:10px;\n"
"border:2px solid rgb(0, 150, 255);")
        self.gridLayout_10 = QGridLayout(self.widget_8)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(12, -1, -1, -1)
        self.label_13 = QLabel(self.widget_8)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"border-style:none;color:rgb(0, 150, 255);")

        self.gridLayout_10.addWidget(self.label_13, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_8, 3, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(832, 393, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_7, 4, 0, 1, 1)

        self.stackedWidget_mos_right.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout_15 = QGridLayout(self.page_5)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.line_5 = QFrame(self.page_5)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"color:rgb(214, 214, 214)")
        self.line_5.setFrameShadow(QFrame.Plain)
        self.line_5.setMidLineWidth(1)
        self.line_5.setFrameShape(QFrame.HLine)

        self.gridLayout_15.addWidget(self.line_5, 2, 0, 2, 2)

        self.horizontalSpacer_6 = QSpacerItem(832, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_6, 0, 0, 1, 2)

        self.verticalSpacer_8 = QSpacerItem(796, 368, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_8, 5, 1, 1, 1)

        self.label_15 = QLabel(self.page_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"border-style:none;color:rgb(33, 33, 33);font-size: 17px;background-color: rgba(255, 255, 255, 0);")
        self.label_15.setIndent(10)

        self.gridLayout_15.addWidget(self.label_15, 1, 0, 1, 2)

        self.widget_9 = QWidget(self.page_5)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setStyleSheet(u"border-radius:10px;\n"
"border:2px solid rgb(0, 150, 255);")
        self.gridLayout_11 = QGridLayout(self.widget_9)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(12, -1, -1, -1)
        self.label_14 = QLabel(self.widget_9)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"border-style:none;color:rgb(0, 150, 255);")

        self.gridLayout_11.addWidget(self.label_14, 1, 0, 1, 1)


        self.gridLayout_15.addWidget(self.widget_9, 4, 0, 1, 2)

        self.stackedWidget_mos_right.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.gridLayout_14 = QGridLayout(self.page_6)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(832, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_7, 0, 0, 1, 2)

        self.label_17 = QLabel(self.page_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"border-style:none;color:rgb(33, 33, 33);font-size: 17px;background-color: rgba(255, 255, 255, 0);")
        self.label_17.setIndent(10)

        self.gridLayout_14.addWidget(self.label_17, 1, 0, 1, 1)

        self.line_6 = QFrame(self.page_6)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setStyleSheet(u"color:rgb(214, 214, 214)")
        self.line_6.setFrameShadow(QFrame.Plain)
        self.line_6.setMidLineWidth(1)
        self.line_6.setFrameShape(QFrame.HLine)

        self.gridLayout_14.addWidget(self.line_6, 2, 0, 1, 2)

        self.widget_10 = QWidget(self.page_6)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.gridLayout_19 = QGridLayout(self.widget_10)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.widget_13 = QWidget(self.widget_10)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setStyleSheet(u"border-radius:15px;border:2px solid rgba(0, 150, 255, 128);")
        self.verticalLayout_3 = QVBoxLayout(self.widget_13)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.widget_13)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"border-style:none;")

        self.verticalLayout_3.addWidget(self.label)

        self.widget_11 = QWidget(self.widget_13)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setStyleSheet(u"border-style:none;background-color: rgb(235, 235, 235);border-radius:15px;")
        self.gridLayout_12 = QGridLayout(self.widget_11)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
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
        self.label_16.setStyleSheet(u"border-style:none;")

        self.gridLayout_12.addWidget(self.label_16, 1, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.widget_13)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setStyleSheet(u"border-style:none;background-color: rgb(235, 235, 235);border-radius:15px;")
        self.gridLayout_17 = QGridLayout(self.widget_12)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_18 = QLabel(self.widget_12)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"border-style:none;")

        self.gridLayout_17.addWidget(self.label_18, 0, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.widget_12)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"border-style:none;")
        icon7 = QIcon()
        icon7.addFile(u"../picture/david.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon7)
        self.pushButton_4.setIconSize(QSize(40, 40))

        self.gridLayout_17.addWidget(self.pushButton_4, 0, 0, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(34, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_9, 0, 2, 1, 1)


        self.verticalLayout_3.addWidget(self.widget_12)

        self.widget_14 = QWidget(self.widget_13)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setStyleSheet(u"border-style:none;background-color: rgb(235, 235, 235);border-radius:15px;")
        self.gridLayout_18 = QGridLayout(self.widget_14)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.label_22 = QLabel(self.widget_14)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"border-style:none;")

        self.gridLayout_18.addWidget(self.label_22, 0, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.widget_14)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"border-style:none;")
        icon8 = QIcon()
        icon8.addFile(u"../picture/heimnad.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon8)
        self.pushButton_9.setIconSize(QSize(40, 40))

        self.gridLayout_18.addWidget(self.pushButton_9, 0, 0, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(34, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_10, 0, 2, 1, 1)


        self.verticalLayout_3.addWidget(self.widget_14)


        self.gridLayout_19.addWidget(self.widget_13, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(796, 368, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_19.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.gridLayout_14.addWidget(self.widget_10, 3, 0, 1, 2)

        self.stackedWidget_mos_right.addWidget(self.page_6)

        self.gridLayout_13.addWidget(self.stackedWidget_mos_right, 0, 1, 1, 1)

        MOS.setCentralWidget(self.centralwidget)

        self.retranslateUi(MOS)

        self.stackedWidget_mos_right.setCurrentIndex(0)
        self.stackedWidget_gonggao.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MOS)
    # setupUi

    def retranslateUi(self, MOS):
        MOS.setWindowTitle(QCoreApplication.translate("MOS", u"MainWindow", None))
        self.label_mos_left_top_user.setText(QCoreApplication.translate("MOS", u"\u65e0\u7528\u6237", None))
        self.pushButton_mos_left_top.setText("")
        self.label_mos_left_top_add.setText(QCoreApplication.translate("MOS", u"\u70b9\u51fb\u6dfb\u52a0", None))
        self.pushButton_home.setText(QCoreApplication.translate("MOS", u"Home", None))
        self.pushButton_lianji.setText(QCoreApplication.translate("MOS", u"\u8054\u673a", None))
        self.pushButton_xiazai.setText(QCoreApplication.translate("MOS", u"\u4e0b\u8f7d", None))
        self.pushButton_music.setText(QCoreApplication.translate("MOS", u"\u97f3\u4e50", None))
        self.pushButton_shezhi.setText(QCoreApplication.translate("MOS", u"\u8bbe\u7f6e", None))
        self.pushButton_about.setText(QCoreApplication.translate("MOS", u"\u5173\u4e8e", None))
        self.label_mosll.setText(QCoreApplication.translate("MOS", u"MOS II", None))
        self.label_gonggao_left_txt.setText(QCoreApplication.translate("MOS", u"\u516c\u544a", None))
        self.label_2.setText(QCoreApplication.translate("MOS", u"\u6b63\u5728\u52a0\u8f7d\n"
"\n"
"\u5f53\u524d\u6b65\u9aa4\uff1a\u4e0b\u8f7d\u516c\u544a\u2026\u2026\u8bf7\u7a0d\u540e\n"
"", None))
        self.label_3.setText(QCoreApplication.translate("MOS", u"\u542f\u52a8\u7684\u56fe\u7247", None))
        self.label_7.setText(QCoreApplication.translate("MOS", u"\u542f\u52a8\u541b\uff1a\u5f85\u547d\u4e2d\u2026\u2026", None))
        self.pushButton__gonggao_start.setText(QCoreApplication.translate("MOS", u"\u542f\u52a8\u6e38\u620f", None))
        self.label__gonggao_right_txt.setText(QCoreApplication.translate("MOS", u"\u9009\u62e9\u8981\u542f\u52a8\u7684\u6e38\u620f", None))
        self.label_9.setText(QCoreApplication.translate("MOS", u"\u8054\u673a\u6a21\u5757", None))
        self.label_8.setText(QCoreApplication.translate("MOS", u"\u8054\u673a\u6a21\u5757\u6b63\u5728\u5f00\u53d1\u4e2d\u2026\u2026\n"
"\u4e0d\u8981\u7740\u6025\u5566 \u4f60\u7684\u8d5e\u52a9\u5c31\u662f\u6211\u66f4\u65b0\u7684\u52a8\u529b\uff01\u563b\u563b\uff5e", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MOS", u"\u6e38\u620f\u4e0b\u8f7d", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MOS", u"Mod\u4e0b\u8f7d", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MOS", u"\u6574\u5408\u5305\u4e0b\u8f7d", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MOS", u"\u4e16\u754c\u4e0b\u8f7d", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MOS", u"\u4e0b\u8f7d/\u5b89\u88c5/\u5df2\u5b8c\u6210", None))

        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MOS", u"\u79cd\u7c7b", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MOS", u"\u7248\u672c\u5217\u8868", None));
        self.pushButton_5.setText(QCoreApplication.translate("MOS", u"\uff08\u56fe\u7247\uff09", None))
        self.label_11.setText(QCoreApplication.translate("MOS", u"\u6a21\u7ec4\u52a0\u8f7d\u5668\uff08forge", None))
        self.label_19.setText(QCoreApplication.translate("MOS", u"\u6a21\u7ec4\u52a0\u8f7d\u5668\uff08fabric", None))
        self.pushButton_6.setText(QCoreApplication.translate("MOS", u"\uff08\u56fe\u7247\uff09", None))
        self.label_20.setText(QCoreApplication.translate("MOS", u"\u9ad8\u6e05\u4fee\u590doptifine", None))
        self.pushButton_7.setText(QCoreApplication.translate("MOS", u"\uff08\u56fe\u7247\uff09", None))
        self.label_21.setText(QCoreApplication.translate("MOS", u"\u6a21\u7ec4\u52a0\u8f7d\u5668\uff08quilt", None))
        self.pushButton_8.setText(QCoreApplication.translate("MOS", u"\uff08\u56fe\u7247\uff09", None))
        self.label_10.setText(QCoreApplication.translate("MOS", u"\u4e0b\u8f7d", None))
        self.label_12.setText(QCoreApplication.translate("MOS", u"\u97f3\u4e50", None))
        self.label_13.setText(QCoreApplication.translate("MOS", u"\u97f3\u4e50 \u6b63\u5728\u5f00\u53d1\u4e2d\u2026\u2026\n"
"\u4e0d\u8981\u7740\u6025\u5566 \u4f60\u7684\u8d5e\u52a9\u5c31\u662f\u6211\u66f4\u65b0\u7684\u52a8\u529b\uff01\u563b\u563b\uff5e", None))
        self.label_15.setText(QCoreApplication.translate("MOS", u"\u8bbe\u7f6e", None))
        self.label_14.setText(QCoreApplication.translate("MOS", u"\u8bbe\u7f6e \u6b63\u5728\u5f00\u53d1\u4e2d\u2026\u2026\n"
"\u4e0d\u8981\u7740\u6025\u5566 \u4f60\u7684\u8d5e\u52a9\u5c31\u662f\u6211\u66f4\u65b0\u7684\u52a8\u529b\uff01\u563b\u563b\uff5e", None))
        self.label_17.setText(QCoreApplication.translate("MOS", u"\u5173\u4e8e", None))
        self.label.setText(QCoreApplication.translate("MOS", u"\u5173\u4e8e\uff1a", None))
        self.pushButton.setText("")
        self.label_16.setText(QCoreApplication.translate("MOS", u"MOS\u542f\u52a8\u5668\n"
"\u7248\u672cV2.0.2-alpha-\u5185\u90e8\u7248\u672c\n"
"\u8bf7\u52ff\u6cc4\u6f0f\uff01", None))
        self.label_18.setText(QCoreApplication.translate("MOS", u"MOS\u552f\u4e00\u5f00\u53d1\u8005\uff1aDavid", None))
        self.pushButton_4.setText("")
        self.label_22.setText(QCoreApplication.translate("MOS", u"MOS\u7f51\u7ad9\u652f\u6301\u3001\u6d4b\u8bd5\u5c0f\u7ec4\u8d1f\u8d23\u4eba\uff1aHeimNad", None))
        self.pushButton_9.setText("")
    # retranslateUi

