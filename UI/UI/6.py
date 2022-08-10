
from PyQt5 import QtCore, QtGui, QtWidgets


class LoginButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setMinimumSize(60, 60)

        self.color1 = QtGui.QColor(240, 53, 218)
        self.color2 = QtGui.QColor(61, 217, 245)

        self._animation = QtCore.QVariantAnimation(
            self,
            valueChanged=self._animate, #值改变
            startValue=0.00001, #开始值
            endValue=0.9999, #最终值
            duration=250 #持续时间
        )
        #print(self._animate())

    def _animate(self, value):
        qss = """
            font: 75 10pt "Microsoft YaHei UI";
            font-weight: bold;
            color: rgb(255, 255, 255);
            border-style: solid;
            border-radius:21px;
        """
        # self.color1.name() ==> #f035da
        grad = "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 {color1}, stop:{value} {color2}, stop: 1.0 {color1});".format(
            color1=self.color1.name(), color2=self.color2.name(), value=value
        )
        qss += grad
        print(qss) # 动画实现原理：动态改变 按钮 中的渐变效果
        self.setStyleSheet(qss)

    def enterEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Forward) #动画方向
        print("开始")
        self._animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Backward) #动画方向
        print("结束")
        self._animation.start()
        super().enterEvent(event)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    w = QtWidgets.QWidget()
    lay = QtWidgets.QVBoxLayout(w)

    for i in range(5):
        # 添加控件
        button = LoginButton()
        button.setText("Login")
        lay.addWidget(button)
    lay.addStretch()
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())