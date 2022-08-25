# coding=utf-8

# https://mp.weixin.qq.com/s/kxWmO6Q_VYt749OhAoTEUA
# https://blog.csdn.net/bluehawksky/article/details/106283636
# http://t.zoukankan.com/qiu-hua-p-12862576.html

# from gevent import monkey
import sys

import aiohttp
import nest_asyncio

nest_asyncio.apply()

import json
import os.path
import time
import traceback

import requests
import asyncio

from MC_Dowmloader_UI import Ui_MOS_D_MC_Dialog
from PyQt6.QtWidgets import QApplication, QLabel, QDialogButtonBox, QDialog
from PyQt6.QtCore import QPropertyAnimation, QTimer, QThread, pyqtSignal
from PyQt6 import QtWidgets, QtCore
from MOS_Dowmloader import Dowmloader
pool = []
pool_2 = []
time_1 = ''

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
        self.show()

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
        u_get_json['id'] = self.MC_Name

        # 解析为json格式 并存储 (版本的json文件)
        u_text_file = os.path.join(self.Game_Current_File, 'versions', self.MC_Name, str(self.MC_Name + '.json'))
        # 创建文件夹
        u_text_file_c = os.path.join(self.Game_Current_File, 'versions', self.MC_Name)
        os.makedirs(u_text_file_c, exist_ok=True)

        with open(u_text_file, 'w+', encoding='utf-8') as f:
            json.dump(u_get_json, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))



        # 下载游戏主文件
        file_1 = os.path.join(self.Game_Current_File, 'versions', self.MC_Name,str(self.MC_Name + '.jar'))
        u_mc_z = u_get_json['downloads']['client']
        self.u_mc_z_s = D_MC_Z(u_mc_z,file_1)
        self.u_mc_z_s.start()


        # 下载资源索引文件
        self.D_MC_ZY_ = D_MC_ZY(u_get_json,self.Game_Current_File)
        self.D_MC_ZY_.sinOut.connect(self.D_MC_ZY_sinOut)
        self.D_MC_ZY_.start()

        # 下载资源索引文件
        self.D_MC_YL_ = D_MC_YL(u_get_json,self.Game_Current_File)
        self.D_MC_YL_.start()


    def D_MC_ZY_sinOut(self):
        self.label.setText('11111111111111')

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





class D_MC_ZY(QThread):
    sinOut = pyqtSignal()

    def __init__(self,u_get_json,Game_Current_File):
        """下载资源文件"""
        self.u_get_json = u_get_json
        self.Game_Current_File = Game_Current_File
        super(D_MC_ZY, self).__init__()
    def run(self):

        # 获取 存储资源文件的json文件
        self.u_ziyuan_json_1 = self.u_get_json['assetIndex']['url']  # 获取资源文件链接
        self.u_ziyuan_json_get = requests.get(self.u_ziyuan_json_1)
        self.u_ziyuan_json_get_json = self.u_ziyuan_json_get.json()


        # 解析为json格式 并存储 (资源文件)
        self.u_ziyuan_file = os.path.join(self.Game_Current_File, 'assets', 'indexes', os.path.basename(self.u_ziyuan_json_1))
        with open(self.u_ziyuan_file, 'w+', encoding='utf-8') as f:
            json.dump(self.u_ziyuan_json_get_json, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))


        file_1 = os.path.join(self.Game_Current_File, 'assets', 'objects')

        for u_ziyuan_1, u_ziyuan_2 in self.u_ziyuan_json_get_json['objects'].items():
            hash = u_ziyuan_2['hash']
            hash_2 = hash[:2]
            size = u_ziyuan_2['size']
            url = 'http://resources.download.minecraft.net/' + str(hash_2) + '/' + str(hash)
            file_first = os.path.join(file_1, hash_2)
            file = os.path.join(file_first, hash)
            a = [url, file_first, file]
            pool.append(a)

        self.a_len = int(len(pool))
        self.a_len_s_1 = 25 #每个协程任务量
        self.a_len_s_2 = -self.a_len_s_1
        self.a_len_1 = self.a_len // self.a_len_s_1
        if self.a_len % self.a_len_s_1 != 0:
            # 如果正好整除
            pass
        else:
            self.a_len_1 += 1

        self.sinOut.emit()

        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        asyncio.run(asyncio.gather(self.D_R()))

    async def D_R(self):
        try:
            a = []
            s = 0
            while self.a_len_1:
                s += 1
                self.a_len_s_2 += self.a_len_s_1
                if self.a_len - self.a_len_s_2 < self.a_len_s_1:
                    pool_2 = pool[self.a_len_s_2:]
                    a.append(self.D_X(pool_2))
                    break
                else:
                    pool_2 = pool[self.a_len_s_2:self.a_len_s_2 + self.a_len_s_1]
                    a.append(asyncio.ensure_future(self.D_X(pool_2)))
                    print(str(self.a_len_s_2) + ' : ' + str(self.a_len_s_2 + self.a_len_s_1))

            await asyncio.wait([self.D_X_Start(a)])

            self.time_2 = time.perf_counter()
            print(self.time_2 - self.time_1)
        except:
            traceback.print_exc()

    async def D_X_Start(self,a):
        """创建"""
        try:
            self.time_1 = time.perf_counter()
            await asyncio.wait(a)
        except:
            traceback.print_exc()

    async def D_X(self,pool_2):
        """下载"""
        global pool
        for pool_3 in pool_2:
            while True:
                try:
                    os.makedirs(pool_3[1], exist_ok=True)
                    async with aiohttp.ClientSession() as session:
                        # aiohttp.client_exceptions.ServerDisconnectedError: Server disconnected
                        async with session.post(pool_3[0]) as resp:
                            with open(pool_3[2], 'wb') as fd:
                                # iter_chunked() 设置每次保存文件内容大小，单位bytes
                                async for chunk in resp.content.iter_chunked(3172):
                                    fd.write(chunk)
                    break
                except OSError:
                    print('存储异常 重试')
                except aiohttp.client_exceptions.ServerDisconnectedError:
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



