# coding=utf-8
from Delete_Game_F_UI import Ui_Delete_Game_F_UI_J

from PyQt6.QtWidgets import  QApplication, QLabel,QDialogButtonBox,QDialog
from PyQt6.QtCore import QPropertyAnimation, QTimer,QThread,pyqtSignal
from PyQt6 import QtWidgets,QtCore

class Ui_Delete_Game_F_J(QDialog, Ui_Delete_Game_F_UI_J):
    def __init__(self):
        super(Ui_Delete_Game_F_J, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.clicked_pushButton_close)
        self.show()
    def run(self):
        pass

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