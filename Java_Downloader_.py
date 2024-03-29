import traceback

import requests
from Java_Downloader_UI import Ui_Dialog as Ui_Java_Dowmloader
from Java_Downloader_OK import Java_OK_UI as Ui_Java_Dowmloader_OK_

from PyQt6.QtWidgets import QApplication, QLabel, QDialogButtonBox, QDialog
from PyQt6.QtCore import QPropertyAnimation, QTimer, QThread, pyqtSignal
from PyQt6 import QtWidgets, QtCore


class Java_Downloader__(QDialog, Ui_Java_Dowmloader):
    sinOut = pyqtSignal()

    def __init__(self, v=None, url=None, file=None):
        super().__init__()
        self.v = v
        self.url = url
        self.file = file
        self.setupUi(self)
        self.show()

        # 添加阴影
        self.effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.effect_shadow.setOffset(0, 0)  # 偏移
        self.effect_shadow.setBlurRadius(15)  # 阴影半径
        self.effect_shadow.setColor(QtCore.Qt.GlobalColor.gray)  # 阴影颜色
        self.setGraphicsEffect(self.effect_shadow)  # 将设置套用到窗口中

    def start_(self):
        self.progressBar.setValue(0)
        self.pushButton.clicked.connect(self.J_D_stop)
        self.progressBar.setValue(0)
        self.progressBar_2.setValue(0)
        self.progressBar_2.setMaximum(0)
        # QApplication.processEvents()
        # 启动线程
        self.d = Java_d(self.url, self.file)
        self.d.sinOut_d_j.connect(self.sinOut_d_j_)  # 下载进度
        self.d.start()

    def J_D_stop(self):
        """暂停&取消下载"""
        from MOS_Downloader import Downloader
        Downloader.q_()
        self.d.terminate()  # 强行终止
        self.d.wait()
        self.clicked_pushButton_close()

    def clicked_pushButton_close(self):
        self.pushButton.setEnabled(False)  # 为了防止重复操作 直接禁用按钮
        self.anim = QPropertyAnimation(self, b"windowOpacity")  # 设置动画对象
        self.anim.setDuration(300)  # 设置动画时长
        self.anim.setStartValue(1)  # 设置初始属性，1.0为不透明
        self.anim.setEndValue(0)  # 设置结束属性，0为完全透明
        self.anim.finished.connect(self.close_)  # 动画结束时，关闭窗口
        self.anim.start()  # 开始动画

    def sinOut_d_j_(self, j):
        """下载线程的状态"""
        if j == 'D':
            # 这个计时器用来更新 进度+网速
            self.j_h = QTimer()  # 创建计时器对象
            self.j_h.timeout.connect(self.Java_d_j)  # 要执行的槽
            self.j_h.start(50)  # 开始计时器

        elif j == 'P_1':
            # 配置第1步
            self.j_h.stop()  # 停止刷新进度的计时器
            self.progressBar.setValue(110)
            self.progressBar_2.setMaximum(100)
            self.label_5.setText("正在解压……(1/6)")
        elif j == 'P_2':
            # 配置第2步
            self.progressBar_2.setValue(10)
            self.label_5.setText("正在解压……(2/6)")
        elif j == 'P_3':
            # 配置第3步
            self.progressBar_2.setValue(35)
            self.label_5.setText("正在解压……(3/6)")
        elif j == 'P_4':
            # 配置第4步
            self.progressBar_2.setValue(60)
            self.label_5.setText("正在解压……(4/6)")
        elif j == 'P_5':
            # 配置第5步
            self.progressBar_2.setValue(85)
            self.label_5.setText("正在解压……(5/6)")
        elif j == 'OK':
            # 配置OK
            self.progressBar_2.setValue(100)
            self.label_5.setText("正在解压……(6/6)")
            self.sinOut.emit()
            self.progressBar.setValue(0)
            self.clicked_pushButton_close()

    def Java_d_j(self):
        import MOS_Downloader
        a = MOS_Dowmloader.j_h()
        b = MOS_Dowmloader.w_h()
        self.progressBar.setValue(a)
        self.label_5.setText(b)

    def close_(self):
        self.close()


class Java_d(QThread):
    sinOut_d_j = pyqtSignal(str)  # 进度(下载/配置)

    def __init__(self, url, file):
        super(Java_d, self).__init__()
        self.url = url
        self.file = file

    def run(self):
        from MOS_Downloader import Downloader
        from multiprocessing import Process
        try:
            a = Downloader(self.url, 100, self.file)
        except requests.exceptions.MissingSchema:
            pass
        self.sinOut_d_j.emit("D")  # 告诉槽 已经开始下载
        a.run()
        self.sinOut_d_j.emit("P_1")  # 开始配置

        import os
        f_name = self.file.replace(".gz", "")
        # 获取文件的名称，去掉
        import gzip
        g_file = gzip.GzipFile(self.file)

        self.sinOut_d_j.emit("P_2")  # 配置02

        open(f_name, "w+").write(str(g_file.read()))  # 创建gzip对象
        # gzip对象用read()打开后，写入open()建立的文件里。
        g_file.close()
        # 关闭gzip对象

        self.sinOut_d_j.emit("P_3")  # 配置03

        import tarfile
        tar = tarfile.open(self.file)
        names = tar.getnames()
        self.sinOut_d_j.emit("P_4")  # 配置04
        a = str(self.file).split('.tar.gz')
        a_1 = a[0]
        self.file = a_1

        import shutil
        if os.path.exists(self.file):
            shutil.rmtree(self.file)
        else:
            pass

        if os.path.isdir(self.file):
            pass
        else:
            os.mkdir(self.file)
        self.sinOut_d_j.emit("P_5")  # 配置05
        # 因为解压后是很多文件，预先建立同名目录
        for name in names:
            tar.extract(name, self.file)
        tar.close()

        from MOS_UI_Main import file_h

        file_2 = os.path.join(file_h(), '.MOS', 'Java')

        if os.path.exists(file_2):
            shutil.rmtree(file_2)
        else:
            shutil.move(self.file, file_2)

        self.sinOut_d_j.emit("OK")  # OK
