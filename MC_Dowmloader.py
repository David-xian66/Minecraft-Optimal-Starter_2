# coding=utf-8

# https://mp.weixin.qq.com/s/kxWmO6Q_VYt749OhAoTEUA
# https://blog.csdn.net/bluehawksky/article/details/106283636
# http://t.zoukankan.com/qiu-hua-p-12862576.html

# from gevent import monkey
import sys
import zipfile

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
import MOS_Downloader

pool = []
pool_2 = []
pool_f = []
run_ = True


class Ui_MOS_D_MC_Dialog_(QDialog, Ui_MOS_D_MC_Dialog):
    """下载&安装游戏"""
    sinOut_OK = pyqtSignal()

    def __init__(self, Game_Current_File, MC_File, G_D_Y, Json_File, MC, MC_Name, Forge, Forge_json,Fabric, Optifine, TimeOut, MOS_File):
        """
            需要的参数：
                Game_Current_File: 游戏目录
                MC_File: MC文件夹目录
                G_D_Y: 下载源
                Json_File: 这个版本Json的地址
                MC: 版本
                MC_Name: 游戏名
                Forge: Forge版本
                Fabric: Fabric版本
                Optifine: Optifine版本
                TimeOut: 请求超时时间
                MOS_File: MOS缓存目录
        """
        super(Ui_MOS_D_MC_Dialog_, self).__init__()
        self.setupUi(self)

        global pool
        pool = []

        self.Game_Current_File = Game_Current_File
        self.MC_File = MC_File
        self.G_D_Y = G_D_Y
        self.Json_File = Json_File
        self.MC = MC
        self.MC_Name = MC_Name
        self.Forge = Forge
        self.Forge_json = Forge_json
        self.Fabric = Fabric
        self.Optifine = Optifine
        self.TimeOut = TimeOut
        self.MOS_File = MOS_File

        self.pushButton.clicked.connect(self.clicked_pushButton_close_q)

    def run(self):
        with open(self.Json_File, 'r', encoding='utf_8') as f:
            b = json.load(f)
        for b_1 in b['versions']:
            if b_1['id'] == self.MC:
                json_url_1 = b_1['url']
                break
        print(json_url_1)

        if self.G_D_Y == 'MC':
            self.url_q_ = 'http://launchermeta.mojang.com/'
            self.url_q_l = 'http://libraries.minecraft.net/'  # 依赖
            self.url_q_zy = 'http://resources.download.minecraft.net/'  # 资源文件
        elif self.G_D_Y == 'MCBBS':
            self.url_q_ = 'http://download.mcbbs.net/'  # json文件
            self.url_q_l = 'http://download.mcbbs.net/maven/'  # 依赖
            self.url_q_zy = 'http://download.mcbbs.net/assets/'  # 资源文件
        else:
            self.url_q_ = 'http://bmclapi2.bangbang93.com/'  # json文件
            self.url_q_l = 'http://bmclapi2.bangbang93.com/maven/'  # 依赖
            self.url_q_zy = 'http://bmclapi2.bangbang93.com/assets/'  # 资源文件

        if self.G_D_Y != 'MC':
            json_url = self.url_q_ + 'version/' + self.MC + '/json'
        else:
            json_url = json_url_1

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
        u_text_file_2 = os.path.join(self.Game_Current_File, 'versions', self.MC_Name)
        os.makedirs(u_text_file_2, exist_ok=True)
        with open(u_text_file, 'w+', encoding='utf-8') as f:
            json.dump(u_get_json, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))

        self.size_all = 0  # 安装需要下载的总大小
        self.size_all_ok = 0  # 目前下载完成的总大小
        self.ws_d = 0  # 网速
        self.ziyuan_s = 0  # 资源文件总数量
        self.yilai_s = 0  # 依赖库总速度
        self.ws_s = 0  # 资源库总数

        global run_
        run_ = True

        '''
        # 下载游戏主文件
        file_1 = os.path.join(self.Game_Current_File, 'versions', self.MC_Name, str(self.MC_Name + '.jar'))
        u_mc_z = u_get_json['downloads']['client']
        self.u_mc_z_s = D_MC_Z(u_mc_z, file_1, self.MC, self.G_D_Y)
        self.u_mc_z_s.sinOut_start.connect(self.D_MC_Z_sinOut_start)  # 网速
        self.u_mc_z_s.sinOut_ok.connect(self.D_MC_Z_sinOut_ok)  # 完成后通知
        self.u_mc_z_s.start()

        # 下载资源索引文件
        self.D_MC_ZY_ = D_MC_ZY(u_get_json, self.Game_Current_File, self.G_D_Y, self.url_q_zy, self.url_q_,
                                self.TimeOut)
        self.D_MC_ZY_.sinOut_size.connect(self.D_MC_ZY_sinOut_size)  # 数量
        self.D_MC_ZY_.sinOut_j.connect(self.D_MC_ZY_sinOut_j)  # 进度
        self.D_MC_ZY_.sinOut_s.connect(self.D_MC_ZY_sinOut_s)  # 网速
        self.D_MC_ZY_.start()

        # 下载依赖库文件
        self.D_MC_YL_ = D_MC_YL(u_get_json, self.Game_Current_File, self.url_q_l, self.TimeOut)
        self.D_MC_YL_.sinOut_size.connect(self.D_MC_YL_sinOut_size)  # 数量
        self.D_MC_YL_.sinOut_j.connect(self.D_MC_YL_sinOut_j)  # 进度
        self.D_MC_YL_.sinOut_s.connect(self.D_MC_YL_sinOut_s)  # 网速
        self.D_MC_YL_.start()
        
        '''

        if self.Forge != None:
            # 下载Forge主文件
            # file_1 = os.path.join(self.Game_Current_File, 'versions', self.MC_Name, str(self.MC_Name + '.jar'))
            self.u_mc_f_z = D_MC_F_D(self.Game_Current_File, self.MC_File, self.MC, self.G_D_Y, self.Forge,
                                     self.Forge_json, self.Game_Current_File, self.MOS_File)
            # self.u_mc_f_z.sinOut_start.connect(self.D_MC_f_d_sinOut_start)  # 网速
            # self.u_mc_f_z.sinOut_ok.connect(self.D_MC_f_d_sinOut_ok)  # 完成后通知
            self.u_mc_f_z.start()


        # 在UI上显示总下载速度(网速)
        self.ws_ui_ = QTimer()
        self.ws_ui_.start(1000)
        self.ws_ui_.timeout.connect(self.ws_ui)

        # 在UI上显示总共要下载的大小
        self.ds_ui_ = QTimer()
        self.ds_ui_.start(500)
        self.ds_ui_.timeout.connect(self.ds_ui)

    def MC_D_OK_C(self):
        """检查是否全部完成"""
        if self.progressBar_4.maximum() and self.progressBar_2.maximum() != 0:
            if self.progressBar_4.value() == self.progressBar_4.maximum() and self.progressBar_2.value() == self.progressBar_2.maximum() and self.progressBar.value() == 105:
                self.clicked_pushButton_close()

    def D_MC_Z_sinOut_size(self, size):
        """主文件总文件大小"""
        self.size_all += int(size)

    def D_MC_Z_sinOut_j(self, j):
        """设置 主文件下载进度"""
        # self.size_all_ok += size
        self.progressBar.setValue(int(j))

    def D_MC_Z_sinOut_s(self, w):
        """主文件下载网速"""
        # 需要识别后缀
        j_ = w.split(' ')
        j_1 = j_[1]
        if j_1 == 'MB/s':
            j_2 = j_[0] * 1024 * 1024
        else:
            j_2 = j_[0] * 1024
        self.ws_d += j_2

    def D_MC_Z_sinOut_start(self):
        """Jar下载开始后"""
        # 获取大小(jar文件)
        self.s_h_ = QTimer()  # 创建计时器对象
        self.s_h_.start(800)  # 开始计时器
        self.s_h_.timeout.connect(self.h_size)  # 要执行的槽

        # 获取进度(jar文件)
        self.j_h_ = QTimer()  # 创建计时器对象
        self.j_h_.start(1000)  # 开始计时器
        self.j_h_.timeout.connect(self.h_j)  # 要执行的槽

    def D_MC_Z_sinOut_ok(self):
        """Jar下载完成后"""
        self.progressBar.setValue(105)
        self.j_h_.stop()
        self.s_h_.stop()
        self.MC_D_OK_C()


    def D_MC_ZY_sinOut_size(self, size):
        """资源文件大小"""
        self.size_all += size
        self.ziyuan_s += 1
        self.progressBar_2.setMaximum(self.ziyuan_s)

    def D_MC_ZY_sinOut_j(self):
        """设置 资源文件下载进度 (完成一个就调用一次)"""
        a = self.progressBar_2.value()
        self.progressBar_2.setValue(a + 1)
        if self.progressBar_2.value() == self.progressBar_2.maximum():
            self.MC_D_OK_C()

    def D_MC_ZY_sinOut_s(self, size):
        """资源文件下载网速"""
        self.ws_d += size
        self.ws_s += 1

    def D_MC_YL_sinOut_size(self, size):
        """依赖文件大小(size)"""
        self.size_all += int(size)
        self.yilai_s += 1
        self.progressBar_4.setMaximum(self.yilai_s)

    def D_MC_YL_sinOut_j(self):
        """设置 依赖文件下载进度 (完成一个就调用一次)"""
        a = self.progressBar_4.value()
        self.progressBar_4.setValue(a + 1)
        if self.progressBar_4.maximum() == self.progressBar_4.value():
            self.MC_D_OK_C()

    def D_MC_YL_sinOut_s(self, size):
        """依赖下载网速"""
        self.ws_d += size

    def ws_ui(self):
        """总网速显示"""
        ws_d_1 = int(self.ws_d) / 1024
        self.ws_d = 0
        if ws_d_1 > 1024:
            ws_d = str(round(ws_d_1 / 1024, 2)) + 'MB/s'
        else:
            ws_d = str(round(ws_d_1, 2)) + 'KB/s'
        self.label_5.setText(ws_d)

    def ds_ui(self):
        """需要下载的总大小显示"""
        size_1 = self.size_all / 1024
        if size_1 > 1024:
            size = str(round(size_1 / 1024, 2)) + ' MB'
        else:
            size = str(size_1) + ' KB'
        # self.label.setText('安装游戏 ' + '(' +str(self.size_all_ok) + '/' + size + ')')
        self.label.setText('安装游戏 ' + '(' + size + ')')

    def h_size(self):
        """获取大小(jar文件)"""
        size = MOS_Downloader.s_h()
        if size != 0:
            self.s_h_.stop()
            self.D_MC_Z_sinOut_size(size)

    def h_j(self):
        """获取进度(jar文件)"""
        print(time.time())
        j = MOS_Downloader.j_h()
        if j != 0:
            self.D_MC_Z_sinOut_j(j)

    def clicked_pushButton_close(self):
        self.pushButton.setEnabled(False)  # 为了防止重复操作 直接禁用按钮
        self.anim = QPropertyAnimation(self, b"windowOpacity")  # 设置动画对象
        self.anim.setDuration(300)  # 设置动画时长
        self.anim.setStartValue(1)  # 设置初始属性，1.0为不透明
        self.anim.setEndValue(0)  # 设置结束属性，0为完全透明
        self.anim.finished.connect(self.close_)  # 动画结束时，关闭窗口
        self.anim.start()  # 开始动画

    def close_(self):
        global run_
        if run_ == True:
            self.sinOut_OK.emit()
        self.close()

    def clicked_pushButton_close_q(self):
        """点取消后"""
        self.pushButton.setText('正在终止……')
        QApplication.processEvents()
        MOS_Downloader.stop()
        global run_
        run_ = False
        # 终止线程
        self.u_mc_z_s.terminate()
        self.D_MC_ZY_.quit()
        self.D_MC_YL_.quit()
        print('222')
        self.u_mc_z_s.wait()
        print('333')
        self.D_MC_ZY_.wait()
        print('444')
        self.D_MC_YL_.wait()
        print('555')
        self.clicked_pushButton_close()

