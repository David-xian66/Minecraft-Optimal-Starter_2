import json
import os
import sys
from tkinter.messagebox import NO
import traceback
import webbrowser


os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r'.\site-packages\PyQt6\Qt6\plugins'  #### 这一行是新增的。用的是相对路径。

from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from Java_Dowmloader_ import Java_Dowmloader__
from MOS_print_ import MOS_print
from MOS_UI import Ui_MOS
import MOS_rc
# https://www.wenjuan.com/s/UZBZJvEm2uK/#《MOS ll 错误反馈》，快来参与吧。【问卷网提供支持】om PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MOS_Main(QtWidgets.QMainWindow,Ui_MOS,Java_Dowmloader__):
    def __init__(self):
        super(Ui_MOS_Main, self).__init__()
        self.setupUi(self)
        self.show()
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
        MOS_catalogue_picture_user_png = os.path.join("picture", "picture_user.png")


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
        self.pushButton_22.clicked.connect(self.chick_pushButton_Java_check)
        self.pushButton_23.clicked.connect(self.chick_pushButton_Java_shezhi_xiazai)
        self.comboBox_2.currentIndexChanged.connect(self.click_comboBox_xiazai)
        self.pushButton_27.clicked.connect(self.click_pushButton_Gitee)
        self.pushButton_29.clicked.connect(self.click_pushButton_GitHub)
        self.listWidget_3.itemClicked.connect(self.click_listWidget_Java_xiazai)
        self.pushButton_24.clicked.connect(self.click_pushButton_Java_Dowmloader)
        self.radioButton.toggled.connect(self.click_radioButton_checking_updates)
        self.pushButton_28.clicked.connect(self.click_pushButton_about_j_gitee)
        self.pushButton_30.clicked.connect(self.click_pushButton_about_j_github)
        self.pushButton_31.clicked.connect(self.click_pushButton_about_b_github)
        self.pushButton_32.clicked.connect(self.click_pushButton_about_b_gitee)
        self.pushButton_25.clicked.connect(self.click_pushButton_about_b_wenjuan)


        self.comboBox_gonggao_right.clear()
        self.listWidget.clear()
        self.pushButton_18.setEnabled(False)

        self.progressBar_2.setMinimum(0)
        self.progressBar_2.setMaximum(99)
        self.progressBar_2.setValue(0)
        self.stackedWidget_mos_right.setCurrentIndex(0)
        # 启动线程
        self.a = MOS_file()
        self.a.sinOut_updates_no.connect(self.MOS_file_return_updates_no)
        self.a.sinOut_updates.connect(self.MOS_file_return_updates)
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
    
    def click_pushButton_about_j_gitee(self):
        """点击“提出建议”中的Gitee按钮"""
        webbrowser.open("https://gitee.com/xian66/minecraft-optimal-starter_2/issues")
    
    def click_pushButton_about_j_github(self):
        """点击“提出建议”中的GitHub按钮"""
        webbrowser.open("https://github.com/xianyongjian080402/Minecraft-Optimal-Starter_2/issues/new/choose")
    
    def click_pushButton_about_b_github(self):
        """点击“反馈Bug”中的GitHub按钮"""
        webbrowser.open("https://github.com/xianyongjian080402/Minecraft-Optimal-Starter_2/issues/new/choose")
    
    def click_pushButton_about_b_gitee(self):
        """点击“反馈Bug”中的Gitee按钮"""
        webbrowser.open("https://gitee.com/xian66/minecraft-optimal-starter_2/issues")
    
    def click_pushButton_about_b_wenjuan(self):
        """点击“反馈Bug”中的问卷按钮"""
        webbrowser.open("https://www.wenjuan.com/s/UZBZJvEm2uK/#")

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
        dir.setDirectory(file_h())
        #dir.setNameFilter('999(*.png)') 名称过滤器
        if dir.exec():
            MOS_banbenwenjianjia_file = dir.selectedFiles()
            MOS_print("info",str("选择文件夹" + str(MOS_banbenwenjianjia_file)))
            for MOS_banbenwenjianjia_file_1 in MOS_banbenwenjianjia_file:
                self.label_46.setText(str(MOS_banbenwenjianjia_file_1))
            if self.lineEdit_4.text() == '':
                self.pushButton_18.setEnabled(False)
                QApplication.processEvents()
            else:
                self.pushButton_18.setEnabled(True)
                QApplication.processEvents()


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

    def click_comboBox_xiazai(self):
        a = self.comboBox_2.currentIndex()
        if a == 0:
            self.stackedWidget_2.setCurrentIndex(a)
        elif a == 1:
            self.stackedWidget_2.setCurrentIndex(2)
        elif a == 2:
            self.stackedWidget_2.setCurrentIndex(4)
        elif a == 3:
            self.stackedWidget_2.setCurrentIndex(6)
        elif a == 4:
            self.stackedWidget_2.setCurrentIndex(8)
        elif a == 5:
            self.stackedWidget_2.setCurrentIndex(9)

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
            if self.pushButton_19.text() == '下载完成 - 点击打开下载目录 请进行手动安装(启动器会自动退出)':
                n_1 = file_h()
                n = os.path.join(n_1,'.MOS','Download')
                if system_h() == 'darwin':
                    #如果是Mac
                    os.system(str('open ' + n))
                elif system_h() == 'win32' or system_h() == 'cygwin':
                    #如果是win
                    os.system(str('start' + n))
                quit()
            else:
                self.pushButton_19.setEnabled(False)
                self.v = MOS_versions()
                self.v.sinOut_versions.connect(self.click_pushButton_jianchagengxin_sinOut)
                self.v.sinOut_versions_error.connect(self.click_pushButton_jianchagengxin_sinOut_error)
                self.v.sinOut_versions_yes_no.connect(self.click_pushButton_jianchagengxin_sinOut_versions_yes_no)
                self.v.sinOut_versions_yes.connect(self.click_pushButton_jianchagengxin_sinOut_versions_yes)
                self.v.start()

        else:
            self.pushButton_19.setEnabled(True)
        
    
    def click_pushButton_jianchagengxin_sinOut(self,text):
        self.pushButton_19.setText(text)

    def click_pushButton_jianchagengxin_sinOut_error(self,text,t):
        """当获取更新发生错误时… text是错误类型 t是在哪里错了
            t
        """
        if t != '':
            self.pushButton_19.setText(str("检测失败 - "+ "在" + t +"时 出现"+text))
        else:
            # 如果报错未知
            self.pushButton_19.setText(str("检测失败 - "+ "在" + t +"时 出现未知的异常 建议关于中进行反馈"))

    def click_pushButton_jianchagengxin_sinOut_versions_yes_no(self,text):
        if text == "No":
            self.pushButton_19.setText("检测完毕 没有更新 点击重新获取")
            self.pushButton_19.setEnabled(True)

    def click_pushButton_jianchagengxin_sinOut_versions_yes(self,url,text,v):
        self.pushButton_19.setText("检查到更新，在弹出的窗口中下载&查看更新内容")
        self.pushButton_19.setEnabled(True)
        a = QMessageBox.information(None,"更新",str("<html><head/><body><h1> 版本" + v + "的更新内容： </h1><p>" + text + "</p></body></html>"),QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel,QMessageBox.StandardButton.Ok)

        if a == QMessageBox.StandardButton.Ok: #点了OK按钮
            # 下面衔接下载模块 记得指定路径（按照系统
            if system_h() == 'darwin':
                d_name = 'MOS.dmg'
            else:
                d_name = 'MOS.zip'
            MOS_print('info',str('更新下载地址：' + url))
            d_file = os.path.join(file_h(),'.MOS','Download',d_name)
            #from MOS_Dowmloader import Dowmloader_
            #down = Dowmloader_(url,8,d_file)
            self.pushButton_19.setEnabled(False)
            self.pushButton_19.setText("正在下载中")

            self.v_d = MOS_versions_dowmloader(url,8,d_file)
            self.v_d.sinOut_versions_d.connect(self.click_pushButton_jianchagengxin_sinOut_versions_dowmloader_ok)
            self.v_d.start()
    
    def click_pushButton_java_sinOut_java_dowmloader_start(self,text):
        """开始下载后……"""
        
        
        self.pushButton_24.setText("已开始下载 点击查看")
        self.pushButton_24.setEnabled(True)
        

    def click_pushButton_java_sinOut_java_dowmloader(self,file_name):
        """下载完成后…… file_name:文件名 int:第几行的"""
        f_name = file_name.replace(".gz", "")
        #获取文件的名称，去掉
        import gzip
        g_file = gzip.GzipFile(file_name)
        #创建gzip对象
        open(f_name, "w+").write(str(g_file.read()))
        #gzip对象用read()打开后，写入open()建立的文件里。
        g_file.close()
        #关闭gzip对象
        import tarfile
        tar = tarfile.open(file_name)
        names = tar.getnames()
        if os.path.isdir(file_name + "_files"):
            pass
        else:
            os.mkdir(file_name + "_files")
        #因为解压后是很多文件，预先建立同名目录
        for name in names:
            tar.extract(name, file_name + "_files/")
        tar.close()



    def click_pushButton_jianchagengxin_sinOut_versions_dowmloader_ok(self):
        self.pushButton_19.setText("下载完成 - 点击打开下载目录 请进行手动安装(启动器会自动退出)")
        self.pushButton_19.setEnabled(True)


    def chick_pushButton_Java_check(self):
        a = Java_check()
        MOS_print("info",a)
        self.comboBox_7.clear()
        self.comboBox_7.addItem("让MOS自动为您选择")
        for a_1, a_2 in a.items():
            a_3 = a_2 + "  ––>  " + a_1
            self.comboBox_7.addItem(a_3)
        java_json = MOS_json_read(All='Yes')
        if 'Java' in java_json:
            java_json['Java'] = a
        else:
            java_json['Java'] = a
        MOS_json_write(java_json)

    def chick_pushButton_Java_shezhi_xiazai(self):
        self.stackedWidget_2.setCurrentIndex(8)
        self.stackedWidget_mos_right.setCurrentIndex(3)
        self.comboBox_2.setCurrentIndex(4)
        self.click_pushButton_xiazai()
        
    def click_listWidget_Java_xiazai(self,item):
        """点击下载Java列表中的项时……"""
        if item.isSelected():
            a = item.text()
            MOS_print("info",str("点击: " + a))
            self.pushButton_24.setText(str("下载 - " + a))
            self.pushButton_24.setEnabled(True)
    
    def click_pushButton_Java_Dowmloader(self):
        a = self.pushButton_24.text()
        if a == '下载 - 免安装版 Java 8':
            self.pushButton_24.setEnabled(False)
            self.pushButton_24.setText("正在准备下载")
            if system_h() == 'darwin':
                url = 'https://moslauncher.tk/download/java/version_grean/Java%208/Java-8-x64%20Mac%20jre-8u333-macosx-x64.tar.gz'
                d_file_name = 'n_java8.tar.gz'
                d_file = os.path.join(file_h(),'.MOS','Download',d_file_name)

            elif system_h() == 'cygwin' or system_h() == 'win32':
                url = 'https://moslauncher.tk/download/java/version_grean/Java%208/Java-8%20Win%20openjdk-8u42-b03-windows-i586-14_jul_2022.zip'
                d_file_name = 'n_java16.zip'
                d_file = os.path.join(file_h(),'.MOS','Download',d_file_name)
            java_v = 'Java 8'
            self.java_d(java_v,url,d_file)

        elif a == '下载 - 免安装版 Java 16':
            self.pushButton_24.setEnabled(False)
            self.pushButton_24.setText("正在准备下载")
            if system_h() == 'darwin':
                url = 'https://moslauncher.tk/download/java/version_grean/Java%2016/Java-16-x64%20Mac%20jdk-16.0.2_osx-x64_bin.tar.gz'
                d_file_name = 'n_java16.tar.gz'
                d_file = os.path.join(file_h(),'.MOS','Download',d_file_name)

            elif system_h() == 'cygwin' or system_h() == 'win32':
                url = 'https://moslauncher.tk/download/java/version_grean/Java%2016/Java-16-x64%20Win%20jdk-16.0.2_windows-x64_bin.zip'
                d_file_name = 'n_java16.zip'
                d_file = os.path.join(file_h(),'.MOS','Download',d_file_name)
            java_v = 'Java 16'
            self.java_d(java_v,url,d_file)

        elif a == '下载 - 免安装版 Java 17':
            self.pushButton_24.setEnabled(False)
            self.pushButton_24.setText("正在准备下载")
            if system_h() == 'darwin':
                url = 'https://moslauncher.tk/download/java/version_grean/Java%208/Java-8-x64%20Mac%20jre-8u333-macosx-x64.tar.gz'
                d_file_name = 'n_java17.tar.gz'
                d_file = os.path.join(file_h(),'.MOS','Download',d_file_name)

            elif system_h() == 'cygwin' or system_h() == 'win32':
                url = 'https://moslauncher.tk/download/java/version_grean/Java%208/Java-8%20Win%20openjdk-8u42-b03-windows-i586-14_jul_2022.zip'
                d_file_name = 'n_java17.zip'
                d_file = os.path.join(file_h(),'.MOS','Download',d_file_name)
            java_v = 'Java 17'
            self.java_d(java_v,url,d_file)
        
        elif a == '已开始下载 点击查看':
            self.comboBox_2.setCurrentIndex(5)
            self.stackedWidget_2.setCurrentIndex(9)
        else:
            webbrowser.open("https://www.123pan.com/s/xCVDVv-gXuY3")

    def click_radioButton_checking_updates(self):
        if self.radioButton.isChecked():
            # 如果选择了
            t = MOS_json_read(All='Yes')
            t['Automatically_checking_for_updates'] = "True"
            MOS_json_write(t)
            MOS_print("info","自动检查更新已开启")
        else:
            #如果没有
            t = MOS_json_read(All='Yes')
            t['Automatically_checking_for_updates'] = "False"
            MOS_json_write(t)
            MOS_print("info","自动检查更新已关闭")


    def click_pushButton_GitHub(self):
        webbrowser.open("https://github.com/xianyongjian080402/Minecraft-Optimal-Starter_2")

    def click_pushButton_Gitee(self):
        webbrowser.open("https://gitee.com/xian66/minecraft-optimal-starter_2")
    
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

    
    def setfont_size(self):
        '''修改默认字体大小(已弃用)'''

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
        try:
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
        except:
            pass
            
    def json_error(self):
        a = QMessageBox.critical(None,"错误","您是否删除了MOS启动器生成的JSON文件？请在删除后重启启动器 即将退出启动器",QMessageBox.StandardButton.Yes,QMessageBox.StandardButton.Yes)
        if a == QMessageBox.StandardButton.Yes: #检查是否点了OK按钮
            quit()

    def MOS_file_return_updates_no(self):
        """如果自动检查更新关闭…"""
        self.radioButton.setChecked(False)

    def MOS_file_return_updates(self):
        self.updates_time=QTimer() #创建计时器对象
        self.updates_time.start(2000) #开始计时器
        self.updates_time.timeout.connect(self.updates_time_) #要执行的槽
    
    def updates_time_(self):
        self.updates_time.stop()
        # 启动线程
        self.pushButton_19.setEnabled(False)
        self.v = MOS_versions()
        self.v.sinOut_versions.connect(self.click_pushButton_jianchagengxin_sinOut)
        self.v.sinOut_versions_error.connect(self.click_pushButton_jianchagengxin_sinOut_error)
        self.v.sinOut_versions_yes_no.connect(self.click_pushButton_jianchagengxin_sinOut_versions_yes_no)
        self.v.sinOut_versions_yes.connect(self.click_pushButton_jianchagengxin_sinOut_versions_yes)
        self.v.start()


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

    def java_d(self,v,url,file):
        MOS_print("info",str('Java下载模块 下载版本：' + v + ' 链接：' + url + ' 存储路径：' + file))

        self.a = Java_Dowmloader__(v,url,file)
        
        self.xy_size = self.geometry()  #获取主界面 初始坐标
        self.a.move(self.xy_size.x()+284,self.xy_size.y()+177) #子界面移动到 居中

        self.a.setWindowFlags(QtCore.Qt.WindowType.WindowCloseButtonHint | QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint | QtCore.Qt.WindowType.WindowStaysOnTopHint | QtCore.Qt.WindowType.FramelessWindowHint| QtCore.Qt.WindowType.Tool)
        self.a.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal) 
        self.a.show()
        self.a_w = QTimer() #创建计时器对象
        self.a_w.start(0) #开始计时器
        self.a_w.timeout.connect(self.a_w_) #要执行的槽
    
    def a_w_(self):
        """检测主窗口位置 并移动下载Java的窗口 到主窗口中央"""
        self.xy_size = self.geometry()  #获取主界面 初始坐标
        self.a.move(self.xy_size.x()+284,self.xy_size.y()+177) #子界面移动到 居中
    

    # =================================分割线===================================#



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
        import sys
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
    sinOut_versions_error = pyqtSignal(str,str)
    sinOut_versions_yes_no = pyqtSignal(str)
    sinOut_versions_yes = pyqtSignal(str,str,str)
    
    def __init__(self):
        super(MOS_versions, self).__init__()
        self.a = str(system_h())

    def run(self):
        import requests
        self.sinOut_versions.emit("正在准备检查更新(1/2)")
        if self.a == 'darwin':
            self.sinOut_versions.emit("正在准备检查更新(2/2)")
            url = 'http://api.2018k.cn/checkVersion?id=6edb1fb4d4154cd7a104f6f0702fcbed&version=' + versions()
            url_text = 'http://api.2018k.cn/getExample?id=6edb1fb4d4154cd7a104f6f0702fcbed&data=remark'
        else:
            self.sinOut_versions.emit("正在准备检查更新(2/2)")
            url = 'http://api.2018k.cn/checkVersion?id=b7c5251e83a644e7ad8b5bd8451ceb0a&version=' + versions()
            url_text = 'http://api.2018k.cn/getExample?id=b7c5251e83a644e7ad8b5bd8451ceb0a&data=remark'
        self.sinOut_versions.emit("正在获取更新(1/5)")
        header = {'User-Agent':'Mozilla/55.0 (Macintosh; Intel Mac OS X 55.55; rv:101.0) Gecko/20100101 Firefox/101.0'}    # 伪装浏览器
        try:
            t = '检查是否有更新'
            r_2 = requests.get(url, timeout=(5,50), headers = header)
            r_3 = r_2.text
            r_4 = r_3.split('|') #分割
            if r_4[0] == 'true':
                '''如果要更新'''
                self.sinOut_versions.emit("正在获取更新(2/5)")
                url_2 = 'https://purge.jsdelivr.net/gh/xianyongjian080402/Minecraft-Optimal-Starter_2/MOS_versions.json'
                url_3 = 'https://cdn.jsdelivr.net/gh/xianyongjian080402/Minecraft-Optimal-Starter_2/MOS_versions.json'
                self.sinOut_versions.emit("正在获取更新(3/5)")
                t = '更新远程公告支持文件'
                r_5 = requests.get(url_2, timeout=(5,50), headers = header) # 更新公告文件
                self.sinOut_versions.emit("正在获取更新(4/5)")
                t = '获取远程公告支持文件'
                r_6 = requests.get(url_3, timeout=(5,50), headers = header) # 获取公告更新文件（其实这个文件存储的是版本编号所对应版本
                self.sinOut_versions.emit("正在获取更新(5/5)")
                t = '更新更新内容'
                r_7 = requests.get(url_text, timeout=(5,50), headers = header) # 获取更新内容   
                r_7.encoding = 'utf-8'
                r_7_1 = r_7.text

                self.sinOut_versions.emit("正在准备……")
                json_1 = r_6.json()
                r_7 = r_4[4]
                json_2 = json_1[r_7]
                MOS_print("info",str("新版本：" + json_2 + " ->编号：" + r_7) + '更新内容：\n' + r_7_1)
                self.sinOut_versions_yes.emit(r_4[3],r_7_1,json_2)
            else:
                self.sinOut_versions_yes_no.emit('No')

        except requests.exceptions.ReadTimeout:
            self.sinOut_versions_error.emit('读取超时',t)
        except requests.exceptions.ConnectionError:
            self.sinOut_versions_error.emit('连接错误',t)
        except:
            error = traceback.print_exc()
            MOS_print("error",error)
            #因为“TypeError: native Qt signal is not callable”所以 不传error内容
            self.sinOut_versions_error.emit('',t)

