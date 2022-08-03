from Java_Dowmloader_UI import Ui_Form as Ui_Java_Dowmloader

from PyQt6.QtWidgets import  QApplication, QLabel,QDialogButtonBox,QDialog
from PyQt6.QtCore import QPropertyAnimation, QTimer,QThread,pyqtSignal

class Java_Dowmloader__(QDialog, Ui_Java_Dowmloader):
    def __init__(self,v=None,url=None,file=None):
        super().__init__()
        self.v = v
        self.url = url
        self.file = file
        self.setupUi(self)
        #self.show()
        self.pushButton.clicked.connect(self.clicked_pushButton_close)
        self.progressBar.setValue(0)
        self.progressBar_2.setValue(0)
        self.progressBar_2.setMaximum(0)

        #启动线程
        self.d = Java_d(self.url,self.file)
        self.d.sinOut_d_j.connect(self.sinOut_d_j) #下载进度
        self.d.sinOut_d_s.connect(self.sinOut_d_s) #下载速度（网速
        self.d.start()

    def clicked_pushButton_close(self):
        self.pushButton.setEnabled(False) #为了防止重复操作 直接禁用按钮
        self.anim = QPropertyAnimation(self, b"windowOpacity") # 设置动画对象
        self.anim.setDuration(300) # 设置动画时长
        self.anim.setStartValue(1) # 设置初始属性，1.0为不透明
        self.anim.setEndValue(0) # 设置结束属性，0为完全透明
        self.anim.finished.connect(self.close_) # 动画结束时，关闭窗口
        self.anim.start() # 开始动画

    def sinOut_d_j(self,j):
        pass

    def sinOut_d_s(self,s):
        pass

    def close_(self):
        self.close()

class Java_d(QThread):
    sinOut_d_j = pyqtSignal(int) #进度
    sinOut_d_s = pyqtSignal(str) #网速

    def __init__(self,url,file):
        super(Java_d, self).__init__()
    def run(self):
        import MOS_Dowmloader
        