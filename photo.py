import json
import requests
from bs4 import BeautifulSoup
import os

def ana_web(url,header):
    response = requests.get(url,headers=header)
    response.encoding = 'gbk'
    soup = BeautifulSoup(response.text,'lxml')
    tags = soup.find_all('img')
    return tags


def setDir():
    print("你正处于的路径：")
    print('\n')
    os.chdir('/Users/zerrari/Pictures/wallpaper')
    print(os.path.abspath('.'))

def check_img(input,check):
    result = check in input
    return result
    
def download_img(tags,nums,flag):
    for tag in tags:
        print(tag.get('data-src'))
        if tag.get('data-src') is None:
            continue
        else:
            img = requests.get(tag.get('data-src')).content
            with open('index' + str(flag) + '_' + str(nums)+'.jpg','wb') as f:
                f.write(img)
                f.close()
                nums = nums + 1

            
target_url_p1 = 'https://wallhaven.cc/hot?page='
target_header = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 FS'}

flag = 1
index = int(input('请输入：\n'))
nums = 1
setDir()

while flag <= index:
    target_url = target_url_p1 + str(flag)
    tags = ana_web(target_url,target_header)
    download_img(tags,nums,flag)
    nums = 1
    flag = flag + 1


    



