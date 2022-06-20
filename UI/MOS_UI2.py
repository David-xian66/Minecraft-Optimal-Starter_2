from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import *


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")


        # MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)


        MainWindow.resize(480, 180)
        MainWindow.setMinimumSize(QtCore.QSize(480, 180))
        MainWindow.setSizeIncrement(QtCore.QSize(480, 180))
        MainWindow.setBaseSize(QtCore.QSize(480, 180))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def MOSclose(self):
        quit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MOS错误"))
        self.pushButton.setText(_translate("MainWindow", "退出"))
        self.label.setText(_translate("MainWindow", "当前目录无读写权限，无法运行MOS"))
        self.pushButton.clicked.connect(self.MOSclose)
