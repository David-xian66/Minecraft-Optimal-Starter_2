try:
    if __name__ == '__main__':
        versions = '2.0.5'
        import sys,os
        import ui
        from PyQt6.QtWidgets import QApplication,QMainWindow
        from MOS_print_ import MOS_print
        # import shutil
        # shutil.rmtree(".MOS")
        # shutil.rmtree(".minecraft")
        a = str(sys.platform)
        if a == "darwin":
            MOS_print("info",'当前系统为Mac')
            user_name = os.getlogin()
            # 获取当前系统用户目录
            user_home = os.path.expanduser('~')
            file = user_home + '/Documents'
        else:
            file = ''
 
        app = QApplication(sys.argv)
        mainWindow = QMainWindow()
        ui = ui.Ui_MOS()
        #  向主窗口添加控件
        ui.setupUi(mainWindow)
        mainWindow.show()
        sys.exit(app.exec())
except KeyboardInterrupt:
    MOS_print("info","程序以强行退出")
except Exception as error:
    MOS_print("error",error)