class MOS_versions_dowmloader(QThread):
    sinOut_versions_d = pyqtSignal()
    def __init__(self,url,thread_num,file):
        self.url = url
        self.thread_num = thread_num
        self.file = file
        super(MOS_versions_dowmloader, self).__init__()
    def run(self):
        from MOS_Dowmloader import Dowmloader
        a = Dowmloader(self.url, self.thread_num, self.file)
        a.run()
        self.sinOut_versions_d.emit()


class MOS_file(QThread):
    '''初始化文件/设置'''
    sinOut = pyqtSignal(str)
    sinOut_font = pyqtSignal(str)
    sinOut_updates_no = pyqtSignal()
    sinOut_updates = pyqtSignal()
    def __init__(self):
        super(MOS_file, self).__init__()

    def run(self):
        import os
        MOS_print("info","文件初始化线程开始")
        try:
            #a = sys.platform()
            #print(a)
            #if a = 

            file = file_h()

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

            MOS_file_1 =os.path.join(file,".MOS","Download")
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
                        'Automatically_checking_for_updates':'True',
                        'game_file_name':['默认目录'],
                        '默认目录':MOS_file_1}
                    json.dump(a, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
                with open(MOS_file_json, 'r', encoding='utf-8') as f:
                    b = json.load(f)
                    MOS_print("info",'默认字体：' + b['font'])
                    try:
                        Ui_MOS.click_pushButton_shezhi_fond_moren(self)
                    except AttributeError:
                        pass
            else:
                #如果不是
                with open(MOS_file_json, 'r', encoding='utf-8') as f:
                    try:
                        b = json.load(f)
                        MOS_print("info",str("自动检查更新" + b['Automatically_checking_for_updates']))
                        
                        if b['Automatically_checking_for_updates'] == 'False':
                            self.sinOut_updates_no.emit()

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

            # 不管他是不是 都判断是否自动检查更新
            if b['Automatically_checking_for_updates'] == 'True':
                MOS_print("info","自动检查更新为开启状态")
                self.sinOut_updates.emit()
            else:
                MOS_print("info","自动检查更新已关闭")
                    

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



def Java_check():
    import subprocess
    Java_1 = os.environ.get('JAVA_HOM')
    Java_2 = os.environ.get('JDK_HOME')
    file_java_2 = [Java_1,Java_2]
    if system_h() == 'darwin':
        Java_file = "/usr/bin/java"
        if os.path.exists(Java_file):
            file_java_2.append(Java_file)
        java_mac = subprocess.getoutput('/usr/libexec/java_home -V')
        java_mac_1 = java_mac.split('\n') # ['Matching Java Virtual Machines (2):', '    1.8.321.07 (x86_64) "Oracle Corporation" - "Java" /Library/Internet Plug-Ins/JavaAppletPlugin.plugin/Contents/Home', '    1.8.0_321 (x86_64) "Oracle Corporation" - "Java SE 8" /Library/Java/JavaVirtualMachines/jdk1.8.0_321.jdk/Contents/Home', '/Library/Internet Plug-Ins/JavaAppletPlugin.plugin/Contents/Home']
        java_mac_2 = java_mac_1[1:-1] #['    1.8.321.07 (x86_64) "Oracle Corporation" - "Java" /Library/Internet Plug-Ins/JavaAppletPlugin.plugin/Contents/Home', '    1.8.0_321 (x86_64) "Oracle Corporation" - "Java SE 8" /Library/Java/JavaVirtualMachines/jdk1.8.0_321.jdk/Contents/Home']
        for java_mac_2_1 in java_mac_2:
            java_mac_2_2 = java_mac_2_1.split('"') # ['    1.8.321.07 (x86_64) ', 'Oracle Corporation', ' - ', 'Java', ' /Library/Internet Plug-Ins/JavaAppletPlugin.plugin/Contents/Home']
            java_mac_2_3 = java_mac_2_2[-1] + '/bin/java'
            java_mac_2_4 = java_mac_2_3[1:] #删除前面的空格
            file_java_2.append(java_mac_2_4)
    file_java = {}
    for file_java_1 in file_java_2:
        if file_java_1 == None:
            pass
        else:
            file_java_1_2 = '"' + file_java_1 + '"' +' -version'
            #print(file_java_1_2)
            # https://blog.csdn.net/henghenghalala/article/details/98868979
            # https://www.runoob.com/w3cnote/python3-subprocess.html
            # https://blog.csdn.net/u013019701/article/details/121205743
            result = subprocess.getoutput(file_java_1_2)
            k_2 = str(result).split('\n') # ['java version "1.8.0_321"', 'Java(TM) SE Runtime Environment (build 1.8.0_321-b07)', 'Java HotSpot(TM) 64-Bit Server VM (build 25.321-b07, mixed mode)']
            k_1 = k_2[0].split('"') # ['java version ', '1.8.0_321', '']
            k = k_1[1]
            file_java[file_java_1] = k
            
    return file_java

def MOS_json_read(All = None, MOS_game_dir = None, MOS_game_dir_name_or_dir = None, MOS_game_name_dir = None, MOS_game_dir_to_name = None,file = None):
    '''All: 是否获取Json的全部数据？(直接输出全部的Json内容) 'Yes'
        MOS_game_dir: 是否获取版本路径相关的？'Yes'
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
        MOS_print("error", "Json文件出现：FileNotFoundError 错误！")
        Ui_MOS.json_error()
    except:
        error = traceback.print_exc()
        MOS_print("error",error)

def MOS_json_write(text):
    '''写入Json文件，注意: 类型必须是字典'''
    MOS_file_json =os.path.join(file_h(),".MOS","MOS.json")
    try:
        with open(MOS_file_json, 'w+', encoding='utf-8') as f:
            json.dump(text, f, ensure_ascii=False, sort_keys=False, indent=4, separators=(',', ': '))
    except FileNotFoundError:
        MOS_print("error", "Json文件出现：FileNotFoundError 错误！")
        Ui_MOS.json_error()
    except:
        error = traceback.print_exc()
        MOS_print("error",error)



def file_h():
    if system_h() == "darwin":
        user_name = os.getlogin()
        # 获取当前系统用户目录
        user_home = os.path.expanduser('~')
        file = user_home + '/Documents'
    else:
        file = ''
    return file

def system_h():
    """
        'win32':Windows
        'cygwin':Windows/Cygwin
        'darwin':macOS
        'aix':AIX
        'linux':Linux
    """
    a = str(sys.platform)
    return a

def versions():
    versions = '2.0.5'
    return versions



def except_hook(cls, exception, traceback):
    '''报错显示'''
    sys.__excepthook__(cls, exception, traceback)


# 子进程要执行的代码
def run_ui():
    from MOS_print_ import MOS_print
    MOS_print("info","加速进程开始导入库！")
    import sys
    from PyQt6.QtWidgets import QApplication,QMainWindow
    import MOS_start_loading
    MOS_print("info","加速进程的Ui程序已开始运行！")
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    MOS_print("info","加速进程正在运行……请稍等...")
    MainWindow = QMainWindow()
    MOS_print("info","加速进程 创建窗口对象成功！")
    ui = MOS_start_loading.Ui_MainWindow()
    MOS_print("info","加速进程 创建PyQt窗口对象成功！")
    ui.setupUi(MainWindow)
    MOS_print("info","加速进程 初始化设置成功！")
    MainWindow.show()
    MOS_print("info","加速进程 已成功显示窗体")
    sys.exit(app.exec())

def start():
    MOS_print("info","程序已开始运行！")
    MOS_print("info","开始导入库")
    from multiprocessing import Process
    MOS_print("info","导入进程库完成")
    p = Process(target=run_ui) #设置进程参数
    MOS_print("info","设置加速进程完成")
    import time
    start_time=time.time()
    p.start()

    app = QApplication(sys.argv)
    mos = Ui_MOS_Main()

    p.kill()

    MOS_print("info",str("加速进程执行时间" + str(time.time()-start_time)))
    MOS_print("info", "加速进程已退出")

    sys.exit(app.exec())
