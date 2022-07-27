import requests
import shutil
 
'''不推荐用这个写法'''

def download_file(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
 
    return local_filename

#url = 'https://mirrors.tuna.tsinghua.edu.cn/pypi/web/packages/0d/ea/f936c14b6e886221e53354e1992d0c4e0eb9566fcc70201047bb664ce777/tensorflow-2.3.1-cp37-cp37m-macosx_10_9_x86_64.whl#sha256=1f72edee9d2e8861edbb9e082608fd21de7113580b3fdaa4e194b472c2e196d0'
#url = 'https://download.visualstudio.microsoft.com/download/pr/cc04076c-d188-4c20-9b4f-89be06f1a39c/32da746ef46fbeedb4f609b67cb451c3/windowsdesktop-runtime-6.0.6-win-x86.exe'
#url = 'https://visualstudio.microsoft.com/aabf4bb0-b5f4-4e42-8aae-6ad17ec46db2'
#url = 'https://file.skyworldstudio.top/d/SoftwareRelease/MOS/Publish/2.0.4-alpha/2.0.4-alpha-win.zip'
url = 'https://download.visualstudio.microsoft.com/download/pr/ca7c7580-dd29-42d8-a0b1-3223e61f1623/b38739f51587806a5751419435d6c4ad/visualstudioformacinstaller-17.0.4.5.dmg'

download_file(url)