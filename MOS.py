def except_hook(cls, exception, traceback):
    '''报错显示'''
    sys.__excepthook__(cls, exception, traceback)

# 子进程要执行的代码
def run_ui():
    from MOS_print_ import MOS_print
    MOS_print("info","加速进程开始导入库！")
    import sys
    from PyQt6.QtWidgets import QApplication,QMainWindow
    import MOS_start_loading
    MOS_print("info","加速进程的Ui程序已开始运行！")
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    MOS_print("info","加速进程正在运行……请稍等...")
    MainWindow = QMainWindow()
    MOS_print("info","加速进程 创建窗口对象成功！")
    ui = MOS_start_loading.Ui_MainWindow()
    MOS_print("info","加速进程 创建PyQt窗口对象成功！")
    ui.setupUi(MainWindow)
    MOS_print("info","加速进程 初始化设置成功！")
    MainWindow.show()
    MOS_print("info","加速进程 已成功显示窗体")
    sys.exit(app.exec())


if __name__ == '__main__':
    try:
        import time,traceback
        from MOS_print_ import MOS_print
        import sys,os
        import MOS_UI_Main
        from MOS_start_loading import Ui_MainWindow

        a = str(sys.platform)
        if a == "darwin":
            MOS_print("info",'当前系统为Mac')
            user_name = os.getlogin()
            # 获取当前系统用户目录
            user_home = os.path.expanduser('~')
            file = user_home + '/Documents'
        else:
            file = ''
    
        MOS_print("info","Ui程序已开始运行！")
        sys.excepthook = except_hook
        MOS_print("info","请稍等...")

        ui = MOS_UI_Main.start()

    except KeyboardInterrupt:
        MOS_print("info","程序以强行退出")
    except:
        error = traceback.print_exc()
        if error == None:
            MOS_print("error","出现了一个None，如果您确定这是在您退出窗口后出现的，那么请忽略。如果不是，建议提交反馈。错误已打印")
            MOS_print("error",error)
        else:
            MOS_print("error",error)