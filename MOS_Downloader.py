# -*- coding: utf-8 -*-
# @Time  : 2020/5/5 22:18
# @Author: 哦嚯嚯哦
# @File  : test_demo.py
# @tool  : PyCharm

"""
使用python实现百行代码高速下载，同IDM
使用Dowmloader_调用下载
"""
import MOS_UI

"""建议用这个 经过我测试 这个最稳定 经常是最快的"""
import os
import time
import sys
from requests import get,head
from concurrent.futures import ThreadPoolExecutor,wait

j = 0 #进度
w = "0 KB/s - 正在准备下载" #网速
size = 0
pool = ''

#网速获取和 进度获取

def w_h():
    """网速获取"""
    return w

def j_h():
    """进度获取"""
    return j

def s_h():
    """大小获取 没有开始的时候 为0 """
    return size

def stop():
    pool.shutdown(wait=False)

class Downloader():
    def __init__(self, url, nums, file):
        self.url = url      # url链接
        self.num = nums     # 线程数
        self.name = file    # 文件名字(路径)
        self.getSize = 0    # 大小
        self.info = {
            'main': {
                'progress': 0,
                'speed': ''
            },
            'sub': {
                'progress': [0 for i in range(nums)],    # 子线程状态
                'stat': [1 for i in range(nums)]         # 下载状态
            }
        }
        r = head(self.url, allow_redirects=False)  # 禁止自动重定向
        # 状态码显示302则迭代寻找文件
        while True:
            if r.status_code == 302 or 301:
                print(r.headers)

                try:
                    self.url = r.headers['Location']
                except KeyError:
                    print('状态码为' + str(r.status_code) + ' 请求头内无location值 重定向失败')
                    break

                print("此url已重定向至 " + format(self.url))
                r = head(self.url,allow_redirects=False)  # 禁止自动重定向
            else:
                break

        self.size = int(r.headers['Content-Length'])
        global size
        size = self.size
        print('该文件大小为: {} bytes'.format(self.size))

    # ************************************************** #
    def Dowmloader_(url, thread_num, file):
        """
            url=地址 thread_num=线程数量 file=保存路径(要写全)
        """
        down = Downloader(url, thread_num, file)
        a = down.run()
        return a

    # ************************************************** #


    def down(self, start, end, thread_id, chunk_size = 99200):
        raw_start = start
        for _ in range(10):
            try:
                headers = {'User-Agent':'Mozilla/55.0 (Macintosh; Intel Mac OS X 55.55; rv:101.0) Gecko/20100101 Firefox/101.0',
                'Range': 'bytes={}-{}'.format(start, end)}
                r = get(self.url, headers=headers, timeout=10, stream=True)
                print(f"线程{thread_id}连接成功")
                size = 0
                with open(self.name, "rb+") as fp:
                    fp.seek(start)
                    for chunk in r.iter_content(chunk_size=chunk_size):
                        if chunk:
                            self.getSize += chunk_size
                            fp.write(chunk)
                            start += chunk_size
                            size += chunk_size
                            progress = round(size / (end - raw_start) * 100, 2)
                            self.info['sub']['progress'][thread_id - 1] = progress
                            self.info['sub']['stat'][thread_id - 1] = 1
                return
            except Exception as error:
                print(error)
                self.down(start, end, thread_id)
        print(f"{start}-{end}, 下载失败")
        self.info['sub']['start'][thread_id - 1] = 0

    def show(self):
        while True:
            speed = self.getSize
            print(speed)
            time.sleep(0.5)
            speed = int((self.getSize - speed) * 2 / 1024)
            if speed > 1024:
                speed = f"{round(speed / 1024, 2)} MB/s" # round() 方法返回浮点数四舍五入值
            else:
                speed = f"{speed} KB/s"
            progress = round(self.getSize / self.size * 100, 2)
            self.info['main']['progress'] = progress
            self.info['main']['speed'] = speed
            b = self.info['main']
            b_2 = int(b['progress'])
            b_3 = str(b['speed'])
            
            global j,w
            j = b_2
            w = b_3
            print(self.info)

            if progress >= 100:
                print(self.info)
                break
                """
                c = self.info['sub']['progress']
                d = len(c) #计算有多少个
                e = 0 #存储列表中所有值
                for a in c:
                    e += a
                f = e/d
                g = 0
                for a in c:
                    #再次循环 看看每一个值是不是和平均值相等
                    if a == f:
                        g += 1 #如果是就+1
                    else:
                        pass # 如果不是 不做处理
                if g == d:
                    #如果相等的等于 d（值得数量
                    break #打破循环
                else:
                    pass #继续循环
                """

    def run(self):
        # 创建一个要下载的文件
        fp = open(self.name, 'wb')
        print(f"正在初始化下载文件: {self.name}")
        fp.truncate(self.size)
        print(f"文件初始化完成")
        start_time = time.time()
        fp.close()
        part = self.size // self.num
        global pool
        pool = ThreadPoolExecutor(max_workers=self.num + 1)
        futures = []
        for i in range(self.num):
            start = part * i
            if i == self.num - 1:
                end = self.size
            else:
                end = start + part - 1
            futures.append(pool.submit(self.down, start, end, i + 1))
        futures.append(pool.submit(self.show))
        print(f"正在使用{self.num}个线程进行下载...")

        start = time.perf_counter()
        
        wait(futures)
        end_time = time.time()
        speed = int(self.size / 1024 / (end_time - start_time))
        if speed > 1024:
            speed = f"{round(speed / 1024, 2)} M/s"
        else:
            speed = f"{speed} KB/s"
        print(f"{self.name}下载完成，平均速度: {speed}")

        end_time_1 = time.perf_counter()
        print("用时" + str(end_time_1))





if __name__ == '__main__':
    debug = 1           # 测试情况
    if debug:
        #url = 'https://mirrors.tuna.tsinghua.edu.cn/pypi/web/packages/0d/ea/f936c14b6e886221e53354e1992d0c4e0eb9566fcc70201047bb664ce777/tensorflow-2.3.1-cp37-cp37m-macosx_10_9_x86_64.whl#sha256=1f72edee9d2e8861edbb9e082608fd21de7113580b3fdaa4e194b472c2e196d0'
        url = 'https://download.visualstudio.microsoft.com/download/pr/cc04076c-d188-4c20-9b4f-89be06f1a39c/32da746ef46fbeedb4f609b67cb451c3/windowsdesktop-runtime-6.0.6-win-x86.exe'
        #url = 'https://visualstudio.microsoft.com/aabf4bb0-b5f4-4e42-8aae-6ad17ec46db2'
        #url = 'https://file.skyworldstudio.top/d/SoftwareRelease/MOS/Publish/2.0.4-alpha/2.0.4-alpha-win.zip'
        #url = 'https://download.visualstudio.microsoft.com/download/pr/ca7c7580-dd29-42d8-a0b1-3223e61f1623/b38739f51587806a5751419435d6c4ad/visualstudioformacinstaller-17.0.4.5.dmg'
        down = Downloader(url, 8, os.path.basename(url))
    else:
        # 命令行执行方式
        url = sys.argv[1]       # 下载链接
        file = sys.argv[2]      # 默认保存在项目路径下,文件的名字以文件格式结尾
        thread_num = int(sys.argv[3])  # 使用的线程数量
        down = Downloader(url, thread_num, file)
    down.run()

