import sys, os, requests, json, datetime, time, traceback, webbrowser, platform


os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r'.\site-packages\PyQt5\Qt5\plugins'  #### 这一行是新增的。用的是相对路径。



from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6 import *
# from PyQt6.QtWidgets import (QMainWindow, QTextEdit,QFileDialog, QApplication)
from PyQt6.QtGui import QIcon, QAction
# from pathlib import Path
# import MOS_2
# https://www.wenjuan.com/s/UZBZJvEm2uK/#《MOS ll 错误反馈》，快来参与吧。【问卷网提供支持】om PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MOS(object):
    def setupUi(self, MOS):
        MOS.setObjectName("MOS")
        MOS.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        MOS.resize(1000, 533)
        MOS.setMinimumSize(QtCore.QSize(1000, 533))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/Users/xyj/Desktop/MOS/UI/../picture/ico.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MOS.setWindowIcon(icon)
        MOS.setStyleSheet("QMainWindow{\n"
"    border-radius:15px;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MOS)
        self.centralwidget.setStyleSheet("background-color: rgba(255, 255, 255,100);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setHorizontalSpacing(0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.widget_mos_left = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_mos_left.sizePolicy().hasHeightForWidth())
        self.widget_mos_left.setSizePolicy(sizePolicy)
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
"    border:2px solid rgba(229, 228, 226,0);\n"
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
"    border:2px solid rgba(229, 228, 226,0);background-color: rgb(192, 192, 192);\n"
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
"    background-color: rgb(231, 230, 228);\n"
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
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.pushButton_home = QtWidgets.QPushButton(self.widget_mos_left)
        self.pushButton_home.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_home.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.pushButton_home.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButton_home.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/Users/xyj/Desktop/MOS/UI/../picture/home.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_home.setIcon(icon1)
        self.pushButton_home.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_home.setObjectName("pushButton_home")
        self.verticalLayout_2.addWidget(self.pushButton_home)
        self.pushButton_lianji = QtWidgets.QPushButton(self.widget_mos_left)
        self.pushButton_lianji.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_lianji.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/Users/xyj/Desktop/MOS/UI/../picture/online.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_lianji.setIcon(icon2)
        self.pushButton_lianji.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_lianji.setObjectName("pushButton_lianji")
        self.verticalLayout_2.addWidget(self.pushButton_lianji)
        self.pushButton_xiazai = QtWidgets.QPushButton(self.widget_mos_left)
        self.pushButton_xiazai.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_xiazai.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("/Users/xyj/Desktop/MOS/UI/../picture/download.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_xiazai.setIcon(icon3)
        self.pushButton_xiazai.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_xiazai.setObjectName("pushButton_xiazai")
        self.verticalLayout_2.addWidget(self.pushButton_xiazai)
        self.pushButton_music = QtWidgets.QPushButton(self.widget_mos_left)
        self.pushButton_music.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_music.setStyleSheet("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("/Users/xyj/Desktop/MOS/UI/../picture/music.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_music.setIcon(icon4)
        self.pushButton_music.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_music.setObjectName("pushButton_music")
        self.verticalLayout_2.addWidget(self.pushButton_music)
        self.pushButton_shezhi = QtWidgets.QPushButton(self.widget_mos_left)
        self.pushButton_shezhi.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_shezhi.setStyleSheet("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("/Users/xyj/Desktop/MOS/UI/../picture/settings.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_shezhi.setIcon(icon5)
        self.pushButton_shezhi.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_shezhi.setObjectName("pushButton_shezhi")
        self.verticalLayout_2.addWidget(self.pushButton_shezhi)
        self.pushButton_about = QtWidgets.QPushButton(self.widget_mos_left)
        self.pushButton_about.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_about.setStyleSheet("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("/Users/xyj/Desktop/MOS/UI/../picture/about.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_about.setIcon(icon6)
        self.pushButton_about.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_about.setObjectName("pushButton_about")
        self.verticalLayout_2.addWidget(self.pushButton_about)
        spacerItem = QtWidgets.QSpacerItem(20, 184, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label_mosll = QtWidgets.QLabel(self.widget_mos_left)
        self.label_mosll.setStyleSheet("color: rgb(0, 150, 255);font-size: 17px;font: 75 17pt \"Yuanti SC\";background-color: rgba(240, 239, 238,0);")
        self.label_mosll.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_mosll.setObjectName("label_mosll")
        self.verticalLayout_2.addWidget(self.label_mosll)
        self.gridLayout_13.addWidget(self.widget_mos_left, 0, 0, 1, 1)
        self.stackedWidget_mos_right = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget_mos_right.setStyleSheet("background-color: rgba(255, 255, 255, 128);")
        self.stackedWidget_mos_right.setObjectName("stackedWidget_mos_right")
        self.page_gonggao = QtWidgets.QWidget()
        self.page_gonggao.setStyleSheet("")
        self.page_gonggao.setObjectName("page_gonggao")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.page_gonggao)
        self.horizontalLayout.setContentsMargins(12, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea_page_gonggao = QtWidgets.QScrollArea(self.page_gonggao)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
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
"    background-color: rgba(0, 150, 255, 150);\n"
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
        self.label__gonggao_right_txt = QtWidgets.QLabel(self.widget_scrollArea_page_gonggao_right)
        self.label__gonggao_right_txt.setStyleSheet("border-style:none;font-size: 14px;")
        self.label__gonggao_right_txt.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label__gonggao_right_txt.setObjectName("label__gonggao_right_txt")
        self.gridLayout_6.addWidget(self.label__gonggao_right_txt, 0, 0, 1, 2)
        self.comboBox_gonggao_right = QtWidgets.QComboBox(self.widget_scrollArea_page_gonggao_right)
        self.comboBox_gonggao_right.setObjectName("comboBox_gonggao_right")
        self.gridLayout_6.addWidget(self.comboBox_gonggao_right, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 5, 0, 1, 1)
        self.line_8 = QtWidgets.QFrame(self.widget_scrollArea_page_gonggao_right)
        self.line_8.setStyleSheet("background-color: rgb(169, 169, 169);border:none;")
        self.line_8.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_6.addWidget(self.line_8, 1, 0, 1, 2)
        self.pushButton__gonggao_start = QtWidgets.QPushButton(self.widget_scrollArea_page_gonggao_right)
        self.pushButton__gonggao_start.setStyleSheet("border:2px solid rgb(142, 250, 0);height:25px;border-radius:12px;")
        self.pushButton__gonggao_start.setObjectName("pushButton__gonggao_start")
        self.gridLayout_6.addWidget(self.pushButton__gonggao_start, 4, 1, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.widget_scrollArea_page_gonggao_right)
        self.pushButton_16.setStyleSheet("border:2px solid rgb(192, 192, 192);height:23px;border-radius:12px;")
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_6.addWidget(self.pushButton_16, 3, 0, 1, 1)
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
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 1, 2, 3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget_scrollArea_page_gonggao_statring)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 1, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 0, 4, 2, 1)
        self.gridLayout_6.addWidget(self.widget_scrollArea_page_gonggao_statring, 2, 0, 1, 2)
        self.pushButton_17 = QtWidgets.QPushButton(self.widget_scrollArea_page_gonggao_right)
        self.pushButton_17.setStyleSheet("border:2px solid rgb(192, 192, 192);height:23px;border-radius:12px;")
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_6.addWidget(self.pushButton_17, 3, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_6.addItem(spacerItem4, 5, 1, 1, 1)
        self.gridLayout_16.addWidget(self.widget_scrollArea_page_gonggao_right, 0, 1, 1, 1)
        self.widget_scrollArea_page_gonggao_left = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_scrollArea_page_gonggao_left.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_scrollArea_page_gonggao_left.setStyleSheet("border:2px solid rgb(0, 150, 255);border-radius:15px;")
        self.widget_scrollArea_page_gonggao_left.setObjectName("widget_scrollArea_page_gonggao_left")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_scrollArea_page_gonggao_left)
        self.gridLayout_5.setContentsMargins(10, -1, 10, -1)
        self.gridLayout_5.setHorizontalSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.stackedWidget_gonggao = QtWidgets.QStackedWidget(self.widget_scrollArea_page_gonggao_left)
        self.stackedWidget_gonggao.setStyleSheet("border-style:none;")
        self.stackedWidget_gonggao.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
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
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_21.addItem(spacerItem5, 0, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 30, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_21.addItem(spacerItem6, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.page_gonggao_jiazai_ing)
        self.label_2.setStyleSheet("font-size: 13px;color: rgb(0, 150, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_21.addWidget(self.label_2, 1, 0, 1, 1)
        self.progressBar_2 = QtWidgets.QProgressBar(self.page_gonggao_jiazai_ing)
        self.progressBar_2.setStyleSheet("background-color: rgba(0, 150, 255, 10);height:15px;color: rgb(66, 66, 66);")
        self.progressBar_2.setMinimum(0)
        self.progressBar_2.setMaximum(100)
        self.progressBar_2.setProperty("value", 25)
        self.progressBar_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.progressBar_2.setTextVisible(True)
        self.progressBar_2.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.progressBar_2.setInvertedAppearance(False)
        self.progressBar_2.setTextDirection(QtWidgets.QProgressBar.Direction.TopToBottom)
        self.progressBar_2.setObjectName("progressBar_2")
        self.gridLayout_21.addWidget(self.progressBar_2, 2, 0, 1, 1)
        self.stackedWidget_gonggao.addWidget(self.page_gonggao_jiazai_ing)
        self.gridLayout_5.addWidget(self.stackedWidget_gonggao, 2, 0, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_5.addItem(spacerItem7, 3, 0, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.widget_scrollArea_page_gonggao_left)
        self.line_7.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.line_7.setAutoFillBackground(False)
        self.line_7.setStyleSheet("background-color: rgb(169, 169, 169);border:none;")
        self.line_7.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_7.setLineWidth(1)
        self.line_7.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_7.setObjectName("line_7")
        self.gridLayout_5.addWidget(self.line_7, 1, 0, 1, 2)
        self.label_gonggao_left_txt = QtWidgets.QLabel(self.widget_scrollArea_page_gonggao_left)
        self.label_gonggao_left_txt.setStyleSheet("font-size: 14px;border-style:none;")
        self.label_gonggao_left_txt.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_gonggao_left_txt.setObjectName("label_gonggao_left_txt")
        self.gridLayout_5.addWidget(self.label_gonggao_left_txt, 0, 0, 1, 1)
        self.gridLayout_16.addWidget(self.widget_scrollArea_page_gonggao_left, 0, 0, 1, 1)
        self.scrollArea_page_gonggao.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea_page_gonggao)
        self.stackedWidget_mos_right.addWidget(self.page_gonggao)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.gridLayout_50 = QtWidgets.QGridLayout(self.page_8)
        self.gridLayout_50.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_50.setObjectName("gridLayout_50")
        self.stackedWidget_mos_right_2 = QtWidgets.QStackedWidget(self.page_8)
        self.stackedWidget_mos_right_2.setStyleSheet("background-color: rgba(255, 255, 255, 128);")
        self.stackedWidget_mos_right_2.setObjectName("stackedWidget_mos_right_2")
        self.page_gonggao_2 = QtWidgets.QWidget()
        self.page_gonggao_2.setStyleSheet("")
        self.page_gonggao_2.setObjectName("page_gonggao_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page_gonggao_2)
        self.horizontalLayout_2.setContentsMargins(12, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea_page_gonggao_2 = QtWidgets.QScrollArea(self.page_gonggao_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.scrollArea_page_gonggao_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_page_gonggao_2.setSizePolicy(sizePolicy)
        self.scrollArea_page_gonggao_2.setMinimumSize(QtCore.QSize(790, 0))
        self.scrollArea_page_gonggao_2.setStyleSheet("border-style:none;background-color: rgba(255, 255, 255, 128);")
        self.scrollArea_page_gonggao_2.setWidgetResizable(True)
        self.scrollArea_page_gonggao_2.setObjectName("scrollArea_page_gonggao_2")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 790, 280))
        self.scrollAreaWidgetContents_4.setStyleSheet("")
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.gridLayout_27 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_27.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.widget_scrollArea_page_gonggao_right_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents_4)
        self.widget_scrollArea_page_gonggao_right_2.setStyleSheet("QWidget  {\n"
"    border:2px solid rgb(0, 150, 255);border-radius:15px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 2px solid rgb(235, 235, 235); /* border: 宽度 线类型 颜色 */\n"
"    border-radius: 3px;\n"
"    height:25px;\n"
"    font-size: 14px;\n"
"    background-color: rgba(0, 150, 255, 150);\n"
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
        self.widget_scrollArea_page_gonggao_right_2.setObjectName("widget_scrollArea_page_gonggao_right_2")
        self.gridLayout_28 = QtWidgets.QGridLayout(self.widget_scrollArea_page_gonggao_right_2)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.label__gonggao_right_txt_2 = QtWidgets.QLabel(self.widget_scrollArea_page_gonggao_right_2)
        self.label__gonggao_right_txt_2.setStyleSheet("border-style:none;font-size: 14px;")
        self.label__gonggao_right_txt_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label__gonggao_right_txt_2.setObjectName("label__gonggao_right_txt_2")
        self.gridLayout_28.addWidget(self.label__gonggao_right_txt_2, 0, 0, 1, 2)
        self.comboBox_gonggao_right_2 = QtWidgets.QComboBox(self.widget_scrollArea_page_gonggao_right_2)
        self.comboBox_gonggao_right_2.setObjectName("comboBox_gonggao_right_2")
        self.gridLayout_28.addWidget(self.comboBox_gonggao_right_2, 4, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_28.addItem(spacerItem8, 5, 0, 1, 1)
        self.line_9 = QtWidgets.QFrame(self.widget_scrollArea_page_gonggao_right_2)
        self.line_9.setStyleSheet("background-color: rgb(169, 169, 169);border:none;")
        self.line_9.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout_28.addWidget(self.line_9, 1, 0, 1, 2)
        self.pushButton__gonggao_start_2 = QtWidgets.QPushButton(self.widget_scrollArea_page_gonggao_right_2)
        self.pushButton__gonggao_start_2.setStyleSheet("border:2px solid rgb(142, 250, 0);height:25px;border-radius:12px;")
        self.pushButton__gonggao_start_2.setObjectName("pushButton__gonggao_start_2")
        self.gridLayout_28.addWidget(self.pushButton__gonggao_start_2, 4, 1, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.widget_scrollArea_page_gonggao_right_2)
        self.pushButton_18.setStyleSheet("border:2px solid rgb(192, 192, 192);height:23px;border-radius:12px;")
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout_28.addWidget(self.pushButton_18, 3, 0, 1, 1)
        self.widget_scrollArea_page_gonggao_statring_2 = QtWidgets.QWidget(self.widget_scrollArea_page_gonggao_right_2)
        self.widget_scrollArea_page_gonggao_statring_2.setStyleSheet("border-style:none;")
        self.widget_scrollArea_page_gonggao_statring_2.setObjectName("widget_scrollArea_page_gonggao_statring_2")
        self.gridLayout_29 = QtWidgets.QGridLayout(self.widget_scrollArea_page_gonggao_statring_2)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.progressBar_3 = QtWidgets.QProgressBar(self.widget_scrollArea_page_gonggao_statring_2)
        self.progressBar_3.setStyleSheet("background-color: rgba(0, 150, 255, 10);height:15px;")
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName("progressBar_3")
        self.gridLayout_29.addWidget(self.progressBar_3, 2, 0, 1, 5)
        self.label_5 = QtWidgets.QLabel(self.widget_scrollArea_page_gonggao_statring_2)
        self.label_5.setStyleSheet("border-style:none;")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_29.addWidget(self.label_5, 0, 1, 2, 3)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_29.addItem(spacerItem9, 0, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.widget_scrollArea_page_gonggao_statring_2)
        self.label_14.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_29.addWidget(self.label_14, 3, 1, 1, 3)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_29.addItem(spacerItem10, 0, 4, 2, 1)
        self.gridLayout_28.addWidget(self.widget_scrollArea_page_gonggao_statring_2, 2, 0, 1, 2)
        self.pushButton_19 = QtWidgets.QPushButton(self.widget_scrollArea_page_gonggao_right_2)
        self.pushButton_19.setStyleSheet("border:2px solid rgb(192, 192, 192);height:23px;border-radius:12px;")
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout_28.addWidget(self.pushButton_19, 3, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_28.addItem(spacerItem11, 5, 1, 1, 1)
        self.gridLayout_27.addWidget(self.widget_scrollArea_page_gonggao_right_2, 0, 1, 1, 1)
        self.widget_scrollArea_page_gonggao_left_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents_4)
        self.widget_scrollArea_page_gonggao_left_2.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_scrollArea_page_gonggao_left_2.setStyleSheet("border:2px solid rgb(0, 150, 255);border-radius:15px;")
        self.widget_scrollArea_page_gonggao_left_2.setObjectName("widget_scrollArea_page_gonggao_left_2")
        self.gridLayout_30 = QtWidgets.QGridLayout(self.widget_scrollArea_page_gonggao_left_2)
        self.gridLayout_30.setContentsMargins(10, -1, 10, -1)
        self.gridLayout_30.setHorizontalSpacing(0)
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.stackedWidget_gonggao_2 = QtWidgets.QStackedWidget(self.widget_scrollArea_page_gonggao_left_2)
        self.stackedWidget_gonggao_2.setStyleSheet("border-style:none;")
        self.stackedWidget_gonggao_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.stackedWidget_gonggao_2.setLineWidth(2)
        self.stackedWidget_gonggao_2.setObjectName("stackedWidget_gonggao_2")
        self.page_gonggao_jiazai_2 = QtWidgets.QWidget()
        self.page_gonggao_jiazai_2.setObjectName("page_gonggao_jiazai_2")
        self.gridLayout_31 = QtWidgets.QGridLayout(self.page_gonggao_jiazai_2)
        self.gridLayout_31.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_31.setObjectName("gridLayout_31")
        self.textBrowser_gonggao_left_txt_2 = QtWidgets.QTextBrowser(self.page_gonggao_jiazai_2)
        self.textBrowser_gonggao_left_txt_2.setStyleSheet("border-style:none;")
        self.textBrowser_gonggao_left_txt_2.setObjectName("textBrowser_gonggao_left_txt_2")
        self.gridLayout_31.addWidget(self.textBrowser_gonggao_left_txt_2, 0, 0, 1, 1)
        self.stackedWidget_gonggao_2.addWidget(self.page_gonggao_jiazai_2)
        self.page_gonggao_jiazai_ing_2 = QtWidgets.QWidget()
        self.page_gonggao_jiazai_ing_2.setStyleSheet("QProgressBar{\n"
"    text-align: center;\n"
"    border-style:none;\n"
"    border-radius:7px;\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"QProgressBar::chunk{\n"
"    border-radius:7px;\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(53, 244, 252, 255), stop:1 rgba(222, 255, 255, 255));\n"
"}")
        self.page_gonggao_jiazai_ing_2.setObjectName("page_gonggao_jiazai_ing_2")
        self.gridLayout_32 = QtWidgets.QGridLayout(self.page_gonggao_jiazai_ing_2)
        self.gridLayout_32.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_32.setObjectName("gridLayout_32")
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_32.addItem(spacerItem12, 0, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 30, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_32.addItem(spacerItem13, 3, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.page_gonggao_jiazai_ing_2)
        self.label_23.setStyleSheet("font-size: 13px;color: rgb(0, 150, 255);")
        self.label_23.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout_32.addWidget(self.label_23, 1, 0, 1, 1)
        self.progressBar_4 = QtWidgets.QProgressBar(self.page_gonggao_jiazai_ing_2)
        self.progressBar_4.setStyleSheet("background-color: rgba(0, 150, 255, 10);height:15px;color: rgb(66, 66, 66);")
        self.progressBar_4.setMinimum(0)
        self.progressBar_4.setMaximum(100)
        self.progressBar_4.setProperty("value", 25)
        self.progressBar_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.progressBar_4.setTextVisible(True)
        self.progressBar_4.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.progressBar_4.setInvertedAppearance(False)
        self.progressBar_4.setTextDirection(QtWidgets.QProgressBar.Direction.TopToBottom)
        self.progressBar_4.setObjectName("progressBar_4")
        self.gridLayout_32.addWidget(self.progressBar_4, 2, 0, 1, 1)
        self.stackedWidget_gonggao_2.addWidget(self.page_gonggao_jiazai_ing_2)
        self.gridLayout_30.addWidget(self.stackedWidget_gonggao_2, 2, 0, 1, 2)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_30.addItem(spacerItem14, 3, 0, 1, 1)
        self.line_10 = QtWidgets.QFrame(self.widget_scrollArea_page_gonggao_left_2)
        self.line_10.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.line_10.setAutoFillBackground(False)
        self.line_10.setStyleSheet("background-color: rgb(169, 169, 169);border:none;")
        self.line_10.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_10.setLineWidth(1)
        self.line_10.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_10.setObjectName("line_10")
        self.gridLayout_30.addWidget(self.line_10, 1, 0, 1, 2)
        self.label_gonggao_left_txt_2 = QtWidgets.QLabel(self.widget_scrollArea_page_gonggao_left_2)
        self.label_gonggao_left_txt_2.setStyleSheet("font-size: 14px;border-style:none;")
        self.label_gonggao_left_txt_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_gonggao_left_txt_2.setObjectName("label_gonggao_left_txt_2")
        self.gridLayout_30.addWidget(self.label_gonggao_left_txt_2, 0, 0, 1, 1)
        self.gridLayout_27.addWidget(self.widget_scrollArea_page_gonggao_left_2, 0, 0, 1, 1)
        self.scrollArea_page_gonggao_2.setWidget(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_2.addWidget(self.scrollArea_page_gonggao_2)
        self.stackedWidget_mos_right_2.addWidget(self.page_gonggao_2)
        self.page_11 = QtWidgets.QWidget()
        self.page_11.setObjectName("page_11")
        self.stackedWidget_mos_right_2.addWidget(self.page_11)
        self.page_12 = QtWidgets.QWidget()
        self.page_12.setObjectName("page_12")
        self.gridLayout_33 = QtWidgets.QGridLayout(self.page_12)
        self.gridLayout_33.setObjectName("gridLayout_33")
        self.label_26 = QtWidgets.QLabel(self.page_12)
        self.label_26.setObjectName("label_26")
        self.gridLayout_33.addWidget(self.label_26, 3, 0, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(805, 13, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_33.addItem(spacerItem15, 0, 0, 1, 3)
        self.label_24 = QtWidgets.QLabel(self.page_12)
        self.label_24.setStyleSheet("border-style:none;color:rgb(33, 33, 33);font-size: 17px;background-color: rgba(255, 255, 255, 0);")
        self.label_24.setIndent(10)
        self.label_24.setObjectName("label_24")
        self.gridLayout_33.addWidget(self.label_24, 1, 0, 1, 3)
        self.line_11 = QtWidgets.QFrame(self.page_12)
        self.line_11.setStyleSheet("color:rgb(214, 214, 214)")
        self.line_11.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_11.setMidLineWidth(1)
        self.line_11.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_11.setObjectName("line_11")
        self.gridLayout_33.addWidget(self.line_11, 2, 0, 1, 3)
        self.listWidget = QtWidgets.QListWidget(self.page_12)
        self.listWidget.setStyleSheet("")
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_33.addWidget(self.listWidget, 4, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.widget_6 = QtWidgets.QWidget(self.page_12)
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_51 = QtWidgets.QGridLayout(self.widget_6)
        self.gridLayout_51.setObjectName("gridLayout_51")
        self.label_43 = QtWidgets.QLabel(self.widget_6)
        self.label_43.setObjectName("label_43")
        self.gridLayout_51.addWidget(self.label_43, 0, 0, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_51.addItem(spacerItem16, 2, 0, 1, 1)
        self.listWidget_2 = QtWidgets.QListWidget(self.widget_6)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout_51.addWidget(self.listWidget_2, 1, 0, 1, 2)
        self.gridLayout_33.addWidget(self.widget_6, 3, 1, 2, 1)
        self.stackedWidget_mos_right_2.addWidget(self.page_12)
        self.page_13 = QtWidgets.QWidget()
        self.page_13.setStyleSheet("QComboBox {\n"
"    border: 2px solid rgb(235, 235, 235); /* border: 宽度 线类型 颜色 */\n"
"    border-radius: 3px;\n"
"    height:25px;\n"
"    font-size: 14px;\n"
"    background-color: rgba(0, 150, 255, 150);\n"
"    border-radius:10px;\n"
"}\n"
"/*QComboBox::down-arrow\n"
"是 右面那个 \n"
"*/")
        self.page_13.setObjectName("page_13")
        self.gridLayout_34 = QtWidgets.QGridLayout(self.page_13)
        self.gridLayout_34.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_34.setObjectName("gridLayout_34")
        self.line_12 = QtWidgets.QFrame(self.page_13)
        self.line_12.setStyleSheet("color:rgb(214, 214, 214)")
        self.line_12.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_12.setMidLineWidth(1)
        self.line_12.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_12.setObjectName("line_12")
        self.gridLayout_34.addWidget(self.line_12, 3, 0, 1, 2)
        self.label_27 = QtWidgets.QLabel(self.page_13)
        self.label_27.setStyleSheet("border-style:none;color:rgb(33, 33, 33);font-size: 17px;background-color: rgba(255, 255, 255, 0);")
        self.label_27.setIndent(10)
        self.label_27.setObjectName("label_27")
        self.gridLayout_34.addWidget(self.label_27, 1, 0, 2, 1)
        self.comboBox_7 = QtWidgets.QComboBox(self.page_13)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.gridLayout_34.addWidget(self.comboBox_7, 1, 1, 2, 1)
        spacerItem17 = QtWidgets.QSpacerItem(832, 13, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_34.addItem(spacerItem17, 0, 0, 1, 2)
        self.stackedWidget_3 = QtWidgets.QStackedWidget(self.page_13)
        self.stackedWidget_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.stackedWidget_3.setObjectName("stackedWidget_3")
        self.page_14 = QtWidgets.QWidget()
        self.page_14.setStyleSheet("QAbstractItemView::item {\n"
"    min-height: 110px;\n"
"    min-width: 40px; \n"
"}\n"
"")
        self.page_14.setObjectName("page_14")
        self.gridLayout_35 = QtWidgets.QGridLayout(self.page_14)
        self.gridLayout_35.setObjectName("gridLayout_35")
        self.treeWidget_2 = QtWidgets.QTreeWidget(self.page_14)
        self.treeWidget_2.setStyleSheet("")
        self.treeWidget_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.treeWidget_2.setDragDropOverwriteMode(False)
        self.treeWidget_2.setAlternatingRowColors(True)
        self.treeWidget_2.setUniformRowHeights(True)
        self.treeWidget_2.setAnimated(True)
        self.treeWidget_2.setAllColumnsShowFocus(False)
        self.treeWidget_2.setWordWrap(False)
        self.treeWidget_2.setHeaderHidden(False)
        self.treeWidget_2.setColumnCount(2)
        self.treeWidget_2.setObjectName("treeWidget_2")
        self.gridLayout_35.addWidget(self.treeWidget_2, 0, 0, 1, 1)
        self.stackedWidget_3.addWidget(self.page_14)
        self.page_15 = QtWidgets.QWidget()
        self.page_15.setStyleSheet("")
        self.page_15.setObjectName("page_15")
        self.gridLayout_36 = QtWidgets.QGridLayout(self.page_15)
        self.gridLayout_36.setObjectName("gridLayout_36")
        self.widget_3 = QtWidgets.QWidget(self.page_15)
        self.widget_3.setStyleSheet("QWidget{border-radius: 23px;border:2px solid rgb(0, 150, 255);}\n"
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
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_37 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_37.setObjectName("gridLayout_37")
        spacerItem18 = QtWidgets.QSpacerItem(199, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_37.addItem(spacerItem18, 0, 2, 1, 2)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_37.addItem(spacerItem19, 3, 2, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_20.setStyleSheet("border-style:none;width:50px;height:50px;border-radius: 23px;background-color: rgba(235, 235, 235, 0);")
        self.pushButton_20.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("/Users/xyj/Desktop/MOS/UI/../picture/quilt.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_20.setIcon(icon7)
        self.pushButton_20.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout_37.addWidget(self.pushButton_20, 3, 0, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_37.addItem(spacerItem20, 2, 2, 1, 2)
        self.comboBox_8 = QtWidgets.QComboBox(self.widget_3)
        self.comboBox_8.setMinimumSize(QtCore.QSize(120, 25))
        self.comboBox_8.setStyleSheet("border: 2px solid rgb(235, 235, 235);")
        self.comboBox_8.setObjectName("comboBox_8")
        self.gridLayout_37.addWidget(self.comboBox_8, 2, 5, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_37.addItem(spacerItem21, 1, 2, 1, 2)
        self.label_28 = QtWidgets.QLabel(self.widget_3)
        self.label_28.setStyleSheet("border-style:none;font-size: 14px;")
        self.label_28.setObjectName("label_28")
        self.gridLayout_37.addWidget(self.label_28, 3, 1, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.widget_3)
        self.label_29.setStyleSheet("border-style:none;font-size: 14px;")
        self.label_29.setObjectName("label_29")
        self.gridLayout_37.addWidget(self.label_29, 2, 1, 1, 1)
        self.pushButton_21 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_21.setStyleSheet("border-style:none;width:50px;height:50px;border-radius: 23px;background-color: rgba(235, 235, 235, 0);")
        self.pushButton_21.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("/Users/xyj/Desktop/MOS/UI/../picture/loading.gif"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_21.setIcon(icon8)
        self.pushButton_21.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout_37.addWidget(self.pushButton_21, 1, 4, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_22.setStyleSheet("border-style:none;width:50px;height:50px;border-radius: 23px;background-color: rgba(235, 235, 235, 0);")
        self.pushButton_22.setText("")
        self.pushButton_22.setIcon(icon8)
        self.pushButton_22.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout_37.addWidget(self.pushButton_22, 2, 4, 1, 1)
        self.pushButton_23 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_23.setStyleSheet("border-style:none;width:50px;height:50px;border-radius: 23px;background-color: rgba(235, 235, 235, 0);")
        self.pushButton_23.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("/Users/xyj/Desktop/MOS/UI/../picture/forge.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_23.setIcon(icon9)
        self.pushButton_23.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout_37.addWidget(self.pushButton_23, 0, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.widget_3)
        self.label_30.setStyleSheet("border-style:none;font-size: 15px;")
        self.label_30.setObjectName("label_30")
        self.gridLayout_37.addWidget(self.label_30, 0, 1, 1, 1)
        self.pushButton_24 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_24.setStyleSheet("border-style:none;width:50px;height:50px;border-radius: 23px;background-color: rgba(235, 235, 235, 0);")
        self.pushButton_24.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("/Users/xyj/Desktop/MOS/UI/../picture/optifine.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_24.setIcon(icon10)
        self.pushButton_24.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_24.setObjectName("pushButton_24")
        self.gridLayout_37.addWidget(self.pushButton_24, 2, 0, 1, 1)
        self.pushButton_25 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_25.setStyleSheet("border-style:none;width:50px;height:50px;border-radius: 23px;background-color: rgba(235, 235, 235, 0);")
        self.pushButton_25.setText("")
        self.pushButton_25.setIcon(icon8)
        self.pushButton_25.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_25.setObjectName("pushButton_25")
        self.gridLayout_37.addWidget(self.pushButton_25, 3, 4, 1, 1)
        self.comboBox_9 = QtWidgets.QComboBox(self.widget_3)
        self.comboBox_9.setMinimumSize(QtCore.QSize(120, 25))
        self.comboBox_9.setStyleSheet("border: 2px solid rgb(235, 235, 235);")
        self.comboBox_9.setObjectName("comboBox_9")
        self.gridLayout_37.addWidget(self.comboBox_9, 3, 5, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.widget_3)
        self.label_31.setStyleSheet("border-style:none;font-size: 14px;")
        self.label_31.setObjectName("label_31")
        self.gridLayout_37.addWidget(self.label_31, 1, 1, 1, 1)
        self.comboBox_10 = QtWidgets.QComboBox(self.widget_3)
        self.comboBox_10.setMinimumSize(QtCore.QSize(210, 25))
        self.comboBox_10.setStyleSheet("border: 2px solid rgb(235, 235, 235);")
        self.comboBox_10.setObjectName("comboBox_10")
        self.gridLayout_37.addWidget(self.comboBox_10, 0, 5, 1, 1)
        self.pushButton_26 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_26.setStyleSheet("border-style:none;width:50px;height:50px;border-radius: 23px;background-color: rgba(235, 235, 235, 0);")
        self.pushButton_26.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("/Users/xyj/Desktop/MOS/UI/../picture/fabric.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_26.setIcon(icon11)
        self.pushButton_26.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_26.setObjectName("pushButton_26")
        self.gridLayout_37.addWidget(self.pushButton_26, 1, 0, 1, 1)
        self.pushButton_27 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_27.setStyleSheet("border-style:none;width:50px;height:50px;border-radius: 23px;background-color: rgba(235, 235, 235, 0);")
        self.pushButton_27.setText("")
        self.pushButton_27.setIcon(icon8)
        self.pushButton_27.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_27.setObjectName("pushButton_27")
        self.gridLayout_37.addWidget(self.pushButton_27, 0, 4, 1, 1)
        self.comboBox_11 = QtWidgets.QComboBox(self.widget_3)
        self.comboBox_11.setMinimumSize(QtCore.QSize(120, 25))
        self.comboBox_11.setStyleSheet("border: 2px solid rgb(235, 235, 235);")
        self.comboBox_11.setObjectName("comboBox_11")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.gridLayout_37.addWidget(self.comboBox_11, 1, 5, 1, 1)
        self.gridLayout_36.addWidget(self.widget_3, 0, 0, 1, 3)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_36.addItem(spacerItem22, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_15)
        self.lineEdit_2.setStyleSheet("height:25px;border-radius: 5px;border:2px solid rgb(169, 169, 169);color: rgb(0, 0, 0);")
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_36.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.pushButton_28 = QtWidgets.QPushButton(self.page_15)
        self.pushButton_28.setStyleSheet("height:25px;border-radius: 5px;width:70px;border:2px solid rgb(169, 169, 169);")
        self.pushButton_28.setObjectName("pushButton_28")
        self.gridLayout_36.addWidget(self.pushButton_28, 1, 2, 1, 1)
        self.stackedWidget_3.addWidget(self.page_15)
        self.gridLayout_34.addWidget(self.stackedWidget_3, 4, 0, 1, 2)
        self.stackedWidget_mos_right_2.addWidget(self.page_13)
        self.page_16 = QtWidgets.QWidget()
        self.page_16.setObjectName("page_16")
        self.gridLayout_38 = QtWidgets.QGridLayout(self.page_16)
        self.gridLayout_38.setContentsMargins(5, 0, 5, 0)
        self.gridLayout_38.setObjectName("gridLayout_38")
        spacerItem23 = QtWidgets.QSpacerItem(832, 13, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_38.addItem(spacerItem23, 0, 0, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.page_16)
        self.label_32.setStyleSheet("border-style:none;color:rgb(33, 33, 33);font-size: 17px;background-color: rgba(255, 255, 255, 0);")
        self.label_32.setIndent(10)
        self.label_32.setObjectName("label_32")
        self.gridLayout_38.addWidget(self.label_32, 1, 0, 1, 1)
        self.line_13 = QtWidgets.QFrame(self.page_16)
        self.line_13.setStyleSheet("color:rgb(214, 214, 214)")
        self.line_13.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_13.setMidLineWidth(1)
        self.line_13.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_13.setObjectName("line_13")
        self.gridLayout_38.addWidget(self.line_13, 2, 0, 1, 1)
        self.widget_9 = QtWidgets.QWidget(self.page_16)
        self.widget_9.setStyleSheet("border-radius:10px;\n"
"border:2px solid rgb(0, 150, 255);")
        self.widget_9.setObjectName("widget_9")
        self.gridLayout_39 = QtWidgets.QGridLayout(self.widget_9)
        self.gridLayout_39.setContentsMargins(12, -1, -1, -1)
        self.gridLayout_39.setObjectName("gridLayout_39")
        self.label_33 = QtWidgets.QLabel(self.widget_9)
        self.label_33.setStyleSheet("border-style:none;color:rgb(0, 150, 255);")
        self.label_33.setObjectName("label_33")
        self.gridLayout_39.addWidget(self.label_33, 1, 0, 1, 1)
        self.gridLayout_38.addWidget(self.widget_9, 3, 0, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(832, 393, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_38.addItem(spacerItem24, 4, 0, 1, 1)
        self.stackedWidget_mos_right_2.addWidget(self.page_16)
        self.page_17 = QtWidgets.QWidget()
        self.page_17.setStyleSheet("QComboBox {\n"
"    border: 2px solid rgb(235, 235, 235); /* border: 宽度 线类型 颜色 */\n"
"    border-radius: 3px;\n"
"    height:25px;\n"
"    font-size: 14px;\n"
"    background-color: rgba(0, 150, 255, 150);\n"
"    border-radius:10px;\n"
"}\n"
"/*QComboBox::down-arrow\n"
"是 右面那个 \n"
"*/")
        self.page_17.setObjectName("page_17")
        self.gridLayout_40 = QtWidgets.QGridLayout(self.page_17)
        self.gridLayout_40.setContentsMargins(5, 0, 5, 0)
        self.gridLayout_40.setObjectName("gridLayout_40")
        self.comboBox_12 = QtWidgets.QComboBox(self.page_17)
        self.comboBox_12.setStyleSheet("")
        self.comboBox_12.setObjectName("comboBox_12")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.gridLayout_40.addWidget(self.comboBox_12, 1, 1, 1, 1)
        self.stackedWidget_4 = QtWidgets.QStackedWidget(self.page_17)
        self.stackedWidget_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.stackedWidget_4.setObjectName("stackedWidget_4")
        self.page_18 = QtWidgets.QWidget()
        self.page_18.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.page_18.setObjectName("page_18")
        self.gridLayout_41 = QtWidgets.QGridLayout(self.page_18)
        self.gridLayout_41.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_41.setObjectName("gridLayout_41")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.page_18)
        self.scrollArea_3.setStyleSheet("border-style:none;background-color: rgba(255, 255, 255, 0);")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 373, 627))
        self.scrollAreaWidgetContents_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.gridLayout_42 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_42.setContentsMargins(5, 0, 5, 0)
        self.gridLayout_42.setObjectName("gridLayout_42")
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_42.addItem(spacerItem25, 6, 0, 1, 2)
        self.widget_4 = QtWidgets.QWidget(self.scrollAreaWidgetContents_5)
        self.widget_4.setStyleSheet("QWidget{background-color: rgba(255, 255, 255, 0);border-radius:15px;border: 2px solid rgb(0, 150, 255);}\n"
"QComboBox {\n"
"    border: 2px solid rgb(235, 235, 235); /* border: 宽度 线类型 颜色 */\n"
"    height:25px;\n"
"    font-size: 14px;\n"
"    background-color: rgba(0, 150, 255, 150);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"/*下拉框的样式*/\n"
"QComboBox QAbstractItemView \n"
"{\n"
"    outline: 0px solid gray;  /*取消选中虚线*/\n"
"    border: 1px solid rgb(31, 156, 255);\n"
"    color: rgb(66, 66, 66);\n"
"    background-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(0, 150, 255);\n"
"    border-radius:5px;\n"
"    height:50px;\n"
"}\n"
" /*选中每一项高度*/\n"
"QComboBox QAbstractItemView::item\n"
"{ \n"
"    height: 25px;\n"
"    border-radius:5px;\n"
" }\n"
"/*选中每一项的字体颜色和背景颜色*/\n"
"QComboBox QAbstractItemView::item:selected \n"
"{\n"
"    color: rgb(31,163,246);\n"
"    background-color: rgb(0, 150, 255);\n"
"    border-radius:5px;\n"
"}\n"
"/*QComboBox::down-arrow\n"
"是 右面那个 \n"
"*/\n"
"\n"
"\n"
"\n"
"/* QComboBox中的垂直滚动条 */\n"
"QComboBox QAbstractScrollArea QScrollBar:vertical {\n"
"    width: 13px;\n"
"    height: 5px;\n"
"    background-color: #d0d2d4;   /* 空白区域的背景色*/\n"
"    border-style:none;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical {\n"
"    border-radius: 5px;   /* 圆角 */\n"
"    background: rgb(160,160,160);   /* 小方块的背景色深灰lightblue */\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical:hover {\n"
"    background: rgb(255, 255, 255);   /* 越过小方块的背景色*/\n"
"}\n"
"\n"
"QPushButton{height:30px;background-color: rgba(255, 255, 255,0);border-radius:7px;border:2px solid rgb(255, 59, 0);font-size: 13.5px;}\n"
"QPushButton::hover{color: rgb(255, 59, 0)}\n"
"QPushButton::pressed{background-color: rgba(255, 0, 0, 100);}")
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_43 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_43.setObjectName("gridLayout_43")
        self.label_34 = QtWidgets.QLabel(self.widget_4)
        self.label_34.setStyleSheet("border-style:none;")
        self.label_34.setScaledContents(False)
        self.label_34.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_34.setWordWrap(True)
        self.label_34.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.label_34.setObjectName("label_34")
        self.gridLayout_43.addWidget(self.label_34, 0, 0, 2, 1)
        self.fontComboBox_2 = QtWidgets.QFontComboBox(self.widget_4)
        self.fontComboBox_2.setMaxVisibleItems(15)
        self.fontComboBox_2.setDuplicatesEnabled(False)
        self.fontComboBox_2.setObjectName("fontComboBox_2")
        self.gridLayout_43.addWidget(self.fontComboBox_2, 0, 1, 1, 3)
        self.pushButton_29 = QtWidgets.QPushButton(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_29.sizePolicy().hasHeightForWidth())
        self.pushButton_29.setSizePolicy(sizePolicy)
        self.pushButton_29.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_29.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_29.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_29.setStyleSheet("")
        self.pushButton_29.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_29.setObjectName("pushButton_29")
        self.gridLayout_43.addWidget(self.pushButton_29, 1, 3, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.widget_4)
        self.label_35.setStyleSheet("font-size: 14px;border-style:none;")
        self.label_35.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.gridLayout_43.addWidget(self.label_35, 1, 1, 1, 2)
        self.gridLayout_42.addWidget(self.widget_4, 3, 0, 1, 2)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_5)
        self.gridLayout_41.addWidget(self.scrollArea_3, 0, 0, 1, 1)
        self.stackedWidget_4.addWidget(self.page_18)
        self.page_19 = QtWidgets.QWidget()
        self.page_19.setObjectName("page_19")
        self.gridLayout_44 = QtWidgets.QGridLayout(self.page_19)
        self.gridLayout_44.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_44.setObjectName("gridLayout_44")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.page_19)
        self.scrollArea_4.setStyleSheet("border-style:none;")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_6)
        self.gridLayout_44.addWidget(self.scrollArea_4, 0, 0, 1, 1)
        self.stackedWidget_4.addWidget(self.page_19)
        self.gridLayout_40.addWidget(self.stackedWidget_4, 6, 0, 1, 2)
        self.label_36 = QtWidgets.QLabel(self.page_17)
        self.label_36.setStyleSheet("border-style:none;color:rgb(33, 33, 33);font-size: 17px;background-color: rgba(255, 255, 255, 0);")
        self.label_36.setIndent(10)
        self.label_36.setObjectName("label_36")
        self.gridLayout_40.addWidget(self.label_36, 1, 0, 1, 1)
        self.line_14 = QtWidgets.QFrame(self.page_17)
        self.line_14.setStyleSheet("color:rgb(214, 214, 214)")
        self.line_14.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_14.setMidLineWidth(1)
        self.line_14.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_14.setObjectName("line_14")
        self.gridLayout_40.addWidget(self.line_14, 3, 0, 2, 2)
        spacerItem26 = QtWidgets.QSpacerItem(832, 13, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_40.addItem(spacerItem26, 0, 0, 1, 2)
        self.stackedWidget_mos_right_2.addWidget(self.page_17)
        self.page_20 = QtWidgets.QWidget()
        self.page_20.setObjectName("page_20")
        self.gridLayout_45 = QtWidgets.QGridLayout(self.page_20)
        self.gridLayout_45.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_45.setObjectName("gridLayout_45")
        self.widget_15 = QtWidgets.QWidget(self.page_20)
        self.widget_15.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.widget_15.setObjectName("widget_15")
        self.gridLayout_46 = QtWidgets.QGridLayout(self.widget_15)
        self.gridLayout_46.setObjectName("gridLayout_46")
        self.widget_16 = QtWidgets.QWidget(self.widget_15)
        self.widget_16.setStyleSheet("QWidget{border-radius:15px;border:2px solid rgba(0, 150, 255, 230);}")
        self.widget_16.setObjectName("widget_16")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_16)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_37 = QtWidgets.QLabel(self.widget_16)
        self.label_37.setStyleSheet("border-style:none;")
        self.label_37.setObjectName("label_37")
        self.verticalLayout_4.addWidget(self.label_37)
        self.widget_17 = QtWidgets.QWidget(self.widget_16)
        self.widget_17.setStyleSheet("border-style:none;background-color: rgb(235, 235, 235);border-radius:15px;")
        self.widget_17.setObjectName("widget_17")
        self.gridLayout_47 = QtWidgets.QGridLayout(self.widget_17)
        self.gridLayout_47.setHorizontalSpacing(7)
        self.gridLayout_47.setObjectName("gridLayout_47")
        self.pushButton_30 = QtWidgets.QPushButton(self.widget_17)
        self.pushButton_30.setStyleSheet("border-style:none;")
        self.pushButton_30.setText("")
        self.pushButton_30.setIcon(icon)
        self.pushButton_30.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_30.setObjectName("pushButton_30")
        self.gridLayout_47.addWidget(self.pushButton_30, 1, 0, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(34, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_47.addItem(spacerItem27, 1, 2, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.widget_17)
        self.label_38.setStyleSheet("font-size: 13px;border-style:none;")
        self.label_38.setObjectName("label_38")
        self.gridLayout_47.addWidget(self.label_38, 1, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.widget_17)
        self.widget_18 = QtWidgets.QWidget(self.widget_16)
        self.widget_18.setStyleSheet("QWidget{border-style:none;background-color: rgb(235, 235, 235);border-radius:15px;}\n"
"#pushButton_3{width:120px;height:30px;background-color: rgba(255, 255, 255,0);}\n"
"#pushButton_3::hover{background-color: rgb(255, 255, 255);}\n"
"#pushButton_3::pressed{background-color: rgba(0, 150, 255, 51);}")
        self.widget_18.setObjectName("widget_18")
        self.gridLayout_48 = QtWidgets.QGridLayout(self.widget_18)
        self.gridLayout_48.setHorizontalSpacing(7)
        self.gridLayout_48.setObjectName("gridLayout_48")
        self.label_39 = QtWidgets.QLabel(self.widget_18)
        self.label_39.setStyleSheet("font-size: 13px;border-style:none;")
        self.label_39.setObjectName("label_39")
        self.gridLayout_48.addWidget(self.label_39, 0, 1, 1, 1)
        spacerItem28 = QtWidgets.QSpacerItem(34, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_48.addItem(spacerItem28, 0, 2, 1, 1)
        self.pushButton_31 = QtWidgets.QPushButton(self.widget_18)
        self.pushButton_31.setStyleSheet("border-style:none;")
        self.pushButton_31.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("/Users/xyj/Desktop/MOS/UI/../picture/david.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_31.setIcon(icon12)
        self.pushButton_31.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_31.setObjectName("pushButton_31")
        self.gridLayout_48.addWidget(self.pushButton_31, 0, 0, 1, 1)
        self.pushButton_32 = QtWidgets.QPushButton(self.widget_18)
        self.pushButton_32.setStyleSheet("border-radius:7px;border:2px solid rgb(0, 150, 255);")
        self.pushButton_32.setObjectName("pushButton_32")
        self.gridLayout_48.addWidget(self.pushButton_32, 0, 3, 1, 1)
        self.verticalLayout_4.addWidget(self.widget_18)
        self.widget_19 = QtWidgets.QWidget(self.widget_16)
        self.widget_19.setStyleSheet("QWidget{border-style:none;background-color: rgb(235, 235, 235);border-radius:15px;}\n"
"#pushButton_10{width:120px;height:30px;background-color: rgba(255, 255, 255,0);}\n"
"#pushButton_10::hover{background-color: rgb(255, 255, 255);}\n"
"#pushButton_10::pressed{background-color: rgba(0, 150, 255, 51);}")
        self.widget_19.setObjectName("widget_19")
        self.gridLayout_49 = QtWidgets.QGridLayout(self.widget_19)
        self.gridLayout_49.setHorizontalSpacing(2)
        self.gridLayout_49.setObjectName("gridLayout_49")
        spacerItem29 = QtWidgets.QSpacerItem(34, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_49.addItem(spacerItem29, 0, 3, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.widget_19)
        self.label_40.setText("")
        self.label_40.setObjectName("label_40")
        self.gridLayout_49.addWidget(self.label_40, 0, 1, 1, 1)
        self.pushButton_33 = QtWidgets.QPushButton(self.widget_19)
        self.pushButton_33.setStyleSheet("border-style:none;")
        self.pushButton_33.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("/Users/xyj/Desktop/MOS/UI/../picture/heimnad.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_33.setIcon(icon13)
        self.pushButton_33.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_33.setObjectName("pushButton_33")
        self.gridLayout_49.addWidget(self.pushButton_33, 0, 0, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.widget_19)
        self.label_41.setStyleSheet("font-size: 13px;border-style:none;")
        self.label_41.setObjectName("label_41")
        self.gridLayout_49.addWidget(self.label_41, 0, 2, 1, 1)
        self.pushButton_34 = QtWidgets.QPushButton(self.widget_19)
        self.pushButton_34.setStyleSheet("border-radius:7px;border:2px solid rgb(0, 150, 255);")
        self.pushButton_34.setObjectName("pushButton_34")
        self.gridLayout_49.addWidget(self.pushButton_34, 0, 4, 1, 1)
        self.verticalLayout_4.addWidget(self.widget_19)
        self.gridLayout_46.addWidget(self.widget_16, 0, 0, 1, 1)
        spacerItem30 = QtWidgets.QSpacerItem(796, 368, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_46.addItem(spacerItem30, 1, 0, 1, 1)
        self.gridLayout_45.addWidget(self.widget_15, 3, 0, 1, 2)
        self.line_15 = QtWidgets.QFrame(self.page_20)
        self.line_15.setStyleSheet("color:rgb(214, 214, 214)")
        self.line_15.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_15.setMidLineWidth(1)
        self.line_15.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_15.setObjectName("line_15")
        self.gridLayout_45.addWidget(self.line_15, 2, 0, 1, 2)
        spacerItem31 = QtWidgets.QSpacerItem(832, 13, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_45.addItem(spacerItem31, 0, 0, 1, 2)
        self.label_42 = QtWidgets.QLabel(self.page_20)
        self.label_42.setStyleSheet("border-style:none;color:rgb(33, 33, 33);font-size: 17px;background-color: rgba(255, 255, 255, 0);")
        self.label_42.setIndent(10)
        self.label_42.setObjectName("label_42")
        self.gridLayout_45.addWidget(self.label_42, 1, 0, 1, 2)
        self.stackedWidget_mos_right_2.addWidget(self.page_20)
        self.gridLayout_50.addWidget(self.stackedWidget_mos_right_2, 0, 0, 1, 1)
        self.stackedWidget_mos_right.addWidget(self.page_8)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_7.setContentsMargins(5, 0, 5, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem32 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_7.addItem(spacerItem32, 4, 0, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setStyleSheet("border-style:none;color:rgb(33, 33, 33);font-size: 17px;background-color: rgba(255, 255, 255, 0);")
        self.label_9.setIndent(10)
        self.label_9.setObjectName("label_9")
        self.gridLayout_7.addWidget(self.label_9, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.page_2)
        self.line.setStyleSheet("color:rgb(214, 214, 214)")
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
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
        spacerItem33 = QtWidgets.QSpacerItem(49, 13, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_7.addItem(spacerItem33, 0, 0, 1, 1)
        self.stackedWidget_mos_right.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setStyleSheet("QComboBox {\n"
"    border: 2px solid rgb(235, 235, 235); /* border: 宽度 线类型 颜色 */\n"
"    border-radius: 3px;\n"
"    height:25px;\n"
"    font-size: 14px;\n"
"    background-color: rgba(0, 150, 255, 150);\n"
"    border-radius:10px;\n"
"}\n"
"/*QComboBox::down-arrow\n"
"是 右面那个 \n"
"*/")
        self.page_3.setObjectName("page_3")
        self.gridLayout = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.line_3 = QtWidgets.QFrame(self.page_3)
        self.line_3.setStyleSheet("color:rgb(214, 214, 214)")
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_3.setMidLineWidth(1)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 3, 0, 1, 2)
        self.label_10 = QtWidgets.QLabel(self.page_3)
        self.label_10.setStyleSheet("border-style:none;color:rgb(33, 33, 33);font-size: 17px;background-color: rgba(255, 255, 255, 0);")
        self.label_10.setIndent(10)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 0, 2, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.page_3)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 2, 1)
        spacerItem34 = QtWidgets.QSpacerItem(832, 13, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem34, 0, 0, 1, 2)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.page_3)
        self.stackedWidget_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setStyleSheet("QAbstractItemView::item {\n"
"    min-height: 110px;\n"
"    min-width: 40px; \n"
"}\n"
"")
        self.page_9.setObjectName("page_9")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.page_9)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.treeWidget = QtWidgets.QTreeWidget(self.page_9)
        self.treeWidget.setStyleSheet("")
        self.treeWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.treeWidget.setDragDropOverwriteMode(False)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setUniformRowHeights(True)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setAllColumnsShowFocus(False)
        self.treeWidget.setWordWrap(False)
        self.treeWidget.setHeaderHidden(False)
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setObjectName("treeWidget")
        self.gridLayout_9.addWidget(self.treeWidget, 0, 0, 1, 1)
        self.stackedWidget_2.addWidget(self.page_9)
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setStyleSheet("")
        self.page_10.setObjectName("page_10")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.page_10)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.widget_2 = QtWidgets.QWidget(self.page_10)
        self.widget_2.setStyleSheet("QWidget{border-radius: 23px;border:2px solid rgb(0, 150, 255);}\n"
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
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_25.setObjectName("gridLayout_25")
        spacerItem35 = QtWidgets.QSpacerItem(199, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_25.addItem(spacerItem35, 0, 2, 1, 2)
        spacerItem36 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_25.addItem(spacerItem36, 3, 2, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_8.setStyleSheet("border-style:none;width:50px;height:50px;border-radius: 23px;background-color: rgba(235, 235, 235, 0);")
        self.pushButton_8.setText("")
        self.pushButton_8.setIcon(icon7)
        self.pushButton_8.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_25.addWidget(self.pushButton_8, 3, 0, 1, 1)
        spacerItem37 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_25.addItem(spacerItem37, 2, 2, 1, 2)
        self.comboBox_5 = QtWidgets.QComboBox(self.widget_2)
        self.comboBox_5.setMinimumSize(QtCore.QSize(120, 25))
        self.comboBox_5.setStyleSheet("border: 2px solid rgb(235, 235, 235);")
        self.comboBox_5.setObjectName("comboBox_5")
        self.gridLayout_25.addWidget(self.comboBox_5, 2, 5, 1, 1)
        spacerItem38 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_25.addItem(spacerItem38, 1, 2, 1, 2)
        self.label_21 = QtWidgets.QLabel(self.widget_2)
        self.label_21.setStyleSheet("border-style:none;font-size: 14px;")
        self.label_21.setObjectName("label_21")
        self.gridLayout_25.addWidget(self.label_21, 3, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.widget_2)
        self.label_20.setStyleSheet("border-style:none;font-size: 14px;")
        self.label_20.setObjectName("label_20")
        self.gridLayout_25.addWidget(self.label_20, 2, 1, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_13.setStyleSheet("border-style:none;width:50px;height:50px;border-radius: 23px;background-color: rgba(235, 235, 235, 0);")
        self.pushButton_13.setText("")
        self.pushButton_13.setIcon(icon8)
        self.pushButton_13.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_25.addWidget(self.pushButton_13, 1, 4, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_14.setStyleSheet("border-style:none;width:50px;height:50px;border-radius: 23px;background-color: rgba(235, 235, 235, 0);")
        self.pushButton_14.setText("")
        self.pushButton_14.setIcon(icon8)
        self.pushButton_14.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_25.addWidget(self.pushButton_14, 2, 4, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_5.setStyleSheet("border-style:none;width:50px;height:50px;border-radius: 23px;background-color: rgba(235, 235, 235, 0);")
        self.pushButton_5.setText("")
        self.pushButton_5.setIcon(icon9)
        self.pushButton_5.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_25.addWidget(self.pushButton_5, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.widget_2)
        self.label_11.setStyleSheet("border-style:none;font-size: 15px;")
        self.label_11.setObjectName("label_11")
        self.gridLayout_25.addWidget(self.label_11, 0, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_7.setStyleSheet("border-style:none;width:50px;height:50px;border-radius: 23px;background-color: rgba(235, 235, 235, 0);")
        self.pushButton_7.setText("")
        self.pushButton_7.setIcon(icon10)
        self.pushButton_7.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_25.addWidget(self.pushButton_7, 2, 0, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_15.setStyleSheet("border-style:none;width:50px;height:50px;border-radius: 23px;background-color: rgba(235, 235, 235, 0);")
        self.pushButton_15.setText("")
        self.pushButton_15.setIcon(icon8)
        self.pushButton_15.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_25.addWidget(self.pushButton_15, 3, 4, 1, 1)
        self.comboBox_6 = QtWidgets.QComboBox(self.widget_2)
        self.comboBox_6.setMinimumSize(QtCore.QSize(120, 25))
        self.comboBox_6.setStyleSheet("border: 2px solid rgb(235, 235, 235);")
        self.comboBox_6.setObjectName("comboBox_6")
        self.gridLayout_25.addWidget(self.comboBox_6, 3, 5, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.widget_2)
        self.label_19.setStyleSheet("border-style:none;font-size: 14px;")
        self.label_19.setObjectName("label_19")
        self.gridLayout_25.addWidget(self.label_19, 1, 1, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.widget_2)
        self.comboBox_3.setMinimumSize(QtCore.QSize(210, 25))
        self.comboBox_3.setStyleSheet("border: 2px solid rgb(235, 235, 235);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout_25.addWidget(self.comboBox_3, 0, 5, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_6.setStyleSheet("border-style:none;width:50px;height:50px;border-radius: 23px;background-color: rgba(235, 235, 235, 0);")
        self.pushButton_6.setText("")
        self.pushButton_6.setIcon(icon11)
        self.pushButton_6.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_25.addWidget(self.pushButton_6, 1, 0, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_12.setStyleSheet("border-style:none;width:50px;height:50px;border-radius: 23px;background-color: rgba(235, 235, 235, 0);")
        self.pushButton_12.setText("")
        self.pushButton_12.setIcon(icon8)
        self.pushButton_12.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_25.addWidget(self.pushButton_12, 0, 4, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.widget_2)
        self.comboBox_4.setMinimumSize(QtCore.QSize(120, 25))
        self.comboBox_4.setStyleSheet("border: 2px solid rgb(235, 235, 235);")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout_25.addWidget(self.comboBox_4, 1, 5, 1, 1)
        self.gridLayout_26.addWidget(self.widget_2, 0, 0, 1, 3)
        spacerItem39 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_26.addItem(spacerItem39, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.page_10)
        self.lineEdit.setStyleSheet("height:25px;border-radius: 5px;border:2px solid rgb(169, 169, 169);color: rgb(0, 0, 0);")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_26.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_2.setStyleSheet("height:25px;border-radius: 5px;width:70px;border:2px solid rgb(169, 169, 169);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_26.addWidget(self.pushButton_2, 1, 2, 1, 1)
        self.stackedWidget_2.addWidget(self.page_10)
        self.gridLayout.addWidget(self.stackedWidget_2, 4, 0, 1, 2)
        self.stackedWidget_mos_right.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_3.setContentsMargins(5, 0, 5, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem40 = QtWidgets.QSpacerItem(832, 13, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem40, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.page_4)
        self.label_12.setStyleSheet("border-style:none;color:rgb(33, 33, 33);font-size: 17px;background-color: rgba(255, 255, 255, 0);")
        self.label_12.setIndent(10)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 1, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.page_4)
        self.line_4.setStyleSheet("color:rgb(214, 214, 214)")
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_4.setMidLineWidth(1)
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
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
        spacerItem41 = QtWidgets.QSpacerItem(832, 393, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem41, 4, 0, 1, 1)
        self.stackedWidget_mos_right.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setStyleSheet("QComboBox {\n"
"    border: 2px solid rgb(235, 235, 235); /* border: 宽度 线类型 颜色 */\n"
"    border-radius: 3px;\n"
"    height:25px;\n"
"    font-size: 14px;\n"
"    background-color: rgba(0, 150, 255, 150);\n"
"    border-radius:10px;\n"
"}\n"
"/*QComboBox::down-arrow\n"
"是 右面那个 \n"
"*/")
        self.page_5.setObjectName("page_5")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_15.setContentsMargins(5, 0, 5, 0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.comboBox = QtWidgets.QComboBox(self.page_5)
        self.comboBox.setStyleSheet("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_15.addWidget(self.comboBox, 1, 1, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.page_5)
        self.stackedWidget.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.page.setObjectName("page")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.scrollArea = QtWidgets.QScrollArea(self.page)
        self.scrollArea.setStyleSheet("border-style:none;background-color: rgba(255, 255, 255, 0);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 822, 456))
        self.scrollAreaWidgetContents_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_23.setContentsMargins(5, 0, 5, 0)
        self.gridLayout_23.setObjectName("gridLayout_23")
        spacerItem42 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_23.addItem(spacerItem42, 6, 0, 1, 2)
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.widget.setStyleSheet("QWidget{background-color: rgba(255, 255, 255, 0);border-radius:15px;border: 2px solid rgb(0, 150, 255);}\n"
"QComboBox {\n"
"    border: 2px solid rgb(235, 235, 235); /* border: 宽度 线类型 颜色 */\n"
"    height:25px;\n"
"    font-size: 14px;\n"
"    background-color: rgba(0, 150, 255, 150);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"/*下拉框的样式*/\n"
"QComboBox QAbstractItemView \n"
"{\n"
"    outline: 0px solid gray;  /*取消选中虚线*/\n"
"    border: 1px solid rgb(31, 156, 255);\n"
"    color: rgb(66, 66, 66);\n"
"    background-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(0, 150, 255);\n"
"    border-radius:5px;\n"
"    height:50px;\n"
"}\n"
" /*选中每一项高度*/\n"
"QComboBox QAbstractItemView::item\n"
"{ \n"
"    height: 25px;\n"
"    border-radius:5px;\n"
" }\n"
"/*选中每一项的字体颜色和背景颜色*/\n"
"QComboBox QAbstractItemView::item:selected \n"
"{\n"
"    color: rgb(31,163,246);\n"
"    background-color: rgb(0, 150, 255);\n"
"    border-radius:5px;\n"
"}\n"
"/*QComboBox::down-arrow\n"
"是 右面那个 \n"
"*/\n"
"\n"
"\n"
"\n"
"/* QComboBox中的垂直滚动条 */\n"
"QComboBox QAbstractScrollArea QScrollBar:vertical {\n"
"    width: 13px;\n"
"    height: 5px;\n"
"    background-color: #d0d2d4;   /* 空白区域的背景色*/\n"
"    border-style:none;\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical {\n"
"    border-radius: 5px;   /* 圆角 */\n"
"    background: rgb(160,160,160);   /* 小方块的背景色深灰lightblue */\n"
"}\n"
"\n"
"QComboBox QAbstractScrollArea QScrollBar::handle:vertical:hover {\n"
"    background: rgb(255, 255, 255);   /* 越过小方块的背景色*/\n"
"}\n"
"\n"
"QPushButton{height:30px;background-color: rgba(255, 255, 255,0);border-radius:7px;border:2px solid rgb(255, 59, 0);font-size: 13.5px;}\n"
"QPushButton::hover{color: rgb(255, 59, 0)}\n"
"QPushButton::pressed{background-color: rgba(255, 0, 0, 100);}")
        self.widget.setObjectName("widget")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setStyleSheet("border-style:none;")
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.label_4.setObjectName("label_4")
        self.gridLayout_24.addWidget(self.label_4, 0, 0, 2, 1)
        self.fontComboBox = QtWidgets.QFontComboBox(self.widget)
        self.fontComboBox.setMaxVisibleItems(15)
        self.fontComboBox.setDuplicatesEnabled(False)
        self.fontComboBox.setObjectName("fontComboBox")
        self.gridLayout_24.addWidget(self.fontComboBox, 0, 1, 1, 3)
        self.pushButton_11 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_11.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_11.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_11.setStyleSheet("")
        self.pushButton_11.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_24.addWidget(self.pushButton_11, 1, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setStyleSheet("font-size: 14px;border-style:none;")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_24.addWidget(self.label_6, 1, 1, 1, 2)
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
        self.gridLayout_15.addWidget(self.stackedWidget, 6, 0, 1, 2)
        self.label_15 = QtWidgets.QLabel(self.page_5)
        self.label_15.setStyleSheet("border-style:none;color:rgb(33, 33, 33);font-size: 17px;background-color: rgba(255, 255, 255, 0);")
        self.label_15.setIndent(10)
        self.label_15.setObjectName("label_15")
        self.gridLayout_15.addWidget(self.label_15, 1, 0, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.page_5)
        self.line_5.setStyleSheet("color:rgb(214, 214, 214)")
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_5.setMidLineWidth(1)
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_5.setObjectName("line_5")
        self.gridLayout_15.addWidget(self.line_5, 3, 0, 2, 2)
        spacerItem43 = QtWidgets.QSpacerItem(832, 13, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_15.addItem(spacerItem43, 0, 0, 1, 2)
        self.stackedWidget_mos_right.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.page_6)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.widget_10 = QtWidgets.QWidget(self.page_6)
        self.widget_10.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.widget_10.setObjectName("widget_10")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.widget_10)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.widget_13 = QtWidgets.QWidget(self.widget_10)
        self.widget_13.setStyleSheet("QWidget{border-radius:15px;border:2px solid rgba(0, 150, 255, 230);}")
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
        self.gridLayout_12.setHorizontalSpacing(7)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.pushButton = QtWidgets.QPushButton(self.widget_11)
        self.pushButton.setStyleSheet("border-style:none;")
        self.pushButton.setText("")
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_12.addWidget(self.pushButton, 1, 0, 1, 1)
        spacerItem44 = QtWidgets.QSpacerItem(34, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_12.addItem(spacerItem44, 1, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.widget_11)
        self.label_16.setStyleSheet("font-size: 13px;border-style:none;")
        self.label_16.setObjectName("label_16")
        self.gridLayout_12.addWidget(self.label_16, 1, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.widget_11)
        self.widget_12 = QtWidgets.QWidget(self.widget_13)
        self.widget_12.setStyleSheet("QWidget{border-style:none;background-color: rgb(235, 235, 235);border-radius:15px;}\n"
"#pushButton_3{width:120px;height:30px;background-color: rgba(255, 255, 255,0);}\n"
"#pushButton_3::hover{background-color: rgb(255, 255, 255);}\n"
"#pushButton_3::pressed{background-color: rgba(0, 150, 255, 51);}")
        self.widget_12.setObjectName("widget_12")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.widget_12)
        self.gridLayout_17.setHorizontalSpacing(7)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.label_18 = QtWidgets.QLabel(self.widget_12)
        self.label_18.setStyleSheet("font-size: 13px;border-style:none;")
        self.label_18.setObjectName("label_18")
        self.gridLayout_17.addWidget(self.label_18, 0, 1, 1, 1)
        spacerItem45 = QtWidgets.QSpacerItem(34, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_17.addItem(spacerItem45, 0, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_12)
        self.pushButton_4.setStyleSheet("border-style:none;")
        self.pushButton_4.setText("")
        self.pushButton_4.setIcon(icon12)
        self.pushButton_4.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_17.addWidget(self.pushButton_4, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_12)
        self.pushButton_3.setStyleSheet("border-radius:7px;border:2px solid rgb(0, 150, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_17.addWidget(self.pushButton_3, 0, 3, 1, 1)
        self.verticalLayout_3.addWidget(self.widget_12)
        self.widget_14 = QtWidgets.QWidget(self.widget_13)
        self.widget_14.setStyleSheet("QWidget{border-style:none;background-color: rgb(235, 235, 235);border-radius:15px;}\n"
"#pushButton_10{width:120px;height:30px;background-color: rgba(255, 255, 255,0);}\n"
"#pushButton_10::hover{background-color: rgb(255, 255, 255);}\n"
"#pushButton_10::pressed{background-color: rgba(0, 150, 255, 51);}")
        self.widget_14.setObjectName("widget_14")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.widget_14)
        self.gridLayout_18.setHorizontalSpacing(2)
        self.gridLayout_18.setObjectName("gridLayout_18")
        spacerItem46 = QtWidgets.QSpacerItem(34, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_18.addItem(spacerItem46, 0, 3, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.widget_14)
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.gridLayout_18.addWidget(self.label_25, 0, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget_14)
        self.pushButton_9.setStyleSheet("border-style:none;")
        self.pushButton_9.setText("")
        self.pushButton_9.setIcon(icon13)
        self.pushButton_9.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_18.addWidget(self.pushButton_9, 0, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.widget_14)
        self.label_22.setStyleSheet("font-size: 13px;border-style:none;")
        self.label_22.setObjectName("label_22")
        self.gridLayout_18.addWidget(self.label_22, 0, 2, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.widget_14)
        self.pushButton_10.setStyleSheet("border-radius:7px;border:2px solid rgb(0, 150, 255);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_18.addWidget(self.pushButton_10, 0, 4, 1, 1)
        self.verticalLayout_3.addWidget(self.widget_14)
        self.gridLayout_19.addWidget(self.widget_13, 0, 0, 1, 1)
        spacerItem47 = QtWidgets.QSpacerItem(796, 368, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_19.addItem(spacerItem47, 1, 0, 1, 1)
        self.gridLayout_14.addWidget(self.widget_10, 3, 0, 1, 2)
        self.line_6 = QtWidgets.QFrame(self.page_6)
        self.line_6.setStyleSheet("color:rgb(214, 214, 214)")
        self.line_6.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_6.setMidLineWidth(1)
        self.line_6.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_6.setObjectName("line_6")
        self.gridLayout_14.addWidget(self.line_6, 2, 0, 1, 2)
        spacerItem48 = QtWidgets.QSpacerItem(832, 13, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_14.addItem(spacerItem48, 0, 0, 1, 2)
        self.label_17 = QtWidgets.QLabel(self.page_6)
        self.label_17.setStyleSheet("border-style:none;color:rgb(33, 33, 33);font-size: 17px;background-color: rgba(255, 255, 255, 0);")
        self.label_17.setIndent(10)
        self.label_17.setObjectName("label_17")
        self.gridLayout_14.addWidget(self.label_17, 1, 0, 1, 2)
        self.stackedWidget_mos_right.addWidget(self.page_6)
        self.gridLayout_13.addWidget(self.stackedWidget_mos_right, 0, 1, 1, 1)
        MOS.setCentralWidget(self.centralwidget)

        self.retranslateUi(MOS)
        self.stackedWidget_mos_right.setCurrentIndex(0)
        self.stackedWidget_gonggao.setCurrentIndex(1)
        self.stackedWidget_mos_right_2.setCurrentIndex(2)
        self.stackedWidget_gonggao_2.setCurrentIndex(1)
        self.stackedWidget_3.setCurrentIndex(0)
        self.stackedWidget_4.setCurrentIndex(0)
        self.fontComboBox_2.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.fontComboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MOS)


        # =============================================================================#

        #dir = QFileDialog()
        #dir.setFileMode(QFileDialog.DirectoryOnly)
        #home_dir = str(Path.home())
        #fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)

        self.progressBar_2.setMinimum(0)
        self.progressBar_2.setMaximum(99)
        self.progressBar_2.setValue(0)
        self.stackedWidget_mos_right.setCurrentIndex(0)
        # 启动线程
        self.a = MOS_file()
        self.a.sinOut.connect(self.MOS_file_return)
        self.a.sinOut_font.connect(self.MOS_file_return_font)
        self.a.start()
        # =============================================================================#

    # =================================分割线===================================#

    def click_pushButton_home(self):
        self.stackedWidget_mos_right.setCurrentIndex(0)
        pushButton_home_true = ("QWidget\n"
                                 "{\n"
                                 "    background-color: rgba(231, 230, 228, 100);\n"
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
                                 "    border:2px solid rgba(229, 228, 226, 0);\n"
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
                                 "    border:2px solid rgba(229, 228, 226, 0);background-color: rgb(192, 192, 192);\n"
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
        self.stackedWidget_mos_right.setCurrentIndex(2)
        pushButton_lianji_true = ("QWidget\n"
                                 "{\n"
                                 "    background-color: rgba(231, 230, 228, 100);\n"
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
                                 "    border:2px solid rgba(229, 228, 226, 0);\n"
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
                                 "#pushButton_lianji\n"
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
                                 "    border:2px solid rgba(229, 228, 226, 0);background-color: rgb(192, 192, 192);\n"
                                 "}\n"
                                 "#pushButton_lianji::hover\n"
                                 "{\n"
                                 "    background-color: rgb(192, 192, 192);\n"
                                 "}\n"
                                 "#pushButton_lianji::pressed\n"
                                 "{\n"
                                 "    border:2px solid rgb(0, 150, 255);\n"
                                 "}")
        self.widget_mos_left.setStyleSheet(pushButton_lianji_true)

    def click_pushButton_xiazai(self):
        self.stackedWidget_mos_right.setCurrentIndex(3)
        pushButton_xiazai_true = ("QWidget\n"
                                 "{\n"
                                 "    background-color: rgba(231, 230, 228, 100);\n"
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
                                 "    border:2px solid rgba(229, 228, 226, 0);\n"
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
                                 "#pushButton_xiazai\n"
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
                                 "    border:2px solid rgba(229, 228, 226, 0);background-color: rgb(192, 192, 192);\n"
                                 "}\n"
                                 "#pushButton_xiazai::hover\n"
                                 "{\n"
                                 "    background-color: rgb(192, 192, 192);\n"
                                 "}\n"
                                 "#pushButton_xiazai::pressed\n"
                                 "{\n"
                                 "    border:2px solid rgb(0, 150, 255);\n"
                                 "}")
        self.widget_mos_left.setStyleSheet(pushButton_xiazai_true)

    def click_pushButton_music(self):
        self.stackedWidget_mos_right.setCurrentIndex(4)
        pushButton_music_true = ("QWidget\n"
                                 "{\n"
                                 "    background-color: rgba(231, 230, 228, 100);\n"
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
                                 "    border:2px solid rgba(229, 228, 226, 0);\n"
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
                                 "#pushButton_music\n"
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
                                 "    border:2px solid rgba(229, 228, 226, 0);background-color: rgb(192, 192, 192);\n"
                                 "}\n"
                                 "#pushButton_music::hover\n"
                                 "{\n"
                                 "    background-color: rgb(192, 192, 192);\n"
                                 "}\n"
                                 "#pushButton_music::pressed\n"
                                 "{\n"
                                 "    border:2px solid rgb(0, 150, 255);\n"
                                 "}")
        self.widget_mos_left.setStyleSheet(pushButton_music_true)

    def click_pushButton_shezhi(self):
        self.stackedWidget_mos_right.setCurrentIndex(5)
        pushButton_shezhi_true = ("QWidget\n"
                                 "{\n"
                                 "    background-color: rgba(231, 230, 228, 100);\n"
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
                                 "    border:2px solid rgba(229, 228, 226, 0);\n"
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
                                 "#pushButton_shezhi\n"
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
                                 "    border:2px solid rgba(229, 228, 226, 0);background-color: rgb(192, 192, 192);\n"
                                 "}\n"
                                 "#pushButton_shezhi::hover\n"
                                 "{\n"
                                 "    background-color: rgb(192, 192, 192);\n"
                                 "}\n"
                                 "#pushButton_shezhi::pressed\n"
                                 "{\n"
                                 "    border:2px solid rgb(0, 150, 255);\n"
                                 "}")
        self.widget_mos_left.setStyleSheet(pushButton_shezhi_true)

    def click_pushButton_about(self):
        self.stackedWidget_mos_right.setCurrentIndex(6)
        pushButton_about_true = ("QWidget\n"
                                 "{\n"
                                 "    background-color: rgba(231, 230, 228, 100);\n"
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
                                 "    border:2px solid rgba(229, 228, 226, 0);\n"
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
                                 "#pushButton_about\n"
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
                                 "    border:2px solid rgba(229, 228, 226, 0);background-color: rgb(192, 192, 192);\n"
                                 "}\n"
                                 "#pushButton_about::hover\n"
                                 "{\n"
                                 "    background-color: rgb(192, 192, 192);\n"
                                 "}\n"
                                 "#pushButton_about::pressed\n"
                                 "{\n"
                                 "    border:2px solid rgb(0, 150, 255);\n"
                                 "}")
        self.widget_mos_left.setStyleSheet(pushButton_about_true)

    def click_pushButton_zanshuzuozhe(self):
        webbrowser.open("https://afdian.net/@David_MOS")

    def click_pushButton_qhqqi_blog(self):
        webbrowser.open("https://blog.qhqqi.top")

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
        self.textBrowser_gonggao_left_txt.setHtml(str)
        self.stackedWidget_gonggao.setCurrentIndex(0)
        self.progressBar_2.setMinimum(0)
        self.progressBar_2.setMaximum(99)
        self.progressBar_2.setValue(0)

    def gonggao_text(self, text1, text2):
        _translate = QtCore.QCoreApplication.translate
        self.label_gonggao_left_txt.setText(_translate(text1,text2))



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
        self.label_gonggao_left_txt.setFont(QtGui.QFont(self.fontComboBox.currentText()))



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
        self.pushButton_11.setFont(QtGui.QFont(self.fontComboBox.currentText()))


        self.comboBox_gonggao_right.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.comboBox_2.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.comboBox_3.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.comboBox_4.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.comboBox_5.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.comboBox_6.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.comboBox.setFont(QtGui.QFont(self.fontComboBox.currentText()))
        self.fontComboBox.setFont(QtGui.QFont(self.fontComboBox.currentText()))


        self.progressBar.setFont(QtGui.QFont(self.fontComboBox.currentText()))

        # 修改在json中的字体
        MOS_file_json =os.path.join(file,".MOS","MOS.json")
        try:
            with open(MOS_file_json, 'r+', encoding='utf-8') as f:
                b = json.load(f)
                b['font'] = self.fontComboBox.currentText()
            with open(MOS_file_json, 'w+', encoding='utf-8') as f:
                json.dump(b, f, sort_keys=True, indent=4, separators=(',', ': '))
                b1 = str(b)
                print('默认字体：' + b1)
        except KeyError:
            print("json文件有问题")
        except json.decoder.JSONDecodeError:
            print("json数据异常")


    def click_pushButton_shezhi_fond_moren(self):
        str1 = 'Academy Engraved LET'
        self.label_4.setFont(QtGui.QFont(str1))
        self.label_6.setFont(QtGui.QFont(str1))
        self.label_mos_left_top_user.setFont(QtGui.QFont(str1))
        self.label_mos_left_top_add.setFont(QtGui.QFont(str1))
        self.label_gonggao_left_txt.setFont(QtGui.QFont(str1))
        self.label_2.setFont(QtGui.QFont(str1))
        self.progressBar_2.setFont(QtGui.QFont(str1))
        self.label__gonggao_right_txt.setFont(QtGui.QFont(str1))
        self.label_3.setFont(QtGui.QFont(str1))
        self.progressBar.setFont(QtGui.QFont(str1))
        self.label_7.setFont(QtGui.QFont(str1))
        self.label_9.setFont(QtGui.QFont(str1))
        self.label_8.setFont(QtGui.QFont(str1))
        self.label_10.setFont(QtGui.QFont(str1))
        self.label_11.setFont(QtGui.QFont(str1))
        self.label_19.setFont(QtGui.QFont(str1))
        self.label_20.setFont(QtGui.QFont(str1))
        self.label_21.setFont(QtGui.QFont(str1))
        self.label_12.setFont(QtGui.QFont(str1))
        self.label_13.setFont(QtGui.QFont(str1))
        self.label_15.setFont(QtGui.QFont(str1))
        self.label_17.setFont(QtGui.QFont(str1))
        self.label.setFont(QtGui.QFont(str1))
        self.label_16.setFont(QtGui.QFont(str1))
        self.label_18.setFont(QtGui.QFont(str1))
        self.label_22.setFont(QtGui.QFont(str1))
        self.label_gonggao_left_txt.setFont(QtGui.QFont(str1))
        self.pushButton_home.setFont(QtGui.QFont(str1))
        self.pushButton_lianji.setFont(QtGui.QFont(str1))
        self.pushButton_music.setFont(QtGui.QFont(str1))
        self.pushButton_shezhi.setFont(QtGui.QFont(str1))
        self.pushButton_xiazai.setFont(QtGui.QFont(str1))
        self.pushButton_about.setFont(QtGui.QFont(str1))
        self.pushButton__gonggao_start.setFont(QtGui.QFont(str1))
        self.pushButton_5.setFont(QtGui.QFont(str1))
        self.pushButton_6.setFont(QtGui.QFont(str1))
        self.pushButton_7.setFont(QtGui.QFont(str1))
        self.pushButton_8.setFont(QtGui.QFont(str1))
        self.pushButton_11.setFont(QtGui.QFont(str1))
        self.comboBox_gonggao_right.setFont(QtGui.QFont(str1))
        self.comboBox_2.setFont(QtGui.QFont(str1))
        self.comboBox_3.setFont(QtGui.QFont(str1))
        self.comboBox_4.setFont(QtGui.QFont(str1))
        self.comboBox_5.setFont(QtGui.QFont(str1))
        self.comboBox_6.setFont(QtGui.QFont(str1))
        self.comboBox.setFont(QtGui.QFont(str1))
        self.fontComboBox.setFont(QtGui.QFont(str1))
        self.progressBar.setFont(QtGui.QFont(str1))

        # 修改在json中的字体
        MOS_file_json =os.path.join(".MOS","MOS.json")
        try:
            with open(MOS_file_json, 'r+', encoding='utf-8') as f:
                b = json.load(f)
                b['font'] = str1
            with open(MOS_file_json, 'w+', encoding='utf-8') as f:
                json.dump(b, f, sort_keys=True, indent=4, separators=(',', ': '))
                b1 = str(b)
                print('默认字体：' + b1)
        except KeyError:
            print("json文件有问题")
        except json.decoder.JSONDecodeError:
            print("json数据异常")

 

        
    def MOS_file_return_font(self, a):
        print(str)
        str1 = str(a)
        self.label_4.setFont(QtGui.QFont(str1))
        self.label_6.setFont(QtGui.QFont(str1))
        self.label_mos_left_top_user.setFont(QtGui.QFont(str1))
        self.label_mos_left_top_add.setFont(QtGui.QFont(str1))
        self.label_gonggao_left_txt.setFont(QtGui.QFont(str1))
        self.label_2.setFont(QtGui.QFont(str1))
        self.progressBar_2.setFont(QtGui.QFont(str1))
        self.label__gonggao_right_txt.setFont(QtGui.QFont(str1))
        self.label_3.setFont(QtGui.QFont(str1))
        self.progressBar.setFont(QtGui.QFont(str1))
        self.label_7.setFont(QtGui.QFont(str1))
        self.label_9.setFont(QtGui.QFont(str1))
        self.label_8.setFont(QtGui.QFont(str1))
        self.label_10.setFont(QtGui.QFont(str1))
        self.label_11.setFont(QtGui.QFont(str1))
        self.label_19.setFont(QtGui.QFont(str1))
        self.label_20.setFont(QtGui.QFont(str1))
        self.label_21.setFont(QtGui.QFont(str1))
        self.label_12.setFont(QtGui.QFont(str1))
        self.label_13.setFont(QtGui.QFont(str1))
        self.label_15.setFont(QtGui.QFont(str1))
        self.label_17.setFont(QtGui.QFont(str1))
        self.label.setFont(QtGui.QFont(str1))
        self.label_16.setFont(QtGui.QFont(str1))
        self.label_18.setFont(QtGui.QFont(str1))
        self.label_22.setFont(QtGui.QFont(str1))
        self.label_gonggao_left_txt.setFont(QtGui.QFont(str1))
        self.pushButton_home.setFont(QtGui.QFont(str1))
        self.pushButton_lianji.setFont(QtGui.QFont(str1))
        self.pushButton_music.setFont(QtGui.QFont(str1))
        self.pushButton_shezhi.setFont(QtGui.QFont(str1))
        self.pushButton_xiazai.setFont(QtGui.QFont(str1))
        self.pushButton_about.setFont(QtGui.QFont(str1))
        self.pushButton__gonggao_start.setFont(QtGui.QFont(str1))
        self.pushButton_5.setFont(QtGui.QFont(str1))
        self.pushButton_6.setFont(QtGui.QFont(str1))
        self.pushButton_7.setFont(QtGui.QFont(str1))
        self.pushButton_8.setFont(QtGui.QFont(str1))
        self.pushButton_11.setFont(QtGui.QFont(str1))
        self.comboBox_gonggao_right.setFont(QtGui.QFont(str1))
        self.comboBox_2.setFont(QtGui.QFont(str1))
        self.comboBox_3.setFont(QtGui.QFont(str1))
        self.comboBox_4.setFont(QtGui.QFont(str1))
        self.comboBox_5.setFont(QtGui.QFont(str1))
        self.comboBox_6.setFont(QtGui.QFont(str1))
        self.comboBox.setFont(QtGui.QFont(str1))
        self.fontComboBox.setFont(QtGui.QFont(str1))
        self.progressBar.setFont(QtGui.QFont(str1)) 




    def MOS_file_return(self, str):
        if str == "OK!":
            self.g = gonggao()
            self.g.sinOut_gonggao_ok.connect(self.gonggao)
            self.g.sinOut_gonggao_jindu.connect(self.gonggao_jindu)
            self.g.sinOut_gonggao_error.connect(self.gonggao_error)
            self.g.sinOut_gonggao_text.connect(self.gonggao_text)
            self.g.start()
        elif str == "ERROR_PermissionError" :
            #self.second = MOS_UI2.Ui_MainWindow()
            #self.second.show()
            a = QMessageBox.critical(None,"错误","配置文件有问题，您是否自行修改了文件？。即将退出程序",QMessageBox.StandardButton.Yes,QMessageBox.StandardButton.Yes)
            if a == QMessageBox.StandardButton.Yes:  # 检查是否点了OK按钮
                quit()
            #reply = QMessageBox()
            #reply.setText("Some random text.")
            #reply.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        elif str == 'KeyError' :
            a = QMessageBox.critical(None,"错误","配置文件有问题，您是否自行修改了文件？。即将退出程序",QMessageBox.StandardButton.Yes,QMessageBox.StandardButton.Yes)
            if a == QMessageBox.StandardButton.Yes: #检查是否点了OK按钮
                quit()

    
    
    # =================================分割线===================================#






    def retranslateUi(self, MOS):
        _translate = QtCore.QCoreApplication.translate
        MOS.setWindowTitle(_translate("MOS", "MOS ll 启动器"))
        self.label_mos_left_top_add.setText(_translate("MOS", "点击添加"))
        self.label_mos_left_top_user.setText(_translate("MOS", "无用户"))
        self.pushButton_home.setText(_translate("MOS", "主页"))
        self.pushButton_lianji.setText(_translate("MOS", "联机"))
        self.pushButton_xiazai.setText(_translate("MOS", "下载"))
        self.pushButton_music.setText(_translate("MOS", "音乐"))
        self.pushButton_shezhi.setText(_translate("MOS", "设置"))
        self.pushButton_about.setText(_translate("MOS", "关于"))
        self.label_mosll.setText(_translate("MOS", "MOS II"))
        self.label__gonggao_right_txt.setText(_translate("MOS", "<html><head/><body><p>启动游戏 <span style=\" color:#0096ff;\">•等待启动</span></p></body></html>"))
        self.pushButton__gonggao_start.setText(_translate("MOS", "启动游戏"))
        self.pushButton_16.setText(_translate("MOS", "版本列表"))
        self.label_3.setText(_translate("MOS", "启动的图片"))
        self.label_7.setText(_translate("MOS", "启动君：待命中……"))
        self.pushButton_17.setText(_translate("MOS", "版本设置"))
        self.label_2.setText(_translate("MOS", "正在加载\n"
"\n"
"当前步骤：下载公告……请稍后\n"
""))
        self.label_gonggao_left_txt.setText(_translate("MOS", "<html><head/><body><p>官方公告 <span style=\" color:#55f976;\">•正在加载中</span></p></body></html>"))
        self.label__gonggao_right_txt_2.setText(_translate("MOS", "<html><head/><body><p>启动游戏 <span style=\" color:#0096ff;\">•等待启动</span></p></body></html>"))
        self.pushButton__gonggao_start_2.setText(_translate("MOS", "启动游戏"))
        self.pushButton_18.setText(_translate("MOS", "版本列表"))
        self.label_5.setText(_translate("MOS", "启动的图片"))
        self.label_14.setText(_translate("MOS", "启动君：待命中……"))
        self.pushButton_19.setText(_translate("MOS", "版本设置"))
        self.label_23.setText(_translate("MOS", "正在加载\n"
"\n"
"当前步骤：下载公告……请稍后\n"
""))
        self.label_gonggao_left_txt_2.setText(_translate("MOS", "<html><head/><body><p>官方公告 <span style=\" color:#55f976;\">•正在加载中</span></p></body></html>"))
        self.label_26.setText(_translate("MOS", "游戏目录"))
        self.label_24.setText(_translate("MOS", "版本列表"))
        self.label_43.setText(_translate("MOS", "游戏目录下的游戏"))
        self.label_27.setText(_translate("MOS", "下载"))
        self.comboBox_7.setItemText(0, _translate("MOS", "游戏下载"))
        self.comboBox_7.setItemText(1, _translate("MOS", "Mod下载"))
        self.comboBox_7.setItemText(2, _translate("MOS", "整合包下载"))
        self.comboBox_7.setItemText(3, _translate("MOS", "世界下载"))
        self.comboBox_7.setItemText(4, _translate("MOS", "下载/安装/已完成"))
        self.treeWidget_2.setSortingEnabled(False)
        self.treeWidget_2.headerItem().setText(0, _translate("MOS", "版本列表"))
        self.treeWidget_2.headerItem().setText(1, _translate("MOS", "种类"))
        self.label_28.setText(_translate("MOS", "Quilt\n"
"模组加载器"))
        self.label_29.setText(_translate("MOS", "Optifine\n"
"高清修复"))
        self.label_30.setText(_translate("MOS", "Forge\n"
"模组加载器"))
        self.label_31.setText(_translate("MOS", "Fabric\n"
"模组加载器"))
        self.comboBox_11.setItemText(0, _translate("MOS", "1.0.1"))
        self.comboBox_11.setItemText(1, _translate("MOS", "2.0.2"))
        self.lineEdit_2.setPlaceholderText(_translate("MOS", "版本名"))
        self.pushButton_28.setText(_translate("MOS", "安装"))
        self.label_32.setText(_translate("MOS", "音乐"))
        self.label_33.setText(_translate("MOS", "音乐 正在开发中……\n"
"不要着急啦 你的赞助就是我更新的动力！嘻嘻～"))
        self.comboBox_12.setItemText(0, _translate("MOS", "启动器设置"))
        self.comboBox_12.setItemText(1, _translate("MOS", "游戏设置"))
        self.label_34.setText(_translate("MOS", "<html><head/><body style=\"line-height:1px;\"><p style=\"line-height:1px;\"><span style=\" font-size:20pt;\">启动器字体</span></p><p  style=\"line-height:1px;\">在这里 你可以自定义启动器字体 有的字体相差很小，导致有人可能认为<span style=\" font-style:italic;line-height:1px;\">字体没有更改</span>，其实不是的</p></body></html>"))
        self.pushButton_29.setText(_translate("MOS", "恢复默认"))
        self.label_35.setText(_translate("MOS", "Hello Minecraft Optimal Starter 2 !"))
        self.label_36.setText(_translate("MOS", "设置"))
        self.label_37.setText(_translate("MOS", "关于："))
        self.label_38.setText(_translate("MOS", "MOS启动器\n"
"版本V2.0.3-alpha"))
        self.label_39.setText(_translate("MOS", "MOS唯一开发者 David"))
        self.pushButton_32.setText(_translate("MOS", "赞助作者"))
        self.label_41.setText(_translate("MOS", "MOS网站支持、测试小组负责人 HeimNad"))
        self.pushButton_34.setText(_translate("MOS", "打开博客"))
        self.label_42.setText(_translate("MOS", "关于"))
        self.label_9.setText(_translate("MOS", "联机模块"))
        self.label_8.setText(_translate("MOS", "联机模块正在开发中……\n"
"不要着急啦 你的赞助就是我更新的动力！嘻嘻～"))
        self.label_10.setText(_translate("MOS", "下载"))
        self.comboBox_2.setItemText(0, _translate("MOS", "游戏下载"))
        self.comboBox_2.setItemText(1, _translate("MOS", "Mod下载"))
        self.comboBox_2.setItemText(2, _translate("MOS", "整合包下载"))
        self.comboBox_2.setItemText(3, _translate("MOS", "世界下载"))
        self.comboBox_2.setItemText(4, _translate("MOS", "下载/安装/已完成"))
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.headerItem().setText(0, _translate("MOS", "版本列表"))
        self.treeWidget.headerItem().setText(1, _translate("MOS", "种类"))
        self.label_21.setText(_translate("MOS", "Quilt\n"
"模组加载器"))
        self.label_20.setText(_translate("MOS", "Optifine\n"
"高清修复"))
        self.label_11.setText(_translate("MOS", "Forge\n"
"模组加载器"))
        self.label_19.setText(_translate("MOS", "Fabric\n"
"模组加载器"))
        self.comboBox_4.setItemText(0, _translate("MOS", "1.0.1"))
        self.comboBox_4.setItemText(1, _translate("MOS", "2.0.2"))
        self.lineEdit.setPlaceholderText(_translate("MOS", "版本名"))
        self.pushButton_2.setText(_translate("MOS", "安装"))
        self.label_12.setText(_translate("MOS", "音乐"))
        self.label_13.setText(_translate("MOS", "音乐 正在开发中……\n"
"不要着急啦 你的赞助就是我更新的动力！嘻嘻～"))
        self.comboBox.setItemText(0, _translate("MOS", "启动器设置"))
        self.comboBox.setItemText(1, _translate("MOS", "游戏设置"))
        self.label_4.setText(_translate("MOS", "<html><head/><body style=\"line-height:1px;\"><p style=\"line-height:1px;\"><span style=\" font-size:20pt;\">启动器字体</span></p><p  style=\"line-height:1px;\">在这里 你可以自定义启动器字体 有的字体相差很小，导致有人可能认为<span style=\" font-style:italic;line-height:1px;\">字体没有更改</span>，其实不是的</p></body></html>"))
        self.pushButton_11.setText(_translate("MOS", "恢复默认"))
        self.label_6.setText(_translate("MOS", "Hello Minecraft Optimal Starter 2 !"))
        self.label_15.setText(_translate("MOS", "设置"))
        self.label.setText(_translate("MOS", "关于："))
        self.label_16.setText(_translate("MOS", "MOS启动器\n"
"版本V2.0.3-alpha"))
        self.label_18.setText(_translate("MOS", "MOS唯一开发者 David"))
        self.pushButton_3.setText(_translate("MOS", "赞助作者"))
        self.label_22.setText(_translate("MOS", "MOS网站支持、测试小组负责人 HeimNad"))
        self.pushButton_10.setText(_translate("MOS", "打开博客"))
        self.label_17.setText(_translate("MOS", "关于"))





        
        # =================================分割线===================================#

        self.pushButton_home.clicked.connect(self.click_pushButton_home)
        self.pushButton_lianji.clicked.connect(self.click_pushButton_lianji)
        self.pushButton_xiazai.clicked.connect(self.click_pushButton_xiazai)
        self.pushButton_music.clicked.connect(self.click_pushButton_music)
        self.pushButton_shezhi.clicked.connect(self.click_pushButton_shezhi)
        self.pushButton_about.clicked.connect(self.click_pushButton_about)
        self.pushButton_3.clicked.connect(self.click_pushButton_zanshuzuozhe)
        self.pushButton_10.clicked.connect(self.click_pushButton_qhqqi_blog)
        self.pushButton_11.clicked.connect(self.click_pushButton_shezhi_fond_moren)
        # 在‘……………………’里显示所有
        # 为字体选择控件 连接槽
        self.fontComboBox.currentIndexChanged.connect(self.setfont)



class gonggao(QThread):
    '''获取公告'''
    sinOut_gonggao_ok = pyqtSignal(str)
    sinOut_gonggao_jindu = pyqtSignal(str)
    sinOut_gonggao_error = pyqtSignal(str)
    sinOut_gonggao_text = pyqtSignal(str,str)

    def __init__(self):
        super(gonggao, self).__init__()

    def run(self):
        import requests
        import time
        import linecache

        self.sinOut_gonggao_jindu.emit('10')
        print("开始获取公告")
        url = 'https://file.skyworldstudio.top/d/SoftwareRelease/MOS/announcement.html'
        self.sinOut_gonggao_jindu.emit('30')
        try:
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
                self.sinOut_gonggao_text.emit("MOS", "<html><head/><body><p>官方公告 <span style=\" color:#55f976;\">•公告获取成功！✓</span></p></body></html>")
                print("请求成功")
                        
            elif r.status_code != 200:
                if r.status_code == 404:
                    print("公告请求失败，状态码为404")
                    if os.path.isfile(a)==True:
                        gangshu = len(linecache.getlines(a))    # 统计行数
                        gangshu1 = 0
                        gonggao = ''
                        while gangshu1 <= gangshu:
                            g = linecache.getline(a,gangshu1)
                            gonggao = gonggao + g
                            gangshu1 += 1
                        print(gonggao)
                        gonggao = str(gonggao)
                        self.sinOut_gonggao_text.emit("MOS", "<html><head/><body><p>官方公告 <span style=\" color:rgb(255, 38, 0);\">•获取失败！✗ 404找不到文件 以为您自动显示上次获取到的内容</span></p></body></html>")
                        self.sinOut_gonggao_error.emit(gonggao) 
                    else:
                        self.sinOut_gonggao_error.emit("404，找不到文件")
                elif r.status_code == 403:
                    print("公告请求失败，状态码为403")
                    if os.path.isfile(a)==True:
                        gangshu = len(linecache.getlines(a))    # 统计行数
                        gangshu1 = 0
                        gonggao = ''
                        while gangshu1 <= gangshu:
                            g = linecache.getline(a,gangshu1)
                            gonggao = gonggao + g
                            gangshu1 += 1
                        print(gonggao)
                        gonggao = str(gonggao)
                        self.sinOut_gonggao_text.emit("MOS", "<html><head/><body><p>官方公告 <span style=\" color:rgb(255, 38, 0);\">•获取失败！✗ 403无权访问 以为您自动显示上次获取到的内容</span></p></body></html>")
                        self.sinOut_gonggao_error.emit(gonggao) 
                    else:
                        self.sinOut_gonggao_error.emit("403，无权限访问")

                else:
                    gonggao_r_status_code = r.status_code
                    gonggao_r_status_code1 = str(gonggao_r_status_code)
                    gonggao_111 = ("公告请求失败，状态码为" + gonggao_r_status_code1)
                    print(gonggao_111)
                    if os.path.isfile(a)==True:
                        gangshu = len(linecache.getlines(a))    # 统计行数
                        gangshu1 = 0
                        gonggao = ''
                        while gangshu1 <= gangshu:
                            g = linecache.getline(a,gangshu1)
                            gonggao = gonggao + g
                            gangshu1 += 1
                        print(gonggao)
                        gonggao = str(gonggao)
                        self.sinOut_gonggao_text.emit("MOS", "<html><head/><body><p>官方公告 <span style=\" color:rgb(255, 38, 0);\">•获取失败！✗ 403无权访问 以为您自动显示上次获取到的内容</span></p></body></html>")
                        self.sinOut_gonggao_error.emit(gonggao) 
                    else:
                        self.sinOut_gonggao_error.emit(gonggao_111)
                


        except requests.exceptions.ConnectTimeout:
            # self.sinOut_gonggao_error.emit("请求超时")
            a = os.path.join(".MOS","Html","announcement.html")
            if os.path.isfile(a)==True:
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
                self.sinOut_gonggao_text.emit("MOS", "<html><head/><body><p>官方公告 <span style=\" color:rgb(255, 38, 0);\">•获取失败！✗ 请求超时 以为您自动显示上次获取到的内容</span></p></body></html>")
                self.sinOut_gonggao_error.emit(gonggao)

            else:
                self.sinOut_gonggao_error.emit("请求超时")
                self.sinOut_gonggao_text.emit("MOS", "<html><head/><body><p>官方公告 <span style=\" color:rgb(255, 38, 0);\">•获取失败！✗ 请求超时 无缓存可加载</span></p></body></html>")

        except requests.exceptions.ReadTimeout:
            # self.sinOut_gonggao_error.emit("读取超时")
            a = os.path.join(".MOS","Html","announcement.html")
            if os.path.isfile(a)==True:
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
                self.sinOut_gonggao_text.emit("MOS", "<html><head/><body><p>官方公告 <span style=\" color:rgb(255, 38, 0);\">•获取失败！✗ 读取超时 以为您自动显示上次获取到的内容</span></p></body></html>")
                self.sinOut_gonggao_error.emit(gonggao)

            else:
                self.sinOut_gonggao_error.emit("读取超时")
                self.sinOut_gonggao_text.emit("MOS", "<html><head/><body><p>官方公告 <span style=\" color:rgb(255, 38, 0);\">•获取失败！✗ 读取超时 无缓存可加载</span></p></body></html>")

        except requests.exceptions.SSLError:
            # self.sinOut_gonggao_error.emit("SSL错误")
            a = os.path.join(".MOS","Html","announcement.html")
            if os.path.isfile(a)==True:
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
                self.sinOut_gonggao_text.emit("MOS", "<html><head/><body><p>官方公告 <span style=\" color:rgb(255, 38, 0);\">•获取失败！✗ SSL证书错误 以为您自动显示上次获取到的内容</span></p></body></html>")
                self.sinOut_gonggao_error.emit(gonggao)

            else:
                self.sinOut_gonggao_error.emit("SSL证书错误")
                self.sinOut_gonggao_text.emit("MOS", "<html><head/><body><p>官方公告 <span style=\" color:rgb(255, 38, 0);\">•获取失败！✗ SSL证书错误 无缓存可加载</span></p></body></html>")

        except requests.exceptions.ConnectionError:
            # self.sinOut_gonggao_error.emit("连接错误\n")            
            a = os.path.join(".MOS","Html","announcement.html")
            if os.path.isfile(a)==True:
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
                self.sinOut_gonggao_text.emit("MOS", "<html><head/><body><p>官方公告 <span style=\" color:rgb(255, 38, 0);\">•获取失败！✗ 连接错误 以为您自动显示上次获取到的内容</span></p></body></html>")
                self.sinOut_gonggao_error.emit(gonggao)

            else:
                self.sinOut_gonggao_error.emit("连接错误")
                self.sinOut_gonggao_text.emit("MOS", "<html><head/><body><p>官方公告 <span style=\" color:rgb(255, 38, 0);\">•获取失败！✗ 连接错误 无缓存可加载</span></p></body></html>")
        except:
            traceback.print_exc()
            print("请求失败 未知错误")
            a = os.path.join(".MOS","Html","announcement.html")
            if os.path.isfile(a)==True:
                gangshu = len(linecache.getlines(a))    # 统计行数
                gangshu1 = 0
                gonggao = ''
                while gangshu1 <= gangshu:
                    g = linecache.getline(a,gangshu1)
                    gonggao = gonggao + g
                    gangshu1 += 1
                print(gonggao)
                gonggao = str(gonggao)
                self.sinOut_gonggao_text.emit("MOS", "<html><head/><body><p>官方公告 <span style=\" color:rgb(255, 38, 0);\">•获取失败！✗ 未知错误 以为您自动显示上次获取到的内容</span></p></body></html>")
                self.sinOut_gonggao_error.emit(gonggao)
            else:
                self.sinOut_gonggao_text.emit("MOS", "<html><head/><body><p>官方公告 <span style=\" color:rgb(255, 38, 0);\">•获取失败！✗ 未知错误 无缓存可加载</span></p></body></html>")


class MOS_file(QThread):
    '''初始化文件/设置'''
    sinOut = pyqtSignal(str)
    sinOut_font = pyqtSignal(str) 
    def __init__(self):
        super(MOS_file, self).__init__()

    def run(self):
        import os,sys,platform
        print("文件初始化线程开始")



        try:
            #a = sys.platform()
            #print(a)
            #if a = 
            
            MOS_file_1=os.path.join(file,".minecraft","mods")
            os.makedirs(MOS_file_1, exist_ok=True)

            MOS_file_1 =os.path.join(file,".minecraft","logs")
            os.makedirs(MOS_file_1, exist_ok=True)

            MOS_file_1 =os.path.join(file,".minecraft","versions")
            os.makedirs(MOS_file_1, exist_ok=True)

            MOS_file_1 =os.path.join(file,".MOS","Html")
            os.makedirs(MOS_file_1, exist_ok=True)

            MOS_file_1 =os.path.join(file,".MOS","Java")
            os.makedirs(MOS_file_1, exist_ok=True)
        
            MOS_file_1 =os.path.join(file,".MOS","Music")
            os.makedirs(MOS_file_1, exist_ok=True)

            MOS_file_json =os.path.join(file,".MOS","MOS.json")

            if os.path.isfile(MOS_file_json)==True:
                MOS_first_run = "NoFirst"
                print("程序不是第一次运行")
            elif os.path.isfile(MOS_file_1)==False:
                MOS_first_run = "First"
                MOS_json=open(MOS_file_json,"w")
                MOS_json.close()
                print("程序是第一次运行")
            self.sinOut.emit("OK!")

            if MOS_first_run == 'First':
                with open(MOS_file_json, 'w+', encoding='utf-8') as f:
                    a = {'font':'Academy Engraved LET'}
                    json.dump(a, f, sort_keys=True, indent=4, separators=(',', ': '))
                with open(MOS_file_json, 'r', encoding='utf-8') as f:
                    b = json.load(f)
                    print('默认字体：' + b['font'])
            else:
                with open(MOS_file_json, 'r', encoding='utf-8') as f:
                    try:
                        b = json.load(f)
                        c = str(b['font'])
                        print('默认字体：' + c)
                        self.sinOut_font.emit(c)
                    except KeyError:
                        print("json文件有问题")
                        self.sinOut.emit("KeyError")
                    

        except PermissionError:
            print("初始化失败 没有权限，操作不被许可")
            self.sinOut.emit("ERROR_PermissionError")
        except Exception as e:
            print(e)


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
        a = str(sys.platform)

        if a == "darwin":
            print('当前系统为Mac')
            user_name = os.getlogin()
            # 获取当前系统用户目录
            user_home = os.path.expanduser('~')
            print(user_home)

            file = user_home + '/Documents'
            print(file)
        else:
            file = ''

        print("初始化设置成功！")
        MainWindow.show()
        print("已成功显示窗体")
        sys.exit(app.exec())
except KeyboardInterrupt:
    print("程序以强行退出")
except:
    traceback.print_exc()

