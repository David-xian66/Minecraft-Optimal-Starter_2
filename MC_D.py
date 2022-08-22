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
from PyQt6.QtCore import QPropertyAnimation, QTimer, QThread, pyqtSignal
from PyQt6 import QtWidgets, QtCore

pool = []


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

        global pool
        pool = []

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
        file_1 = os.path.join(self.Game_Current_File, 'assets', 'objects')

        for u_ziyuan_1, u_ziyuan_2 in u_ziyuan_json_get_json['objects'].items():
            hash = u_ziyuan_2['hash']
            hash_2 = hash[:2]
            size = u_ziyuan_2['size']
            url = 'http://resources.download.minecraft.net/' + str(hash_2) + '/' + str(hash)
            file_first = os.path.join(file_1, hash_2)
            file = os.path.join(file_first, hash)
            a = [url, file_first, file]
            pool.append(a)

        self.a_len = len(pool)
        self.a_len_s_1 = 50 #每个线程任务量
        self.a_len_s_2 = -self.a_len_s_1
        self.a_len_1 = self.a_len // self.a_len_s_1
        if self.a_len % self.a_len_s_1 != 0:
            # 如果正好整除
            pass
        else:
            self.a_len_1 += 1
        asyncio.run(self.D_R_Start())

    async def D_R_Start(self):
        await asyncio.gather(self.D_R())


    async def D_R(self):
        try:
            a = []
            s = 0
            while self.a_len_1:
                s += 1
                self.a_len_s_2 += self.a_len_s_1
                if self.a_len - self.a_len_s_2 < self.a_len_s_1:
                    pool_2 = pool[self.a_len_s_2:]
                    a[s] = D_X(pool_2)
                    break
                else:
                    pool_2 = pool[self.a_len_s_2:self.a_len_s_2 + self.a_len_s_1 - 1]
                    a[s] = D_X(pool_2)
                    print(str(self.a_len_s_2) + ' : ' + str(self.a_len_s_2 + self.a_len_s_1 - 1))

            await asyncio.wait([D_X_Start_2(a)])
            print(1)

        except:
            traceback.print_exc()


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


async def D_X_Start_2(a):
    try:
        for a_1 in a.values():
            pass
        await asyncio.wait(b)
    except:
        traceback.print_exc()


async def D_X(pool_2):
    """下载"""
    global pool
    await asyncio.sleep(0)
    for pool_3 in pool_2:
        while True:
            await asyncio.sleep(0)
            try:
                await asyncio.sleep(0)
                a = requests.get(pool_3[0], stream=True)
                os.makedirs(pool_3[1], exist_ok=True)
                await asyncio.sleep(0)
                with open(pool_3[2], 'wb') as f:
                    await asyncio.sleep(0)
                    f.write(a.content)
                    await asyncio.sleep(0)
                    f.flush()
                    await asyncio.sleep(0)
                    f.close()
                break
            except OSError:
                print('存储异常 重试')
                time.sleep(0.1)
            except requests.exceptions.ConnectionError:
                print('链接失败 重试')
            except:
                traceback.print_exc()
        while True:
            try:
                print(pool_3[2])
                pool.remove(pool_3)
                print(len(pool))
                break
            except:
                traceback.print_exc()
                print(pool)
                break