class D_MC_Z(QThread):
    def __init__(self,l,file):
        """下载jar文件"""
        self.l = l
        self.file = file
        super(D_MC_Z, self).__init__()
    def run(self):
        shal = self.l['sha1']
        size = self.l['size']
        url = self.l['url']
        Dowmloader(url,50,self.file).run()
        #
        #r = requests.get(url, stream=True)
        #with open(self.file, 'wb') as fp:
        #    for item in r.iter_content(102400):
        #        # 10240表示每次会写入10240个字节，即10KB
        #        fp.write(item)
        #
        print('###############################################')


class D_MC_YL(QThread):
    def __init__(self,u_get_json,Game_Current_File):
        """下载依赖库文件"""
        self.u_get_json = u_get_json
        self.Game_Current_File = Game_Current_File
        super(D_MC_YL, self).__init__()
    def run(self):
        # 遍历json中的资源文件部分
        a = self.u_get_json['libraries']
        global pool_2
        for a_ in a:
            a_1 = a_['downloads']
            try:
                try:
                    m = a_1['rules']['os']
                    s = system_h()

                    if s == 'win32' or 'cygwin':
                        sy = 'windows'
                    elif s == 'darwin':
                        sy = 'osx'
                    else:
                        sy = 'linux'

                    if sy == m:
                        path_1 = a_1['artifact']['path']
                        sha1 = a_1['artifact']['sha1']
                        size = a_1['artifact']['size']
                        url = a_1['artifact']['url']

                except KeyError:
                    path_1 = a_1['artifact']['path']
                    sha1 = a_1['artifact']['sha1']
                    size = a_1['artifact']['size']
                    url = a_1['artifact']['url']

                path = os.path.join(self.Game_Current_File, 'libraries', path_1)
                path_q = path.split(os.path.basename(path))[0]
                c = [url, path, path_q, size]
                pool_2.append(c)

            except KeyError:
                try:
                    # natives文件
                    s = system_h()
                    if s == 'win32' or 'cygwin':
                        sy = 'natives-windows'
                    elif s == 'darwin':
                        sy = 'natives-osx'
                    else:
                        sy = 'natives-linux'

                    path_1 = a_1['classifiers'][sy]['path']
                    sha1 = a_1['classifiers'][sy]['sha1']
                    size = a_1['classifiers'][sy]['size']
                    url = a_1['classifiers'][sy]['url']

                    path = os.path.join(self.Game_Current_File, 'libraries', path_1)
                    path_q = path.split(os.path.basename(path))[0]
                    c = [url, path, path_q, size]
                    pool_2.append(c)

                except KeyError:
                    s = system_h()
                    c = ['natives-windows','natives-osx','natives-macos','natives-linux']
                    if s == 'win32' or 'cygwin':
                        sy = ['natives-windows']
                    elif s == 'darwin':
                        sy = ['natives-osx','natives-macos']
                    else:
                        sy = ['natives-linux']

                    classifiers_ = a_1['classifiers']

                    try:
                        for b_1 in sy:
                            try:
                                c.remove(b_1)
                            except KeyError:
                                pass
                        for b_2 in sy:
                            try:
                                del classifiers_[b_2]
                            except KeyError:
                                pass

                        for a_2 in classifiers_.keys():
                            path_1 = a_1['classifiers'][a_2]['path']
                            sha1 = a_1['classifiers'][a_2]['sha1']
                            size = a_1['classifiers'][a_2]['size']
                            url = a_1['classifiers'][a_2]['url']
                            path = os.path.join(self.Game_Current_File, 'libraries', path_1)
                            path_q = path.split(os.path.basename(path))[0]
                            a = [url, path, path_q, size]
                            pool_2.append(a)

                    except KeyError:
                        for a_2 in a_1['classifiers'].keys():
                            path_1 = a_1['classifiers'][a_2]['path']
                            sha1 = a_1['classifiers'][a_2]['sha1']
                            size = a_1['classifiers'][a_2]['size']
                            url = a_1['classifiers'][a_2]['url']
                            path = os.path.join(self.Game_Current_File, 'libraries', path_1)
                            path_q = path.split(os.path.basename(path))[0]
                            a = [url, path, path_q, size]
                            pool_2.append(a)


                        path_1 = a_1['artifact']['path']
                        sha1 = a_1['artifact']['sha1']
                        size = a_1['artifact']['size']
                        url = a_1['artifact']['url']

                        path = os.path.join(self.Game_Current_File, 'libraries', path_1)
                        path_q = path.split(os.path.basename(path))[0]
                        c = [url, path, path_q, size]
                        pool_2.append(c)


        self.a_len = int(len(pool_2))
        self.a_len_s_1 = 2 #每个协程任务量
        self.a_len_s_2 = -self.a_len_s_1
        self.a_len_1 = self.a_len // self.a_len_s_1
        if self.a_len % self.a_len_s_1 != 0:
            # 如果正好整除
            pass
        else:
            self.a_len_1 += 1
        print(self.a_len_1)

        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        asyncio.run(asyncio.gather(self.D_R()))


    async def D_R(self):
        try:
            self.a = []
            s = 0
            global pool_2
            while self.a_len_1:
                s += 1
                self.a_len_s_2 += self.a_len_s_1
                print(111111111111111111)
                if self.a_len - self.a_len_s_2 < self.a_len_s_1:
                    pool_3 = pool_2[self.a_len_s_2:]
                    self.a.append(self.D_X(pool_3))
                    break
                else:
                    pool_3 = pool_2[self.a_len_s_2:self.a_len_s_2 + self.a_len_s_1]
                    self.a.append(asyncio.ensure_future(self.D_X(pool_3)))
                    print(str(self.a_len_s_2) + ' : ' + str(self.a_len_s_2 + self.a_len_s_1) + 'ZY')

            await asyncio.wait([self.D_X_Start(self.a)])

            self.time_2 = time.perf_counter()
            print(self.time_2 - self.time_1)
        except:
            traceback.print_exc()


    async def D_X_Start(self,a):
        """创建"""
        try:
            self.time_1 = time.perf_counter()
            print(a)
            await asyncio.wait(a)
        except:
            traceback.print_exc()

    async def D_X(self,pool_3):
        """下载"""
        try:
            global pool_2
            for pool_4 in pool_3:
                while True:
                    try:
                        os.makedirs(pool_4[2], exist_ok=True)
                        async with aiohttp.ClientSession() as session:
                            async with session.post(pool_4[0]) as resp:
                                with open(pool_4[1], 'wb') as fd:
                                    # iter_chunked() 设置每次保存文件内容大小，单位bytes
                                    async for chunk in resp.content.iter_chunked(3172):
                                        fd.write(chunk)
                        break

                    except aiohttp.client_exceptions.ServerDisconnectedError:
                        print('链接失败 重试')
                    except OSError:
                        print('存储异常 重试')

                    except:
                        traceback.print_exc()
                while True:
                    try:
                        pool_2.remove(pool_4)
                        print(str(len(pool_2)) + 'pppppp')
                        break
                    except:
                        traceback.print_exc()
                        print(pool)
                        break
        except:
            traceback.print_exc()


class D_MC_Q(QThread):
    def __init__(self,u_get_json):
        """下载其他文件"""
        self.json = u_get_json
        super(D_MC_Q, self).__init__()
    def run(self):
        try:
            logging_ = self.json['logging']
        except KeyError:
            pass
        except:
            traceback.print_exc()


def system_h():
    """
        'win32':Windows
        'cygwin':Windows/Cygwin
        'darwin':macOS
        'aix':AIX
        'linux':Linux
    """
    a = str(sys.platform)
    return a