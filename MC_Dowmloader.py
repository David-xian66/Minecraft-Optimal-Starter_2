# coding=utf-8

# from gevent import monkey
import nest_asyncio

nest_asyncio.apply()

import json
import os.path
import queue
import time
import traceback
from threading import Thread
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import requests
import asyncio

import uvloop

from MC_Dowmloader_UI import Ui_MOS_D_MC_Dialog

from PyQt6.QtWidgets import QApplication, QLabel, QDialogButtonBox, QDialog
from PyQt6.QtCore import QPropertyAnimation, QTimer, QThread, pyqtSignal,QThreadPool
from PyQt6 import QtWidgets, QtCore


class Ui_MOS_D_MC_Dialog_(QDialog, Ui_MOS_D_MC_Dialog):
    """下载&安装游戏"""

    def __init__(self, Game_Current_File, G_D_Y, Json_File, MC, MC_Name, Forge, Fabric, Optifine):
        """
            需要的参数：
                Game_Current_File: 游戏目录
                 G_D_Y: 下载源
                 Json_File: 这个版本Json的地址
                 MC: 版本
                 MC_Name: 游戏名
                 Forge: Forge版本
                 Fabric: Fabric版本
                 Optifine: Optifine版本
        """
        super(Ui_MOS_D_MC_Dialog_, self).__init__()
        self.setupUi(self)

        self.Game_Current_File = Game_Current_File
        self.G_D_Y = G_D_Y
        self.Json_File = Json_File
        self.MC = MC
        self.MC_Name = MC_Name
        self.Forge = Forge
        self.Fabric = Fabric
        self.Optifine = Optifine

        self.pushButton.clicked.connect(self.clicked_pushButton_close)
        self.show()

    def startCoroutine(self) -> asyncio.events.AbstractEventLoop:
        """
        创建并开始协程。返回 loop 实体
        """

        def startLoop(loop):
            asyncio.set_event_loop(loop)
            loop.run_forever()

        myLoop = asyncio.new_event_loop()  # 获得事件循环
        myThread = Thread(target=startLoop, args=(myLoop,))  # 将 loop 装入线程。参数中的逗号是必要的
        myThread.start()  # 开启线程
        return myLoop

    def run(self):
        with open(self.Json_File, 'r', encoding='utf_8') as f:
            b = json.load(f)
        for b_1 in b['versions']:
            if b_1['id'] == self.MC:
                json_url = b_1['url']
                break
        print(json_url)
        # 下载版本的json文件
        u = requests.get(json_url)
        u_get_json = u.json()

        # 解析为json格式 并存储
        u_text_file = os.path.join(self.Game_Current_File, 'versions', self.MC_Name, os.path.basename(json_url))
        # 创建文件夹
        u_text_file_c = os.path.join(self.Game_Current_File, 'versions', self.MC_Name)
        os.makedirs(u_text_file_c, exist_ok=True)

        with open(u_text_file, 'w+', encoding='utf-8') as f:
            json.dump(u_get_json, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))

        # 获取 存储资源文件的json文件
        u_ziyuan_json_1 = u_get_json['assetIndex']['url']  # 获取资源文件链接
        u_ziyuan_json_get = requests.get(u_ziyuan_json_1)
        u_ziyuan_json_get_json = u_ziyuan_json_get.json()

        # 解析为json格式 并存储
        u_ziyuan_file = os.path.join(self.Game_Current_File, 'assets', 'indexes', os.path.basename(u_ziyuan_json_1))
        with open(u_ziyuan_file, 'w+', encoding='utf-8') as f:
            json.dump(u_ziyuan_json_get_json, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))

        # 下载资源索引文件
        self.pool = []
        file_1 = os.path.join(self.Game_Current_File, 'assets', 'objects')

        for u_ziyuan_1, u_ziyuan_2 in u_ziyuan_json_get_json['objects'].items():
            hash = u_ziyuan_2['hash']
            hash_2 = hash[:2]
            size = u_ziyuan_2['size']
            url = 'http://resources.download.minecraft.net/' + str(hash_2) + '/' + str(hash)
            file_first = os.path.join(file_1, hash_2)
            file = os.path.join(file_first, hash)
            a = [url, file_first, file]
            self.pool.append(a)

        self.a_len = len(self.pool)
        self.a_len_s_1 = 70 #每个线程任务量
        self.a_len_s_2 = -self.a_len_s_1
        self.a_len_1 = self.a_len // self.a_len_s_1
        if self.a_len % self.a_len_s_1 != 0:
            # 如果不能整除
            self.a_len_1 += 1
        while True:
            self.a_len_s_2 += self.a_len_s_1
            if self.a_len - self.a_len_s_2 < self.a_len_s_1:
                pool_2 = self.pool[self.a_len_s_2:]
                print(str(self.a_len_s_2) + ' : ~')
                break
            else:
                pool_2 = self.pool[self.a_len_s_2:self.a_len_s_2 + self.a_len_s_1 - 1]
                print(str(self.a_len_s_2) + ' : ' + str(self.a_len_s_2 + self.a_len_s_1 - 1))

            D = M_D_(pool_2)
            D.start()

    def clicked_pushButton_close(self):
        self.pushButton.setEnabled(False)  # 为了防止重复操作 直接禁用按钮
        self.anim = QPropertyAnimation(self, b"windowOpacity")  # 设置动画对象
        self.anim.setDuration(300)  # 设置动画时长
        self.anim.setStartValue(1)  # 设置初始属性，1.0为不透明
        self.anim.setEndValue(0)  # 设置结束属性，0为完全透明
        self.anim.finished.connect(self.close_)  # 动画结束时，关闭窗口
        self.anim.start()  # 开始动画

    def close_(self):
        self.close()


class M_D_(QThread):
    def __init__(self, l):
        self.l = l
        super(M_D_, self).__init__()

    def run(self):
        for l_2 in l:
            url = l_2[0]
            os.makedirs(l_2[1], exist_ok=True)
            a = requests.get(url, stream=True)
            with open(l_2[2], 'wb') as f:
                f.write(a.content)
                f.flush()
                f.close()
            print(l_2[2])
