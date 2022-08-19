# coding=utf-8
import json

from MC_Dowmloader_UI import Ui_MOS_D_MC_Dialog

from PyQt6.QtWidgets import  QApplication, QLabel,QDialogButtonBox,QDialog
from PyQt6.QtCore import QPropertyAnimation, QTimer,QThread,pyqtSignal
from PyQt6 import QtWidgets,QtCore

class Ui_MOS_D_MC_Dialog_(QDialog, Ui_MOS_D_MC_Dialog):
    """下载&安装游戏"""
    def __init__(self,Game_Current_File,G_D_Y,Json_File,MC,Forge,Fabric,Optifine):
        """
            需要的参数：
                Game_Current_File: 游戏目录
                 G_D_Y: 下载源
                 Json_File: 这个版本Json的地址
                 MC: 版本
                 Forge: Forge版本
                 Fabric: Fabric版本
                 Optifine: Optifine版本
        """
        super(Ui_MOS_D_MC_Dialog_, self).__init__()
        self.setupUi(self)

        self.Game_Current_File = Game_Current_File
        self.G_D_Y = G_D_Y
        self.Json_File = Json_File
        self.MC = MC
        self.Forge = Forge
        self.Fabric = Fabric
        self.Optifine = Optifine

        self.pushButton.clicked.connect(self.clicked_pushButton_close)
        self.show()
    def run(self):
        with open(self.Json_File,'r',encoding='utf_8') as f:
            b = json.load(f)
        for b_1 in b['versions']:
            if b_1['id'] == self.MC:
                json_url = b_1['url']
                break
        print(json_url)

    def clicked_pushButton_close(self):
        self.pushButton.setEnabled(False) #为了防止重复操作 直接禁用按钮
        self.anim = QPropertyAnimation(self, b"windowOpacity") # 设置动画对象
        self.anim.setDuration(300) # 设置动画时长
        self.anim.setStartValue(1) # 设置初始属性，1.0为不透明
        self.anim.setEndValue(0) # 设置结束属性，0为完全透明
        self.anim.finished.connect(self.close_) # 动画结束时，关闭窗口
        self.anim.start() # 开始动画


    def close_(self):
        self.close()