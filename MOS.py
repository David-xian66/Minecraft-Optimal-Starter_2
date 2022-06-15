import sys, os, requests, json, datetime
import time

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r'.\site-packages\PyQt5\Qt5\plugins'  #### 这一行是新增的。用的是相对路径。

from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MOS(object):
    def setupUi(self, MOS):

        MOS_catalogue_picture_ico_png = os.path.join("picture", "ico.png")
        MOS_catalogue_picture_home_png = os.path.join("picture", "home.png")
        MOS_catalogue_picture_online_png = os.path.join("picture", "online.png")
        MOS_catalogue_picture_download_png = os.path.join("picture", "download.png")
        MOS_catalogue_picture_music_png = os.path.join("picture", "music.png")
        MOS_catalogue_picture_settings_png = os.path.join("picture", "settings.png")
        MOS_catalogue_picture_about_png = os.path.join("picture", "about.png")
        MOS_catalogue_picture_david_png = os.path.join("picture", "david.jpg")
        MOS_catalogue_picture_heimnad_png = os.path.join("picture", "heimnad.png")

        MOS.setObjectName("MOS")
        MOS.setWindowModality(QtCore.Qt.NonModal)
        MOS.resize(1000, 533)
        MOS.setMinimumSize(QtCore.QSize(1000, 533))
        MOS.setStyleSheet("QMainWindow{\n"
"    border-radius:15px;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MOS)
        self.centralwidget.setStyleSheet("background-color: rgba(255, 255, 255,100);")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_mos_left = QtWidgets.QWidget(self.centralwidget)
        self.widget_mos_left.setAutoFillBackground(False)
        self.widget_mos_left.setStyleSheet("QWidget\n"
"{\n"
"    background-color: rgba(231, 230, 228,100);\n"
"    border-bottom-left-radius:15px;\n"
"    border-top-left-radius:15px;\n"
"    font-size: 13px;\n"
"}\n"
"#widget_mos_left_top\n"
"{\n"
"    background-color: rgb(231, 230, 228);\n"
"    border-style:none;\n"
"    border-radius:15px;\n"
"}\n"
"#widget_mos_left_top::hover\n"
"{\n"
"    background-color: rgba(0, 150, 255, 51);\n"
"}\n"
"#widget_mos_left_top::pressed\n"
"{\n"
"    background-color: rgba(0, 150, 255, 51);\n"
"}\n"
"QPushButton\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:15px;\n"
"    padding-left:5px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226,0);\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}\n"
"\n"
"#pushButton_home\n"
"{\n"
"    color: blue;\n"
"    height:35px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:15px;\n"
"    padding-left:5px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:8px;\n"
"    border:2px solid rgb(229, 228, 226,0);background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_home::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"#pushButton_home::pressed\n"
"{\n"
"    border:2px solid rgb(0, 150, 255);\n"
"}")
        self.widget_mos_left.setObjectName("widget_mos_left")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_mos_left)
        self.verticalLayout_2.setContentsMargins(9, -1, 9, -1)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_mos_left_top = QtWidgets.QWidget(self.widget_mos_left)
        self.widget_mos_left_top.setStyleSheet("QWidget\n"
"{\n"
"    background-color: rgba(231, 230, 228);\n"
"    border-style:none;\n"
"    border-radius:15px;\n"
"}\n"
"QWidget::hover\n"
"{\n"
"    background-color: rgba(0, 150, 255, 51);\n"
"}\n"
"QWidget::pressed\n"
"{\n"
"    background-color: rgba(0, 150, 255, 51);\n"
"}\n"
"QPushButton\n"
"{\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:0px;\n"
"    padding-left:0px;\n"
"}\n"
"")
        self.widget_mos_left_top.setObjectName("widget_mos_left_top")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_mos_left_top)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_mos_left_top_add = QtWidgets.QLabel(self.widget_mos_left_top)
        self.label_mos_left_top_add.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_mos_left_top_add.setObjectName("label_mos_left_top_add")
        self.gridLayout_4.addWidget(self.label_mos_left_top_add, 1, 1, 1, 1)
        self.pushButton_mos_left_top = QtWidgets.QPushButton(self.widget_mos_left_top)
        self.pushButton_mos_left_top.setStyleSheet("width:50px;height:50px;border-radius: 23px;background-color: rgba(255, 255, 255, 0);")
        self.pushButton_mos_left_top.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(MOS_catalogue_picture_ico_png), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_mos_left_top.setIcon(icon)
        self.pushButton_mos_left_top.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_mos_left_top.setObjectName("pushButton_mos_left_top")
        self.gridLayout_4.addWidget(self.pushButton_mos_left_top, 0, 0, 2, 1)
        self.label_mos_left_top_user = QtWidgets.QLabel(self.widget_mos_left_top)
        self.label_mos_left_top_user.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_mos_left_top_user.setObjectName("label_mos_left_top_user")
        self.gridLayout_4.addWidget(self.label_mos_left_top_user, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.widget_mos_left_top)
        self.line_2 = QtWidgets.QFrame(self.widget_mos_left)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.pushButton_home = QtWidgets.QPushButton(self.widget_mos_left)
        self.pushButton_home.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_home.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton_home.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_home.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(MOS_catalogue_picture_home_png), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_home.setIcon(icon1)
        self.pushButton_home.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_home.setObjectName("pushButton_home")
        self.verticalLayout_2.addWidget(self.pushButton_home)
        self.pushButton_lianji = QtWidgets.QPushButton(self.widget_mos_left)
        self.pushButton_lianji.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_lianji.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(MOS_catalogue_picture_picture_png), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_lianji.setIcon(icon2)
        self.pushButton_lianji.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_lianji.setObjectName("pushButton_lianji")
        self.verticalLayout_2.addWidget(self.pushButton_lianji)
        self.pushButton_xiazai = QtWidgets.QPushButton(self.widget_mos_left)
        self.pushButton_xiazai.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_xiazai.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(MOS_catalogue_picture_download_png), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_xiazai.setIcon(icon3)
        self.pushButton_xiazai.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_xiazai.setObjectName("pushButton_xiazai")
        self.verticalLayout_2.addWidget(self.pushButton_xiazai)
        self.pushButton_music = QtWidgets.QPushButton(self.widget_mos_left)
        self.pushButton_music.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_music.setStyleSheet("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(MOS_catalogue_picture_music_png), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_music.setIcon(icon4)
        self.pushButton_music.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_music.setObjectName("pushButton_music")
        self.verticalLayout_2.addWidget(self.pushButton_music)
        self.pushButton_shezhi = QtWidgets.QPushButton(self.widget_mos_left)
        self.pushButton_shezhi.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_shezhi.setStyleSheet("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(MOS_catalogue_picture_settings_png), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_shezhi.setIcon(icon5)
        self.pushButton_shezhi.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_shezhi.setObjectName("pushButton_shezhi")
        self.verticalLayout_2.addWidget(self.pushButton_shezhi)
        self.pushButton_about = QtWidgets.QPushButton(self.widget_mos_left)
        self.pushButton_about.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_about.setStyleSheet("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(MOS_catalogue_picture_about_png), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_about.setIcon(icon6)
        self.pushButton_about.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_about.setObjectName("pushButton_about")
        self.verticalLayout_2.addWidget(self.pushButton_about)
        spacerItem = QtWidgets.QSpacerItem(20, 184, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label_mosll = QtWidgets.QLabel(self.widget_mos_left)
        self.label_mosll.setStyleSheet("color: rgb(0, 150, 255);font-size: 17px;font: 75 17pt \"Yuanti SC\";background-color: rgb(240, 239, 238,0);")
        self.label_mosll.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mosll.setObjectName("label_mosll")
        self.verticalLayout_2.addWidget(self.label_mosll)
        self.horizontalLayout_2.addWidget(self.widget_mos_left)
        self.stackedWidget_mos_right = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget_mos_right.setStyleSheet("font: 13pt \"PingFang SC\";background-color: rgba(255, 255, 255, 128);")
        self.stackedWidget_mos_right.setObjectName("stackedWidget_mos_right")
        self.page_gonggao = QtWidgets.QWidget()
        self.page_gonggao.setStyleSheet("")
        self.page_gonggao.setObjectName("page_gonggao")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.page_gonggao)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea_page_gonggao = QtWidgets.QScrollArea(self.page_gonggao)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.scrollArea_page_gonggao.sizePolicy().hasHeightForWidth())
        self.scrollArea_page_gonggao.setSizePolicy(sizePolicy)
        self.scrollArea_page_gonggao.setMinimumSize(QtCore.QSize(790, 0))
        self.scrollArea_page_gonggao.setStyleSheet("border-style:none;background-color: rgba(255, 255, 255, 128);")
        self.scrollArea_page_gonggao.setWidgetResizable(True)
        self.scrollArea_page_gonggao.setObjectName("scrollArea_page_gonggao")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 808, 509))
        self.scrollAreaWidgetContents.setStyleSheet("")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.widget_scrollArea_page_gonggao_right = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_scrollArea_page_gonggao_right.setStyleSheet("QWidget  {\n"
"    border:2px solid rgb(0, 150, 255);border-radius:15px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 2px solid rgb(235, 235, 235); /* border: 宽度 线类型 颜色 */\n"
"    border-radius: 3px;\n"
"    height:25px;\n"
"    font-size: 14px;\n"
"    background-color: rgba(0, 150, 255, 77);\n"
"    border-radius:10px;\n"
"}\n"
"/*QComboBox::down-arrow\n"
"是 右面那个 \n"
"*/\n"
"QProgressBar{\n"
"    text-align: center;\n"
"    border-style:none;\n"
"    border-radius:7px;\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"QProgressBar::chunk{\n"
"    border-radius:7px;\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 224, 249, 255), stop:1 rgba(212, 255, 255, 255));\n"
"}")
        self.widget_scrollArea_page_gonggao_right.setObjectName("widget_scrollArea_page_gonggao_right")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_scrollArea_page_gonggao_right)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 4, 1, 1, 1)
        self.widget_scrollArea_page_gonggao_statring = QtWidgets.QWidget(self.widget_scrollArea_page_gonggao_right)
        self.widget_scrollArea_page_gonggao_statring.setStyleSheet("border-style:none;")
        self.widget_scrollArea_page_gonggao_statring.setObjectName("widget_scrollArea_page_gonggao_statring")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_scrollArea_page_gonggao_statring)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.progressBar = QtWidgets.QProgressBar(self.widget_scrollArea_page_gonggao_statring)
        self.progressBar.setStyleSheet("background-color: rgba(0, 150, 255, 10);height:15px;")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 2, 0, 1, 5)
        self.label_3 = QtWidgets.QLabel(self.widget_scrollArea_page_gonggao_statring)
        self.label_3.setStyleSheet("border-style:none;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 1, 2, 3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget_scrollArea_page_gonggao_statring)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 1, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 0, 4, 2, 1)
        self.gridLayout_6.addWidget(self.widget_scrollArea_page_gonggao_statring, 2, 0, 1, 2)
        self.label__gonggao_right_txt = QtWidgets.QLabel(self.widget_scrollArea_page_gonggao_right)
        self.label__gonggao_right_txt.setStyleSheet("border-style:none;font-size: 14px;")
        self.label__gonggao_right_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.label__gonggao_right_txt.setObjectName("label__gonggao_right_txt")
        self.gridLayout_6.addWidget(self.label__gonggao_right_txt, 0, 0, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem4, 4, 0, 1, 1)
        self.pushButton__gonggao_start = QtWidgets.QPushButton(self.widget_scrollArea_page_gonggao_right)
        self.pushButton__gonggao_start.setStyleSheet("border-radius:8px;")
        self.pushButton__gonggao_start.setObjectName("pushButton__gonggao_start")
        self.gridLayout_6.addWidget(self.pushButton__gonggao_start, 3, 1, 1, 1)
        self.comboBox_gonggao_right = QtWidgets.QComboBox(self.widget_scrollArea_page_gonggao_right)
        self.comboBox_gonggao_right.setObjectName("comboBox_gonggao_right")
        self.gridLayout_6.addWidget(self.comboBox_gonggao_right, 3, 0, 1, 1)
        self.line_8 = QtWidgets.QFrame(self.widget_scrollArea_page_gonggao_right)
        self.line_8.setStyleSheet("background-color: rgb(169, 169, 169);border:none;")
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_6.addWidget(self.line_8, 1, 0, 1, 2)
        self.gridLayout_16.addWidget(self.widget_scrollArea_page_gonggao_right, 0, 1, 1, 1)
        self.widget_scrollArea_page_gonggao_left = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_scrollArea_page_gonggao_left.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_scrollArea_page_gonggao_left.setStyleSheet("border:2px solid rgb(0, 150, 255);border-radius:15px;")
        self.widget_scrollArea_page_gonggao_left.setObjectName("widget_scrollArea_page_gonggao_left")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_scrollArea_page_gonggao_left)
        self.gridLayout_5.setContentsMargins(10, -1, 10, -1)
        self.gridLayout_5.setHorizontalSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_gonggao_left_txt = QtWidgets.QLabel(self.widget_scrollArea_page_gonggao_left)
        self.label_gonggao_left_txt.setStyleSheet("font-size: 14px;border-style:none;")
        self.label_gonggao_left_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.label_gonggao_left_txt.setObjectName("label_gonggao_left_txt")
        self.gridLayout_5.addWidget(self.label_gonggao_left_txt, 0, 0, 1, 1)
        self.stackedWidget_gonggao = QtWidgets.QStackedWidget(self.widget_scrollArea_page_gonggao_left)
        self.stackedWidget_gonggao.setStyleSheet("border-style:none;")
        self.stackedWidget_gonggao.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget_gonggao.setLineWidth(2)
        self.stackedWidget_gonggao.setObjectName("stackedWidget_gonggao")
        self.page_gonggao_jiazai = QtWidgets.QWidget()
        self.page_gonggao_jiazai.setObjectName("page_gonggao_jiazai")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.page_gonggao_jiazai)
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.textBrowser_gonggao_left_txt = QtWidgets.QTextBrowser(self.page_gonggao_jiazai)
        self.textBrowser_gonggao_left_txt.setStyleSheet("border-style:none;")
        self.textBrowser_gonggao_left_txt.setObjectName("textBrowser_gonggao_left_txt")
        self.gridLayout_20.addWidget(self.textBrowser_gonggao_left_txt, 0, 0, 1, 1)
        self.stackedWidget_gonggao.addWidget(self.page_gonggao_jiazai)
        self.page_gonggao_jiazai_ing = QtWidgets.QWidget()
        self.page_gonggao_jiazai_ing.setStyleSheet("QProgressBar{\n"
"    text-align: center;\n"
"    border-style:none;\n"
"    border-radius:7px;\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"QProgressBar::chunk{\n"
"    border-radius:7px;\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(53, 244, 252, 255), stop:1 rgba(222, 255, 255, 255));\n"
"}")
        self.page_gonggao_jiazai_ing.setObjectName("page_gonggao_jiazai_ing")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.page_gonggao_jiazai_ing)
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_21.setObjectName("gridLayout_21")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_21.addItem(spacerItem5, 0, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_21.addItem(spacerItem6, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.page_gonggao_jiazai_ing)
        self.label_2.setStyleSheet("font-size: 13px;color: rgb(0, 150, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_21.addWidget(self.label_2, 1, 0, 1, 1)
        self.progressBar_2 = QtWidgets.QProgressBar(self.page_gonggao_jiazai_ing)
        self.progressBar_2.setStyleSheet("background-color: rgba(0, 150, 255, 10);height:15px;color: rgb(66, 66, 66);")
        self.progressBar_2.setMinimum(0)
        self.progressBar_2.setMaximum(100)
        self.progressBar_2.setProperty("value", 25)
        self.progressBar_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.progressBar_2.setTextVisible(True)
        self.progressBar_2.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar_2.setInvertedAppearance(False)
        self.progressBar_2.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_2.setObjectName("progressBar_2")
        self.gridLayout_21.addWidget(self.progressBar_2, 2, 0, 1, 1)
        self.stackedWidget_gonggao.addWidget(self.page_gonggao_jiazai_ing)
        self.gridLayout_5.addWidget(self.stackedWidget_gonggao, 2, 0, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem7, 3, 0, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.widget_scrollArea_page_gonggao_left)
        self.line_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.line_7.setAutoFillBackground(False)
        self.line_7.setStyleSheet("background-color: rgb(169, 169, 169);border:none;")
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setLineWidth(1)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setObjectName("line_7")
        self.gridLayout_5.addWidget(self.line_7, 1, 0, 1, 2)
        self.gridLayout_16.addWidget(self.widget_scrollArea_page_gonggao_left, 0, 0, 1, 1)
        self.scrollArea_page_gonggao.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea_page_gonggao)
        self.stackedWidget_mos_right.addWidget(self.page_gonggao)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem8 = QtWidgets.QSpacerItem(49, 13, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem8, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setStyleSheet("border-style:none;color:rgb(33, 33, 33);font-size: 17px;background-color: rgba(255, 255, 255, 0);")
        self.label_9.setIndent(10)
        self.label_9.setObjectName("label_9")
        self.gridLayout_7.addWidget(self.label_9, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.page_2)
        self.line.setStyleSheet("color:rgb(214, 214, 214)")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout_7.addWidget(self.line, 2, 0, 1, 2)
        self.widget_5 = QtWidgets.QWidget(self.page_2)
        self.widget_5.setStyleSheet("border-radius:10px;border:2px solid rgb(0, 150, 255);")
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout_8.setContentsMargins(12, -1, -1, -1)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_8 = QtWidgets.QLabel(self.widget_5)
        self.label_8.setStyleSheet("border-style:none;color:rgb(0, 150, 255);")
        self.label_8.setObjectName("label_8")
        self.gridLayout_8.addWidget(self.label_8, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.widget_5, 3, 0, 1, 2)
        spacerItem9 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem9, 4, 0, 1, 2)
        self.stackedWidget_mos_right.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setStyleSheet("QComboBox {\n"
"    border: 2px solid rgb(235, 235, 235); /* border: 宽度 线类型 颜色 */\n"
"    border-radius: 3px;\n"
"    height:25px;\n"
"    font-size: 14px;\n"
"    background-color: rgba(0, 150, 255, 77);\n"
"    border-radius:10px;\n"
"}\n"
"/*QComboBox::down-arrow\n"
"是 右面那个 \n"
"*/")
        self.page_3.setObjectName("page_3")
        self.gridLayout = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_2 = QtWidgets.QComboBox(self.page_3)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 2, 1)
        self.line_3 = QtWidgets.QFrame(self.page_3)
        self.line_3.setStyleSheet("color:rgb(214, 214, 214)")
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setMidLineWidth(1)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 3, 0, 1, 2)
        spacerItem10 = QtWidgets.QSpacerItem(832, 13, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 0, 0, 1, 2)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.page_3)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setStyleSheet("QAbstractItemView::item {\n"
"    min-height: 110px;\n"
"    min-width: 40px; \n"
"}")
        self.page_9.setObjectName("page_9")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.page_9)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.treeWidget = QtWidgets.QTreeWidget(self.page_9)
        self.treeWidget.setStyleSheet("")
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setUniformRowHeights(False)
        self.treeWidget.setObjectName("treeWidget")
        self.gridLayout_9.addWidget(self.treeWidget, 0, 0, 1, 1)
        self.stackedWidget_2.addWidget(self.page_9)
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.pushButton_5 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 50, 113, 32))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_11 = QtWidgets.QLabel(self.page_10)
        self.label_11.setGeometry(QtCore.QRect(200, 70, 171, 16))
        self.label_11.setObjectName("label_11")
        self.comboBox_3 = QtWidgets.QComboBox(self.page_10)
        self.comboBox_3.setGeometry(QtCore.QRect(410, 50, 91, 32))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4 = QtWidgets.QComboBox(self.page_10)
        self.comboBox_4.setGeometry(QtCore.QRect(450, 180, 91, 32))
        self.comboBox_4.setObjectName("comboBox_4")
        self.label_19 = QtWidgets.QLabel(self.page_10)
        self.label_19.setGeometry(QtCore.QRect(240, 200, 171, 16))
        self.label_19.setObjectName("label_19")
        self.pushButton_6 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_6.setGeometry(QtCore.QRect(80, 180, 113, 32))
        self.pushButton_6.setObjectName("pushButton_6")
        self.comboBox_5 = QtWidgets.QComboBox(self.page_10)
        self.comboBox_5.setGeometry(QtCore.QRect(440, 280, 91, 32))
        self.comboBox_5.setObjectName("comboBox_5")
        self.label_20 = QtWidgets.QLabel(self.page_10)
        self.label_20.setGeometry(QtCore.QRect(230, 300, 171, 16))
        self.label_20.setObjectName("label_20")
        self.pushButton_7 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_7.setGeometry(QtCore.QRect(70, 280, 113, 32))
        self.pushButton_7.setObjectName("pushButton_7")
        self.comboBox_6 = QtWidgets.QComboBox(self.page_10)
        self.comboBox_6.setGeometry(QtCore.QRect(460, 360, 91, 32))
        self.comboBox_6.setObjectName("comboBox_6")
        self.label_21 = QtWidgets.QLabel(self.page_10)
        self.label_21.setGeometry(QtCore.QRect(250, 380, 171, 16))
        self.label_21.setObjectName("label_21")
        self.pushButton_8 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_8.setGeometry(QtCore.QRect(90, 360, 113, 32))
        self.pushButton_8.setObjectName("pushButton_8")
        self.stackedWidget_2.addWidget(self.page_10)
        self.gridLayout.addWidget(self.stackedWidget_2, 4, 0, 1, 2)
        self.label_10 = QtWidgets.QLabel(self.page_3)
        self.label_10.setStyleSheet("border-style:none;color:rgb(33, 33, 33);font-size: 17px;background-color: rgba(255, 255, 255, 0);")
        self.label_10.setIndent(10)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 0, 2, 1)
        self.stackedWidget_mos_right.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem11 = QtWidgets.QSpacerItem(832, 13, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem11, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.page_4)
        self.label_12.setStyleSheet("border-style:none;color:rgb(33, 33, 33);font-size: 17px;background-color: rgba(255, 255, 255, 0);")
        self.label_12.setIndent(10)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 1, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.page_4)
        self.line_4.setStyleSheet("color:rgb(214, 214, 214)")
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setMidLineWidth(1)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.gridLayout_3.addWidget(self.line_4, 2, 0, 1, 1)
        self.widget_8 = QtWidgets.QWidget(self.page_4)
        self.widget_8.setStyleSheet("border-radius:10px;\n"
"border:2px solid rgb(0, 150, 255);")
        self.widget_8.setObjectName("widget_8")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.widget_8)
        self.gridLayout_10.setContentsMargins(12, -1, -1, -1)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_13 = QtWidgets.QLabel(self.widget_8)
        self.label_13.setStyleSheet("border-style:none;color:rgb(0, 150, 255);")
        self.label_13.setObjectName("label_13")
        self.gridLayout_10.addWidget(self.label_13, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.widget_8, 3, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(832, 393, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem12, 4, 0, 1, 1)
        self.stackedWidget_mos_right.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setStyleSheet("QComboBox {\n"
"    border: 2px solid rgb(235, 235, 235); /* border: 宽度 线类型 颜色 */\n"
"    border-radius: 3px;\n"
"    height:25px;\n"
"    font-size: 14px;\n"
"    background-color: rgba(0, 150, 255, 77);\n"
"    border-radius:10px;\n"
"}\n"
"/*QComboBox::down-arrow\n"
"是 右面那个 \n"
"*/")
        self.page_5.setObjectName("page_5")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.comboBox = QtWidgets.QComboBox(self.page_5)
        self.comboBox.setStyleSheet("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_15.addWidget(self.comboBox, 1, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(832, 13, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_15.addItem(spacerItem13, 0, 0, 1, 2)
        self.line_5 = QtWidgets.QFrame(self.page_5)
        self.line_5.setStyleSheet("color:rgb(214, 214, 214)")
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setMidLineWidth(1)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setObjectName("line_5")
        self.gridLayout_15.addWidget(self.line_5, 3, 0, 2, 2)
        self.label_15 = QtWidgets.QLabel(self.page_5)
        self.label_15.setStyleSheet("border-style:none;color:rgb(33, 33, 33);font-size: 17px;background-color: rgba(255, 255, 255, 0);")
        self.label_15.setIndent(10)
        self.label_15.setObjectName("label_15")
        self.gridLayout_15.addWidget(self.label_15, 1, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.page_5)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.scrollArea = QtWidgets.QScrollArea(self.page)
        self.scrollArea.setStyleSheet("border-style:none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 832, 456))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_23.setContentsMargins(5, 0, 5, 0)
        self.gridLayout_23.setObjectName("gridLayout_23")
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_23.addItem(spacerItem14, 6, 0, 1, 2)
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.widget.setStyleSheet("QWidget{background-color: rgba(255, 255, 255, 0);}\n"
"QComboBox {\n"
"    border: 2px solid rgb(235, 235, 235); /* border: 宽度 线类型 颜色 */\n"
"    border-radius: 3px;\n"
"    height:25px;\n"
"    font-size: 14px;\n"
"    background-color: rgba(0, 150, 255, 77);\n"
"    border-radius:10px;\n"
"}\n"
"/*QComboBox::down-arrow\n"
"是 右面那个 \n"
"*/")
        self.widget.setObjectName("widget")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.line_10 = QtWidgets.QFrame(self.widget)
        self.line_10.setStyleSheet("background-color: rgb(169, 169, 169);border:none;")
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout_24.addWidget(self.line_10, 1, 0, 1, 2)
        self.fontComboBox = QtWidgets.QFontComboBox(self.widget)
        self.fontComboBox.setObjectName("fontComboBox")
        self.gridLayout_24.addWidget(self.fontComboBox, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_24.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setStyleSheet("font-size: 14px;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_24.addWidget(self.label_4, 2, 0, 1, 1)
        self.gridLayout_23.addWidget(self.widget, 3, 0, 1, 2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_11.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.page_7)
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.page_7)
        self.scrollArea_2.setStyleSheet("border-style:none;")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_22.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_7)
        self.gridLayout_15.addWidget(self.stackedWidget, 5, 0, 1, 2)
        self.stackedWidget_mos_right.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.page_6)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        spacerItem15 = QtWidgets.QSpacerItem(832, 13, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem15, 0, 0, 1, 2)
        self.label_17 = QtWidgets.QLabel(self.page_6)
        self.label_17.setStyleSheet("border-style:none;color:rgb(33, 33, 33);font-size: 17px;background-color: rgba(255, 255, 255, 0);")
        self.label_17.setIndent(10)
        self.label_17.setObjectName("label_17")
        self.gridLayout_14.addWidget(self.label_17, 1, 0, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.page_6)
        self.line_6.setStyleSheet("color:rgb(214, 214, 214)")
        self.line_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_6.setMidLineWidth(1)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setObjectName("line_6")
        self.gridLayout_14.addWidget(self.line_6, 2, 0, 1, 2)
        self.widget_10 = QtWidgets.QWidget(self.page_6)
        self.widget_10.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.widget_10.setObjectName("widget_10")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.widget_10)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.widget_13 = QtWidgets.QWidget(self.widget_10)
        self.widget_13.setStyleSheet("border-radius:15px;border:2px solid rgba(0, 150, 255, 128);")
        self.widget_13.setObjectName("widget_13")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_13)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.widget_13)
        self.label.setStyleSheet("border-style:none;")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.widget_11 = QtWidgets.QWidget(self.widget_13)
        self.widget_11.setStyleSheet("border-style:none;background-color: rgb(235, 235, 235);border-radius:15px;")
        self.widget_11.setObjectName("widget_11")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.widget_11)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.pushButton = QtWidgets.QPushButton(self.widget_11)
        self.pushButton.setStyleSheet("border-style:none;")
        self.pushButton.setText("")
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_12.addWidget(self.pushButton, 1, 0, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(34, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem16, 1, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.widget_11)
        self.label_16.setStyleSheet("border-style:none;")
        self.label_16.setObjectName("label_16")
        self.gridLayout_12.addWidget(self.label_16, 1, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.widget_11)
        self.widget_12 = QtWidgets.QWidget(self.widget_13)
        self.widget_12.setStyleSheet("border-style:none;background-color: rgb(235, 235, 235);border-radius:15px;")
        self.widget_12.setObjectName("widget_12")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.widget_12)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.label_18 = QtWidgets.QLabel(self.widget_12)
        self.label_18.setStyleSheet("border-style:none;")
        self.label_18.setObjectName("label_18")
        self.gridLayout_17.addWidget(self.label_18, 0, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_12)
        self.pushButton_4.setStyleSheet("border-style:none;")
        self.pushButton_4.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(MOS_catalogue_picture_david_png), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon7)
        self.pushButton_4.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_17.addWidget(self.pushButton_4, 0, 0, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(34, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_17.addItem(spacerItem17, 0, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.widget_12)
        self.widget_14 = QtWidgets.QWidget(self.widget_13)
        self.widget_14.setStyleSheet("border-style:none;background-color: rgb(235, 235, 235);border-radius:15px;")
        self.widget_14.setObjectName("widget_14")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.widget_14)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.label_22 = QtWidgets.QLabel(self.widget_14)
        self.label_22.setStyleSheet("border-style:none;")
        self.label_22.setObjectName("label_22")
        self.gridLayout_18.addWidget(self.label_22, 0, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget_14)
        self.pushButton_9.setStyleSheet("border-style:none;")
        self.pushButton_9.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(MOS_catalogue_picture_heimnad_png), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon8)
        self.pushButton_9.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_18.addWidget(self.pushButton_9, 0, 0, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(34, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_18.addItem(spacerItem18, 0, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.widget_14)
        self.gridLayout_19.addWidget(self.widget_13, 0, 0, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(796, 368, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_19.addItem(spacerItem19, 1, 0, 1, 1)
        self.gridLayout_14.addWidget(self.widget_10, 3, 0, 1, 2)
        self.stackedWidget_mos_right.addWidget(self.page_6)
        self.horizontalLayout_2.addWidget(self.stackedWidget_mos_right)
        MOS.setCentralWidget(self.centralwidget)

        self.retranslateUi(MOS)
        self.stackedWidget_mos_right.setCurrentIndex(0)
        self.stackedWidget_gonggao.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MOS)


        # =============================================================================#
        self.progressBar_2.setMinimum(0)
        self.progressBar_2.setMaximum(99)
        self.progressBar_2.setValue(0)
        self.stackedWidget_mos_right.setCurrentIndex(0)
        # 启动线程
        self.a = MOS_file()
        self.a.sinOut.connect(self.MOS_file_return)
        self.a.start()
        # =============================================================================#

    # =================================分割线===================================#

    def click_pushButton_home(self):
        self.stackedWidget_mos_right.setCurrentIndex(0)
        pushButton_home_true = ("QWidget\n"
                                "{\n"
                                "    background-color: rgba(231, 230, 228,100);\n"
                                "    border-bottom-left-radius:15px;\n"
                                "    border-top-left-radius:15px;\n"
                                "}\n"
                                "#pushButton_about\n"
                                "{\n"
                                "    color: blue;\n"
                                "    height:35px;\n"
                                "    color: rgb(0, 150, 255);\n"
                                "    background-position: left;\n"
                                "    text-align: left;\n"
                                "    padding-right:10px;\n"
                                "    padding-left:3px;\n"
                                "    font-size: 15px;\n"
                                "    border-style:none;\n"
                                "    border-radius:8px;\n"
                                "    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
                                "}\n"
                                "#pushButton_about::hover\n"
                                "{\n"
                                "    background-color: rgb(192, 192, 192);\n"
                                "}\n"
                                "#pushButton_about::pressed\n"
                                "{\n"
                                "    border:2px solid rgb(0, 150, 255);\n"
                                "}\n"
                                "\n"
                                "\n"
                                "#pushButton_xiazai\n"
                                "{\n"
                                "    color: blue;\n"
                                "    height:35px;\n"
                                "    color: rgb(0, 150, 255);\n"
                                "    background-position: left;\n"
                                "    text-align: left;\n"
                                "    padding-right:10px;\n"
                                "    padding-left:3px;\n"
                                "    font-size: 15px;\n"
                                "    border-style:none;\n"
                                "    border-radius:8px;\n"
                                "    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
                                "}\n"
                                "#pushButton_xiazai::hover\n"
                                "{\n"
                                "    background-color: rgb(192, 192, 192);\n"
                                "}\n"
                                "#pushButton_xiazai::pressed\n"
                                "{\n"
                                "    border:2px solid rgb(0, 150, 255);\n"
                                "}\n"
                                "\n"
                                "\n"
                                "#pushButton_shezhi\n"
                                "{\n"
                                "    color: blue;\n"
                                "    height:35px;\n"
                                "    color: rgb(0, 150, 255);\n"
                                "    background-position: left;\n"
                                "    text-align: left;\n"
                                "    padding-right:10px;\n"
                                "    padding-left:3px;\n"
                                "    font-size: 15px;\n"
                                "    border-style:none;\n"
                                "    border-radius:8px;\n"
                                "    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
                                "}\n"
                                "#pushButton_shezhi::hover\n"
                                "{\n"
                                "    background-color: rgb(192, 192, 192);\n"
                                "}\n"
                                "#pushButton_shezhi::pressed\n"
                                "{\n"
                                "    border:2px solid rgb(0, 150, 255);\n"
                                "}\n"
                                "\n"
                                "\n"
                                "#pushButton_music\n"
                                "{\n"
                                "    color: blue;\n"
                                "    height:35px;\n"
                                "    color: rgb(0, 150, 255);\n"
                                "    background-position: left;\n"
                                "    text-align: left;\n"
                                "    padding-right:10px;\n"
                                "    padding-left:3px;\n"
                                "    font-size: 15px;\n"
                                "    border-style:none;\n"
                                "    border-radius:8px;\n"
                                "    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
                                "}\n"
                                "#pushButton_music::hover\n"
                                "{\n"
                                "    background-color: rgb(192, 192, 192);\n"
                                "}\n"
                                "#pushButton_music::pressed\n"
                                "{\n"
                                "    border:2px solid rgb(0, 150, 255);\n"
                                "}\n"
                                "\n"
                                "\n"
                                "#pushButton_lianji\n"
                                "{\n"
                                "    color: blue;\n"
                                "    height:35px;\n"
                                "    color: rgb(0, 150, 255);\n"
                                "    background-position: left;\n"
                                "    text-align: left;\n"
                                "    padding-right:10px;\n"
                                "    padding-left:3px;\n"
                                "    font-size: 15px;\n"
                                "    border-style:none;\n"
                                "    border-radius:8px;\n"
                                "    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
                                "}\n"
                                "#pushButton_lianji::hover\n"
                                "{\n"
                                "    background-color: rgb(192, 192, 192);\n"
                                "}\n"
                                "#pushButton_lianji::pressed\n"
                                "{\n"
                                "    border:2px solid rgb(0, 150, 255);\n"
                                "}\n"
                                "\n"
                                "\n"
                                "#pushButton_home\n"
                                "{\n"
                                "    color: blue;\n"
                                "    height:35px;\n"
                                "    color: rgb(0, 150, 255);\n"
                                "    background-position: left;\n"
                                "    text-align: left;\n"
                                "    padding-right:10px;\n"
                                "    padding-left:3px;\n"
                                "    font-size: 15px;\n"
                                "    border-style:none;\n"
                                "    border-radius:8px;\n"
                                "    border:2px solid rgb(229, 228, 226);background-color: rgb(192, 192, 192);\n"
                                "}\n"
                                "#pushButton_home::hover\n"
                                "{\n"
                                "    background-color: rgb(192, 192, 192);\n"
                                "}\n"
                                "#pushButton_home::pressed\n"
                                "{\n"
                                "    border:2px solid rgb(0, 150, 255);\n"
                                "}")
        self.widget_mos_left.setStyleSheet(pushButton_home_true)

    def click_pushButton_lianji(self):
        self.stackedWidget_mos_right.setCurrentIndex(1)
        pushButton_lianji_true = ("QWidget\n"
                                  "{\n"
                                  "    background-color: rgba(231, 230, 228,100);\n"
                                  "    border-bottom-left-radius:15px;\n"
                                  "    border-top-left-radius:15px;\n"
                                  "}\n"
                                  "#pushButton_about\n"
                                  "{\n"
                                  "    color: blue;\n"
                                  "    height:35px;\n"
                                  "    color: rgb(0, 150, 255);\n"
                                  "    background-position: left;\n"
                                  "    text-align: left;\n"
                                  "    padding-right:10px;\n"
                                  "    padding-left:3px;\n"
                                  "    font-size: 15px;\n"
                                  "    border-style:none;\n"
                                  "    border-radius:8px;\n"
                                  "    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
                                  "}\n"
                                  "#pushButton_about::hover\n"
                                  "{\n"
                                  "    background-color: rgb(192, 192, 192);\n"
                                  "}\n"
                                  "#pushButton_about::pressed\n"
                                  "{\n"
                                  "    border:2px solid rgb(0, 150, 255);\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "#pushButton_xiazai\n"
                                  "{\n"
                                  "    color: blue;\n"
                                  "    height:35px;\n"
                                  "    color: rgb(0, 150, 255);\n"
                                  "    background-position: left;\n"
                                  "    text-align: left;\n"
                                  "    padding-right:10px;\n"
                                  "    padding-left:3px;\n"
                                  "    font-size: 15px;\n"
                                  "    border-style:none;\n"
                                  "    border-radius:8px;\n"
                                  "    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192, 0);\n"
                                  "}\n"
                                  "#pushButton_xiazai::hover\n"
                                  "{\n"
                                  "    background-color: rgb(192, 192, 192);\n"
                                  "}\n"
                                  "#pushButton_xiazai::pressed\n"
                                  "{\n"
                                  "    border:2px solid rgb(0, 150, 255);\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "#pushButton_shezhi\n"
                                  "{\n"
                                  "    color: blue;\n"
                                  "    height:35px;\n"
                                  "    color: rgb(0, 150, 255);\n"
                                  "    background-position: left;\n"
                                  "    text-align: left;\n"
                                  "    padding-right:10px;\n"
                                  "    padding-left:3px;\n"
                                  "    font-size: 15px;\n"
                                  "    border-style:none;\n"
                                  "    border-radius:8px;\n"
                                  "    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
                                  "}\n"
                                  "#pushButton_shezhi::hover\n"
                                  "{\n"
                                  "    background-color: rgb(192, 192, 192);\n"
                                  "}\n"
                                  "#pushButton_shezhi::pressed\n"
                                  "{\n"
                                  "    border:2px solid rgb(0, 150, 255);\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "#pushButton_music\n"
                                  "{\n"
                                  "    color: blue;\n"
                                  "    height:35px;\n"
                                  "    color: rgb(0, 150, 255);\n"
                                  "    background-position: left;\n"
                                  "    text-align: left;\n"
                                  "    padding-right:10px;\n"
                                  "    padding-left:3px;\n"
                                  "    font-size: 15px;\n"
                                  "    border-style:none;\n"
                                  "    border-radius:8px;\n"
                                  "    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
                                  "}\n"
                                  "#pushButton_music::hover\n"
                                  "{\n"
                                  "    background-color: rgb(192, 192, 192);\n"
                                  "}\n"
                                  "#pushButton_music::pressed\n"
                                  "{\n"
                                  "    border:2px solid rgb(0, 150, 255);\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "#pushButton_lianji\n"
                                  "{\n"
                                  "    color: blue;\n"
                                  "    height:35px;\n"
                                  "    color: rgb(0, 150, 255);\n"
                                  "    background-position: left;\n"
                                  "    text-align: left;\n"
                                  "    padding-right:10px;\n"
                                  "    padding-left:3px;\n"
                                  "    font-size: 15px;\n"
                                  "    border-style:none;\n"
                                  "    border-radius:8px;\n"
                                  "    border:2px solid rgb(229, 228, 226);background-color: rgb(192, 192, 192);\n"
                                  "}\n"
                                  "#pushButton_lianji::hover\n"
                                  "{\n"
                                  "    background-color: rgb(192, 192, 192);\n"
                                  "}\n"
                                  "#pushButton_lianji::pressed\n"
                                  "{\n"
                                  "    border:2px solid rgb(0, 150, 255);\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "#pushButton_home\n"
                                  "{\n"
                                  "    color: blue;\n"
                                  "    height:35px;\n"
                                  "    color: rgb(0, 150, 255);\n"
                                  "    background-position: left;\n"
                                  "    text-align: left;\n"
                                  "    padding-right:10px;\n"
                                  "    padding-left:3px;\n"
                                  "    font-size: 15px;\n"
                                  "    border-style:none;\n"
                                  "    border-radius:8px;\n"
                                  "    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192 ,0);\n"
                                  "}\n"
                                  "#pushButton_home::hover\n"
                                  "{\n"
                                  "    background-color: rgb(192, 192, 192);\n"
                                  "}\n"
                                  "#pushButton_home::pressed\n"
                                  "{\n"
                                  "    border:2px solid rgb(0, 150, 255);\n"
                                  "}")
        self.widget_mos_left.setStyleSheet(pushButton_lianji_true)

    def click_pushButton_xiazai(self):
        self.stackedWidget_mos_right.setCurrentIndex(2)
        pushButton_xiazai_true = ("QWidget\n"
                                  "{\n"
                                  "    background-color: rgba(231, 230, 228,100);\n"
                                  "    border-bottom-left-radius:15px;\n"
                                  "    border-top-left-radius:15px;\n"
                                  "}\n"
                                  "#pushButton_about\n"
                                  "{\n"
                                  "    color: blue;\n"
                                  "    height:35px;\n"
                                  "    color: rgb(0, 150, 255);\n"
                                  "    background-position: left;\n"
                                  "    text-align: left;\n"
                                  "    padding-right:10px;\n"
                                  "    padding-left:3px;\n"
                                  "    font-size: 15px;\n"
                                  "    border-style:none;\n"
                                  "    border-radius:8px;\n"
                                  "    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
                                  "}\n"
                                  "#pushButton_about::hover\n"
                                  "{\n"
                                  "    background-color: rgb(192, 192, 192);\n"
                                  "}\n"
                                  "#pushButton_about::pressed\n"
                                  "{\n"
                                  "    border:2px solid rgb(0, 150, 255);\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "#pushButton_xiazai\n"
                                  "{\n"
                                  "    color: blue;\n"
                                  "    height:35px;\n"
                                  "    color: rgb(0, 150, 255);\n"
                                  "    background-position: left;\n"
                                  "    text-align: left;\n"
                                  "    padding-right:10px;\n"
                                  "    padding-left:3px;\n"
                                  "    font-size: 15px;\n"
                                  "    border-style:none;\n"
                                  "    border-radius:8px;\n"
                                  "    border:2px solid rgb(229, 228, 226);background-color: rgb(192, 192, 192);\n"
                                  "}\n"
                                  "#pushButton_xiazai::hover\n"
                                  "{\n"
                                  "    background-color: rgb(192, 192, 192);\n"
                                  "}\n"
                                  "#pushButton_xiazai::pressed\n"
                                  "{\n"
                                  "    border:2px solid rgb(0, 150, 255);\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "#pushButton_shezhi\n"
                                  "{\n"
                                  "    color: blue;\n"
                                  "    height:35px;\n"
                                  "    color: rgb(0, 150, 255);\n"
                                  "    background-position: left;\n"
                                  "    text-align: left;\n"
                                  "    padding-right:10px;\n"
                                  "    padding-left:3px;\n"
                                  "    font-size: 15px;\n"
                                  "    border-style:none;\n"
                                  "    border-radius:8px;\n"
                                  "    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
                                  "}\n"
                                  "#pushButton_shezhi::hover\n"
                                  "{\n"
                                  "    background-color: rgb(192, 192, 192);\n"
                                  "}\n"
                                  "#pushButton_shezhi::pressed\n"
                                  "{\n"
                                  "    border:2px solid rgb(0, 150, 255);\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "#pushButton_music\n"
                                  "{\n"
                                  "    color: blue;\n"
                                  "    height:35px;\n"
                                  "    color: rgb(0, 150, 255);\n"
                                  "    background-position: left;\n"
                                  "    text-align: left;\n"
                                  "    padding-right:10px;\n"
                                  "    padding-left:3px;\n"
                                  "    font-size: 15px;\n"
                                  "    border-style:none;\n"
                                  "    border-radius:8px;\n"
                                  "    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
                                  "}\n"
                                  "#pushButton_music::hover\n"
                                  "{\n"
                                  "    background-color: rgb(192, 192, 192);\n"
                                  "}\n"
                                  "#pushButton_music::pressed\n"
                                  "{\n"
                                  "    border:2px solid rgb(0, 150, 255);\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "#pushButton_lianji\n"
                                  "{\n"
                                  "    color: blue;\n"
                                  "    height:35px;\n"
                                  "    color: rgb(0, 150, 255);\n"
                                  "    background-position: left;\n"
                                  "    text-align: left;\n"
                                  "    padding-right:10px;\n"
                                  "    padding-left:3px;\n"
                                  "    font-size: 15px;\n"
                                  "    border-style:none;\n"
                                  "    border-radius:8px;\n"
                                  "    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
                                  "}\n"
                                  "#pushButton_lianji::hover\n"
                                  "{\n"
                                  "    background-color: rgb(192, 192, 192);\n"
                                  "}\n"
                                  "#pushButton_lianji::pressed\n"
                                  "{\n"
                                  "    border:2px solid rgb(0, 150, 255);\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "#pushButton_home\n"
                                  "{\n"
                                  "    color: blue;\n"
                                  "    height:35px;\n"
                                  "    color: rgb(0, 150, 255);\n"
                                  "    background-position: left;\n"
                                  "    text-align: left;\n"
                                  "    padding-right:10px;\n"
                                  "    padding-left:3px;\n"
                                  "    font-size: 15px;\n"
                                  "    border-style:none;\n"
                                  "    border-radius:8px;\n"
                                  "    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192 ,0);\n"
                                  "}\n"
                                  "#pushButton_home::hover\n"
                                  "{\n"
                                  "    background-color: rgb(192, 192, 192);\n"
                                  "}\n"
                                  "#pushButton_home::pressed\n"
                                  "{\n"
                                  "    border:2px solid rgb(0, 150, 255);\n"
                                  "}")
        self.widget_mos_left.setStyleSheet(pushButton_xiazai_true)

    def click_pushButton_music(self):
        self.stackedWidget_mos_right.setCurrentIndex(3)
        pushButton_music_true = ("QWidget\n"
                                 "{\n"
                                 "    background-color: rgba(231, 230, 228,100);\n"
                                 "    border-bottom-left-radius:15px;\n"
                                 "    border-top-left-radius:15px;\n"
                                 "}\n"
                                 "#pushButton_about\n"
                                 "{\n"
                                 "    color: blue;\n"
                                 "    height:35px;\n"
                                 "    color: rgb(0, 150, 255);\n"
                                 "    background-position: left;\n"
                                 "    text-align: left;\n"
                                 "    padding-right:10px;\n"
                                 "    padding-left:3px;\n"
                                 "    font-size: 15px;\n"
                                 "    border-style:none;\n"
                                 "    border-radius:8px;\n"
                                 "    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
                                 "}\n"
                                 "#pushButton_about::hover\n"
                                 "{\n"
                                 "    background-color: rgb(192, 192, 192);\n"
                                 "}\n"
                                 "#pushButton_about::pressed\n"
                                 "{\n"
                                 "    border:2px solid rgb(0, 150, 255);\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "#pushButton_xiazai\n"
                                 "{\n"
                                 "    color: blue;\n"
                                 "    height:35px;\n"
                                 "    color: rgb(0, 150, 255);\n"
                                 "    background-position: left;\n"
                                 "    text-align: left;\n"
                                 "    padding-right:10px;\n"
                                 "    padding-left:3px;\n"
                                 "    font-size: 15px;\n"
                                 "    border-style:none;\n"
                                 "    border-radius:8px;\n"
                                 "    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192, 0);\n"
                                 "}\n"
                                 "#pushButton_xiazai::hover\n"
                                 "{\n"
                                 "    background-color: rgb(192, 192, 192);\n"
                                 "}\n"
                                 "#pushButton_xiazai::pressed\n"
                                 "{\n"
                                 "    border:2px solid rgb(0, 150, 255);\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "#pushButton_shezhi\n"
                                 "{\n"
                                 "    color: blue;\n"
                                 "    height:35px;\n"
                                 "    color: rgb(0, 150, 255);\n"
                                 "    background-position: left;\n"
                                 "    text-align: left;\n"
                                 "    padding-right:10px;\n"
                                 "    padding-left:3px;\n"
                                 "    font-size: 15px;\n"
                                 "    border-style:none;\n"
                                 "    border-radius:8px;\n"
                                 "    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
                                 "}\n"
                                 "#pushButton_shezhi::hover\n"
                                 "{\n"
                                 "    background-color: rgb(192, 192, 192);\n"
                                 "}\n"
                                 "#pushButton_shezhi::pressed\n"
                                 "{\n"
                                 "    border:2px solid rgb(0, 150, 255);\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "#pushButton_music\n"
                                 "{\n"
                                 "    color: blue;\n"
                                 "    height:35px;\n"
                                 "    color: rgb(0, 150, 255);\n"
                                 "    background-position: left;\n"
                                 "    text-align: left;\n"
                                 "    padding-right:10px;\n"
                                 "    padding-left:3px;\n"
                                 "    font-size: 15px;\n"
                                 "    border-style:none;\n"
                                 "    border-radius:8px;\n"
                                 "    border:2px solid rgb(229, 228, 226);background-color: rgb(192, 192, 192);\n"
                                 "}\n"
                                 "#pushButton_music::hover\n"
                                 "{\n"
                                 "    background-color: rgb(192, 192, 192);\n"
                                 "}\n"
                                 "#pushButton_music::pressed\n"
                                 "{\n"
                                 "    border:2px solid rgb(0, 150, 255);\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "#pushButton_lianji\n"
                                 "{\n"
                                 "    color: blue;\n"
                                 "    height:35px;\n"
                                 "    color: rgb(0, 150, 255);\n"
                                 "    background-position: left;\n"
                                 "    text-align: left;\n"
                                 "    padding-right:10px;\n"
                                 "    padding-left:3px;\n"
                                 "    font-size: 15px;\n"
                                 "    border-style:none;\n"
                                 "    border-radius:8px;\n"
                                 "    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
                                 "}\n"
                                 "#pushButton_lianji::hover\n"
                                 "{\n"
                                 "    background-color: rgb(192, 192, 192);\n"
                                 "}\n"
                                 "#pushButton_lianji::pressed\n"
                                 "{\n"
                                 "    border:2px solid rgb(0, 150, 255);\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "#pushButton_home\n"
                                 "{\n"
                                 "    color: blue;\n"
                                 "    height:35px;\n"
                                 "    color: rgb(0, 150, 255);\n"
                                 "    background-position: left;\n"
                                 "    text-align: left;\n"
                                 "    padding-right:10px;\n"
                                 "    padding-left:3px;\n"
                                 "    font-size: 15px;\n"
                                 "    border-style:none;\n"
                                 "    border-radius:8px;\n"
                                 "    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192 ,0);\n"
                                 "}\n"
                                 "#pushButton_home::hover\n"
                                 "{\n"
                                 "    background-color: rgb(192, 192, 192);\n"
                                 "}\n"
                                 "#pushButton_home::pressed\n"
                                 "{\n"
                                 "    border:2px solid rgb(0, 150, 255);\n"
                                 "}")
        self.widget_mos_left.setStyleSheet(pushButton_music_true)

    def click_pushButton_shezhi(self):
        self.stackedWidget_mos_right.setCurrentIndex(4)
        pushButton_shezhi_true = ("QWidget\n"
                                  "{\n"
                                  "    background-color: rgba(231, 230, 228,100);\n"
                                  "    border-bottom-left-radius:15px;\n"
                                  "    border-top-left-radius:15px;\n"
                                  "}\n"
                                  "#pushButton_about\n"
                                  "{\n"
                                  "    color: blue;\n"
                                  "    height:35px;\n"
                                  "    color: rgb(0, 150, 255);\n"
                                  "    background-position: left;\n"
                                  "    text-align: left;\n"
                                  "    padding-right:10px;\n"
                                  "    padding-left:3px;\n"
                                  "    font-size: 15px;\n"
                                  "    border-style:none;\n"
                                  "    border-radius:8px;\n"
                                  "    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
                                  "}\n"
                                  "#pushButton_about::hover\n"
                                  "{\n"
                                  "    background-color: rgb(192, 192, 192);\n"
                                  "}\n"
                                  "#pushButton_about::pressed\n"
                                  "{\n"
                                  "    border:2px solid rgb(0, 150, 255);\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "#pushButton_xiazai\n"
                                  "{\n"
                                  "    color: blue;\n"
                                  "    height:35px;\n"
                                  "    color: rgb(0, 150, 255);\n"
                                  "    background-position: left;\n"
                                  "    text-align: left;\n"
                                  "    padding-right:10px;\n"
                                  "    padding-left:3px;\n"
                                  "    font-size: 15px;\n"
                                  "    border-style:none;\n"
                                  "    border-radius:8px;\n"
                                  "    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192, 0);\n"
                                  "}\n"
                                  "#pushButton_xiazai::hover\n"
                                  "{\n"
                                  "    background-color: rgb(192, 192, 192);\n"
                                  "}\n"
                                  "#pushButton_xiazai::pressed\n"
                                  "{\n"
                                  "    border:2px solid rgb(0, 150, 255);\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "#pushButton_shezhi\n"
                                  "{\n"
                                  "    color: blue;\n"
                                  "    height:35px;\n"
                                  "    color: rgb(0, 150, 255);\n"
                                  "    background-position: left;\n"
                                  "    text-align: left;\n"
                                  "    padding-right:10px;\n"
                                  "    padding-left:3px;\n"
                                  "    font-size: 15px;\n"
                                  "    border-style:none;\n"
                                  "    border-radius:8px;\n"
                                  "    border:2px solid rgb(229, 228, 226);background-color: rgb(192, 192, 192);\n"
                                  "}\n"
                                  "#pushButton_shezhi::hover\n"
                                  "{\n"
                                  "    background-color: rgb(192, 192, 192);\n"
                                  "}\n"
                                  "#pushButton_shezhi::pressed\n"
                                  "{\n"
                                  "    border:2px solid rgb(0, 150, 255);\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "#pushButton_music\n"
                                  "{\n"
                                  "    color: blue;\n"
                                  "    height:35px;\n"
                                  "    color: rgb(0, 150, 255);\n"
                                  "    background-position: left;\n"
                                  "    text-align: left;\n"
                                  "    padding-right:10px;\n"
                                  "    padding-left:3px;\n"
                                  "    font-size: 15px;\n"
                                  "    border-style:none;\n"
                                  "    border-radius:8px;\n"
                                  "    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
                                  "}\n"
                                  "#pushButton_music::hover\n"
                                  "{\n"
                                  "    background-color: rgb(192, 192, 192);\n"
                                  "}\n"
                                  "#pushButton_music::pressed\n"
                                  "{\n"
                                  "    border:2px solid rgb(0, 150, 255);\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "#pushButton_lianji\n"
                                  "{\n"
                                  "    color: blue;\n"
                                  "    height:35px;\n"
                                  "    color: rgb(0, 150, 255);\n"
                                  "    background-position: left;\n"
                                  "    text-align: left;\n"
                                  "    padding-right:10px;\n"
                                  "    padding-left:3px;\n"
                                  "    font-size: 15px;\n"
                                  "    border-style:none;\n"
                                  "    border-radius:8px;\n"
                                  "    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
                                  "}\n"
                                  "#pushButton_lianji::hover\n"
                                  "{\n"
                                  "    background-color: rgb(192, 192, 192);\n"
                                  "}\n"
                                  "#pushButton_lianji::pressed\n"
                                  "{\n"
                                  "    border:2px solid rgb(0, 150, 255);\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "#pushButton_home\n"
                                  "{\n"
                                  "    color: blue;\n"
                                  "    height:35px;\n"
                                  "    color: rgb(0, 150, 255);\n"
                                  "    background-position: left;\n"
                                  "    text-align: left;\n"
                                  "    padding-right:10px;\n"
                                  "    padding-left:3px;\n"
                                  "    font-size: 15px;\n"
                                  "    border-style:none;\n"
                                  "    border-radius:8px;\n"
                                  "    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192 ,0);\n"
                                  "}\n"
                                  "#pushButton_home::hover\n"
                                  "{\n"
                                  "    background-color: rgb(192, 192, 192);\n"
                                  "}\n"
                                  "#pushButton_home::pressed\n"
                                  "{\n"
                                  "    border:2px solid rgb(0, 150, 255);\n"
                                  "}")
        self.widget_mos_left.setStyleSheet(pushButton_shezhi_true)

    def click_pushButton_about(self):
        self.stackedWidget_mos_right.setCurrentIndex(5)
        pushButton_about_true = ("QWidget\n"
                                 "{\n"
                                 "    background-color: rgba(231, 230, 228,100);\n"
                                 "    border-bottom-left-radius:15px;\n"
                                 "    border-top-left-radius:15px;\n"
                                 "}\n"
                                 "#pushButton_about\n"
                                 "{\n"
                                 "    color: blue;\n"
                                 "    height:35px;\n"
                                 "    color: rgb(0, 150, 255);\n"
                                 "    background-position: left;\n"
                                 "    text-align: left;\n"
                                 "    padding-right:10px;\n"
                                 "    padding-left:3px;\n"
                                 "    font-size: 15px;\n"
                                 "    border-style:none;\n"
                                 "    border-radius:8px;\n"
                                 "    border:2px solid rgb(229, 228, 226);background-color: rgb(192, 192, 192);\n"
                                 "}\n"
                                 "#pushButton_about::hover\n"
                                 "{\n"
                                 "    background-color: rgb(192, 192, 192);\n"
                                 "}\n"
                                 "#pushButton_about::pressed\n"
                                 "{\n"
                                 "    border:2px solid rgb(0, 150, 255);\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "#pushButton_xiazai\n"
                                 "{\n"
                                 "    color: blue;\n"
                                 "    height:35px;\n"
                                 "    color: rgb(0, 150, 255);\n"
                                 "    background-position: left;\n"
                                 "    text-align: left;\n"
                                 "    padding-right:10px;\n"
                                 "    padding-left:3px;\n"
                                 "    font-size: 15px;\n"
                                 "    border-style:none;\n"
                                 "    border-radius:8px;\n"
                                 "    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192, 0);\n"
                                 "}\n"
                                 "#pushButton_xiazai::hover\n"
                                 "{\n"
                                 "    background-color: rgb(192, 192, 192);\n"
                                 "}\n"
                                 "#pushButton_xiazai::pressed\n"
                                 "{\n"
                                 "    border:2px solid rgb(0, 150, 255);\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "#pushButton_shezhi\n"
                                 "{\n"
                                 "    color: blue;\n"
                                 "    height:35px;\n"
                                 "    color: rgb(0, 150, 255);\n"
                                 "    background-position: left;\n"
                                 "    text-align: left;\n"
                                 "    padding-right:10px;\n"
                                 "    padding-left:3px;\n"
                                 "    font-size: 15px;\n"
                                 "    border-style:none;\n"
                                 "    border-radius:8px;\n"
                                 "    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
                                 "}\n"
                                 "#pushButton_shezhi::hover\n"
                                 "{\n"
                                 "    background-color: rgb(192, 192, 192);\n"
                                 "}\n"
                                 "#pushButton_shezhi::pressed\n"
                                 "{\n"
                                 "    border:2px solid rgb(0, 150, 255);\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "#pushButton_music\n"
                                 "{\n"
                                 "    color: blue;\n"
                                 "    height:35px;\n"
                                 "    color: rgb(0, 150, 255);\n"
                                 "    background-position: left;\n"
                                 "    text-align: left;\n"
                                 "    padding-right:10px;\n"
                                 "    padding-left:3px;\n"
                                 "    font-size: 15px;\n"
                                 "    border-style:none;\n"
                                 "    border-radius:8px;\n"
                                 "    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
                                 "}\n"
                                 "#pushButton_music::hover\n"
                                 "{\n"
                                 "    background-color: rgb(192, 192, 192);\n"
                                 "}\n"
                                 "#pushButton_music::pressed\n"
                                 "{\n"
                                 "    border:2px solid rgb(0, 150, 255);\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "#pushButton_lianji\n"
                                 "{\n"
                                 "    color: blue;\n"
                                 "    height:35px;\n"
                                 "    color: rgb(0, 150, 255);\n"
                                 "    background-position: left;\n"
                                 "    text-align: left;\n"
                                 "    padding-right:10px;\n"
                                 "    padding-left:3px;\n"
                                 "    font-size: 15px;\n"
                                 "    border-style:none;\n"
                                 "    border-radius:8px;\n"
                                 "    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192,0);\n"
                                 "}\n"
                                 "#pushButton_lianji::hover\n"
                                 "{\n"
                                 "    background-color: rgb(192, 192, 192);\n"
                                 "}\n"
                                 "#pushButton_lianji::pressed\n"
                                 "{\n"
                                 "    border:2px solid rgb(0, 150, 255);\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "#pushButton_home\n"
                                 "{\n"
                                 "    color: blue;\n"
                                 "    height:35px;\n"
                                 "    color: rgb(0, 150, 255);\n"
                                 "    background-position: left;\n"
                                 "    text-align: left;\n"
                                 "    padding-right:10px;\n"
                                 "    padding-left:3px;\n"
                                 "    font-size: 15px;\n"
                                 "    border-style:none;\n"
                                 "    border-radius:8px;\n"
                                 "    border:2px solid rgb(229, 228, 226);background-color: rgba(192, 192, 192 ,0);\n"
                                 "}\n"
                                 "#pushButton_home::hover\n"
                                 "{\n"
                                 "    background-color: rgb(192, 192, 192);\n"
                                 "}\n"
                                 "#pushButton_home::pressed\n"
                                 "{\n"
                                 "    border:2px solid rgb(0, 150, 255);\n"
                                 "}")
        self.widget_mos_left.setStyleSheet(pushButton_about_true)

    def gonggao(self, str):
        self.textBrowser_gonggao_left_txt.setHtml(str)
        self.progressBar_2.setMinimum(0)
        self.progressBar_2.setMaximum(99)
        self.progressBar_2.setValue(90)
        self.stackedWidget_gonggao.setCurrentIndex(0)

    def gonggao_jindu(self, t):
        t1 = int(t)
        h=self.progressBar_2.value()
        while t1 >= h:
            h += 1
            if h <= t1 :
                self.progressBar_2.setValue(h)
            else:
                break
    


    def gonggao_error(self, str):
        self.stackedWidget_gonggao.setCurrentIndex(1)
        self.label_2.setText("请求出错 错误信息：" + str)
        self.progressBar_2.setMinimum(0)
        self.progressBar_2.setMaximum(99)
        self.progressBar_2.setValue(0)

    def setfont(self):
        print(self.fontComboBox.currentText())
        self.label_4.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.label_6.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.label_mos_left_top_user.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.label_mos_left_top_add.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.label_gonggao_left_txt.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.label_2.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.progressBar_2.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.label__gonggao_right_txt.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.label_3.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.progressBar.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.label_7.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.label_9.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.label_8.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.label_10.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.label_11.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.label_19.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.label_20.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.label_21.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.label_12.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.label_13.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.label_15.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.label_17.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.label.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.label_16.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.label_18.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.label_22.setFont(QtGui.QFont(self.fontComboBox.currentText()))


        self.pushButton_home.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.pushButton_lianji.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.pushButton_music.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.pushButton_shezhi.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.pushButton_xiazai.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.pushButton_about.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.pushButton__gonggao_start.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.pushButton_5.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.pushButton_6.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.pushButton_7.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.pushButton_8.setFont(QtGui.QFont(self.fontComboBox.currentText()))


        self.comboBox_gonggao_right.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.comboBox_2.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.comboBox_3.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.comboBox_4.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.comboBox_5.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.comboBox_6.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.comboBox.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.fontComboBox.setFont(QtGui.QFont(self.fontComboBox.currentText()))


        self.progressBar.setFont(QtGui.QFont(self.fontComboBox.currentText()))


        
        



    def MOS_file_return(self, str):
        if str == "OK!":
            self.g = gonggao()
            self.g.sinOut_gonggao_ok.connect(self.gonggao)
            self.g.sinOut_gonggao_jindu.connect(self.gonggao_jindu)
            self.g.sinOut_gonggao_error.connect(self.gonggao_error)
            self.g.start()
        elif str == "ERROR_PermissionError" :
            a = QMessageBox.critical(None,"错误","初始化程序失败！请检查当前目录下是否有读写权限。即将退出程序", QMessageBox.Ok)
            if a==QMessageBox.Ok: #检查是否点了OK按钮
                quit()
    
    
    # =================================分割线===================================#


    def retranslateUi(self, MOS):
        _translate = QtCore.QCoreApplication.translate
        MOS.setWindowTitle(_translate("MOS", "MainWindow"))
        self.label_mos_left_top_add.setText(_translate("MOS", "点击添加"))
        self.label_mos_left_top_user.setText(_translate("MOS", "无用户"))
        self.pushButton_home.setText(_translate("MOS", "Home"))
        self.pushButton_lianji.setText(_translate("MOS", "联机"))
        self.pushButton_xiazai.setText(_translate("MOS", "下载"))
        self.pushButton_music.setText(_translate("MOS", "音乐"))
        self.pushButton_shezhi.setText(_translate("MOS", "设置"))
        self.pushButton_about.setText(_translate("MOS", "关于"))
        self.label_mosll.setText(_translate("MOS", "MOS II"))
        self.label_3.setText(_translate("MOS", "启动的图片"))
        self.label_7.setText(_translate("MOS", "启动君：待命中……"))
        self.label__gonggao_right_txt.setText(_translate("MOS", "<html><head/><body><p>启动游戏 <span style=\" color:#0096ff;\">•等待启动</span></p></body></html>"))
        self.pushButton__gonggao_start.setText(_translate("MOS", "启动游戏"))
        self.label_gonggao_left_txt.setText(_translate("MOS", "<html><head/><body><p>官方公告 <span style=\" color:#55f976;\">•正在加载中</span></p></body></html>"))
        self.label_2.setText(_translate("MOS", "正在加载\n"
"\n"
"当前步骤：下载公告……请稍后\n"
""))
        self.label_9.setText(_translate("MOS", "联机模块"))
        self.label_8.setText(_translate("MOS", "联机模块正在开发中……\n"
"不要着急啦 你的赞助就是我更新的动力！嘻嘻～"))
        self.comboBox_2.setItemText(0, _translate("MOS", "游戏下载"))
        self.comboBox_2.setItemText(1, _translate("MOS", "Mod下载"))
        self.comboBox_2.setItemText(2, _translate("MOS", "整合包下载"))
        self.comboBox_2.setItemText(3, _translate("MOS", "世界下载"))
        self.comboBox_2.setItemText(4, _translate("MOS", "下载/安装/已完成"))
        self.treeWidget.headerItem().setText(0, _translate("MOS", "版本列表"))
        self.treeWidget.headerItem().setText(1, _translate("MOS", "种类"))
        self.pushButton_5.setText(_translate("MOS", "（图片）"))
        self.label_11.setText(_translate("MOS", "模组加载器（forge"))
        self.label_19.setText(_translate("MOS", "模组加载器（fabric"))
        self.pushButton_6.setText(_translate("MOS", "（图片）"))
        self.label_20.setText(_translate("MOS", "高清修复optifine"))
        self.pushButton_7.setText(_translate("MOS", "（图片）"))
        self.label_21.setText(_translate("MOS", "模组加载器（quilt"))
        self.pushButton_8.setText(_translate("MOS", "（图片）"))
        self.label_10.setText(_translate("MOS", "下载"))
        self.label_12.setText(_translate("MOS", "音乐"))
        self.label_13.setText(_translate("MOS", "音乐 正在开发中……\n"
"不要着急啦 你的赞助就是我更新的动力！嘻嘻～"))
        self.comboBox.setItemText(0, _translate("MOS", "启动器设置"))
        self.comboBox.setItemText(1, _translate("MOS", "游戏设置"))
        self.label_15.setText(_translate("MOS", "设置"))
        self.label_6.setText(_translate("MOS", "常规设置"))
        self.label_4.setText(_translate("MOS", "启动器字体："))
        self.label_17.setText(_translate("MOS", "关于"))
        self.label.setText(_translate("MOS", "关于："))
        self.label_16.setText(_translate("MOS", "MOS启动器\n"
"版本V2.0.2-alpha-内部版本\n"
"请勿泄漏！"))
        self.label_18.setText(_translate("MOS", "MOS唯一开发者：David"))
        self.label_22.setText(_translate("MOS", "MOS网站支持、测试小组负责人：HeimNad"))

        # =================================分割线===================================#

        self.pushButton_home.clicked.connect(self.click_pushButton_home)
        self.pushButton_lianji.clicked.connect(self.click_pushButton_lianji)
        self.pushButton_xiazai.clicked.connect(self.click_pushButton_xiazai)
        self.pushButton_music.clicked.connect(self.click_pushButton_music)
        self.pushButton_shezhi.clicked.connect(self.click_pushButton_shezhi)
        self.pushButton_about.clicked.connect(self.click_pushButton_about)
        # 在‘……………………’里显示所有
        self.fontComboBox.setFontFilters(QtWidgets.QFontComboBox.AllFonts)
        # 为字体选择控件 连接槽
        self.fontComboBox.currentIndexChanged.connect(self.setfont)


class gonggao(QThread):
    '''获取公告'''
    sinOut_gonggao_ok = pyqtSignal(str)
    sinOut_gonggao_jindu = pyqtSignal(str)
    sinOut_gonggao_error = pyqtSignal(str)
    sinOut_gonggao_fanye = pyqtSignal(str)

    def __init__(self):
        super(gonggao, self).__init__()

    def run(self):
        import requests
        import time
        import linecache

        self.sinOut_gonggao_jindu.emit('10')
        print("开始获取公告")
        url = 'https://api.skyworldstudio.top/d/SWS/MOS/announcement.html'
        self.sinOut_gonggao_jindu.emit('30')
        try:
            self.sinOut_gonggao_fanye.emit('2')
            header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0'}    # 伪装浏览器
            r = requests.get(url, timeout=(5,50), headers = header)  # Get方式获取网页数据
            if r.status_code == 200:
                # 拼接路径
                self.sinOut_gonggao_jindu.emit('55')
                MOS_L=os.path.join(".MOS","Html","announcement.html")
                self.sinOut_gonggao_jindu.emit('60')
                #写入文件
                MOS_Html_gonggao_ok = open(MOS_L, 'w+', encoding='utf-8')
                a = r.text
                MOS_Html_gonggao_ok.write(a)
                MOS_Html_gonggao_ok.close
                print(a)
                self.sinOut_gonggao_ok.emit(a)
                self.sinOut_gonggao_jindu.emit('90')
                print("请求成功")
                        
            elif r.status_code != 200:
                if r.status_code == 404:
                    print("公告请求失败，状态码为404")
                    self.sinOut_gonggao_error.emit("404，找不到文件")
                elif r.status_code == 403:
                    print("公告请求失败，状态码为403")
                    self.sinOut_gonggao_error.emit("403，无权限访问")

                else:
                    gonggao_r_status_code = r.status_code
                    gonggao_111 = ("公告请求失败，状态码为" + gonggao_r_status_code)
                    print(gonggao_111)
                    self.sinOut_gonggao_error.emit(gonggao_111)
                


        except requests.exceptions.ConnectTimeout:
            # self.sinOut_gonggao_error.emit("请求超时")
            a = os.path.join(".MOS","Html","announcement.html")
            gangshu = len(linecache.getlines(a))    # 统计行数
            gangshu1 = 0
            gonggao = ''
            while gangshu1 <= gangshu:
                g = linecache.getline(a,gangshu1)
                gonggao = gonggao + g
                gangshu1 += 1
            print("请求失败 请求超时")
            print(gonggao)
            gonggao = str(gonggao)
            self.sinOut_gonggao_ok.emit(gonggao)

        except requests.exceptions.ReadTimeout:
            # self.sinOut_gonggao_error.emit("读取超时")
            a = os.path.join(".MOS","Html","announcement.html")
            gangshu = len(linecache.getlines(a))    # 统计行数
            gangshu1 = 0
            gonggao = ''
            while gangshu1 <= gangshu:
                g = linecache.getline(a,gangshu1)
                gonggao = gonggao + g
                gangshu1 += 1
            print("请求失败 读取超时")
            print(gonggao)
            gonggao = str(gonggao)
            self.sinOut_gonggao_ok.emit(gonggao)

        except requests.exceptions.SSLError:
            # self.sinOut_gonggao_error.emit("SSL错误")
            a = os.path.join(".MOS","Html","announcement.html")
            gangshu = len(linecache.getlines(a))    # 统计行数
            gangshu1 = 0
            gonggao = ''
            while gangshu1 <= gangshu:
                g = linecache.getline(a,gangshu1)
                gonggao = gonggao + g
                gangshu1 += 1
            print("请求失败 SSL证书错误")
            print(gonggao)
            gonggao = str(gonggao)
            self.sinOut_gonggao_ok.emit(gonggao)

        except requests.exceptions.ConnectionError:
            # self.sinOut_gonggao_error.emit("连接错误\n")
            a = os.path.join(".MOS","Html","announcement.html")
            gangshu = len(linecache.getlines(a))    # 统计行数
            gangshu1 = 0
            gonggao = ''
            while gangshu1 <= gangshu:
                g = linecache.getline(a,gangshu1)
                gonggao = gonggao + g
                gangshu1 += 1
            print("请求失败 连接错误")
            print(gonggao)
            gonggao = str(gonggao)
            self.sinOut_gonggao_ok.emit(gonggao)


class MOS_file(QThread):
    '''初始化文件/设置'''
    sinOut = pyqtSignal(str)
    def __init__(self):
        super(MOS_file, self).__init__()

    def run(self):
        import os
        print("文件初始化线程开始")

        try:
            MOS_file_1=os.path.join(".minecraft","mods")
            os.makedirs(MOS_file_1, exist_ok=True)

            MOS_file_1 =os.path.join(".minecraft","logs")
            os.makedirs(MOS_file_1, exist_ok=True)

            MOS_file_1 =os.path.join(".minecraft","versions")
            os.makedirs(MOS_file_1, exist_ok=True)

            MOS_file_1 =os.path.join(".MOS","Html")
            os.makedirs(MOS_file_1, exist_ok=True)

            MOS_file_1 =os.path.join(".MOS","Java")
            os.makedirs(MOS_file_1, exist_ok=True)
        
            MOS_file_1 =os.path.join(".MOS","Music")
            os.makedirs(MOS_file_1, exist_ok=True)

            MOS_file_1 =os.path.join(".MOS","MOS.json")
            if os.path.isfile(MOS_file_1)==True:
                MOS_first_run = "NoFirst"
                MOS_json=open(MOS_file_1,"w")
                MOS_json.close()
                print("程序不是第一次运行")
            elif os.path.isfile(MOS_file_1)==False:
                MOS_first_run = "First"
                print("程序是第一次运行")
            self.sinOut.emit("OK!")
        except PermissionError:
            print("初始化失败 没有权限，操作不被许可")
            self.sinOut.emit("ERROR_PermissionError")


try:
    if __name__ == '__main__':

        # import shutil
        # shutil.rmtree(".MOS")
        # shutil.rmtree(".minecraft")

        print("程序已开始运行！")
        app = QtWidgets.QApplication(sys.argv)
        print("请稍等...")
        MainWindow = QtWidgets.QMainWindow()
        print("创建窗口对象成功！")
        ui = Ui_MOS()
        print("创建PyQt窗口对象成功！")
        ui.setupUi(MainWindow)
        print("初始化设置成功！")
        MainWindow.show()
        print("已成功显示窗体")
        sys.exit(app.exec_())
except KeyboardInterrupt:
    print("程序以强行退出")
