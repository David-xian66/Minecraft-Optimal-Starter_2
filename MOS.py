
import sys,os, requests, json, datetime
from os import path


from PyQt6.QtCore import *

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MOS(object):
    def setupUi(self, MOS):
        MOS.setObjectName("MOS")
        MOS.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        MOS.resize(1000, 530)
        self.centralwidget = QtWidgets.QWidget(MOS)
        self.centralwidget.setObjectName("centralwidget")
        MOS.setCentralWidget(self.centralwidget)

        self.retranslateUi(MOS)
        QtCore.QMetaObject.connectSlotsByName(MOS)

    def retranslateUi(self, MOS):
        _translate = QtCore.QCoreApplication.translate
        MOS.setWindowTitle(_translate("MOS", "MainWindow"))



if __name__ == '__main__':
    MOS_Json()
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
