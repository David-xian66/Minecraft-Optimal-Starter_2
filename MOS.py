
import sys,os, requests, json, datetime
from os import path

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r'.\site-packages\PyQt5\Qt5\plugins'  #### 这一行是新增的。用的是相对路径。

from PyQt6.QtCore import *

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MOS(object):
    def setupUi(self, MOS):
        MOS_catalogue_picture_ico_png = os.path.join("picture","ico.png")
        MOS_catalogue_picture_home_png = os.path.join("picture","home.png")
        MOS_catalogue_picture_online_png = os.path.join("picture","online.png")
        MOS_catalogue_picture_download_png = os.path.join("picture","download.png")
        MOS_catalogue_picture_music_png = os.path.join("picture","music.png")
        MOS_catalogue_picture_settings_png = os.path.join("picture","settings.png")
        MOS_catalogue_picture_about_png = os.path.join("picture","about.png")
        MOS.setObjectName("MOS")
        MOS.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        MOS.resize(1000, 533)
        MOS.setMinimumSize(QtCore.QSize(1000, 533))
        MOS.setStyleSheet("QMainwindow{\n"
"    border-radius:15px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MOS)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("QWidget\n"
"{\n"
"    background-color: rgb(231, 230, 228);\n"
"    border-bottom-left-radius:15px;\n"
"    border-top-left-radius:15px;\n"
"}\n"
"QPushButton\n"
"{\n"
"    color: blue;\n"
"    height:23px;\n"
"    color: rgb(0, 150, 255);\n"
"    background-position: left;\n"
"    text-align: left;\n"
"    padding-right:10px;\n"
"    font-size: 15px;\n"
"    border-style:none;\n"
"    border-radius:2.5px;\n"
"    border:2px double rgb(229, 228, 226);\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"    background-color: rgb(192, 192, 192);\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"    border:2px double rgb(0, 150, 255);\n"
"}")
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_music = QtWidgets.QPushButton(self.widget)
        self.pushButton_music.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(MOS_catalogue_picture_music_png), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_music.setIcon(icon)
        self.pushButton_music.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_music.setObjectName("pushButton_music")
        self.gridLayout_3.addWidget(self.pushButton_music, 6, 0, 1, 2)
        self.pushButton_lianji = QtWidgets.QPushButton(self.widget)
        self.pushButton_lianji.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(MOS_catalogue_picture_online_png), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_lianji.setIcon(icon1)
        self.pushButton_lianji.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_lianji.setObjectName("pushButton_lianji")
        self.gridLayout_3.addWidget(self.pushButton_lianji, 2, 0, 1, 2)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setStyleSheet("QPushButton::hover\n"
"{\n"
"    background-color: rgb(231, 230, 228);\n"
"    background-color: rgba(0, 150, 255, 51);\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setStyleSheet("width:41px;\n"
"height:50px;\n"
"border-radius: 25px;")
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(MOS_catalogue_picture_ico_png), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_4.addWidget(self.pushButton_2, 0, 0, 2, 1)
        self.gridLayout_3.addWidget(self.widget_2, 0, 0, 1, 2)
        self.pushButton_xiazai = QtWidgets.QPushButton(self.widget)
        self.pushButton_xiazai.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(MOS_catalogue_picture_download_png), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_xiazai.setIcon(icon3)
        self.pushButton_xiazai.setIconSize(QtCore.QSize(19, 19))
        self.pushButton_xiazai.setObjectName("pushButton_xiazai")
        self.gridLayout_3.addWidget(self.pushButton_xiazai, 4, 0, 1, 2)
        self.pushButton_about = QtWidgets.QPushButton(self.widget)
        self.pushButton_about.setStyleSheet("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(MOS_catalogue_picture_about_png), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_about.setIcon(icon4)
        self.pushButton_about.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_about.setObjectName("pushButton_about")
        self.gridLayout_3.addWidget(self.pushButton_about, 9, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 10, 0, 1, 1)
        self.pushButton_home = QtWidgets.QPushButton(self.widget)
        self.pushButton_home.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.pushButton_home.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButton_home.setStyleSheet("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(MOS_catalogue_picture_home_png), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_home.setIcon(icon5)
        self.pushButton_home.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_home.setObjectName("pushButton_home")
        self.gridLayout_3.addWidget(self.pushButton_home, 1, 0, 1, 2)
        self.pushButton_shezhi = QtWidgets.QPushButton(self.widget)
        self.pushButton_shezhi.setStyleSheet("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(MOS_catalogue_picture_settings_png), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_shezhi.setIcon(icon6)
        self.pushButton_shezhi.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_shezhi.setObjectName("pushButton_shezhi")
        self.gridLayout_3.addWidget(self.pushButton_shezhi, 8, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setStyleSheet("color: rgb(0, 150, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 11, 0, 1, 2)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(790, 0))
        self.scrollArea.setStyleSheet("border-style:none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 796, 509))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_3.setStyleSheet("border:2px double rgb(0, 150, 255);border-radius:15px;")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget_3)
        self.textBrowser.setStyleSheet("border-style:none;")
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_5.addWidget(self.textBrowser, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        self.label_4.setStyleSheet("border-style:none;")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_4.setStyleSheet("border:2px double rgb(0, 150, 255);border-radius:15px;")
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.widget_6 = QtWidgets.QWidget(self.widget_4)
        self.widget_6.setStyleSheet("border-style:none;")
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget_6)
        self.label_3.setStyleSheet("border-style:none;")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 1, 2, 3)
        self.label_7 = QtWidgets.QLabel(self.widget_6)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 1, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 0, 4, 2, 1)
        self.progressBar = QtWidgets.QProgressBar(self.widget_6)
        self.progressBar.setStyleSheet("border-style:none;")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 2, 0, 1, 5)
        self.gridLayout_6.addWidget(self.widget_6, 1, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.widget_4)
        self.label_5.setStyleSheet("border-style:none;")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_6.addItem(spacerItem3, 3, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.widget_4)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_6.addWidget(self.comboBox, 2, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_6.addWidget(self.pushButton_3, 2, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_6.addItem(spacerItem4, 3, 1, 1, 1)
        self.horizontalLayout.addWidget(self.widget_4)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)
        MOS.setCentralWidget(self.centralwidget)

        self.retranslateUi(MOS)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MOS)

    def retranslateUi(self, MOS):
        _translate = QtCore.QCoreApplication.translate
        MOS.setWindowTitle(_translate("MOS", "MainWindow"))
        self.pushButton_music.setText(_translate("MOS", "音乐"))
        self.pushButton_lianji.setText(_translate("MOS", "联机"))
        self.label.setText(_translate("MOS", "无用户"))
        self.label_2.setText(_translate("MOS", "点击添加"))
        self.pushButton_xiazai.setText(_translate("MOS", "下载"))
        self.pushButton_about.setText(_translate("MOS", "关于"))
        self.pushButton_home.setText(_translate("MOS", "Home"))
        self.pushButton_shezhi.setText(_translate("MOS", "设置"))
        self.label_6.setText(_translate("MOS", "MOS II"))
        self.label_4.setText(_translate("MOS", "公告"))
        self.label_3.setText(_translate("MOS", "启动的图片"))
        self.label_7.setText(_translate("MOS", "TextLabel"))
        self.label_5.setText(_translate("MOS", "选择要启动的游戏"))
        self.pushButton_3.setText(_translate("MOS", "PushButton"))






if __name__ == '__main__':
    print ("程序已开始运行！")
    app = QtWidgets.QApplication(sys.argv)
    print ("请稍等...")
    MainWindow = QtWidgets.QMainWindow()
    print ("创建窗口对象成功！")
    ui = Ui_MOS()
    print ("创建PyQt窗口对象成功！")
    ui.setupUi(MainWindow)
    print ("初始化设置成功！")
    MainWindow.show()
    print ("已成功显示窗体")
    sys.exit(app.exec())
