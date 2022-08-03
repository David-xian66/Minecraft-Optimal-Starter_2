from Java_Dowmloader_OK_UI import Ui_Dialog_2 as Java_Dowmloader_OK_UI

from PyQt6.QtWidgets import QApplication, QLabel,QDialogButtonBox,QDialog
from PyQt6.QtCore import QPropertyAnimation, QTimer,QThread,pyqtSignal


class Java_OK_UI(QDialog,Java_Dowmloader_OK_UI):
    sinOut = pyqtSignal()
    def __init__(self):
        super(Java_OK_UI, self).__init__()
        self.setupUi(self)
        self.show()
        self.pushButton.clicked.connect(self.clicked_pushButton_close)


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