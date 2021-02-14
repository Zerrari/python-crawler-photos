import json
import requests
from bs4 import BeautifulSoup
import os

target_url = 'http://www.netbian.com/'
target_header = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 FS'}

def ana_web(url,header):
    response = requests.get(url,headers=header)
    response.encoding = 'gbk'
    soup = BeautifulSoup(response.text,'lxml')
    tags = soup.find_all('img')
    return tags


def setDir():
    print("你正处于的路径：")
    print(os.path.abspath('.'))
    now_path = os.path.abspath('.')
    print('\n')
    dir_name = input('请输入你想保存的文件夹名称')
    os.mkdir(dir_name)
    os.chdir(now_path+'/'+dir_name)

def download_img():
    tags=ana_web(target_url,target_header)
    setDir()
    nums = 0
    for tag in tags:
        nums = nums + 1
        img = requests.get(tag['src']).content
        with open(str(nums)+'.jpg','wb') as f:
            f.write(img)
            f.close()

download_img()

    



