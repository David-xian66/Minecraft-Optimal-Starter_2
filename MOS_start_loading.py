# Form implementation generated from reading ui file '/Users/xyj/.npm/ssh/UI/UI/MOS_start_loading.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

import MOS_start_loading_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(175, 175)
        MainWindow.setMinimumSize(QtCore.QSize(175, 175))
        MainWindow.setMaximumSize(QtCore.QSize(175, 175))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.WaitCursor))
        MainWindow.setMouseTracking(True)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setToolTipDuration(0)
        MainWindow.setStyleSheet("")
        MainWindow.setIconSize(QtCore.QSize(100, 100))
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.DockOption.AllowTabbedDocks|QtWidgets.QMainWindow.DockOption.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)

        MainWindow.setWindowFlags(QtCore.Qt.WindowType.WindowStaysOnTopHint | QtCore.Qt.WindowType.FramelessWindowHint)  # 置顶，且去掉边框
        MainWindow.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)  # 窗体背景透明

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.label.setStyleSheet("border-image: url(:/img/ico.png);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
