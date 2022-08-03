from Java_Dowmloader_UI import Ui_Java_Dowmloader
from PyQt6.QtWidgets import *



class Java_Dowmloader(QDialog, Ui_Java_Dowmloader):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.exec()