class D_MC_ZY(QThread):
    sinOut_size = pyqtSignal(int)
    sinOut_j = pyqtSignal()
    sinOut_s = pyqtSignal(int)

    def __init__(self, u_get_json, Game_Current_File, G_D_Y, url_q_zy, url_q_, timeout):
        """下载资源文件"""
        self.u_get_json = u_get_json
        self.Game_Current_File = Game_Current_File
        self.url_q_zy = url_q_zy
        self.G_D_Y = G_D_Y
        self.url_q_ = url_q_
        self.timeout = timeout
        super(D_MC_ZY, self).__init__()

    def run(self):
        global run_
        if run_ == True:
            # 获取 存储资源文件的json文件
            u_ziyuan_json_1_ = self.u_get_json['assetIndex']['url']  # 获取资源文件链接
            if self.G_D_Y != 'MC':
                try:
                    self.u_ziyuan_json_1 = self.url_q_ + u_ziyuan_json_1_.split('https://launcher.mojang.com/')[1]
                except IndexError:
                    self.u_ziyuan_json_1 = self.url_q_ + u_ziyuan_json_1_.split('https://launchermeta.mojang.com/')[1]
            else:
                self.u_ziyuan_json_1 = u_ziyuan_json_1_
            while True:
                try:
                    self.u_ziyuan_json_get = requests.get(self.u_ziyuan_json_1)
                    break
                except requests.exceptions.ConnectionError:
                    print('资源文件Json 请求异常')

            self.u_ziyuan_json_get_json = self.u_ziyuan_json_get.json()

            # 解析为json格式 并存储 (资源文件)
            self.u_ziyuan_file_ = os.path.join(self.Game_Current_File, 'assets', 'indexes')

            self.u_ziyuan_file = os.path.join(self.u_ziyuan_file_, os.path.basename(self.u_ziyuan_json_1))
            os.makedirs(self.u_ziyuan_file_, exist_ok=True)
            with open(self.u_ziyuan_file, 'w+', encoding='utf-8') as f:
                json.dump(self.u_ziyuan_json_get_json, f, ensure_ascii=False, sort_keys=True, indent=4,
                          separators=(',', ': '))

            file_1 = os.path.join(self.Game_Current_File, 'assets', 'objects')

            for u_ziyuan_1, u_ziyuan_2 in self.u_ziyuan_json_get_json['objects'].items():
                hash = u_ziyuan_2['hash']
                hash_2 = hash[:2]
                size = u_ziyuan_2['size']
                url = self.url_q_zy + str(hash_2) + '/' + str(hash)
                file_first = os.path.join(file_1, hash_2)
                file = os.path.join(file_first, hash)
                a = [url, file_first, file, size]
                pool.append(a)
                self.sinOut_size.emit(size)

            self.a_len = int(len(pool))

            print(len(pool))
            if len(pool) <= 500:
                self.a_len_s_1 = 1  # 每个协程任务量
            elif len(pool) <= 1000:
                self.a_len_s_1 = 1  # 每个协程任务量
            elif len(pool) <= 1500:
                self.a_len_s_1 = 2  # 每个协程任务量
            elif len(pool) <= 2000:
                self.a_len_s_1 = 2  # 每个协程任务量
            elif len(pool) <= 3000:
                self.a_len_s_1 = 2  # 每个协程任务量
            elif len(pool) <= 4000:
                self.a_len_s_1 = 3  # 每个协程任务量
            else:
                self.a_len_s_1 = 3  # 每个协程任务量

            print(self.a_len_s_1)

            self.a_len_s_2 = -self.a_len_s_1
            self.a_len_1 = self.a_len // self.a_len_s_1
            if self.a_len % self.a_len_s_1 != 0:
                # 如果正好整除
                pass
            else:
                self.a_len_1 += 1

            self.new_loop = asyncio.new_event_loop()
            asyncio.set_event_loop(self.new_loop)
            asyncio.run(asyncio.gather(self.D_R()))

    async def D_R(self):
        try:
            global run_
            if run_ == True:
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

    async def D_X_Start(self, a):
        """创建"""
        try:
            self.time_1 = time.perf_counter()
            await asyncio.wait(a)
        except:
            traceback.print_exc()

    async def D_X(self, pool_2):
        """下载"""
        global pool, run_
        header = {
            'Proxy-Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}  # 伪装浏览器
        if run_ == True:
            for pool_3 in pool_2:
                print(pool_3[0])
                while True:
                    try:
                        os.makedirs(pool_3[1], exist_ok=True)
                        if run_ == True:
                            async with aiohttp.ClientSession(timeout = aiohttp.ClientTimeout(connect=30)) as session:
                                # aiohttp.client_exceptions.ServerDisconnectedError: Server disconnected
                                if run_ == True:
                                    file = await session.get(pool_3[0], headers=header, ssl=False)
                                    file_code = await file.read()

                                    with open(pool_3[2], 'wb') as f:
                                        f.write(file_code)

                                    '''
                                    async with session.get(pool_3[0], headers=header, ssl=False) as resp:
                                        if run_ == True:
                                            with open(pool_3[2], 'wb') as fd:
                                                # iter_chunked() 设置每次保存文件内容大小，单位bytes
                                                if run_ == True:
                                                    async for chunk in resp.content.iter_chunked(10240000000):
                                                        fd.write(chunk)
                                                else:
                                                    break
                                        else:
                                            break
                                    '''
                                else:
                                    break
                        self.sinOut_j.emit()
                        self.sinOut_s.emit(pool_3[3])
                        break
                    except OSError:
                        print('存储异常 重试(资源)')
                    except aiohttp.client_exceptions.ServerDisconnectedError:
                        print('链接失败 重试(资源)')
                    except asyncio.exceptions.TimeoutError:
                        print('超时重试(资源)')
                    except aiohttp.client_exceptions.ClientPayloadError:
                        print('客户端负载出错(资源)')
                    except:
                        traceback.print_exc()
            if run_ == True:
                while True:
                    try:
                        print(pool_3)
                        pool.remove(pool_3)
                        print(len(pool))
                        break
                    except UnboundLocalError:
                        break
                    except:
                        traceback.print_exc()
                        # print(pool)
                        break


class D_MC_Z(QThread):
    sinOut_start = pyqtSignal()
    sinOut_ok = pyqtSignal()

    def __init__(self, l, file, MC, G_D_Y):
        """下载jar文件"""
        self.l = l
        self.file = file
        self.MC = MC
        self.G_D_Y = G_D_Y
        super(D_MC_Z, self).__init__()

    def run(self):
        shal = self.l['sha1']
        size = self.l['size']
        url_1 = self.l['url']

        if self.G_D_Y != 'MC':
            if self.G_D_Y == 'MCBBS':
                print(str(url_1) + 'asdaksdnkaskdlnsdlknasl')
                try:
                    url = 'http://download.mcbbs.net/' + url_1.split('https://launcher.mojang.com/')[1]
                except IndexError:
                    url = 'http://download.mcbbs.net/' + url_1.split('https://piston-data.mojang.com/')[1]
            else:
                try:
                    url = 'http://bmclapi2.bangbang93.com/' + url_1.split('https://launcher.mojang.com/')[1]
                except IndexError:
                    url = 'http://bmclapi2.bangbang93.com/' + url_1.split('https://piston-data.mojang.com/')[1]
        else:
            url = url_1

        self.sinOut_start.emit()
        MOS_Downloader.Downloader(url, 40, self.file).run()
        self.sinOut_ok.emit()

        print('Jar文件下载完成')


class D_MC_YL(QThread):
    sinOut_size = pyqtSignal(int)
    sinOut_j = pyqtSignal()
    sinOut_s = pyqtSignal(int)

    def __init__(self, u_get_json, Game_Current_File, url_q_l, timeout):
        """下载依赖库文件"""
        self.u_get_json = u_get_json
        self.Game_Current_File = Game_Current_File
        self.url_q_l = url_q_l
        self.timeout = timeout
        super(D_MC_YL, self).__init__()

    def run(self):
        # 遍历json中的资源文件部分
        a = self.u_get_json['libraries']
        global pool_2, run_
        if run_ == True:
            a = self.u_get_json['libraries']
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
                    url_ = self.url_q_l + url.split('https://libraries.minecraft.net/')[1]
                    c = [url, path, path_q, size]
                    pool_2.append(c)
                    self.sinOut_size.emit(size)

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
                        self.sinOut_size.emit(size)

                    except KeyError:
                        s = system_h()
                        c = ['natives-windows', 'natives-osx', 'natives-macos', 'natives-linux']
                        if s == 'win32' or 'cygwin':
                            sy = ['natives-windows']
                        elif s == 'darwin':
                            sy = ['natives-osx', 'natives-macos']
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
                                self.sinOut_size.emit(size)

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
                                self.sinOut_size.emit(size)

                            path_1 = a_1['artifact']['path']
                            sha1 = a_1['artifact']['sha1']
                            size = a_1['artifact']['size']
                            url = a_1['artifact']['url']

                            path = os.path.join(self.Game_Current_File, 'libraries', path_1)
                            path_q = path.split(os.path.basename(path))[0]
                            c = [url, path, path_q, size]
                            pool_2.append(c)
                            self.sinOut_size.emit(size)

            self.a_len = int(len(pool_2))
            self.a_len_s_1 = 2  # 每个协程任务量
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
            global run_
            if run_ == True:
                self.a = []
                s = 0
                global pool_2
                while self.a_len_1:
                    s += 1
                    self.a_len_s_2 += self.a_len_s_1
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

    async def D_X_Start(self, a):
        """创建"""
        try:
            self.time_1 = time.perf_counter()
            print(a)
            await asyncio.wait(a)
        except:
            traceback.print_exc()

    async def D_X(self, pool_3):
        """下载"""
        try:
            global pool_2, run_
            header = {
                'Proxy-Connection': 'keep-alive','User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}  # 伪装浏览器
            if run_ == True:
                for pool_4 in pool_3:
                    print(pool_4[0])
                    while True:
                        try:
                            os.makedirs(pool_4[2], exist_ok=True)
                            if run_ == True:
                                async with aiohttp.ClientSession(timeout = aiohttp.ClientTimeout(connect=20)) as session:
                                    if run_ == True:
                                        async with session.get(pool_4[0], headers=header, ssl=False) as resp:
                                            if run_ == True:
                                                with open(pool_4[1], 'wb') as fd:
                                                    # iter_chunked() 设置每次保存文件内容大小，单位bytes
                                                    if run_ == True:
                                                        async for chunk in resp.content.iter_chunked(10240000000):
                                                            fd.write(chunk)
                                                    else:
                                                        break
                                            else:
                                                break
                                    else:
                                        break
                            else:
                                break
                            self.sinOut_j.emit()
                            self.sinOut_s.emit(pool_4[3])
                            break
                        except aiohttp.client_exceptions.ServerDisconnectedError:
                            print('链接失败 重试(依赖)')
                        except OSError:
                            print('存储异常 重试(依赖)')
                        except asyncio.exceptions.TimeoutError:
                            print('超时重试(依赖)')
                        except aiohttp.client_exceptions.ClientPayloadError:
                            print('客户端负载出错(依赖)')
                        except:
                            traceback.print_exc()
                    if run_ == True:
                        while True:
                            try:
                                pool_2.remove(pool_4)
                                print(str(len(pool_2)) + 'pppppp')
                                print(pool_2)
                                break
                            except UnboundLocalError:
                                break
                            except:
                                traceback.print_exc()
                                # print(pool)
                                break
        except:
            traceback.print_exc()


class D_MC_F_D(QThread):
    sinOut_start = pyqtSignal()
    sinOut_ok = pyqtSignal()
    def __init__(self,file, MC_file,MC, G_D_Y, f_v,json, Game_Current_File, MOS_File):
        super(D_MC_F_D, self).__init__()
        self.file = file
        self.MC_File = MC_file  # MC文件夹目录
        self.MC = MC
        self.G_D_Y = G_D_Y
        self.F_V = f_v
        self.Json = json
        self.Game_Current_File = Game_Current_File
        self.MOS_File = MOS_File
        global pool_f
    def run(self):
        for json_2 in self.Json:
            if json_2['version'] == self.F_V:
                url = 'http://bmclapi2.bangbang93.com/maven/net/minecraftforge/forge/' + self.MC + '-' + self.F_V + '/forge-' + self.MC + '-' + self.F_V + '-' + 'installer.jar'
                print(url)
                break
        file_q = os.path.join(self.MC_File,'MOS_Cache',str(time.time()))
        file_d = os.path.join(file_q,'F.jar')
        os.makedirs(file_q, exist_ok=True)
        print('fffffffffffffffffffffffffffffffffffffff')
        MOS_Downloader.Downloader(url, 3, file_d).run()
        print('okokokokok')
        f = zipfile.ZipFile(file_d, 'r')
        path_j = os.path.join(file_q,'F')
        for file in f.namelist():
            f.extract(file, path_j)
        print('zip-ok')
        zip_path_q = os.path.join(file_q,'F')
        json_path = os.path.join(zip_path_q,'version.json')
        with open(json_path,'r',encoding='utf-8') as f:
            v_json = json.load(f)
        v_json_libraries = v_json['libraries']

        for v_json_libraries_1 in v_json_libraries:
            v_json_libraries_2 = v_json_libraries_1['downloads']['artifact']
            url = v_json_libraries_2['url']
            if url != '':
                path_1 = v_json_libraries_2['path']
                path = os.path.join(self.Game_Current_File, 'libraries', path_1)
                path_q = path.split(os.path.basename(path))[0]
                size = v_json_libraries_2['size']
                v_json_libraries_3 = [url,path,path_q,size]
                print(v_json_libraries_3)
                pool_f.append(v_json_libraries_3)

        # 2号json(install_profile.json)
        json_path = os.path.join(zip_path_q, 'install_profile.json')
        with open(json_path,'r',encoding='utf-8') as f:
            v_json = json.load(f)
        for v_json_libraries_1 in v_json_libraries:
            v_json_libraries_2 = v_json_libraries_1['downloads']['artifact']
            url = v_json_libraries_2['url']
            if url != '':
                path_1 = v_json_libraries_2['path']
                path = os.path.join(self.Game_Current_File, 'libraries', path_1)
                path_q = path.split(os.path.basename(path))[0]
                size = v_json_libraries_2['size']
                v_json_libraries_3 = [url,path,path_q,size]
                print(v_json_libraries_3)
                pool_f.append(v_json_libraries_3)

        self.a_len = int(len(pool_f))
        self.a_len_s_1 = 1  # 每个协程任务量
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

        jar_f_iniatll_path = os.path.join(self.MOS_File,'.MOS','Forge_install',;'install.jar')
        if os.path.exists(jar_f_iniatll_path):
            #如果文件存在
            pass
        else:
            url = ''


    async def D_R(self):
        try:
            global run_
            if run_ == True:
                self.a = []
                s = 0
                global pool_f
                print(pool_f)
                while self.a_len_1:
                    s += 1
                    self.a_len_s_2 += self.a_len_s_1
                    if self.a_len - self.a_len_s_2 < self.a_len_s_1:
                        pool_3 = pool_f[self.a_len_s_2:]
                        self.a.append(self.D_X(pool_3))
                        print(str(pool_3) + 'vvvvvvv')
                        break
                    else:
                        pool_3 = pool_f[self.a_len_s_2:self.a_len_s_2 + self.a_len_s_1]
                        self.a.append(asyncio.ensure_future(self.D_X(pool_3)))
                        print(str(self.a_len_s_2) + ' : ' + str(self.a_len_s_2 + self.a_len_s_1) + 'F-L')

                print(self.a)
                await asyncio.wait([self.D_X_Start(self.a)])

                self.time_2 = time.perf_counter()
                print(self.time_2 - self.time_1)
        except:
            traceback.print_exc()


    async def D_X_Start(self, a):
        """创建"""
        try:
            self.time_1 = time.perf_counter()
            print(a)
            await asyncio.wait(a)
        except:
            traceback.print_exc()

    async def D_X(self, pool_3):
        """下载"""
        try:
            global pool_f, run_
            header = {
                'Proxy-Connection': 'keep-alive','User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}  # 伪装浏览器
            if run_ == True:
                for pool_4 in pool_3:
                    print(pool_3)
                    print(str(pool_4[0]) + 'ppppppppppppplllllllllllll')
                    while True:
                        try:
                            os.makedirs(pool_4[2], exist_ok=True)
                            if run_ == True:
                                async with aiohttp.ClientSession(timeout = aiohttp.ClientTimeout(connect=20)) as session:
                                    if run_ == True:
                                        async with session.get(pool_4[0], headers=header, ssl=False) as resp:
                                            if run_ == True:
                                                with open(pool_4[1], 'wb') as fd:
                                                    # iter_chunked() 设置每次保存文件内容大小，单位bytes
                                                    if run_ == True:
                                                        async for chunk in resp.content.iter_chunked(10240000000):
                                                            fd.write(chunk)
                                                    else:
                                                        break
                                            else:
                                                break
                                    else:
                                        break
                            else:
                                break
                            #self.sinOut_j.emit()
                            #self.sinOut_s.emit(pool_4[3])
                            break
                        except aiohttp.client_exceptions.ServerDisconnectedError:
                            print('链接失败 重试(F-依赖)')
                        except OSError:
                            print('存储异常 重试(F-依赖)')
                        except asyncio.exceptions.TimeoutError:
                            print('超时重试(F-依赖)')
                        except aiohttp.client_exceptions.ClientPayloadError:
                            print('客户端负载出错(F-依赖)')
                        except:
                            traceback.print_exc()
                    if run_ == True:
                        while True:
                            try:
                                pool_f.remove(pool_4)
                                print(str(len(pool_2)) + ' F-L')
                                print(pool_2)
                                break
                            except UnboundLocalError:
                                break
                            except:
                                traceback.print_exc()
                                # print(pool)
                                break
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
