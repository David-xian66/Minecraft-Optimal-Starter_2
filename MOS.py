import sys, os, requests, json, datetime, time, traceback, webbrowser, platform



os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r'.\site-packages\PyQt6\Qt6\plugins'  #### 这一行是新增的。用的是相对路径。

from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtGui, QtWidgets
# from PyQt6.QtWidgets import (QMainWindow, QTextEdit,QFileDialog, QApplication)
from PyQt6.QtGui import QIcon, QAction
import MOS_rc
# https://www.wenjuan.com/s/UZBZJvEm2uK/#《MOS ll 错误反馈》，快来参与吧。【问卷网提供支持】om PyQt6 import QtCore, QtGui, QtWidgets



class Ui_MOS(object):
    def setupUi(self, MOS):

        MOS_catalogue_picture_ico_png = os.path.join("picture", "ico.png")
        MOS_catalogue_picture_home_png = os.path.join("picture", "home.png")
        MOS_catalogue_picture_online_png = os.path.join("picture", "online.png")
        MOS_catalogue_picture_download_png = os.path.join("picture", "download.png")
        MOS_catalogue_picture_music_png = os.path.join("picture", "music.png")
        MOS_catalogue_picture_settings_png = os.path.join("picture", "settings.png")
        MOS_catalogue_picture_about_png = os.path.join("picture", "about.png")
        MOS_catalogue_picture_david_png = os.path.join("picture", "david.png")
        MOS_catalogue_picture_heimnad_png = os.path.join("picture", "heimnad.png")
        MOS_catalogue_picture_fabric_png = os.path.join("picture", "fabric.png")
        MOS_catalogue_picture_forge_png = os.path.join("picture", "forge.png")
        MOS_catalogue_picture_loading_png = os.path.join("picture", "loading.gif")
        MOS_catalogue_picture_loading_black_png = os.path.join("picture", "loading_black.gif")
        MOS_catalogue_picture_loading_2_png = os.path.join("picture", "loading_2.gif")
        MOS_catalogue_picture_loading_2_black_png = os.path.join("picture", "loading_2_black.gif")
        MOS_catalogue_picture_loading_3_png = os.path.join("picture", "loading_3.gif")
        MOS_catalogue_picture_loading_3_black_png = os.path.join("picture", "loading_3_black.gif")
        MOS_catalogue_picture_quilt_png = os.path.join("picture", "quilt.png")
        MOS_catalogue_picture_optifine_png = os.path.join("picture", "optifine.png")
        MOS_catalogue_picture_add_png = os.path.join("picture", "add.png")
        MOS_catalogue_picture_back_png = os.path.join("picture", "back.png")
        MOS_catalogue_picture_back_blue_up_png = os.path.join("picture", "back_blue_up.png")
        MOS_catalogue_picture_back_up_png = os.path.join("picture", "back_up.png")
        MOS_catalogue_picture_back_down_png = os.path.join("picture", "back_down.png")
        MOS_catalogue_picture_back_blue_down_png = os.path.join("picture", "back_blue_down.png")
        MOS_catalogue_picture_folder_add_png = os.path.join("picture", "folder_add.png")
        MOS_catalogue_picture_folder_minus_png = os.path.join("picture", "folder_minus.png")
        MOS_catalogue_picture_folder_open_png = os.path.join("picture", "folder_open.png")
        MOS_catalogue_picture_folder_png = os.path.join("picture", "folder.png")
        MOS_catalogue_picture_trash_red_png = os.path.join("picture", "trash_red.png")
        MOS_catalogue_picture_trash_png = os.path.join("picture", "trash.png")
        MOS_catalogue_picture_user_add_png = os.path.join("picture", "user_add.png")
        MOS_catalogue_picture_picture_user_png = os.path.join("picture", "picture_user.png")

        MOS.setObjectName("MOS")
        MOS.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        MOS.resize(1000, 533)
        MOS.setMinimumSize(QtCore.QSize(1000, 533))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/Users/xyj/.npm/ssh/UI/../picture/ico.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MOS.setWindowIcon(icon)
        MOS.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MOS)
        self.centralwidget.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setHorizontalSpacing(0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.stackedWidget_mos_right = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget_mos_right.setStyleSheet("background-color: rgb(255, 255, 255);")
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
        self.scrollArea_page_gonggao.setStyleSheet("border-style:none;background-color: rgb(255, 255, 255);")
        self.scrollArea_page_gonggao.setWidgetResizable(True)
        self.scrollArea_page_gonggao.setObjectName("scrollArea_page_gonggao")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 808, 509))
        self.scrollAreaWidgetContents.setStyleSheet("")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.widget_scrollArea_page_gonggao_left = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_scrollArea_page_gonggao_left.setMinimumSize(QtCore.QSize(399, 509))
        self.widget_scrollArea_page_gonggao_left.setStyleSheet("QWidget{border:2px solid rgb(0, 150, 255);border-radius:15px;}\n"
"QLabel{border-style:none;}")
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
        self.page_gonggao_jiazai.setStyleSheet("QTextBrowser{border-style:none;background-color: rgba(255, 255, 255, 0);}")
        self.page_gonggao_jiazai.setObjectName("page_gonggao_jiazai")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.page_gonggao_jiazai)
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.textBrowser_gonggao_left_txt = QtWidgets.QTextBrowser(self.page_gonggao_jiazai)
        self.textBrowser_gonggao_left_txt.setStyleSheet("")
        self.textBrowser_gonggao_left_txt.setObjectName("textBrowser_gonggao_left_txt")
        self.gridLayout_20.addWidget(self.textBrowser_gonggao_left_txt, 0, 0, 1, 1)
        self.stackedWidget_gonggao.addWidget(self.page_gonggao_jiazai)
        self.page_gonggao_jiazai_ing = QtWidgets.QWidget()
        self.page_gonggao_jiazai_ing.setStyleSheet("QProgressBar{\n"
"    text-align: center;border-style:none;border-radius:7px;background-color: rgba(0, 150, 255, 10);height:15px;color: rgb(66, 66, 66);\n"
"}\n"
"QProgressBar::chunk{\n"
"    border-radius:7px;\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(53, 244, 252, 255), stop:1 rgba(222, 255, 255, 255));\n"
"}\n"
"QLabel{color: rgb(0, 150, 255);}")
        self.page_gonggao_jiazai_ing.setObjectName("page_gonggao_jiazai_ing")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.page_gonggao_jiazai_ing)
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_21.setObjectName("gridLayout_21")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_21.addItem(spacerItem, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.page_gonggao_jiazai_ing)
        self.label_2.setStyleSheet("font-size: 13px;")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout_21.addWidget(self.label_2, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 30, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_21.addItem(spacerItem1, 3, 0, 1, 1)
        self.progressBar_2 = QtWidgets.QProgressBar(self.page_gonggao_jiazai_ing)
        self.progressBar_2.setStyleSheet("font-size: 13px;")
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
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_5.addItem(spacerItem2, 3, 0, 1, 1)
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
        self.label_gonggao_left_txt.setStyleSheet("font-size: 14px;")
        self.label_gonggao_left_txt.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_gonggao_left_txt.setWordWrap(True)
        self.label_gonggao_left_txt.setObjectName("label_gonggao_left_txt")
        self.gridLayout_5.addWidget(self.label_gonggao_left_txt, 0, 0, 1, 1)
        self.gridLayout_16.addWidget(self.widget_scrollArea_page_gonggao_left, 0, 0, 1, 1)
        self.widget_scrollArea_page_gonggao_right = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_scrollArea_page_gonggao_right.setMinimumSize(QtCore.QSize(399, 509))
        self.widget_scrollArea_page_gonggao_right.setStyleSheet("QWidget{border:2px solid rgb(0, 150, 255);border-radius:15px;}\n"
"QLabel{border-style:none;}\n"
"QProgressBar{\n"
"    text-align: center;border-style:none;border-radius:7px;background-color: rgba(0, 150, 255, 10);height:15px;color: rgb(66, 66, 66);\n"
"}\n"
"QProgressBar::chunk{\n"
"    border-radius:7px;\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(53, 244, 252, 255), stop:1 rgba(222, 255, 255, 255));\n"
"}")
        self.widget_scrollArea_page_gonggao_right.setObjectName("widget_scrollArea_page_gonggao_right")
        self.gridLayout_28 = QtWidgets.QGridLayout(self.widget_scrollArea_page_gonggao_right)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.label__gonggao_right_txt = QtWidgets.QLabel(self.widget_scrollArea_page_gonggao_right)
        self.label__gonggao_right_txt.setStyleSheet("font-size: 14px;")
        self.label__gonggao_right_txt.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label__gonggao_right_txt.setWordWrap(True)
        self.label__gonggao_right_txt.setObjectName("label__gonggao_right_txt")
        self.gridLayout_28.addWidget(self.label__gonggao_right_txt, 0, 0, 1, 1)
        self.line_8 = QtWidgets.QFrame(self.widget_scrollArea_page_gonggao_right)
        self.line_8.setStyleSheet("background-color: rgb(169, 169, 169);border:none;")
        self.line_8.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_28.addWidget(self.line_8, 1, 0, 1, 1)
        self.widget_scrollArea_page_gonggao_statring = QtWidgets.QWidget(self.widget_scrollArea_page_gonggao_right)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_scrollArea_page_gonggao_statring.sizePolicy().hasHeightForWidth())
        self.widget_scrollArea_page_gonggao_statring.setSizePolicy(sizePolicy)
        self.widget_scrollArea_page_gonggao_statring.setStyleSheet("border-style:none;")
        self.widget_scrollArea_page_gonggao_statring.setObjectName("widget_scrollArea_page_gonggao_statring")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_scrollArea_page_gonggao_statring)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.progressBar = QtWidgets.QProgressBar(self.widget_scrollArea_page_gonggao_statring)
        self.progressBar.setStyleSheet("font-size: 13px;")
        self.progressBar.setMinimum(0)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 2, 0, 1, 5)
        spacerItem3 = QtWidgets.QSpacerItem(10, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(10, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 0, 4, 2, 1)
        self.label_3 = QtWidgets.QLabel(self.widget_scrollArea_page_gonggao_statring)
        self.label_3.setStyleSheet("border-style:none;background-color: rgba(255, 255, 255, 0);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("/Users/xyj/.npm/ssh/UI/../../../Desktop/MOS/picture/loading_3.gif"))
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 1, 2, 3)
        self.label_7 = QtWidgets.QLabel(self.widget_scrollArea_page_gonggao_statring)
        self.label_7.setStyleSheet("font-size: 13px;")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 5)
        self.gridLayout_28.addWidget(self.widget_scrollArea_page_gonggao_statring, 2, 0, 1, 1)
        self.widget_9 = QtWidgets.QWidget(self.widget_scrollArea_page_gonggao_right)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy)
        self.widget_9.setStyleSheet("QWidget{border-style:none;}\n"
"QPushButton{border:2px solid rgb(192, 192, 192);border-radius:8px;}\n"
"#pushButton__gonggao_start{border:2px solid rgb(0, 150, 255);height:25px;border-radius:8px;}\n"
"#pushButton__gonggao_start::hover{color: rgb(0, 150, 255,100);}\n"
"#pushButton__gonggao_start::pressed{background-color: rgba(0, 150, 255, 50);}\n"
"\n"
"QComboBox {\n"
"    border: 2px solid rgb(169, 169, 169); /* border: 宽度 线类型 颜色 */\n"
"    height:25px;\n"
"    /*background-color: rgba(0, 150, 255, 150);*/\n"
"    background-color: rgba(214, 214, 214,100);\n"
"    border-radius:8px;\n"
"}\n"
"\n"
"/*下拉框的样式*/\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    outline: 0px solid gray;  /*取消选中虚线*/\n"
"    border: 1px solid rgb(31, 156, 255);\n"
"    color: rgb(66, 66, 66);\n"
"    background-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(0, 150, 255);\n"
"    border-radius:5px;\n"
"    height:35px;\n"
"    border:None;\n"
"}\n"
"/*选中每一项的字体颜色和背景颜色*/\n"
"QComboBox::item:selected \n"
"{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 150, 255);\n"
"    border-radius:5px;\n"
"}\n"
"/*右边*/\n"
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
"/* QComboBox中的垂直滚动条 */\n"
"QComboBox QAbstractScrollArea QScrollBar:vertical {\n"
"    width: 10px;\n"
"    height: 8px;\n"
"    background-color: rgb(255, 64, 255);   /* 空白区域的背景色*/\n"
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
"}")
        self.widget_9.setObjectName("widget_9")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_9)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setHorizontalSpacing(5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushButton_16 = QtWidgets.QPushButton(self.widget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)
        self.pushButton_16.setMinimumSize(QtCore.QSize(183, 29))
        self.pushButton_16.setStyleSheet("font-size: 14px;")
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_6.addWidget(self.pushButton_16, 0, 0, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.widget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy)
        self.pushButton_17.setMinimumSize(QtCore.QSize(183, 29))
        self.pushButton_17.setStyleSheet("font-size: 14px;")
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_6.addWidget(self.pushButton_17, 0, 1, 1, 1)
        self.comboBox_gonggao_right = QtWidgets.QComboBox(self.widget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_gonggao_right.sizePolicy().hasHeightForWidth())
        self.comboBox_gonggao_right.setSizePolicy(sizePolicy)
        self.comboBox_gonggao_right.setMinimumSize(QtCore.QSize(183, 29))
        self.comboBox_gonggao_right.setMouseTracking(False)
        self.comboBox_gonggao_right.setStyleSheet("font-size: 14px;")
        self.comboBox_gonggao_right.setEditable(False)
        self.comboBox_gonggao_right.setMaxVisibleItems(15)
        self.comboBox_gonggao_right.setMaxCount(2147483647)
        self.comboBox_gonggao_right.setMinimumContentsLength(0)
        self.comboBox_gonggao_right.setDuplicatesEnabled(False)
        self.comboBox_gonggao_right.setFrame(True)
        self.comboBox_gonggao_right.setModelColumn(0)
        self.comboBox_gonggao_right.setObjectName("comboBox_gonggao_right")
        self.gridLayout_6.addWidget(self.comboBox_gonggao_right, 1, 0, 1, 1)
        self.pushButton__gonggao_start = QtWidgets.QPushButton(self.widget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton__gonggao_start.sizePolicy().hasHeightForWidth())
        self.pushButton__gonggao_start.setSizePolicy(sizePolicy)
        self.pushButton__gonggao_start.setMinimumSize(QtCore.QSize(183, 29))
        self.pushButton__gonggao_start.setStyleSheet("font-size: 14px;")
        self.pushButton__gonggao_start.setObjectName("pushButton__gonggao_start")
        self.gridLayout_6.addWidget(self.pushButton__gonggao_start, 1, 1, 1, 1)
        self.gridLayout_28.addWidget(self.widget_9, 3, 0, 1, 1)
        self.gridLayout_16.addWidget(self.widget_scrollArea_page_gonggao_right, 0, 1, 1, 1)
        self.scrollArea_page_gonggao.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea_page_gonggao)
        self.stackedWidget_mos_right.addWidget(self.page_gonggao)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setStyleSheet("QLabel{border-style:none;color:rgb(33, 33, 33);background-color: rgba(255, 255, 255, 0);}")
        self.page_8.setObjectName("page_8")
        self.gridLayout_50 = QtWidgets.QGridLayout(self.page_8)
        self.gridLayout_50.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_50.setVerticalSpacing(0)
        self.gridLayout_50.setObjectName("gridLayout_50")
        self.stackedWidget_mos_right_2 = QtWidgets.QStackedWidget(self.page_8)
        self.stackedWidget_mos_right_2.setStyleSheet("background-color: rgba(255, 255, 255, 128);")
        self.stackedWidget_mos_right_2.setObjectName("stackedWidget_mos_right_2")
        self.page_12 = QtWidgets.QWidget()
        self.page_12.setStyleSheet("#pushButton_35\n"
"{\n"
"    width:30px;border-radius: 13px;background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"#pushButton_35::hover\n"
"{\n"
"    border-radius: 13px;\n"
"    background-color: rgba(192, 192, 192, 128);\n"
"}\n"
"#pushButton_35::pressed\n"
"{\n"
"    background-color: rgba(0, 150, 255, 51);\n"
"}\n"
"#pushButton_41\n"
"{\n"
"    width:30px;border-radius: 13px;background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"#pushButton_41::hover\n"
"{\n"
"    border-radius: 13px;\n"
"    background-color: rgba(192, 192, 192, 128);\n"
"}\n"
"#pushButton_41::pressed\n"
"{\n"
"    background-color: rgba(0, 150, 255, 51);\n"
"}")
        self.page_12.setObjectName("page_12")
        self.gridLayout_33 = QtWidgets.QGridLayout(self.page_12)
        self.gridLayout_33.setContentsMargins(5, 0, 5, 5)
        self.gridLayout_33.setHorizontalSpacing(0)
        self.gridLayout_33.setObjectName("gridLayout_33")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_33.addItem(spacerItem5, 1, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(805, 13, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_33.addItem(spacerItem6, 0, 0, 1, 4)
        self.line_11 = QtWidgets.QFrame(self.page_12)
        self.line_11.setStyleSheet("color:rgb(214, 214, 214)")
        self.line_11.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_11.setMidLineWidth(1)
        self.line_11.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_11.setObjectName("line_11")
        self.gridLayout_33.addWidget(self.line_11, 2, 0, 1, 4)
        self.label_24 = QtWidgets.QLabel(self.page_12)
        self.label_24.setStyleSheet("font-size: 17px;")
        self.label_24.setIndent(8)
        self.label_24.setOpenExternalLinks(False)
        self.label_24.setObjectName("label_24")
        self.gridLayout_33.addWidget(self.label_24, 1, 1, 1, 1)
        self.widget_20 = QtWidgets.QWidget(self.page_12)
        self.widget_20.setObjectName("widget_20")
        self.gridLayout_55 = QtWidgets.QGridLayout(self.widget_20)
        self.gridLayout_55.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_55.setHorizontalSpacing(4)
        self.gridLayout_55.setObjectName("gridLayout_55")
        self.line_16 = QtWidgets.QFrame(self.widget_20)
        self.line_16.setStyleSheet("border-style:none;background-color: rgba(66, 66, 66,200);")
        self.line_16.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_16.setObjectName("line_16")
        self.gridLayout_55.addWidget(self.line_16, 0, 1, 1, 1)
        self.widget_7 = QtWidgets.QWidget(self.widget_20)
        self.widget_7.setMaximumSize(QtCore.QSize(185, 16777215))
        self.widget_7.setStyleSheet("#listWidget{border-style:none;}\n"
"QListView::item {\n"
"    height: 30px;\n"
"    padding: 10px;\n"
"    border-left: 3px solid rgba(214, 214, 214,0);\n"
"}\n"
"QListView::item:hover {\n"
"    border-left: 3px solid rgb(214, 214, 214);\n"
"    background-color: transparent;\n"
"}\n"
"QListView::item:selected {\n"
"    background-color: transparent;\n"
"    color: black;\n"
"    border-left: 3px solid rgb(0, 150, 255);\n"
"}\n"
"QPushButton\n"
"{\n"
"    border-radius: 2px;background-color: rgba(255, 255, 255, 0);border-style:none;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"    border-radius: 2px;\n"
"    background-color: rgba(192, 192, 192, 128);\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"    background-color: rgba(0, 150, 255, 51);\n"
"}")
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.widget_7)
        self.listWidget.setStyleSheet("font-size: 15px;")
        self.listWidget.setIconSize(QtCore.QSize(24, 24))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/Users/xyj/.npm/ssh/UI/../picture/folder.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        item.setIcon(icon1)
        self.listWidget.addItem(item)
        self.verticalLayout.addWidget(self.listWidget)
        self.pushButton_38 = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_38.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_38.setStyleSheet("font-size: 13px;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/Users/xyj/.npm/ssh/UI/../picture/settings.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_38.setIcon(icon2)
        self.pushButton_38.setObjectName("pushButton_38")
        self.verticalLayout.addWidget(self.pushButton_38)
        self.pushButton_36 = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_36.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_36.setStyleSheet("font-size: 13px;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("/Users/xyj/.npm/ssh/UI/../picture/folder_add.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_36.setIcon(icon3)
        self.pushButton_36.setObjectName("pushButton_36")
        self.verticalLayout.addWidget(self.pushButton_36)
        self.pushButton_37 = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_37.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_37.setStyleSheet("font-size: 13px;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("/Users/xyj/.npm/ssh/UI/../picture/add.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_37.setIcon(icon4)
        self.pushButton_37.setObjectName("pushButton_37")
        self.verticalLayout.addWidget(self.pushButton_37)
        self.gridLayout_55.addWidget(self.widget_7, 0, 0, 1, 1)
        self.widget_6 = QtWidgets.QWidget(self.widget_20)
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_52 = QtWidgets.QGridLayout(self.widget_6)
        self.gridLayout_52.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_52.setHorizontalSpacing(0)
        self.gridLayout_52.setObjectName("gridLayout_52")
        self.stackedWidget_5 = QtWidgets.QStackedWidget(self.widget_6)
        self.stackedWidget_5.setStyleSheet("")
        self.stackedWidget_5.setObjectName("stackedWidget_5")
        self.page_21 = QtWidgets.QWidget()
        self.page_21.setStyleSheet("#listWidget_2{border-style:none;}\n"
"QListView::item {\n"
"    height: 25px;\n"
"    padding: 8px;\n"
"    border-left: 3px solid rgba(214, 214, 214,0);\n"
"}\n"
"QListView::item:hover {\n"
"    border-left: 3px solid rgb(214, 214, 214);\n"
"    background-color: transparent;\n"
"}\n"
"QListView::item:selected {\n"
"    background-color: transparent;\n"
"    color: black;\n"
"    background-color: rgb(235, 235, 235);\n"
"    border-left: 3px solid rgb(0, 150, 255);\n"
"}")
        self.page_21.setObjectName("page_21")
        self.gridLayout_51 = QtWidgets.QGridLayout(self.page_21)
        self.gridLayout_51.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_51.setObjectName("gridLayout_51")
        self.listWidget_2 = QtWidgets.QListWidget(self.page_21)
        self.listWidget_2.setStyleSheet("font-size: 14px;")
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout_51.addWidget(self.listWidget_2, 0, 0, 1, 1)
        self.stackedWidget_5.addWidget(self.page_21)
        self.page_25 = QtWidgets.QWidget()
        self.page_25.setStyleSheet("#label_43{border-style:none;color:rgb(33, 33, 33);background-color: rgba(255, 255, 255, 0);}")
        self.page_25.setObjectName("page_25")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.page_25)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.widget_22 = QtWidgets.QWidget(self.page_25)
        self.widget_22.setStyleSheet("QWidget{border-radius: 15px;background-color: rgb(249, 249, 249);}\n"
"QLineEdit{border-radius: 10px;border:2px solid rgb(192, 192, 192);background-color: rgb(255, 255, 255);}\n"
"QLineEdit::focus{border:2px solid rgb(0, 250, 146);}")
        self.widget_22.setObjectName("widget_22")
        self.gridLayout_58 = QtWidgets.QGridLayout(self.widget_22)
        self.gridLayout_58.setObjectName("gridLayout_58")
        self.label_44 = QtWidgets.QLabel(self.widget_22)
        self.label_44.setStyleSheet("font-size: 14px;")
        self.label_44.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_44.setObjectName("label_44")
        self.gridLayout_58.addWidget(self.label_44, 0, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_22)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(0, 28))
        self.lineEdit_4.setStyleSheet("font-size: 14px;")
        self.lineEdit_4.setInputMask("")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setDragEnabled(False)
        self.lineEdit_4.setReadOnly(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_58.addWidget(self.lineEdit_4, 0, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_58.addItem(spacerItem7, 1, 0, 1, 1)
        self.label_47 = QtWidgets.QLabel(self.widget_22)
        self.label_47.setStyleSheet("font-size: 14px;")
        self.label_47.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_47.setObjectName("label_47")
        self.gridLayout_58.addWidget(self.label_47, 1, 1, 1, 1)
        self.gridLayout_22.addWidget(self.widget_22, 2, 0, 1, 4)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_22.addItem(spacerItem8, 5, 0, 1, 4)
        self.label_43 = QtWidgets.QLabel(self.page_25)
        self.label_43.setStyleSheet("font-size: 17px;")
        self.label_43.setLineWidth(1)
        self.label_43.setIndent(4)
        self.label_43.setOpenExternalLinks(False)
        self.label_43.setObjectName("label_43")
        self.gridLayout_22.addWidget(self.label_43, 0, 1, 1, 1)
        self.widget_21 = QtWidgets.QWidget(self.page_25)
        self.widget_21.setStyleSheet("QWidget{border-radius: 15px;background-color: rgb(249, 249, 249);}\n"
"QPushButton{border-radius: 10px;border:2px solid rgb(192, 192, 192);background-color: rgb(255, 255, 255);}\n"
"QPushButton::hover{background-color: rgb(118, 214, 255);border:2px solid rgb(128, 217, 255);color: rgb(255, 255, 255);}")
        self.widget_21.setObjectName("widget_21")
        self.gridLayout_57 = QtWidgets.QGridLayout(self.widget_21)
        self.gridLayout_57.setObjectName("gridLayout_57")
        self.label_45 = QtWidgets.QLabel(self.widget_21)
        self.label_45.setStyleSheet("font-size: 14px;")
        self.label_45.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_45.setWordWrap(False)
        self.label_45.setOpenExternalLinks(False)
        self.label_45.setObjectName("label_45")
        self.gridLayout_57.addWidget(self.label_45, 0, 0, 2, 1)
        self.label_48 = QtWidgets.QLabel(self.widget_21)
        self.label_48.setStyleSheet("font-size: 14px;")
        self.label_48.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_48.setObjectName("label_48")
        self.gridLayout_57.addWidget(self.label_48, 2, 0, 1, 1)
        self.pushButton_42 = QtWidgets.QPushButton(self.widget_21)
        self.pushButton_42.setMinimumSize(QtCore.QSize(0, 28))
        self.pushButton_42.setStyleSheet("font-size: 14px;")
        self.pushButton_42.setIcon(icon1)
        self.pushButton_42.setObjectName("pushButton_42")
        self.gridLayout_57.addWidget(self.pushButton_42, 0, 2, 2, 1)
        self.label_46 = QtWidgets.QLabel(self.widget_21)
        self.label_46.setStyleSheet("font-size: 13px;")
        self.label_46.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_46.setObjectName("label_46")
        self.gridLayout_57.addWidget(self.label_46, 2, 2, 1, 1)
        self.gridLayout_22.addWidget(self.widget_21, 1, 0, 1, 4)
        self.pushButton_41 = QtWidgets.QPushButton(self.page_25)
        self.pushButton_41.setStyleSheet("")
        self.pushButton_41.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("/Users/xyj/.npm/ssh/UI/../picture/back.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_41.setIcon(icon5)
        self.pushButton_41.setIconSize(QtCore.QSize(27, 30))
        self.pushButton_41.setAutoDefault(False)
        self.pushButton_41.setDefault(False)
        self.pushButton_41.setFlat(False)
        self.pushButton_41.setObjectName("pushButton_41")
        self.gridLayout_22.addWidget(self.pushButton_41, 0, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.page_25)
        self.widget_3.setEnabled(False)
        self.widget_3.setMinimumSize(QtCore.QSize(602, 44))
        self.widget_3.setStyleSheet("QWiget{background-color: rgba(255, 255, 255, 0);}\n"
"QPushButton\n"
"{\n"
"    border-radius: 10px;border:2px solid rgb(115, 250, 121);background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"    color: rgb(115, 250, 121);\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"    background-color: rgb(115, 250, 121);color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:disabled{\n"
"    /*禁用*/\n"
"    border-radius: 10px;border:2px solid rgb(214, 214, 214);background-color: rgb(255, 255, 255);\n"
"}")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_27 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_27.setObjectName("gridLayout_27")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_27.addItem(spacerItem9, 1, 3, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_27.addItem(spacerItem10, 1, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_27.addItem(spacerItem11, 1, 2, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_18.setEnabled(False)
        self.pushButton_18.setMinimumSize(QtCore.QSize(0, 28))
        self.pushButton_18.setStyleSheet("font-size: 14px;")
        self.pushButton_18.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_18.setChecked(False)
        self.pushButton_18.setAutoRepeat(False)
        self.pushButton_18.setAutoExclusive(False)
        self.pushButton_18.setAutoDefault(False)
        self.pushButton_18.setDefault(False)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout_27.addWidget(self.pushButton_18, 0, 1, 1, 2)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_27.addItem(spacerItem12, 1, 0, 1, 1)
        self.gridLayout_22.addWidget(self.widget_3, 3, 0, 1, 4)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_22.addItem(spacerItem13, 0, 3, 1, 1)
        self.stackedWidget_5.addWidget(self.page_25)
        self.page_22 = QtWidgets.QWidget()
        self.page_22.setStyleSheet("QLineEdit{height:23px;border-radius:8px;border:2px solid rgb(192, 192, 192);}\n"
"#pushButton_39{height:23px;border-radius:8px;border:2px solid rgb(192, 192, 192);}\n"
"#pushButton_40{height:30px;background-color: rgba(255, 255, 255,0);border-radius:7px;border:2px solid rgb(255, 59, 0);height:27px;}\n"
"#pushButton_40::hover{color: rgb(255, 59, 0)}\n"
"#pushButton_40::pressed{background-color: rgba(255, 0, 0, 100);}")
        self.page_22.setObjectName("page_22")
        self.gridLayout_53 = QtWidgets.QGridLayout(self.page_22)
        self.gridLayout_53.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_53.setObjectName("gridLayout_53")
        self.pushButton_40 = QtWidgets.QPushButton(self.page_22)
        self.pushButton_40.setStyleSheet("font-size: 13px;")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("/Users/xyj/.npm/ssh/UI/../picture/trash_red.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_40.setIcon(icon6)
        self.pushButton_40.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_40.setCheckable(False)
        self.pushButton_40.setObjectName("pushButton_40")
        self.gridLayout_53.addWidget(self.pushButton_40, 4, 1, 1, 2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page_22)
        self.lineEdit_3.setStyleSheet("font-size: 13px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_53.addWidget(self.lineEdit_3, 1, 0, 1, 2)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_53.addItem(spacerItem14, 6, 0, 1, 2)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_53.addItem(spacerItem15, 0, 0, 1, 4)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_53.addItem(spacerItem16, 3, 0, 1, 4)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_53.addItem(spacerItem17, 6, 2, 1, 2)
        self.pushButton_39 = QtWidgets.QPushButton(self.page_22)
        self.pushButton_39.setStyleSheet("font-size: 14px;")
        self.pushButton_39.setObjectName("pushButton_39")
        self.gridLayout_53.addWidget(self.pushButton_39, 1, 2, 1, 2)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_53.addItem(spacerItem18, 5, 0, 1, 4)
        self.stackedWidget_5.addWidget(self.page_22)
        self.page_23 = QtWidgets.QWidget()
        self.page_23.setObjectName("page_23")
        self.gridLayout_54 = QtWidgets.QGridLayout(self.page_23)
        self.gridLayout_54.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_54.setObjectName("gridLayout_54")
        self.label_26 = QtWidgets.QLabel(self.page_23)
        self.label_26.setText("")
        self.label_26.setPixmap(QtGui.QPixmap("/Users/xyj/.npm/ssh/UI/../picture/loading.gif"))
        self.label_26.setScaledContents(False)
        self.label_26.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_26.setWordWrap(False)
        self.label_26.setObjectName("label_26")
        self.gridLayout_54.addWidget(self.label_26, 0, 2, 1, 1)
        self.stackedWidget_5.addWidget(self.page_23)
        self.gridLayout_52.addWidget(self.stackedWidget_5, 0, 0, 1, 1)
        self.gridLayout_55.addWidget(self.widget_6, 0, 2, 1, 1)
        self.gridLayout_33.addWidget(self.widget_20, 3, 0, 1, 4)
        self.pushButton_35 = QtWidgets.QPushButton(self.page_12)
        self.pushButton_35.setStyleSheet("")
        self.pushButton_35.setText("")
        self.pushButton_35.setIcon(icon5)
        self.pushButton_35.setIconSize(QtCore.QSize(27, 30))
        self.pushButton_35.setObjectName("pushButton_35")
        self.gridLayout_33.addWidget(self.pushButton_35, 1, 0, 1, 1)
        self.stackedWidget_mos_right_2.addWidget(self.page_12)
        self.gridLayout_50.addWidget(self.stackedWidget_mos_right_2, 0, 0, 1, 1)
        self.stackedWidget_mos_right.addWidget(self.page_8)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setStyleSheet("QLabel{border-style:none;color:rgb(33, 33, 33);background-color: rgba(255, 255, 255, 0);}")
        self.page_2.setObjectName("page_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_7.setContentsMargins(5, 0, 5, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem19 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_7.addItem(spacerItem19, 4, 0, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setStyleSheet("font-size: 17px;")
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
        self.widget_5.setStyleSheet("QWidget{border-radius:10px;border:2px solid rgb(0, 150, 255);}\n"
"QLabel{border-style:none;color:rgb(0, 150, 255);}")
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout_8.setContentsMargins(12, -1, -1, -1)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_8 = QtWidgets.QLabel(self.widget_5)
        self.label_8.setStyleSheet("font-size: 13px;")
        self.label_8.setObjectName("label_8")
        self.gridLayout_8.addWidget(self.label_8, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.widget_5, 3, 0, 1, 2)
        spacerItem20 = QtWidgets.QSpacerItem(49, 13, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_7.addItem(spacerItem20, 0, 0, 1, 1)
        self.stackedWidget_mos_right.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(13)
        self.page_3.setFont(font)
        self.page_3.setStyleSheet("QLabel{border-style:none;color:rgb(33, 33, 33);background-color: rgba(255, 255, 255, 0);}\n"
"QComboBox {\n"
"    border: 2px solid rgb(169, 169, 169); /* border: 宽度 线类型 颜色 */\n"
"    height:25px;\n"
"    /*background-color: rgba(0, 150, 255, 150);*/\n"
"    background-color: rgba(214, 214, 214,100);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"/*下拉框的样式*/\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    outline: 0px solid gray;  /*取消选中虚线*/\n"
"    border: 1px solid rgb(31, 156, 255);\n"
"    color: rgb(66, 66, 66);\n"
"    background-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(0, 150, 255);\n"
"    border-radius:5px;\n"
"    height:35px;\n"
"    border:None;\n"
"}\n"
"/*选中每一项的字体颜色和背景颜色*/\n"
"QComboBox::item:selected \n"
"{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 150, 255);\n"
"    border-radius:5px;\n"
"}\n"
"/*右边*/\n"
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
"/* QComboBox中的垂直滚动条 */\n"
"QComboBox QAbstractScrollArea QScrollBar:vertical {\n"
"    width: 10px;\n"
"    height: 8px;\n"
"    background-color: rgb(255, 64, 255);   /* 空白区域的背景色*/\n"
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
"}")
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
        self.label_10.setStyleSheet("font-size: 17px;")
        self.label_10.setIndent(10)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 0, 2, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.page_3)
        self.comboBox_2.setStyleSheet("font-size: 14px;")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 2, 1)
        spacerItem21 = QtWidgets.QSpacerItem(832, 13, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem21, 0, 0, 1, 2)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.page_3)
        self.stackedWidget_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setStyleSheet("\n"
"QTreeWidget::item {\n"
"    height: 40px;\n"
"}")
        self.page_9.setObjectName("page_9")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.page_9)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.treeWidget = QtWidgets.QTreeWidget(self.page_9)
        self.treeWidget.setStyleSheet("font-size: 13px;")
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
        self.page_10.setStyleSheet("#lineEdit{height:25px;border-radius: 5px;border:2px solid rgb(169, 169, 169);color: rgb(0, 0, 0);}\n"
"#pushButton_2{height:25px;border-radius: 5px;width:70px;border:2px solid rgb(169, 169, 169);}")
        self.page_10.setObjectName("page_10")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.page_10)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.widget_2 = QtWidgets.QWidget(self.page_10)
        self.widget_2.setStyleSheet("QWidget{border-radius: 23px;border:2px solid rgb(0, 150, 255);}\n"
"QLabel{border-style:none;}\n"
"QComboBox {\n"
"    border: 2px solid rgb(169, 169, 169); /* border: 宽度 线类型 颜色 */\n"
"    height:25px;\n"
"    /*background-color: rgba(0, 150, 255, 150);*/\n"
"    background-color: rgba(214, 214, 214,100);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"/*下拉框的样式*/\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    outline: 0px solid gray;  /*取消选中虚线*/\n"
"    border: 1px solid rgb(31, 156, 255);\n"
"    color: rgb(66, 66, 66);\n"
"    background-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(0, 150, 255);\n"
"    border-radius:5px;\n"
"    height:35px;\n"
"    border:None;\n"
"}\n"
"/*选中每一项的字体颜色和背景颜色*/\n"
"QComboBox::item:selected \n"
"{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 150, 255);\n"
"    border-radius:5px;\n"
"}\n"
"/*右边*/\n"
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
"/* QComboBox中的垂直滚动条 */\n"
"QComboBox QAbstractScrollArea QScrollBar:vertical {\n"
"    width: 10px;\n"
"    height: 8px;\n"
"    background-color: rgb(255, 64, 255);   /* 空白区域的背景色*/\n"
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
"}")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_25.setObjectName("gridLayout_25")
        spacerItem22 = QtWidgets.QSpacerItem(199, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_25.addItem(spacerItem22, 0, 2, 1, 2)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_8.setStyleSheet("border-style:none;width:50px;height:50px;border-radius: 23px;background-color: rgba(235, 235, 235, 0);")
        self.pushButton_8.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("/Users/xyj/.npm/ssh/UI/../picture/quilt.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_8.setIcon(icon7)
        self.pushButton_8.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_25.addWidget(self.pushButton_8, 3, 0, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_25.addItem(spacerItem23, 2, 2, 1, 2)
        self.comboBox_5 = QtWidgets.QComboBox(self.widget_2)
        self.comboBox_5.setMinimumSize(QtCore.QSize(120, 25))
        self.comboBox_5.setStyleSheet("font-size: 13px;")
        self.comboBox_5.setObjectName("comboBox_5")
        self.gridLayout_25.addWidget(self.comboBox_5, 2, 5, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_25.addItem(spacerItem24, 1, 2, 1, 2)
        self.label_21 = QtWidgets.QLabel(self.widget_2)
        self.label_21.setStyleSheet("font-size: 15px;")
        self.label_21.setObjectName("label_21")
        self.gridLayout_25.addWidget(self.label_21, 3, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.widget_2)
        self.label_20.setStyleSheet("font-size: 15px;")
        self.label_20.setObjectName("label_20")
        self.gridLayout_25.addWidget(self.label_20, 2, 1, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_13.setStyleSheet("border-style:none;width:50px;height:50px;border-radius: 23px;background-color: rgba(235, 235, 235, 0);")
        self.pushButton_13.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("/Users/xyj/.npm/ssh/UI/../picture/loading.gif"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
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
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("/Users/xyj/.npm/ssh/UI/../picture/forge.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_5.setIcon(icon9)
        self.pushButton_5.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_25.addWidget(self.pushButton_5, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.widget_2)
        self.label_11.setStyleSheet("font-size: 15px;")
        self.label_11.setObjectName("label_11")
        self.gridLayout_25.addWidget(self.label_11, 0, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_7.setStyleSheet("border-style:none;width:50px;height:50px;border-radius: 23px;background-color: rgba(235, 235, 235, 0);")
        self.pushButton_7.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("/Users/xyj/.npm/ssh/UI/../picture/optifine.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
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
        self.comboBox_6.setStyleSheet("font-size: 13px;")
        self.comboBox_6.setObjectName("comboBox_6")
        self.gridLayout_25.addWidget(self.comboBox_6, 3, 5, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.widget_2)
        self.label_19.setStyleSheet("font-size: 15px;")
        self.label_19.setObjectName("label_19")
        self.gridLayout_25.addWidget(self.label_19, 1, 1, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.widget_2)
        self.comboBox_3.setMinimumSize(QtCore.QSize(210, 25))
        self.comboBox_3.setStyleSheet("font-size: 13px;")
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout_25.addWidget(self.comboBox_3, 0, 5, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_6.setStyleSheet("border-style:none;width:50px;height:50px;border-radius: 23px;background-color: rgba(235, 235, 235, 0);")
        self.pushButton_6.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("/Users/xyj/.npm/ssh/UI/../picture/fabric.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
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
        self.comboBox_4.setStyleSheet("font-size: 13px;")
        self.comboBox_4.setObjectName("comboBox_4")
        self.gridLayout_25.addWidget(self.comboBox_4, 1, 5, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_25.addItem(spacerItem25, 3, 2, 1, 1)
        self.gridLayout_26.addWidget(self.widget_2, 0, 0, 1, 3)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_26.addItem(spacerItem26, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.page_10)
        self.lineEdit.setStyleSheet("font-size: 13px;")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_26.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_2.setStyleSheet("font-size: 13px;")
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
        spacerItem27 = QtWidgets.QSpacerItem(832, 13, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem27, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.page_4)
        self.label_12.setStyleSheet("font-size: 17px;")
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
        self.widget_8.setStyleSheet("QWidget{border-radius:10px;border:2px solid rgb(0, 150, 255);}\n"
"QLabel{border-style:none;color:rgb(0, 150, 255);}")
        self.widget_8.setObjectName("widget_8")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.widget_8)
        self.gridLayout_10.setContentsMargins(12, -1, -1, -1)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_13 = QtWidgets.QLabel(self.widget_8)
        self.label_13.setStyleSheet("font-size: 13px;")
        self.label_13.setObjectName("label_13")
        self.gridLayout_10.addWidget(self.label_13, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.widget_8, 3, 0, 1, 1)
        spacerItem28 = QtWidgets.QSpacerItem(832, 393, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem28, 4, 0, 1, 1)
        self.stackedWidget_mos_right.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setStyleSheet("QLabel{border-style:none;color:rgb(33, 33, 33);background-color: rgba(255, 255, 255, 0);}\n"
"QComboBox {\n"
"    border: 2px solid rgb(169, 169, 169); /* border: 宽度 线类型 颜色 */\n"
"    height:25px;\n"
"    /*background-color: rgba(0, 150, 255, 150);*/\n"
"    background-color: rgba(214, 214, 214,100);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"/*下拉框的样式*/\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    outline: 0px solid gray;  /*取消选中虚线*/\n"
"    border: 1px solid rgb(31, 156, 255);\n"
"    color: rgb(66, 66, 66);\n"
"    background-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(0, 150, 255);\n"
"    border-radius:5px;\n"
"    height:35px;\n"
"    border:None;\n"
"}\n"
"/*选中每一项的字体颜色和背景颜色*/\n"
"QComboBox::item:selected \n"
"{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 150, 255);\n"
"    border-radius:5px;\n"
"}\n"
"/*右边*/\n"
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
"/* QComboBox中的垂直滚动条 */\n"
"QComboBox QAbstractScrollArea QScrollBar:vertical {\n"
"    width: 10px;\n"
"    height: 8px;\n"
"    background-color: rgb(255, 64, 255);   /* 空白区域的背景色*/\n"
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
"}")
        self.page_5.setObjectName("page_5")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_15.setContentsMargins(5, 0, 5, 0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        spacerItem29 = QtWidgets.QSpacerItem(832, 13, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_15.addItem(spacerItem29, 0, 0, 1, 2)
        self.line_5 = QtWidgets.QFrame(self.page_5)
        self.line_5.setStyleSheet("color:rgb(214, 214, 214)")
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_5.setMidLineWidth(1)
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_5.setObjectName("line_5")
        self.gridLayout_15.addWidget(self.line_5, 2, 0, 1, 2)
        self.label_15 = QtWidgets.QLabel(self.page_5)
        self.label_15.setStyleSheet("font-size: 17px;")
        self.label_15.setIndent(10)
        self.label_15.setObjectName("label_15")
        self.gridLayout_15.addWidget(self.label_15, 1, 0, 1, 1)
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
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 377, 798))
        self.scrollAreaWidgetContents_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.widget.setStyleSheet("QWidget{background-color: rgba(255, 255, 255, 0);border-radius:15px;border: 2px solid rgb(0, 150, 255);}\n"
"QLabel{border-style:none;}\n"
"#label_6{text-decoration: underline;}\n"
"QComboBox {\n"
"    border: 2px solid rgb(192, 192, 192); /* border: 宽度 线类型 颜色 */\n"
"    height:27px;\n"
"    background-color: rgba(235, 235, 235, 128);\n"
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
"    height:150px;\n"
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
"    width: 10px;\n"
"    height: 8px;\n"
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
"QPushButton{height:30px;background-color: rgba(255, 255, 255,0);border-radius:7px;border:2px solid rgb(255, 59, 0);}\n"
"QPushButton::hover{color: rgb(255, 59, 0)}\n"
"QPushButton::pressed{background-color: rgba(255, 0, 0, 100);}")
        self.widget.setObjectName("widget")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.pushButton_11 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_11.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_11.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_11.setStyleSheet("font-size: 14px;")
        self.pushButton_11.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_24.addWidget(self.pushButton_11, 1, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setStyleSheet("font-size: 13px;")
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.label_4.setObjectName("label_4")
        self.gridLayout_24.addWidget(self.label_4, 0, 0, 2, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setItalic(True)
        font.setUnderline(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font-size: 14px;")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_24.addWidget(self.label_6, 1, 1, 1, 2)
        self.fontComboBox = QtWidgets.QFontComboBox(self.widget)
        self.fontComboBox.setStyleSheet("font-size: 14px;")
        self.fontComboBox.setEditable(True)
        self.fontComboBox.setMaxVisibleItems(20)
        self.fontComboBox.setDuplicatesEnabled(False)
        self.fontComboBox.setObjectName("fontComboBox")
        self.gridLayout_24.addWidget(self.fontComboBox, 0, 1, 1, 3)
        self.gridLayout_23.addWidget(self.widget, 0, 0, 1, 1)
        self.widget_4 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.widget_4.setStyleSheet("QWidget{background-color: rgba(255, 255, 255, 0);border-radius:15px;border: 2px solid rgb(0, 150, 255);}\n"
"QLabel{border-style:none;}\n"
"QComboBox {\n"
"    border: 2px solid rgb(192, 192, 192); /* border: 宽度 线类型 颜色 */\n"
"    height:27px;\n"
"    background-color: rgba(235, 235, 235, 128);\n"
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
"    height:150px;\n"
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
"    width: 10px;\n"
"    height: 8px;\n"
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
"#pushButton_20{height:30px;background-color: rgba(255, 255, 255,0);border-radius:7px;border:2px solid rgb(255, 59, 0);}\n"
"#pushButton_20::hover{color: rgb(255, 59, 0)}\n"
"#pushButton_20::pressed{background-color: rgba(255, 0, 0, 100);}\n"
"\n"
"#pushButton_19{height:30px;background-color: rgba(255, 255, 255,0);border-radius:7px;border:2px solid rgb(0, 250, 146);color: rgb(33, 33, 33);}\n"
"#pushButton_19::hover{color: rgb(0, 250, 146);}\n"
"#pushButton_19::pressed{background-color: rgb(128, 255, 202);color: rgb(255, 255, 255);}\n"
"\n"
"/*禁用*/\n"
"#pushButton_20:disabled{border-radius: 7px;border:2px solid rgb(214, 214, 214);}\n"
"\n"
"QRadioButton{border-style:none;}")
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_29 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.pushButton_19 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_19.setStyleSheet("font-size: 14px;")
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout_29.addWidget(self.pushButton_19, 1, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setStyleSheet("font-size: 13px;")
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.label_5.setObjectName("label_5")
        self.gridLayout_29.addWidget(self.label_5, 1, 0, 2, 1)
        self.radioButton = QtWidgets.QRadioButton(self.widget_4)
        self.radioButton.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.radioButton.setStyleSheet("font-size: 13px;")
        self.radioButton.setChecked(True)
        self.radioButton.setAutoRepeat(False)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_29.addWidget(self.radioButton, 2, 1, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_20.setEnabled(False)
        self.pushButton_20.setStyleSheet("font-size: 14px;")
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout_29.addWidget(self.pushButton_20, 2, 2, 1, 1)
        self.gridLayout_23.addWidget(self.widget_4, 1, 0, 1, 1)
        spacerItem30 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_23.addItem(spacerItem30, 2, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_11.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.gridLayout_32 = QtWidgets.QGridLayout(self.page_7)
        self.gridLayout_32.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_32.setObjectName("gridLayout_32")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.page_7)
        self.scrollArea_2.setStyleSheet("border-style:none;background-color: rgba(255, 255, 255, 0);")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 245, 829))
        self.scrollAreaWidgetContents_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_30 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.widget_15 = QtWidgets.QWidget(self.scrollAreaWidgetContents_3)
        self.widget_15.setStyleSheet("QWidget{background-color: rgba(255, 255, 255, 0);border-radius:15px;border: 2px solid rgb(0, 150, 255);}\n"
"QLabel{border-style:none;}\n"
"#label_6{text-decoration: underline;}\n"
"QComboBox {\n"
"    border: 2px solid rgb(192, 192, 192); /* border: 宽度 线类型 颜色 */\n"
"    height:27px;\n"
"    background-color: rgba(235, 235, 235, 128);\n"
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
"    height:150px;\n"
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
"    width: 10px;\n"
"    height: 8px;\n"
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
"QPushButton{height:30px;background-color: rgba(255, 255, 255,0);border-radius:7px;border:2px solid rgb(255, 59, 0);}\n"
"QPushButton::hover{color: rgb(255, 59, 0)}\n"
"QPushButton::pressed{background-color: rgba(255, 0, 0, 100);}")
        self.widget_15.setObjectName("widget_15")
        self.gridLayout_31 = QtWidgets.QGridLayout(self.widget_15)
        self.gridLayout_31.setObjectName("gridLayout_31")
        self.label_14 = QtWidgets.QLabel(self.widget_15)
        self.label_14.setStyleSheet("font-size: 13px;")
        self.label_14.setScaledContents(False)
        self.label_14.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_14.setWordWrap(True)
        self.label_14.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.label_14.setObjectName("label_14")
        self.gridLayout_31.addWidget(self.label_14, 0, 0, 3, 1)
        self.comboBox_7 = QtWidgets.QComboBox(self.widget_15)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.gridLayout_31.addWidget(self.comboBox_7, 0, 2, 2, 1)
        self.pushButton_21 = QtWidgets.QPushButton(self.widget_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_21.sizePolicy().hasHeightForWidth())
        self.pushButton_21.setSizePolicy(sizePolicy)
        self.pushButton_21.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_21.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_21.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_21.setStyleSheet("font-size: 14px;")
        self.pushButton_21.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout_31.addWidget(self.pushButton_21, 2, 2, 1, 1)
        self.gridLayout_30.addWidget(self.widget_15, 0, 0, 1, 1)
        spacerItem31 = QtWidgets.QSpacerItem(20, 282, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_30.addItem(spacerItem31, 1, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_32.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_7)
        self.gridLayout_15.addWidget(self.stackedWidget, 3, 0, 1, 2)
        self.comboBox = QtWidgets.QComboBox(self.page_5)
        self.comboBox.setStyleSheet("font-size: 14px;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_15.addWidget(self.comboBox, 1, 1, 1, 1)
        self.stackedWidget_mos_right.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setStyleSheet("QLabel{border-style:none;color:rgb(33, 33, 33);background-color: rgba(255, 255, 255, 0);}")
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
        self.widget_13.setStyleSheet("QWidget{border-radius:15px;border:2px solid rgba(0, 150, 255, 230);}\n"
"QLabel{border-style:none;}")
        self.widget_13.setObjectName("widget_13")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_13)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.widget_13)
        self.label.setStyleSheet("font-size: 13px;")
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
        spacerItem32 = QtWidgets.QSpacerItem(34, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_12.addItem(spacerItem32, 1, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.widget_11)
        self.label_16.setStyleSheet("font-size: 13px;")
        self.label_16.setObjectName("label_16")
        self.gridLayout_12.addWidget(self.label_16, 1, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.widget_11)
        self.widget_12 = QtWidgets.QWidget(self.widget_13)
        self.widget_12.setStyleSheet("QWidget{border-style:none;background-color: rgb(235, 235, 235);border-radius:15px;}\n"
"#pushButton_3{width:120px;height:30px;background-color: rgba(255, 255, 255,0);border-radius:7px;border:2px solid rgb(0, 150, 255);}\n"
"#pushButton_3::hover{background-color: rgb(255, 255, 255);}\n"
"#pushButton_3::pressed{background-color: rgba(0, 150, 255, 51);}")
        self.widget_12.setObjectName("widget_12")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.widget_12)
        self.gridLayout_17.setHorizontalSpacing(7)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.label_18 = QtWidgets.QLabel(self.widget_12)
        self.label_18.setStyleSheet("font-size: 13px;")
        self.label_18.setObjectName("label_18")
        self.gridLayout_17.addWidget(self.label_18, 0, 1, 1, 1)
        spacerItem33 = QtWidgets.QSpacerItem(34, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_17.addItem(spacerItem33, 0, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_12)
        self.pushButton_4.setStyleSheet("border-style:none;")
        self.pushButton_4.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("/Users/xyj/.npm/ssh/UI/../picture/david.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon12)
        self.pushButton_4.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_17.addWidget(self.pushButton_4, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_12)
        self.pushButton_3.setStyleSheet("font-size: 13px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_17.addWidget(self.pushButton_3, 0, 3, 1, 1)
        self.verticalLayout_3.addWidget(self.widget_12)
        self.widget_14 = QtWidgets.QWidget(self.widget_13)
        self.widget_14.setStyleSheet("QWidget{border-style:none;background-color: rgb(235, 235, 235);border-radius:15px;}\n"
"#pushButton_10{width:120px;height:30px;background-color: rgba(255, 255, 255,0);border-radius:7px;border:2px solid rgb(0, 150, 255);}\n"
"#pushButton_10::hover{background-color: rgb(255, 255, 255);}\n"
"#pushButton_10::pressed{background-color: rgba(0, 150, 255, 51);}")
        self.widget_14.setObjectName("widget_14")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.widget_14)
        self.gridLayout_18.setHorizontalSpacing(2)
        self.gridLayout_18.setVerticalSpacing(6)
        self.gridLayout_18.setObjectName("gridLayout_18")
        spacerItem34 = QtWidgets.QSpacerItem(34, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_18.addItem(spacerItem34, 0, 3, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.widget_14)
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.gridLayout_18.addWidget(self.label_25, 0, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget_14)
        self.pushButton_9.setStyleSheet("border-style:none;")
        self.pushButton_9.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("/Users/xyj/.npm/ssh/UI/../picture/heimnad.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_9.setIcon(icon13)
        self.pushButton_9.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_18.addWidget(self.pushButton_9, 0, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.widget_14)
        self.label_22.setStyleSheet("font-size: 13px;")
        self.label_22.setObjectName("label_22")
        self.gridLayout_18.addWidget(self.label_22, 0, 2, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.widget_14)
        self.pushButton_10.setStyleSheet("font-size: 13px;")
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_18.addWidget(self.pushButton_10, 0, 4, 1, 1)
        self.verticalLayout_3.addWidget(self.widget_14)
        self.gridLayout_19.addWidget(self.widget_13, 0, 0, 1, 1)
        spacerItem35 = QtWidgets.QSpacerItem(796, 368, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_19.addItem(spacerItem35, 1, 0, 1, 1)
        self.gridLayout_14.addWidget(self.widget_10, 3, 0, 1, 2)
        self.line_6 = QtWidgets.QFrame(self.page_6)
        self.line_6.setStyleSheet("color:rgb(214, 214, 214)")
        self.line_6.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_6.setMidLineWidth(1)
        self.line_6.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_6.setObjectName("line_6")
        self.gridLayout_14.addWidget(self.line_6, 2, 0, 1, 2)
        spacerItem36 = QtWidgets.QSpacerItem(832, 13, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_14.addItem(spacerItem36, 0, 0, 1, 2)
        self.label_17 = QtWidgets.QLabel(self.page_6)
        self.label_17.setStyleSheet("font-size: 17px;")
        self.label_17.setIndent(10)
        self.label_17.setObjectName("label_17")
        self.gridLayout_14.addWidget(self.label_17, 1, 0, 1, 2)
        self.stackedWidget_mos_right.addWidget(self.page_6)
        self.gridLayout_13.addWidget(self.stackedWidget_mos_right, 0, 1, 1, 1)
        self.widget_mos_left = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_mos_left.sizePolicy().hasHeightForWidth())
        self.widget_mos_left.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.widget_mos_left.setFont(font)
        self.widget_mos_left.setAutoFillBackground(False)
        self.widget_mos_left.setStyleSheet("QWidget\n"
"{\n"
"    background-color: rgb(231, 230, 228);\n"
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
        self.widget_mos_left_top.setStyleSheet("#label_mos_left_top_user{background-color: rgba(255, 255, 255, 0);}\n"
"#label_mos_left_top_add{background-color: rgba(255, 255, 255, 0);}\n"
"QWidget\n"
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
        self.label_mos_left_top_add.setStyleSheet("font-size: 13px;")
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
        self.label_mos_left_top_user.setStyleSheet("font-size: 13px;")
        self.label_mos_left_top_user.setObjectName("label_mos_left_top_user")
        self.gridLayout_4.addWidget(self.label_mos_left_top_user, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.widget_mos_left_top)
        self.line_2 = QtWidgets.QFrame(self.widget_mos_left)
        self.line_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.pushButton_home = QtWidgets.QPushButton(self.widget_mos_left)
        self.pushButton_home.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_home.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.pushButton_home.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButton_home.setStyleSheet("font-size: 15px;")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("/Users/xyj/.npm/ssh/UI/../picture/home.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_home.setIcon(icon14)
        self.pushButton_home.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_home.setObjectName("pushButton_home")
        self.verticalLayout_2.addWidget(self.pushButton_home)
        self.pushButton_lianji = QtWidgets.QPushButton(self.widget_mos_left)
        self.pushButton_lianji.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_lianji.setStyleSheet("font-size: 15px;")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("/Users/xyj/.npm/ssh/UI/../picture/online.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_lianji.setIcon(icon15)
        self.pushButton_lianji.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_lianji.setObjectName("pushButton_lianji")
        self.verticalLayout_2.addWidget(self.pushButton_lianji)
        self.pushButton_xiazai = QtWidgets.QPushButton(self.widget_mos_left)
        self.pushButton_xiazai.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_xiazai.setStyleSheet("font-size: 15px;")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("/Users/xyj/.npm/ssh/UI/../picture/download.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_xiazai.setIcon(icon16)
        self.pushButton_xiazai.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_xiazai.setObjectName("pushButton_xiazai")
        self.verticalLayout_2.addWidget(self.pushButton_xiazai)
        self.pushButton_music = QtWidgets.QPushButton(self.widget_mos_left)
        self.pushButton_music.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_music.setStyleSheet("font-size: 15px;")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("/Users/xyj/.npm/ssh/UI/../picture/music.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_music.setIcon(icon17)
        self.pushButton_music.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_music.setObjectName("pushButton_music")
        self.verticalLayout_2.addWidget(self.pushButton_music)
        self.pushButton_shezhi = QtWidgets.QPushButton(self.widget_mos_left)
        self.pushButton_shezhi.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_shezhi.setStyleSheet("font-size: 15px;")
        self.pushButton_shezhi.setIcon(icon2)
        self.pushButton_shezhi.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_shezhi.setObjectName("pushButton_shezhi")
        self.verticalLayout_2.addWidget(self.pushButton_shezhi)
        self.pushButton_about = QtWidgets.QPushButton(self.widget_mos_left)
        self.pushButton_about.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_about.setStyleSheet("font-size: 15px;")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("/Users/xyj/.npm/ssh/UI/../picture/about.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_about.setIcon(icon18)
        self.pushButton_about.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_about.setObjectName("pushButton_about")
        self.verticalLayout_2.addWidget(self.pushButton_about)
        spacerItem37 = QtWidgets.QSpacerItem(20, 184, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem37)
        self.label_mosll = QtWidgets.QLabel(self.widget_mos_left)
        self.label_mosll.setStyleSheet("color: rgb(0, 150, 255);font-size: 17px;font: 75 17pt \"Yuanti SC\";background-color: rgba(240, 239, 238,0);")
        self.label_mosll.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_mosll.setObjectName("label_mosll")
        self.verticalLayout_2.addWidget(self.label_mosll)
        self.gridLayout_13.addWidget(self.widget_mos_left, 0, 0, 1, 1)
        MOS.setCentralWidget(self.centralwidget)

        self.retranslateUi(MOS)
        self.stackedWidget_mos_right.setCurrentIndex(0)
        self.stackedWidget_gonggao.setCurrentIndex(1)
        self.comboBox_gonggao_right.setCurrentIndex(-1)
        self.stackedWidget_mos_right_2.setCurrentIndex(0)
        self.stackedWidget_5.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.fontComboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MOS)


        # =============================================================================#

        #dir = QFileDialog()
        #dir.setFileMode(QFileDialog.DirectoryOnly)
        #home_dir = str(Path.home())
        #fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)
        self.comboBox_gonggao_right.clear()
        self.listWidget.clear()
        self.pushButton_18.setEnabled(False)

        self.progressBar_2.setMinimum(0)
        self.progressBar_2.setMaximum(99)
        self.progressBar_2.setValue(0)
        self.stackedWidget_mos_right.setCurrentIndex(0)
        # 启动线程
        self.a = MOS_file()
        self.a.sinOut.connect(self.MOS_file_return)
        self.a.sinOut_font.connect(self.MOS_file_return_font)
        self.a.start()

        # self.setfont_size()

        
        # =============================================================================#

    # =================================分割线===================================#

    def click_pushButton_home(self):
        self.stackedWidget_mos_right.setCurrentIndex(0)
        pushButton_home_true = ("QWidget\n"
                                 "{\n"
                                 "    background-color: rgb(231, 230, 228);\n"
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
                                 "    background-color: rgb(231, 230, 228);\n"
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
                                 "    background-color: rgb(231, 230, 228);\n"
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
                                 "    background-color: rgb(231, 230, 228);\n"
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
                                 "    background-color: rgb(231, 230, 228);\n"
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
                                 "    background-color: rgb(231, 230, 228);\n"
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
        '''当点击“关于”页面中的“赞助作”按钮后……'''
        webbrowser.open("https://afdian.net/@David_MOS")

    def click_pushButton_qhqqi_blog(self):
        '''当点击“关于”页面中的“打开QHQQI博客”按钮后……'''
        webbrowser.open("https://blog.qhqqi.top")
    
    def click_pushButton_youximululeibiao(self):
        self.stackedWidget_mos_right.setCurrentIndex(1)

    def game_first_initialize_add(self, name, back= None):
        '''将游戏添加到 主页上“选择要启动的游戏”下拉框 和“游戏目录”列表中 所选的目录下的游戏列表中
            如果要 将 “游戏目录列表” 右边的页面 切换为 “当前选择的游戏目录 中的游戏 列表” back='Yes'
            如果不，请写No
        '''
        # 先清空列表
        self.listWidget_2.clear()
        self.listWidget_2.addItems(name)
        if back != 'No':
            self.stackedWidget_5.setCurrentIndex(0)
        elif back == 'No':
            pass
    def game_first_initialize_add_DropDownBox(self, name):
        '''在刚开始运行时，将所有的游戏添加到“选择要启动的游戏”下拉框中'''
        self.comboBox_gonggao_right.clear()
        self.comboBox_gonggao_right.addItems(name)

    def game_first_initialize_add_error(self, error):
        '''当点击 “游戏文件夹列表” 中的 文件夹后，检测目录下的游戏后 发生的错误'''
        if error == '该版本文件夹下无游戏':
            # 先清空列表
            self.listWidget_2.clear()
            self.listWidget_2.addItem("该版本文件夹下无游戏")
            self.stackedWidget_5.setCurrentIndex(0)
        elif error == '该版本文件夹下无游戏目录':
            # 先清空列表
            self.listWidget_2.clear()
            self.listWidget_2.addItem("该版本文件夹下无游戏目录")
            self.stackedWidget_5.setCurrentIndex(0)

    def game_dir_add(self, name):
        '''在游戏文件夹类表中添加（多个）“文本”和图标'''
        for name_1 in name:
            icon2 = os.path.join("picture","folder.png")
            item = QListWidgetItem(QIcon(icon2),name_1)
            self.listWidget.addItem(item)
    
    def click_pushButton_youximululeibiao_back(self):
        '''当点击版本列表页面上方的“返回”按钮后……'''
        self.stackedWidget_mos_right.setCurrentIndex(0)

    def click_pushButton_youximululeibiao_shezhi(self):
        '''点击版本文件夹设置后……'''
        self.stackedWidget_5.setCurrentIndex(2)

    def click_pushButton_youximululeibiao_add_qian(self):
        '''点击版本列表中的“添加版本文件夹”按钮后……'''
        self.stackedWidget_5.setCurrentIndex(1)

    def click_pushButton_youximululeibiao_add(self):
        '''版本文件夹添加页面的目录选择'''
        dir = QFileDialog()
        dir.setFileMode(QFileDialog.FileMode.Directory)
        dir.setDirectory(file)
        #dir.setNameFilter('999(*.png)') 名称过滤器
        if dir.exec():
            MOS_banbenwenjianjia_file = dir.selectedFiles()
            MOS_print("info",str("选择文件夹" + str(MOS_banbenwenjianjia_file)))
            for MOS_banbenwenjianjia_file_1 in MOS_banbenwenjianjia_file:
                self.label_46.setText(str(MOS_banbenwenjianjia_file_1))
            if self.lineEdit_4.text() == '':
                self.pushButton_18.setEnabled(False)
            else:
                self.pushButton_18.setEnabled(True)

        #写法二
        #fname = QFileDialog.getOpenFileName(None, 'Open file', 'l(*.png)')
        '''QWidget = None, caption: str = '', directory: str = '', filter: str = '', initial Filter: str = '''
        '''QWidget = None，标题:str = "，      目录:str = "，         过滤器:str = "，   初始过滤器:str = '''

    def click_pushButton_youximululeibiao_add_back(self):
        '''当点击“添加版本文件夹”页面上方的“返回”按钮后……'''
        self.stackedWidget_5.setCurrentIndex(0)

    def click_lineEdit_youximululeibiao_check(self):
        '''当“添加版本文件夹”页面中的“名称输入框”中的文字改变时，检查是否设置了要添加的文件夹路径。如果没有就不激活按钮，如果有，则激活'''
        a = self.lineEdit_4.text()
        if self.label_46.text() == "请先选择一个目录":
            self.pushButton_18.setEnabled(False)
        else:
            self.pushButton_18.setEnabled(True)
            self.pushButton_18.setText("确认添加")

    def click_lineEdit_youximululeibiao_check_leibiao(self, item):
        '''点击游戏目录列表中的某一项后，加载所对应的路径下的游戏，并显示'''
        # 切换为加载页面
        self.stackedWidget_5.setCurrentIndex(3)
        # 加载动图
        gif_file = os.path.join("picture","loading.gif")
        self.gif = QtGui.QMovie(gif_file)
        self.label_26.setMovie(self.gif)
        self.gif.start()
        # 开始检测对应的路径下的游戏
        file_name = item.text()
        name = MOS_json_read(MOS_game_dir = 'Yes', MOS_game_name_dir = file_name)
        self.game = game_first_initialize(file_versinons=name)
        self.game.sinOut_game_add.connect(self.game_first_initialize_add)
        self.game.sinOut_game_dir_add.connect(self.game_dir_add)
        self.game.sinOut_game_error.connect(self.game_first_initialize_add_error)
        self.game.start()


            



    def click_pushButton_youximululeibiao_add_confirm(self):
        '''当点击“添加游戏目录”页面中的“添加”按钮后……'''
        back = self.pushButton_18.text()
        if back != '添加完成, 再次点击可返回':
            a = self.label_46.text()
            if a == "请先选择一个目录":
                pass
                #self.label_46.setText("请选择目录")
            else:
                b = self.lineEdit_4.text()
                MOS_print("info",str("路径：" + a))
                MOS_print("info",str("名称：" + b))
                self.pushButton_18.setEnabled(False)
                self.pushButton_18.setText("正在设置并添加，请稍等")
                # 获取Json文件内容
                a_1 = MOS_json_read(All = "Yes")
                # 提取名称列表
                b_1 = a_1['game_file_name']
                # 将新的名称加到提取出的名称表中
                b_1.append(b)
                # 将修改过的名称类表 “替换” 到原类表中
                a_1['game_file_name'] = b_1
                # 将对应的 路径 添加到 原类表中
                a_1[b] = a
                MOS_print("info",str(a_1))
                MOS_json_write(a_1)

                self.pushButton_18.setText("添加完成, 等待刷新")
                
                name_2 = MOS_json_read(MOS_game_dir='Yes', MOS_game_dir_name_or_dir='name')
                self.listWidget.clear()
                for name_1 in name_2:
                    icon2 = os.path.join("picture","folder.png")
                    item = QListWidgetItem(QIcon(icon2),name_1)
                    self.listWidget.addItem(item)
                self.pushButton_18.setText("添加完成, 再次点击可返回")
                self.pushButton_18.setEnabled(True)
        elif back == '添加完成, 再次点击可返回':
            self.stackedWidget_5.setCurrentIndex(0)

            

    def gonggao(self, str):
        self.textBrowser_gonggao_left_txt.setHtml(str)
        self.progressBar_2.setMinimum(0)
        self.progressBar_2.setMaximum(99)
        self.progressBar_2.setValue(90)
        self.stackedWidget_gonggao.setCurrentIndex(0)

        

    def gonggao_jindu(self, t, text = None):
        if text == None:
            pass
        else:
            self.label_2.setText(text)
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
        '''显示公告的控件上方的提示'''
        _translate = QtCore.QCoreApplication.translate
        self.label_gonggao_left_txt.setText(_translate(text1,text2))

    def click_comboBox_shezhi(self):
        '''设置页'''
        a = self.comboBox.currentText()
        if a == "启动器设置":
            self.stackedWidget.setCurrentIndex(0)
        elif a == "全局游戏设置":
            self.stackedWidget.setCurrentIndex(1)

    def click_pushButton_jianchagengxin(self):
        self.pushButton_19.setEnabled(False)
        if self.pushButton_19.text() != '检查到更新，点击下载':
            self.pushButton_19.setEnabled(False)
            self.v = MOS_versions(a)
            self.v.sinOut_versions.connect(self.click_pushButton_jianchagengxin_sinOut)
            self.v.sinOut_versions_yes_no.connect(self.click_pushButton_jianchagengxin_sinOut_versions_yes_no)
            self.v.sinOut_versions_yes.connect(self.click_pushButton_jianchagengxin_sinOut_versions_yes)
            self.v.start()
        else:
            self.pushButton_18.setEnabled(True)
        
    
    def click_pushButton_jianchagengxin_sinOut(self,text):
        self.pushButton_19.setText(text)

    def click_pushButton_jianchagengxin_sinOut_versions_yes_no(self,text):
        if text == "No":
            self.pushButton_19.setText("检测完毕 没有更新 点击重新获取")
            self.pushButton_19.setEnabled(True)

    def click_pushButton_jianchagengxin_sinOut_versions_yes(self,url,text,v):
        self.pushButton_19.setText("检查到更新，在弹出的窗口中下载&查看更新内容")
        self.pushButton_19.setEnabled(True)
        a = QMessageBox.information(None,"更新",str("<html><head/><body><h1> 版本" + v + "的更新内容： </h1><p>" + text + "</p></body></html>"),QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel,QMessageBox.StandardButton.Ok)

        if a == QMessageBox.StandardButton.Ok: #点了OK按钮
            dir = QFileDialog()
            dir.setFileMode(QFileDialog.FileMode.Directory)
            dir.setDirectory(str(file_h))
            if dir.exec():
                file_2 = dir.selectedFiles()
                file_1 = file_2[0]
                if str(system_h) == "darwin":
                    file = os.path.join(file_1,'MOS.dmg')
                else:
                    file = os.path.join(file_1,'MOS.zip')
                header = {'User-Agent':'Mozilla/55.0 (Macintosh; Intel Mac OS X 55.55; rv:101.0) Gecko/20100101 Firefox/101.0'}    # 伪装浏览器
                r_2 = open(file, 'w+')
                r_2.close
                r = requests.get(url, stream=True, timeout=(60,120), headers = header)
                with open(file, "wb") as f:
                    for chunk in r.iter_content(chunk_size=10240):  # 每次加载……字节
                        f.write(chunk)
                        print("kk")




    def setfont(self):
        '''在“字体选择下拉菜单”中 更改字体后，设置字体'''
        a = self.fontComboBox.currentText()
        MOS_print("info",a)
        self.label_4.setFont(QtGui.QFont(a))
        self.label_6.setFont(QtGui.QFont(a))
        self.label_mos_left_top_user.setFont(QtGui.QFont(a))
        self.label_mos_left_top_add.setFont(QtGui.QFont(a))
        self.label_gonggao_left_txt.setFont(QtGui.QFont(a))
        self.label_2.setFont(QtGui.QFont(a))
        self.progressBar_2.setFont(QtGui.QFont(a))
        self.label__gonggao_right_txt.setFont(QtGui.QFont(a))
        self.label_3.setFont(QtGui.QFont(a))
        self.progressBar.setFont(QtGui.QFont(a))
        self.label_7.setFont(QtGui.QFont(a))
        self.label_9.setFont(QtGui.QFont(a))
        self.label_8.setFont(QtGui.QFont(a))
        self.label_10.setFont(QtGui.QFont(a))
        self.label_11.setFont(QtGui.QFont(a))
        self.label_19.setFont(QtGui.QFont(a))
        self.label_20.setFont(QtGui.QFont(a))
        self.label_21.setFont(QtGui.QFont(a))
        self.label_12.setFont(QtGui.QFont(a))
        self.label_13.setFont(QtGui.QFont(a))
        self.label_15.setFont(QtGui.QFont(a))
        self.label_17.setFont(QtGui.QFont(a))
        self.label.setFont(QtGui.QFont(a))
        self.label_16.setFont(QtGui.QFont(a))
        self.label_18.setFont(QtGui.QFont(a))
        self.label_22.setFont(QtGui.QFont(a))
        self.label_gonggao_left_txt.setFont(QtGui.QFont(a))
        self.label_24.setFont(QtGui.QFont(a))
        self.pushButton_home.setFont(QtGui.QFont(a))
        self.pushButton_lianji.setFont(QtGui.QFont(a))
        self.pushButton_music.setFont(QtGui.QFont(a))
        self.pushButton_shezhi.setFont(QtGui.QFont(a))
        self.pushButton_xiazai.setFont(QtGui.QFont(a))
        self.pushButton_about.setFont(QtGui.QFont(a))
        self.pushButton__gonggao_start.setFont(QtGui.QFont(a))
        self.pushButton_5.setFont(QtGui.QFont(a))
        self.pushButton_6.setFont(QtGui.QFont(a))
        self.pushButton_7.setFont(QtGui.QFont(a))
        self.pushButton_8.setFont(QtGui.QFont(a))
        self.pushButton_11.setFont(QtGui.QFont(a))
        self.pushButton_17.setFont(QtGui.QFont(a))
        self.pushButton_16.setFont(QtGui.QFont(a))
        self.pushButton_36.setFont(QtGui.QFont(a))
        self.pushButton_37.setFont(QtGui.QFont(a))
        self.pushButton_38.setFont(QtGui.QFont(a))
        self.pushButton_39.setFont(QtGui.QFont(a))
        self.pushButton_40.setFont(QtGui.QFont(a))
        self.comboBox_gonggao_right.setFont(QtGui.QFont(a))
        self.comboBox_2.setFont(QtGui.QFont(a))
        self.comboBox_3.setFont(QtGui.QFont(a))
        self.comboBox_4.setFont(QtGui.QFont(a))
        self.comboBox_5.setFont(QtGui.QFont(a))
        self.comboBox_6.setFont(QtGui.QFont(a))
        self.comboBox.setFont(QtGui.QFont(a))
        self.comboBox_gonggao_right.setFont(QtGui.QFont(a))
        self.fontComboBox.setFont(QtGui.QFont(a))
        self.progressBar.setFont(QtGui.QFont(a))
        self.listWidget.setFont(QtGui.QFont(a))
        self.listWidget_2.setFont(QtGui.QFont(a))
        self.lineEdit_3.setFont(QtGui.QFont(a))
        self.pushButton_19.setFont(QtGui.QFont(a))
        self.label_5.setFont(QtGui.QFont(a))
        self.radioButton.setFont(QtGui.QFont(a))
        self.pushButton_20.setFont(QtGui.QFont(a))
        self.label_14.setFont(QtGui.QFont(a))
        self.comboBox_7.setFont(QtGui.QFont(a))
        self.pushButton_21.setFont(QtGui.QFont(a))
        self.label_14.setFont(QtGui.QFont(a))
        # 修改在json中的字体
        a = str(sys.platform)
        if a == "darwin":
            MOS_print("info",'当前系统为Mac')
            user_name = os.getlogin()
            # 获取当前系统用户目录
            user_home = os.path.expanduser('~')
            file = user_home + '/Documents'
        else:
            file = ''
        MOS_file_json =os.path.join(file,".MOS","MOS.json")
        try:
            with open(MOS_file_json, 'r+', encoding='utf-8') as f:
                b = json.load(f)
                b['font'] = self.fontComboBox.currentText()
                b['font_default'] = 'No'
            with open(MOS_file_json, 'w+', encoding='utf-8') as f:
                json.dump(b, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
                b_1 = '默认字体：' + str(b)
                MOS_print("info",b_1)
        except KeyError:
            MOS_print("error","json文件有问题")
        except json.decoder.JSONDecodeError:
            MOS_print("error","json数据异常")
        except FileNotFoundError:
            pass
            #with open(MOS_file_json, 'w') as f:
            #    print("000")
            #with open(MOS_file_json, 'r+', encoding='utf-8') as f:
            #    b = json.load(f)
            #    b['font'] = self.fontComboBox.currentText()
            #with open(MOS_file_json, 'w+', encoding='utf-8') as f:
            #    json.dump(b, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
            #    b1 = str(b)
            #    print('默认字体：' + b1)

    
    # def setfont_size(self):
        '''修改默认字体大小'''

        Ui_title_left_left_2 = 15
        Ui_title_left = "font-size: " + str(Ui_title_left_left_2) + "px;"
        self.pushButton_home.setStyleSheet(Ui_title_left)
        self.pushButton_lianji.setStyleSheet(Ui_title_left)
        self.pushButton_xiazai.setStyleSheet(Ui_title_left)
        self.pushButton_music.setStyleSheet(Ui_title_left)
        self.pushButton_shezhi.setStyleSheet(Ui_title_left)
        self.pushButton_about.setStyleSheet(Ui_title_left)

        Ui_title_right_2 = 17
        Ui_title_right = "font-size: " + str(Ui_title_right_2) + "px;"
        self.label_24.setStyleSheet(Ui_title_right)
        self.label_43.setStyleSheet(Ui_title_right)
        self.label_9.setStyleSheet(Ui_title_right)
        self.label_10.setStyleSheet(Ui_title_right)
        self.label_12.setStyleSheet(Ui_title_right)
        self.label_15.setStyleSheet(Ui_title_right)
        self.label_17.setStyleSheet(Ui_title_right)

    def click_pushButton_shezhi_fond_moren(self):
        '''当用户点击字体设置的“恢复默认”后……'''
        str1 = 'FangSong'
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
        self.label_24.setFont(QtGui.QFont(str1))
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
        self.pushButton_17.setFont(QtGui.QFont(str1))
        self.pushButton_16.setFont(QtGui.QFont(str1))
        self.pushButton_36.setFont(QtGui.QFont(str1))
        self.pushButton_37.setFont(QtGui.QFont(str1))
        self.pushButton_38.setFont(QtGui.QFont(str1))
        self.pushButton_39.setFont(QtGui.QFont(str1))
        self.pushButton_40.setFont(QtGui.QFont(str1))
        self.comboBox_gonggao_right.setFont(QtGui.QFont(str1))
        self.comboBox_2.setFont(QtGui.QFont(str1))
        self.comboBox_3.setFont(QtGui.QFont(str1))
        self.comboBox_4.setFont(QtGui.QFont(str1))
        self.comboBox_5.setFont(QtGui.QFont(str1))
        self.comboBox_6.setFont(QtGui.QFont(str1))
        self.comboBox.setFont(QtGui.QFont(str1))
        self.comboBox_gonggao_right.setFont(QtGui.QFont(str1))
        self.fontComboBox.setFont(QtGui.QFont(str1))
        self.progressBar.setFont(QtGui.QFont(str1))
        self.listWidget.setFont(QtGui.QFont(str1))
        self.listWidget_2.setFont(QtGui.QFont(str1))
        self.lineEdit_3.setFont(QtGui.QFont(str1))
        self.pushButton_19.setFont(QtGui.QFont(str1))
        self.label_5.setFont(QtGui.QFont(str1))
        self.radioButton.setFont(QtGui.QFont(str1))
        self.pushButton_20.setFont(QtGui.QFont(str1))
        self.label_14.setFont(QtGui.QFont(str1))
        self.comboBox_7.setFont(QtGui.QFont(str1))
        self.pushButton_21.setFont(QtGui.QFont(str1))
        self.label_14.setFont(QtGui.QFont(str1))

        # 修改在json中的字体
        a = str(sys.platform)
        if a == "darwin":
            user_name = os.getlogin()
            # 获取当前系统用户目录
            user_home = os.path.expanduser('~')
            file = user_home + '/Documents'
        else:
            file = ''
        MOS_file_json =os.path.join(file,".MOS","MOS.json")
        try:
            with open(MOS_file_json, 'r+', encoding='utf-8') as f:
                b = json.load(f)
                b['font'] = str1
            with open(MOS_file_json, 'w+', encoding='utf-8') as f:
                json.dump(b, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
                b1 = str(b)
                MOS_print("info",str('默认字体：' + b1))
        except KeyError:
            MOS_print("error","json文件有问题")
        except json.decoder.JSONDecodeError:
            MOS_print("error","json数据异常")

 

        
    def MOS_file_return_font(self, a):
        MOS_print("info",str)
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
        self.label_24.setFont(QtGui.QFont(str1))
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
        self.pushButton_17.setFont(QtGui.QFont(str1))
        self.pushButton_16.setFont(QtGui.QFont(str1))
        self.pushButton_36.setFont(QtGui.QFont(str1))
        self.pushButton_37.setFont(QtGui.QFont(str1))
        self.pushButton_38.setFont(QtGui.QFont(str1))
        self.pushButton_39.setFont(QtGui.QFont(str1))
        self.pushButton_40.setFont(QtGui.QFont(str1))
        self.comboBox_gonggao_right.setFont(QtGui.QFont(str1))
        self.comboBox_2.setFont(QtGui.QFont(str1))
        self.comboBox_3.setFont(QtGui.QFont(str1))
        self.comboBox_4.setFont(QtGui.QFont(str1))
        self.comboBox_5.setFont(QtGui.QFont(str1))
        self.comboBox_6.setFont(QtGui.QFont(str1))
        self.comboBox.setFont(QtGui.QFont(str1))
        self.comboBox_gonggao_right.setFont(QtGui.QFont(str1))
        self.fontComboBox.setFont(QtGui.QFont(str1))
        self.progressBar.setFont(QtGui.QFont(str1))
        self.listWidget.setFont(QtGui.QFont(str1))
        self.listWidget_2.setFont(QtGui.QFont(str1))
        self.lineEdit_3.setFont(QtGui.QFont(str1))
        self.pushButton_19.setFont(QtGui.QFont(str1))
        self.label_5.setFont(QtGui.QFont(str1))
        self.radioButton.setFont(QtGui.QFont(str1))
        self.pushButton_20.setFont(QtGui.QFont(str1))
        self.label_14.setFont(QtGui.QFont(str1))
        self.comboBox_7.setFont(QtGui.QFont(str1))
        self.pushButton_21.setFont(QtGui.QFont(str1))
        self.label_14.setFont(QtGui.QFont(str1))


    def MOS_file_return(self, str):
        '''文件处理后……（如果成功那么启动2进程 如果失败……）'''
        if str == "OK!":
            self.game = game_first_initialize(all='Yes')
            self.game.sinOut_game_add.connect(self.game_first_initialize_add)
            self.game.sinOut_game_add_DropDownBox.connect(self.game_first_initialize_add_DropDownBox)
            self.game.sinOut_game_dir_add.connect(self.game_dir_add)
            self.game.sinOut_game_error.connect(self.game_first_initialize_add_error)
            self.game.start()

            self.g = gonggao()
            self.g.sinOut_gonggao_ok.connect(self.gonggao)
            self.g.sinOut_gonggao_jindu.connect(self.gonggao_jindu)
            self.g.sinOut_gonggao_error.connect(self.gonggao_error)
            self.g.sinOut_gonggao_text.connect(self.gonggao_text)
            self.g.start()
        elif str == "ERROR_PermissionError" :
            #self.second = MOS_UI2.Ui_MainWindow()
            #self.second.show()
            a = QMessageBox.critical(None,"错误","没有权限，无法完成操作。即将退出程序",QMessageBox.StandardButton.Yes,QMessageBox.StandardButton.Yes)
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
        self.label_2.setText(_translate("MOS", "正在加载\n"
"\n"
"当前步骤：下载公告……请稍后\n"
""))
        self.label_gonggao_left_txt.setText(_translate("MOS", "<html><head/><body><p>官方公告 <span style=\" color:#55f976;\">•正在加载中</span></p></body></html>"))
        self.label__gonggao_right_txt.setText(_translate("MOS", "<html><head/><body><p>启动游戏 <span style=\" color:#0096ff;\">•等待启动</span></p></body></html>"))
        self.label_7.setText(_translate("MOS", "启动君：待命中……"))
        self.pushButton_16.setText(_translate("MOS", "版本列表"))
        self.pushButton_17.setText(_translate("MOS", "版本设置"))
        self.pushButton__gonggao_start.setText(_translate("MOS", "启动游戏"))
        self.label_24.setText(_translate("MOS", "版本列表"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MOS", "默认目录"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_38.setText(_translate("MOS", "版本设置"))
        self.pushButton_36.setText(_translate("MOS", "添加版本文件夹"))
        self.pushButton_37.setText(_translate("MOS", "安装整合包"))
        self.label_44.setText(_translate("MOS", "目录名称："))
        self.lineEdit_4.setPlaceholderText(_translate("MOS", "请输入目录名"))
        self.label_47.setText(_translate("MOS", "* 目录名相当于给 游戏目录起了个名字"))
        self.label_43.setText(_translate("MOS", "添加游戏目录"))
        self.label_45.setText(_translate("MOS", "选择目录："))
        self.label_48.setText(_translate("MOS", "选择的路径："))
        self.pushButton_42.setText(_translate("MOS", "选择……"))
        self.label_46.setText(_translate("MOS", "请先选择一个目录"))
        self.pushButton_18.setText(_translate("MOS", "确定添加"))
        self.pushButton_40.setText(_translate("MOS", "删除游戏文件夹"))
        self.pushButton_39.setText(_translate("MOS", "重命名版本文件夹"))
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
        self.lineEdit.setPlaceholderText(_translate("MOS", "版本名"))
        self.pushButton_2.setText(_translate("MOS", "安装"))
        self.label_12.setText(_translate("MOS", "音乐"))
        self.label_13.setText(_translate("MOS", "音乐 正在开发中……\n"
"不要着急啦 你的赞助就是我更新的动力！嘻嘻～"))
        self.label_15.setText(_translate("MOS", "设置"))
        self.pushButton_11.setText(_translate("MOS", "恢复默认"))
        self.label_4.setText(_translate("MOS", "<html><head/><body style=\"line-height:1px;\"><p style=\"line-height:1px;\"><span style=\" font-size:20pt;\">启动器字体</span></p><p  style=\"line-height:1px;\">在这里 你可以自定义启动器字体 有的字体相差很小，导致有人可能认为<span style=\" font-style:italic;line-height:1px;\">字体没有更改</span>，其实不是的</p></body></html>"))
        self.label_6.setText(_translate("MOS", "Hello Minecraft Optimal Starter 2 !"))
        self.pushButton_19.setText(_translate("MOS", "检查更新"))
        self.label_5.setText(_translate("MOS", "<html><head/><body><p><span style=\" font-size:20pt;\">启动器更新</span></p><p>在这里 你可以更新启动器</p><p>你可以在“关于”中查看当前版本</p></body></html>"))
        self.radioButton.setText(_translate("MOS", "自动为您检查更新"))
        self.pushButton_20.setText(_translate("MOS", "开始更新"))
        self.label_14.setText(_translate("MOS", "<html><head/><body><p><span style=\" font-size:20pt;\">Java设置</span></p><p>在这里 你可以设置启动游戏时使用的Java 建议选择 <span style=\" font-style:italic;\">让MOS为您自动选择</span></p><p>注意：<span style=\" font-weight:600;\">不要使用</span><span style=\" font-weight:600; font-style:italic;\">网易启动器</span><span style=\" font-weight:600;\">的Java 、</span><span style=\" font-weight:600; font-style:italic;\">1.17</span><span style=\" font-weight:600;\">及以上版本需用</span><span style=\" font-weight:600; font-style:italic;\">Java16</span><span style=\" font-weight:600;\">及以上版本 1.17一下需用Java8</span></p></body></html>"))
        self.comboBox_7.setItemText(0, _translate("MOS", "让MOS自动为您选择"))
        self.pushButton_21.setText(_translate("MOS", "恢复默认"))
        self.comboBox.setItemText(0, _translate("MOS", "启动器设置"))
        self.comboBox.setItemText(1, _translate("MOS", "全局游戏设置"))
        self.label.setText(_translate("MOS", "关于："))
        self.label_16.setText(_translate("MOS", "MOS启动器\n"
"版本V2.0.5-alpha"))
        self.label_18.setText(_translate("MOS", "MOS唯一开发者 David"))
        self.pushButton_3.setText(_translate("MOS", "赞助作者"))
        self.label_22.setText(_translate("MOS", "MOS网站支持、测试小组负责人 HeimNad"))
        self.pushButton_10.setText(_translate("MOS", "打开博客"))
        self.label_17.setText(_translate("MOS", "关于"))
        self.label_mos_left_top_add.setText(_translate("MOS", "点击添加"))
        self.label_mos_left_top_user.setText(_translate("MOS", "无用户"))
        self.pushButton_home.setText(_translate("MOS", "主页"))
        self.pushButton_lianji.setText(_translate("MOS", "联机"))
        self.pushButton_xiazai.setText(_translate("MOS", "下载"))
        self.pushButton_music.setText(_translate("MOS", "音乐"))
        self.pushButton_shezhi.setText(_translate("MOS", "设置"))
        self.pushButton_about.setText(_translate("MOS", "关于"))
        self.label_mosll.setText(_translate("MOS", "MOS II"))



        
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
        self.pushButton_16.clicked.connect(self.click_pushButton_youximululeibiao)
        self.pushButton_35.clicked.connect(self.click_pushButton_youximululeibiao_back)
        self.pushButton_38.clicked.connect(self.click_pushButton_youximululeibiao_shezhi)
        self.pushButton_36.clicked.connect(self.click_pushButton_youximululeibiao_add_qian)
        self.pushButton_42.clicked.connect(self.click_pushButton_youximululeibiao_add)
        self.pushButton_41.clicked.connect(self.click_pushButton_youximululeibiao_add_back)
        self.pushButton_18.clicked.connect(self.click_pushButton_youximululeibiao_add_confirm)
        self.lineEdit_4.textChanged.connect(self.click_lineEdit_youximululeibiao_check)
        # 在lineEdit_4里显示所有
        # 为字体选择控件 连接槽
        self.fontComboBox.currentIndexChanged.connect(self.setfont)
        self.listWidget.itemClicked.connect(self.click_lineEdit_youximululeibiao_check_leibiao)
        #
        self.comboBox.currentIndexChanged.connect(self.click_comboBox_shezhi)
        self.pushButton_19.clicked.connect(self.click_pushButton_jianchagengxin)


class gonggao(QThread):
    '''获取公告'''
    sinOut_gonggao_ok = pyqtSignal(str)
    sinOut_gonggao_jindu = pyqtSignal(str, str)
    sinOut_gonggao_error = pyqtSignal(str)
    sinOut_gonggao_text = pyqtSignal(str,str)

    def __init__(self):
        super(gonggao, self).__init__()

    def run(self):
        import requests
        import time, sys
        import linecache

        a = str(sys.platform)
        if a == "darwin":
            user_name = os.getlogin()
            # 获取当前系统用户目录
            user_home = os.path.expanduser('~')
            file = user_home + '/Documents'
        else:
            file = ''

        self.sinOut_gonggao_jindu.emit('10','正在加载\n\n当前步骤：初始化(1/2)……请稍后\n')
        MOS_print("info","开始获取公告")
        #url = 'https://file.skyworldstudio.top/d/SoftwareRelease/MOS/announcement.html'
        url = 'https://cdn.jsdelivr.net/gh/xianyongjian080402/Minecraft-Optimal-Starter_2/html/MOS.htmlm'
        url_2 = 'https://purge.jsdelivr.net/gh/xianyongjian080402/Minecraft-Optimal-Starter_2/html/MOS.htmlm'
        self.sinOut_gonggao_jindu.emit('20','正在加载\n\n当前步骤：初始化(2/2)……请稍后\n')
        try:
            header = {'User-Agent':'Mozilla/55.0 (Macintosh; Intel Mac OS X 55.55; rv:101.0) Gecko/20100101 Firefox/101.0'}    # 伪装浏览器
            try:
                self.sinOut_gonggao_jindu.emit('35','正在加载\n\n当前步骤：刷新远程服务器文件(为了确保文件是最新的，我们需要远程服务器刷新文件)……请稍后\n')
                r_2 = requests.get(url_2, timeout=(5,50), headers = header)
            except:
                pass
            self.sinOut_gonggao_jindu.emit('50','正在加载\n\n当前步骤：获取公告……请稍后\n')
            r = requests.get(url, timeout=(5,50), headers = header)  # Get方式获取网页数据

            if r.status_code == 200:
                # 拼接路径
                self.sinOut_gonggao_jindu.emit('80','正在加载\n\n当前步骤：获取完成-正在处理(1/3)……请稍后\n')
                MOS_L=os.path.join(file,".MOS","Html","announcement.html")
                self.sinOut_gonggao_jindu.emit('90','正在加载\n\n当前步骤：获取完成-正在处理(2/3)……请稍后\n')
                #写入文件
                MOS_Html_gonggao_ok = open(MOS_L, 'w+', encoding='utf-8')
                a = r.text
                MOS_Html_gonggao_ok.write(a)
                MOS_Html_gonggao_ok.close
                MOS_print("info",a)
                self.sinOut_gonggao_ok.emit(a)
                self.sinOut_gonggao_jindu.emit('99','正在加载\n\n当前步骤：获取完成-正在处理(3/3)……请稍后\n')
                self.sinOut_gonggao_text.emit("MOS", "<html><head/><body><p>官方公告 <span style=\" color:#55f976;\">•公告获取成功！✓</span></p></body></html>")
                MOS_print("info","请求成功")
                        
            elif r.status_code != 200:
                if r.status_code == 404:
                    self.sinOut_gonggao_jindu.emit('80','正在加载\n\n当前步骤：获取失败-正在准备加载旧公告……请稍后\n')
                    MOS_print("error","公告请求失败，状态码为404")
                    if os.path.isfile(a)==True:
                        gangshu = len(linecache.getlines(a))    # 统计行数
                        self.sinOut_gonggao_jindu.emit('85','正在加载\n\n当前步骤：获取失败-正在加载旧公告(1/3)……请稍后\n')
                        gangshu1 = 0
                        gonggao = ''
                        while gangshu1 <= gangshu:
                            g = linecache.getline(a,gangshu1)
                            gonggao = gonggao + g
                            gangshu1 += 1
                        self.sinOut_gonggao_jindu.emit('90','正在加载\n\n当前步骤：获取失败-正在加载旧公告(2/3)……请稍后\n')
                        MOS_print("info",str('\n'+gonggao))
                        gonggao = str(gonggao)
                        self.sinOut_gonggao_jindu.emit('95','正在加载\n\n当前步骤：获取失败-正在加载旧公告(3/3)……请稍后\n')
                        self.sinOut_gonggao_text.emit("MOS", "<html><head/><body><p>官方公告 <span style=\" color:rgb(255, 38, 0);\">•获取失败！✗ 404找不到文件 以为您自动显示上次获取到的内容</span></p></body></html>")
                        self.sinOut_gonggao_error.emit(gonggao) 
                    else:
                        self.sinOut_gonggao_error.emit("404，找不到文件")
                elif r.status_code == 403:
                    self.sinOut_gonggao_jindu.emit('80','正在加载\n\n当前步骤：获取失败-正在准备加载旧公告……请稍后\n')
                    MOS_print("error","公告请求失败，状态码为403")
                    if os.path.isfile(a)==True:
                        gangshu = len(linecache.getlines(a))    # 统计行数
                        self.sinOut_gonggao_jindu.emit('85','正在加载\n\n当前步骤：获取失败-正在加载旧公告(1/3)……请稍后\n')
                        gangshu1 = 0
                        gonggao = ''
                        while gangshu1 <= gangshu:
                            g = linecache.getline(a,gangshu1)
                            gonggao = gonggao + g
                            gangshu1 += 1
                        self.sinOut_gonggao_jindu.emit('90','正在加载\n\n当前步骤：获取失败-正在加载旧公告(2/3)……请稍后\n')
                        MOS_print("info",str('\n'+gonggao))
                        gonggao = str(gonggao)
                        self.sinOut_gonggao_jindu.emit('95','正在加载\n\n当前步骤：获取失败-正在加载旧公告(3/3)……请稍后\n')
                        self.sinOut_gonggao_text.emit("MOS", "<html><head/><body><p>官方公告 <span style=\" color:rgb(255, 38, 0);\">•获取失败！✗ 403无权访问 以为您自动显示上次获取到的内容</span></p></body></html>")
                        self.sinOut_gonggao_error.emit(gonggao) 
                    else:
                        self.sinOut_gonggao_error.emit("403，无权限访问")

                else:
                    self.sinOut_gonggao_jindu.emit('80','正在加载\n\n当前步骤：获取失败-正在准备加载旧公告……请稍后\n')
                    gonggao_r_status_code = r.status_code
                    gonggao_r_status_code1 = str(gonggao_r_status_code)
                    gonggao_111 = ("公告请求失败，状态码为" + gonggao_r_status_code1)
                    MOS_print("info", gonggao_111)
                    if os.path.isfile(a)==True:
                        gangshu = len(linecache.getlines(a))    # 统计行数
                        self.sinOut_gonggao_jindu.emit('85','正在加载\n\n当前步骤：获取失败-正在加载旧公告(1/3)……请稍后\n')
                        gangshu1 = 0
                        gonggao = ''
                        while gangshu1 <= gangshu:
                            g = linecache.getline(a,gangshu1)
                            gonggao = gonggao + g
                            gangshu1 += 1
                        self.sinOut_gonggao_jindu.emit('90','正在加载\n\n当前步骤：获取失败-正在加载旧公告(2/3)……请稍后\n')
                        MOS_print("info",str('\n'+gonggao))
                        gonggao = str(gonggao)
                        self.sinOut_gonggao_jindu.emit('95','正在加载\n\n当前步骤：获取失败-正在加载旧公告(3/3)……请稍后\n')
                        self.sinOut_gonggao_text.emit("MOS", "<html><head/><body><p>官方公告 <span style=\" color:rgb(255, 38, 0);\">•获取失败！✗ 403无权访问 以为您自动显示上次获取到的内容</span></p></body></html>")
                        self.sinOut_gonggao_error.emit(gonggao) 
                    else:
                        self.sinOut_gonggao_error.emit(gonggao_111)
                


        except requests.exceptions.ConnectTimeout:
            self.sinOut_gonggao_jindu.emit('80','正在加载\n\n当前步骤：获取失败-正在准备加载旧公告……请稍后\n')
            # self.sinOut_gonggao_error.emit("请求超时")
            a = os.path.join(file,".MOS","Html","announcement.html")
            if os.path.isfile(a)==True:
                self.sinOut_gonggao_jindu.emit('85','正在加载\n\n当前步骤：获取失败-正在加载旧公告(1/3)……请稍后\n')
                gangshu = len(linecache.getlines(a))    # 统计行数
                gangshu1 = 0
                gonggao = ''
                while gangshu1 <= gangshu:
                    g = linecache.getline(a,gangshu1)
                    gonggao = gonggao + g
                    gangshu1 += 1
                self.sinOut_gonggao_jindu.emit('90','正在加载\n\n当前步骤：获取失败-正在加载旧公告(2/3)……请稍后\n')
                MOS_print("error","请求失败 请求超时")
                MOS_print("info",str('\n'+gonggao))
                gonggao = str(gonggao)
                self.sinOut_gonggao_jindu.emit('95','正在加载\n\n当前步骤：获取失败-正在加载旧公告(3/3)……请稍后\n')
                self.sinOut_gonggao_text.emit("MOS", "<html><head/><body><p>官方公告 <span style=\" color:rgb(255, 38, 0);\">•获取失败！✗ 请求超时 以为您自动显示上次获取到的内容</span></p></body></html>")
                self.sinOut_gonggao_error.emit(gonggao)

            else:
                self.sinOut_gonggao_error.emit("请求超时")
                self.sinOut_gonggao_text.emit("MOS", "<html><head/><body><p>官方公告 <span style=\" color:rgb(255, 38, 0);\">•获取失败！✗ 请求超时 无缓存可加载</span></p></body></html>")

        except requests.exceptions.ReadTimeout:
            self.sinOut_gonggao_jindu.emit('80','正在加载\n\n当前步骤：获取失败-正在准备加载旧公告……请稍后\n')
            # self.sinOut_gonggao_error.emit("读取超时")
            a = os.path.join(file,".MOS","Html","announcement.html")
            if os.path.isfile(a)==True:
                self.sinOut_gonggao_jindu.emit('85','正在加载\n\n当前步骤：获取失败-正在加载旧公告(1/3)……请稍后\n')
                gangshu = len(linecache.getlines(a))    # 统计行数
                gangshu1 = 0
                gonggao = ''
                while gangshu1 <= gangshu:
                    g = linecache.getline(a,gangshu1)
                    gonggao = gonggao + g
                    gangshu1 += 1
                self.sinOut_gonggao_jindu.emit('90','正在加载\n\n当前步骤：获取失败-正在加载旧公告(2/3)……请稍后\n')
                MOS_print("error","请求失败 读取超时")
                MOS_print("info",str('\n'+gonggao))
                gonggao = str(gonggao)
                self.sinOut_gonggao_jindu.emit('95','正在加载\n\n当前步骤：获取失败-正在加载旧公告(3/3)……请稍后\n')
                self.sinOut_gonggao_text.emit("MOS", "<html><head/><body><p>官方公告 <span style=\" color:rgb(255, 38, 0);\">•获取失败！✗ 读取超时 以为您自动显示上次获取到的内容</span></p></body></html>")
                self.sinOut_gonggao_error.emit(gonggao)

            else:
                self.sinOut_gonggao_error.emit("读取超时")
                self.sinOut_gonggao_text.emit("MOS", "<html><head/><body><p>官方公告 <span style=\" color:rgb(255, 38, 0);\">•获取失败！✗ 读取超时 无缓存可加载</span></p></body></html>")

        except requests.exceptions.SSLError:
            self.sinOut_gonggao_jindu.emit('80','正在加载\n\n当前步骤：获取失败-正在准备加载旧公告……请稍后\n')
            # self.sinOut_gonggao_error.emit("SSL错误")
            a = os.path.join(file,".MOS","Html","announcement.html")
            if os.path.isfile(a)==True:
                self.sinOut_gonggao_jindu.emit('85','正在加载\n\n当前步骤：获取失败-正在加载旧公告(1/3)……请稍后\n')
                gangshu = len(linecache.getlines(a))    # 统计行数
                gangshu1 = 0
                gonggao = ''
                while gangshu1 <= gangshu:
                    g = linecache.getline(a,gangshu1)
                    gonggao = gonggao + g
                    gangshu1 += 1
                self.sinOut_gonggao_jindu.emit('90','正在加载\n\n当前步骤：获取失败-正在加载旧公告(2/3)……请稍后\n')
                MOS_print("error","请求失败 SSL证书错误")
                MOS_print("info",str('\n'+gonggao))
                gonggao = str(gonggao)
                self.sinOut_gonggao_jindu.emit('95','正在加载\n\n当前步骤：获取失败-正在加载旧公告(3/3)……请稍后\n')
                self.sinOut_gonggao_text.emit("MOS", "<html><head/><body><p>官方公告 <span style=\" color:rgb(255, 38, 0);\">•获取失败！✗ SSL证书错误 以为您自动显示上次获取到的内容</span></p></body></html>")
                self.sinOut_gonggao_error.emit(gonggao)

            else:
                self.sinOut_gonggao_error.emit("SSL证书错误")
                self.sinOut_gonggao_text.emit("MOS", "<html><head/><body><p>官方公告 <span style=\" color:rgb(255, 38, 0);\">•获取失败！✗ SSL证书错误 无缓存可加载</span></p></body></html>")

        except requests.exceptions.ConnectionError:
            self.sinOut_gonggao_jindu.emit('80','正在加载\n\n当前步骤：获取失败-正在准备加载旧公告……请稍后\n')
            # self.sinOut_gonggao_error.emit("连接错误\n")            
            a = os.path.join(file,".MOS","Html","announcement.html")
            if os.path.isfile(a)==True:
                self.sinOut_gonggao_jindu.emit('85','正在加载\n\n当前步骤：获取失败-正在加载旧公告(1/3)……请稍后\n')
                gangshu = len(linecache.getlines(a))    # 统计行数
                gangshu1 = 0
                gonggao = ''
                while gangshu1 <= gangshu:
                    g = linecache.getline(a,gangshu1)
                    gonggao = gonggao + g
                    gangshu1 += 1
                self.sinOut_gonggao_jindu.emit('90','正在加载\n\n当前步骤：获取失败-正在加载旧公告(2/3)……请稍后\n')
                MOS_print("error","请求失败 连接错误")
                MOS_print("info",str('\n'+gonggao))
                gonggao = str(gonggao)
                self.sinOut_gonggao_jindu.emit('95','正在加载\n\n当前步骤：获取失败-正在加载旧公告(3/3)……请稍后\n')
                self.sinOut_gonggao_text.emit("MOS", "<html><head/><body><p>官方公告 <span style=\" color:rgb(255, 38, 0);\">•获取失败！✗ 连接错误 以为您自动显示上次获取到的内容</span></p></body></html>")
                self.sinOut_gonggao_error.emit(gonggao)

            else:
                self.sinOut_gonggao_error.emit("连接错误")
                self.sinOut_gonggao_text.emit("MOS", "<html><head/><body><p>官方公告 <span style=\" color:rgb(255, 38, 0);\">•获取失败！✗ 连接错误 无缓存可加载</span></p></body></html>")
        except:
            self.sinOut_gonggao_jindu.emit('80','正在加载\n\n当前步骤：获取失败-正在准备加载旧公告……请稍后\n')
            error = traceback.print_exc()
            MOS_print("error",error)
            MOS_print("error","请求失败 未知错误")
            a = os.path.join(file,".MOS","Html","announcement.html")
            if os.path.isfile(a)==True:
                self.sinOut_gonggao_jindu.emit('85','正在加载\n\n当前步骤：获取失败-正在加载旧公告(1/3)……请稍后\n')
                gangshu = len(linecache.getlines(a))    # 统计行数
                gangshu1 = 0
                gonggao = ''
                while gangshu1 <= gangshu:
                    g = linecache.getline(a,gangshu1)
                    gonggao = gonggao + g
                    gangshu1 += 1
                self.sinOut_gonggao_jindu.emit('90','正在加载\n\n当前步骤：获取失败-正在加载旧公告(2/3)……请稍后\n')
                MOS_print("info",str('\n'+gonggao))
                gonggao = str(gonggao)
                self.sinOut_gonggao_jindu.emit('95','正在加载\n\n当前步骤：获取失败-正在加载旧公告(3/3)……请稍后\n')
                self.sinOut_gonggao_text.emit("MOS", "<html><head/><body><p>官方公告 <span style=\" color:rgb(255, 38, 0);\">•获取失败！✗ 未知错误 以为您自动显示上次获取到的内容</span></p></body></html>")
                self.sinOut_gonggao_error.emit(gonggao)
            else:
                self.sinOut_gonggao_text.emit("MOS", "<html><head/><body><p>官方公告 <span style=\" color:rgb(255, 38, 0);\">•获取失败！✗ 未知错误 无缓存可加载</span></p></body></html>")

class MOS_versions(QThread):
    '''获取更新'''
    sinOut_versions = pyqtSignal(str)
    sinOut_versions_yes_no = pyqtSignal(str)
    sinOut_versions_yes = pyqtSignal(str,str,str)
    
    def __init__(self, a):
        super(MOS_versions, self).__init__()
        self.a = a

    def run(self):
        import requests
        self.sinOut_versions.emit("正在准备检查更新(1/2)")
        if self.a == 'darwin':
            self.sinOut_versions.emit("正在准备检查更新(2/2)")
            url = 'http://api.2018k.cn/checkVersion?id=6edb1fb4d4154cd7a104f6f0702fcbed&version=' + versions
            url_text = 'http://api.2018k.cn/getExample?id=6edb1fb4d4154cd7a104f6f0702fcbed&data=remark'
        else:
            self.sinOut_versions.emit("正在准备检查更新(2/2)")
            url = 'http://api.2018k.cn/checkVersion?id=b7c5251e83a644e7ad8b5bd8451ceb0a&version=' + versions
            url_text = 'http://api.2018k.cn/getExample?id=b7c5251e83a644e7ad8b5bd8451ceb0a&data=remark'
        self.sinOut_versions.emit("正在获取更新(1/5)")
        header = {'User-Agent':'Mozilla/55.0 (Macintosh; Intel Mac OS X 55.55; rv:101.0) Gecko/20100101 Firefox/101.0'}    # 伪装浏览器
        r_2 = requests.get(url, timeout=(5,50), headers = header)
        r_3 = r_2.text
        r_4 = r_3.split('|') #分割
        if r_4[0] == 'true':
            '''如果要更新'''
            self.sinOut_versions.emit("正在获取更新(2/5)")
            url_2 = 'https://purge.jsdelivr.net/gh/xianyongjian080402/Minecraft-Optimal-Starter_2/MOS_versions.json'
            url_3 = 'https://cdn.jsdelivr.net/gh/xianyongjian080402/Minecraft-Optimal-Starter_2/MOS_versions.json'
            self.sinOut_versions.emit("正在获取更新(3/5)")
            r_5 = requests.get(url_2, timeout=(5,50), headers = header)
            self.sinOut_versions.emit("正在获取更新(4/5)")
            r_6 = requests.get(url_3, timeout=(5,50), headers = header)
            self.sinOut_versions.emit("正在获取更新(5/5)")

            r_7 = requests.get(url_text, timeout=(5,50), headers = header)
            r_7.encoding = 'utf-8'
            r_7_1 = r_7.text

            self.sinOut_versions.emit("正在准备……")
            json_1 = r_6.json()
            r_7 = r_4[4]
            json_2 = json_1[r_7]
            MOS_print("info",str("新版本：" + json_2 + " ->编号：" + r_7))
            self.sinOut_versions_yes.emit(r_4[3],r_7_1,json_2)
        else:
            self.sinOut_versions_yes_no.emit('No')

class MOS_file(QThread):
    '''初始化文件/设置'''
    sinOut = pyqtSignal(str)
    sinOut_font = pyqtSignal(str) 
    def __init__(self):
        super(MOS_file, self).__init__()

    def run(self):
        import os,sys,platform
        MOS_print("info","文件初始化线程开始")
        try:
            #a = sys.platform()
            #print(a)
            #if a = 

            a = str(sys.platform)
            if a == "darwin":
                user_name = os.getlogin()
                # 获取当前系统用户目录
                user_home = os.path.expanduser('~')
                file = user_home + '/Documents'
            else:
                file = ''
                MOS_print("info",a)

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
                MOS_print("info","程序不是第一次运行")
            elif os.path.isfile(MOS_file_1)==False:
                MOS_first_run = "First"
                MOS_json=open(MOS_file_json,"w")
                MOS_json.close()
                MOS_print("info","程序是第一次运行")
            self.sinOut.emit("OK!")

            if MOS_first_run == 'First':
                #如果是第一次
                with open(MOS_file_json, 'w+', encoding='utf-8') as f:
                    MOS_file_1 =os.path.join(file,".minecraft")
                    a = {'font':'FangSong',
                        'font_default':'Yes',   
                        'game_file_name':['默认目录'],
                        '默认目录':MOS_file_1}
                    json.dump(a, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
                with open(MOS_file_json, 'r', encoding='utf-8') as f:
                    b = json.load(f)
                    MOS_print("info",'默认字体：' + b['font'])
                    Ui_MOS.click_pushButton_shezhi_fond_moren(self)
            else:
                #如果不是
                with open(MOS_file_json, 'r', encoding='utf-8') as f:
                    try:
                        b = json.load(f)
                        if str(b['font_default']) == 'Yes':
                            c = str('FangSong')
                            self.sinOut_font.emit(c)
                        else:
                            c = str(b['font'])
                            c_1 = '默认字体：' + c
                            MOS_print("info",c_1)
                            self.sinOut_font.emit(c)
                        MOS_game_dir_name = b['game_file_name']
                        MOS_print("info",'游戏版本列表(名称): '+str(MOS_game_dir_name))
                        for MOS_game_dir_name_1 in MOS_game_dir_name:
                            '''在json文件中，根据版本名称列表，读取在字典中对应的路径'''
                            MOS_game_dir = b[MOS_game_dir_name_1]
                            MOS_print("info",MOS_game_dir_name_1+' 游戏目录的路径: '+str(MOS_game_dir))
                    except KeyError:
                        MOS_print("error","json文件有问题")
                        self.sinOut.emit("KeyError")
                    

        except PermissionError:
            MOS_print("error", "初始化失败 没有权限，操作不被许可")
            self.sinOut.emit("ERROR_PermissionError")
        except:
            error = traceback.print_exc()
            MOS_print("error",error)

class game_first_initialize(QThread):
    '''遍历versions文件+缓存
        如果要遍历特定的文件夹，请把file_versinons附上路径
        是程序刚开始运行时初始化的 all="Yes" (会检测Json中所有路径下的游戏，并添加到“选择要启动的游戏”下拉框中 然后单独检测默认目录，将其添加到 “目录下的游戏”列表)
    '''
    sinOut_game_add = pyqtSignal(list,str)
    sinOut_game_dir_add = pyqtSignal(list)
    sinOut_game_add_DropDownBox = pyqtSignal(list)
    sinOut_game_error = pyqtSignal(str)

    def __init__(self, file_versinons= None, all= None):
        self.file_versinons = file_versinons
        self.all = all
        super(game_first_initialize, self).__init__()

    def run(self):
        try:

            a = str(sys.platform)
            if a == "darwin":
                user_name = os.getlogin()
                # 获取当前系统用户目录
                user_home = os.path.expanduser('~')

                file = user_home + '/Documents'
            else:
                file = ''
            

            # file_ 这个是为了在后面判断，这个指定的文件夹下，有没有游戏文件夹（在后面的代码中，如果报：找不到文件夹（就是游戏文件夹）这个变量的值会改变
            file_ = "Yes"

            if self.file_versinons == None:
                # 在程序刚刚开始运行的时候，在Json中获取所有的名称，并传给主窗口的game_dir_add函数，将名称和图标添加到游戏文件夹列表中
                MOS_json_read_geme_dir_Game = MOS_json_read(MOS_game_dir='Yes',MOS_game_dir_name_or_dir='name')
                self.sinOut_game_dir_add.emit(MOS_json_read_geme_dir_Game)

                # 在程序刚刚开始运行的时候默认检测 默认路径 下的游戏
                file_1 = os.path.join(file,".minecraft","versions")
            else:
                file_1 = os.path.join(self.file_versinons,"versions")
            MOS_print("info",'当前检测的游戏文件夹路径'+file_1)
        
            MOS_versions_zhengchang = []
            MOS_versions_not_found_jar = []
            MOS_versions_not_found_json = []

            MOS_versions_zhengchang_name = []
            MOS_versions_not_found_json_name = []
            MOS_versions_not_found_jar_name = []


            s_file  = os.listdir(file_1)
            for f in s_file:
                #f是每个版本的名字
                f_2_yuan=str(f)
                real_url = os.path.join (file_1,f_2_yuan)
                # real_url是versions下的文件的相对路径
                if os.path.isdir(real_url):
                    # real_url是versions下的文件的相对路径，如果是文件夹
                    f_2= os.path.join (file_1 , f)
                    f_3= os.path.join (f_2 , f)
                    # f_2是版本文件夹的相对路径
                    jar = (f_3+".jar")
                    json = (f_3+".json")
                    if os.path.exists(jar):
                        if os.path.exists(json):
                            MOS_versions_zhengchang.append(f_3)
                            MOS_versions_zhengchang_name.append(f_2_yuan)
                        else:
                            MOS_versions_not_found_json.append(f_3)
                            MOS_versions_not_found_json_name.append(f_2_yuan)
                    else:
                        MOS_versions_not_found_jar.append(f_3)
                        MOS_versions_not_found_jar_name.append(f_2_yuan)
        except FileNotFoundError:
            # 在上面说了file_是做什么的
            file_ = "NO"
        
        if self.file_versinons == None:
            b = "默认目录"
        else:
            file_2 = self.file_versinons
            b_1 = MOS_json_read(MOS_game_dir='Yes', MOS_game_dir_to_name=file_2)
            if b_1 != 'Json异常':
                '''列表正常'''
                b = b_1
            else:
                MOS_print("error", b_1)
        
        # 开始处理all
        if self.all != None:
            # 获取所有路径
            all_1 = MOS_json_read(MOS_game_dir='Yes',MOS_game_dir_name_or_dir='dir')
            # 准备列表
            all_name = []
            # 准备遍历
            for all_2 in all_1:
                all_file = os.path.join (all_2, "versions")
                # 开始遍历
                # all_file_2是versions文件夹的路径
                all_file_2 = os.listdir(all_file)
                for all_file_3 in all_file_2:
                    # 开始一个一个进行分析
                    # 注意：all_file_3 里面存的是名字 而不是 路径
                    all_file_4 = os.path.join(all_file, all_file_3)
                    if os.path.isdir(all_file_4):
                        # 如果是文件夹
                        jar = (all_file_3+ ".jar")
                        json = (all_file_3+ ".json")
                        jar_2 = os.path.join(all_file_4, jar)
                        json_2 = os.path.join(all_file_4, json)
                        if os.path.exists(jar_2):
                            # 如果有jar文件
                            if os.path.exists(json_2):
                                # 如果也有Json
                                all_name.append(all_file_3)
                            else:
                                # 如果没Json
                                all_name_2 = str(all_file_3) + "找不到Json文件"
                                all_name.append(all_name_2)
                        else:
                            # 如果连Jar都没有，直接判断，不是游戏文件夹
                            pass
            self.sinOut_game_add_DropDownBox.emit(all_name)



        MOS_print("info","——————————————————————————————————————————————————————")
        MOS_print("info",str("'" + b + "'中" + "正常的游戏："+ str(MOS_versions_zhengchang_name)))
        MOS_print("info",str("所对应的路径" + str(MOS_versions_zhengchang)))
        MOS_print("info","——————————————————————————————————————————————————————")
        MOS_print("info",str("'" + b + "'中" + "找不到.jar文件的游戏："+ str(MOS_versions_not_found_jar_name)))
        MOS_print("info",str("所对应的路径" + str(MOS_versions_not_found_jar)))
        MOS_print("info","——————————————————————————————————————————————————————")
        MOS_print("info",str("'" + b + "'中" + "找不到.json文件的游戏："+ str(MOS_versions_not_found_json_name)))
        MOS_print("info",str("所对应的路径" + str(MOS_versions_not_found_json)))
        MOS_print("info","——————————————————————————————————————————————————————")
        MOS_print("info","检测完毕")

        if file_ == 'Yes':
            '''判断 有没有游戏文件夹 file_的注释在上面'''
            if len(MOS_versions_zhengchang_name) ==0 and len(MOS_versions_not_found_jar_name) == 0 and len(MOS_versions_not_found_json_name) == 0 :
                '''单独判断是不是一个游戏都没有'''
                MOS_print("info", str("'" + b + "'中没有游戏"))
                self.sinOut_game_error.emit("该版本文件夹下无游戏")
            else:
                if len(MOS_versions_zhengchang_name) != 0:
                    if self.file_versinons == None:
                        #正常的
                        self.sinOut_game_add.emit(MOS_versions_zhengchang_name,'No')
                    else:
                        self.sinOut_game_add.emit(MOS_versions_zhengchang_name,'Yes')
                else:
                    MOS_print("info", str("'" + b + "'中没有正常的游戏"))

                if len(MOS_versions_not_found_jar_name) != 0:
                    if self.file_versinons == None:
                        #少jar的
                        self.sinOut_game_add.emit(MOS_versions_not_found_json_name,'No')
                    else:
                        self.sinOut_game_add.emit(MOS_versions_not_found_json_name,'Yes')
                else:
                    MOS_print("info", str("'" + b + "'中没有少Jar的游戏"))

                if len(MOS_versions_not_found_json_name) != 0:
                    if self.file_versinons == None:
                        #少json的
                        self.sinOut_game_add.emit(MOS_versions_not_found_json_name,'NO')
                    else:
                        self.sinOut_game_add.emit(MOS_versions_not_found_json_name,'Yes')
                else:
                    MOS_print("info", str("'" + b + "'中没有少Json的游戏"))
        else:
            self.sinOut_game_error.emit("该版本文件夹下无游戏目录")
            MOS_print("error",str("找不到" + file_1 + "没有游戏目录"))


def MOS_json_read(All = None, MOS_game_dir = None, MOS_game_dir_name_or_dir = None, MOS_game_name_dir = None, MOS_game_dir_to_name = None,file = None):
    '''All: 是否获取Json的全部数据？(直接输出全部的Json内容)
        MOS_game_dir: 是否获取版本路径相关的？
        MOS_game_dir_name_or_dir: 是获取所有的名字还是路径 (MOS_game_dir值要写Yes)
        MOS_game_name_dir: 用路径的昵称 获取对应的路径 (MOS_game_dir值要写Yes)
        MOS_game_dir_name: 用路径，获取对应的名字 (MOS_game_dir值要写Yes)
        file: 强制设定前目录
    '''
    try:
        a = str(sys.platform)
        if a == "darwin":
            user_name = os.getlogin()
            # 获取当前系统用户目录
            user_home = os.path.expanduser('~')
            file = user_home + '/Documents'
        else:
            file = ''
        MOS_file_json =os.path.join(file,".MOS","MOS.json")
        with open(MOS_file_json, 'r', encoding='utf-8') as f:
            b = json.load(f)
            if All == "Yes":
                return b
            else:
                pass
            if MOS_game_dir == 'Yes':
                if MOS_game_dir_name_or_dir == 'name':
                    MOS_game_dir_name_ = b['game_file_name']
                    return MOS_game_dir_name_
                elif MOS_game_dir_name_or_dir == 'dir':
                    MOS_game_dir_name_ = b['game_file_name']
                    MOS_game_dir_DirPrint = []
                    for MOS_game_dir_name_1 in MOS_game_dir_name_:
                        MOS_game_dir = b[MOS_game_dir_name_1]
                        MOS_game_dir_DirPrint.append(MOS_game_dir)
                    return MOS_game_dir_DirPrint
                if MOS_game_name_dir != None:
                    '''根据名字获取路径'''
                    MOS_game_name_dir_1 = b[MOS_game_name_dir]
                    return MOS_game_name_dir_1
                else:
                    pass
                if MOS_game_dir_to_name != None:
                    '''根据路径获取名字'''
                    # 列表推导式
                    # b为整个Json数据 MOS_game_name_dir为路径
                    # 返回的是个类表
                    k_2 = [k for k, v in b.items() if v == MOS_game_dir_to_name]
                    # 为了避免意外，对列表进行检查，检查是否只有一个值
                    if len(k_2) == 1:
                        '''检查通过'''
                        for k_3 in k_2:
                            return k_3
                    else:
                        '''检查不通过'''
                        e = str("Json异常")
                        MOS_print("error", str("Json异常" + str(k_2)))
                        return e
                    
                else:
                    pass
            else:
                return b
    except FileNotFoundError:
        MOS_print("error", "FileNotFoundError")
    except:
        error = traceback.print_exc()
        MOS_print("error",error)

def MOS_json_write(text):
    '''写入Json文件，注意: 类型必须是字典'''
    MOS_file_json =os.path.join(file,".MOS","MOS.json")
    try:
        with open(MOS_file_json, 'w+', encoding='utf-8') as f:
            json.dump(text, f, ensure_ascii=False, sort_keys=False, indent=4, separators=(',', ': '))
    except:
        error = traceback.print_exc()
        MOS_print("error",error)

class MOS_print_colour:
    '''HEADER:偏粉的紫色(?)
        OKBLUE:蓝色
        OKCYAN:青色
        OKGREEN:绿色
        WARNING:黄色
        FAIL:红色
        FAIL_2:加粗的红色
        FAIL_3:有下划线的红色
        ENDC:正常的黑色
        BOLD:加粗的黑色
        UNDERLINE:有下横线的黑色
    '''
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    FAIL_2 = '\033[1;91m'
    FAIL_3 = '\033[4;91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def MOS_print(type_,MOS_print_1):
    '''type_{[error,错误]  [info,提示]}'''
    MOS_print = str(MOS_print_1)
    MOS_time = datetime.datetime.now().strftime('%H:%M:%S.%f')
    if type_ == 'error':
        tybe_1 = 'ERROR'
        tybe_2 = MOS_print_colour.FAIL_3 + tybe_1 + MOS_print_colour.ENDC
        MOS_time_2 = MOS_print_colour.FAIL_3 + MOS_time + MOS_print_colour.ENDC
        left = MOS_print_colour.FAIL + '[' + MOS_print_colour.ENDC
        right = MOS_print_colour.FAIL + ']' +MOS_print_colour.ENDC
        print(left + MOS_time_2 + right + left + tybe_2 + right + MOS_print_colour.FAIL_2 + MOS_print + MOS_print_colour.ENDC)
    elif type_ == 'info':
        tybe_1 = 'INFO'
        left = MOS_print_colour.ENDC + '[' + MOS_print_colour.ENDC
        right = MOS_print_colour.ENDC + ']' +MOS_print_colour.ENDC
        tybe_2 = MOS_print_colour.UNDERLINE + tybe_1 + MOS_print_colour.ENDC
        MOS_time_2 = MOS_print_colour.UNDERLINE + MOS_time + MOS_print_colour.ENDC
        print(left + MOS_time_2 + right + left + tybe_2 + right + MOS_print_colour.ENDC + MOS_print + MOS_print_colour.ENDC)

def except_hook(cls, exception, traceback):
    '''报错显示'''
    sys.__excepthook__(cls, exception, traceback)

def file_h():
    if a == "darwin":
        user_name = os.getlogin()
        # 获取当前系统用户目录
        user_home = os.path.expanduser('~')
        file = user_home + '/Documents'
    else:
        file = ''
    return file

def system_h():
    a = str(sys.platform)
    return a

try:
    if __name__ == '__main__':
        versions = '2.0.5'
        # import shutil
        # shutil.rmtree(".MOS")
        # shutil.rmtree(".minecraft")
        a = str(sys.platform)
        if a == "darwin":
            MOS_print("info",'当前系统为Mac')
            user_name = os.getlogin()
            # 获取当前系统用户目录
            user_home = os.path.expanduser('~')
            file = user_home + '/Documents'
        else:
            file = ''
 
        MOS_print("info","程序已开始运行！")
        app = QtWidgets.QApplication(sys.argv)
        sys.excepthook = except_hook
        MOS_print("info","请稍等...")
        MainWindow = QtWidgets.QMainWindow()
        MOS_print("info","创建窗口对象成功！")
        ui = Ui_MOS()
        MOS_print("info","创建PyQt窗口对象成功！")
        ui.setupUi(MainWindow)
        MOS_print("info","初始化设置成功！")
        MainWindow.show()
        MOS_print("info","已成功显示窗体")
        sys.exit(app.exec())
except KeyboardInterrupt:
    MOS_print("info","程序以强行退出")
except Exception as error:
    MOS_print("error",error)