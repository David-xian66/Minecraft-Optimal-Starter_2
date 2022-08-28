from MC_Dowmloader_OK_UI import Ui_Dialog as MC_Dowmloader_OK_UI_
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QDialog
from PyQt6.QtCore import QPropertyAnimation, pyqtSignal


class MC_D_OK(QDialog,MC_Dowmloader_OK_UI_):
    sinOut = pyqtSignal()
    def __init__(self):
        super(MC_D_OK, self).__init__()
        self.setupUi(self)
        self.show()
        self.pushButton.clicked.connect(self.clicked_pushButton_close)

        # 添加阴影
        self.effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.effect_shadow.setOffset(0,0) # 偏移
        self.effect_shadow.setBlurRadius(155) # 阴影半径
        self.effect_shadow.setColor(QtCore.Qt.GlobalColor.gray) # 阴影颜色
        self.setGraphicsEffect(self.effect_shadow) # 将设置套用到窗口中

    def clicked_pushButton_close(self):
        self.pushButton.setEnabled(False) #为了防止重复操作 直接禁用按钮
        self.anim = QPropertyAnimation(self, b"windowOpacity") # 设置动画对象
        self.anim.setDuration(300) # 设置动画时长
        self.anim.setStartValue(1) # 设置初始属性，1.0为不透明
        self.anim.setEndValue(0) # 设置结束属性，0为完全透明
        self.anim.finished.connect(self.close_) # 动画结束时，关闭窗口
        self.anim.start() # 开始动画


    def close_(self):
        self.sinOut.emit()
        self.close()