python crawler
==============

# 爬虫实践 #


## 库 ##
- `Beautifulsoup`
- `Requests`
- `os`

### Requests ###
`Requests`是一个python的http库

尝试获取某个页面
`r=requests.get(<url>)`
建立了一个名为`r`的`Response`对象

发送一个`post`请求
`r = requests.post('http://httpbin.org/post', data = {'key':'value'})`

传递url参数
```
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
```

读取响应内容
```
r.text
r.encoding
```

二进制响应内容
`r.content`

定制请求头
```
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
```

响应状态码
`r.status_code`

### Beautifulsoup ###
这是一个从`HTML`文件中提取数据的`python`库

导入
`from bs4 import BeautifulSoup`

建立对象
`soup = BeautifulSoup(html_doc,'lxml')`

`Beautiful Soup`将复杂HTML文档转换成一个复杂的树形结构,
每个节点都是`Python`对象,所有对象可以归纳为4种:
- Tag
- NavigableString 
- BeautifulSoup 
- Comment

#### Tag ####
`Tag`对象与`HTML`中的`Tag`一样

获取`tag`的名字
`tag.name`

`Tag`的属性操作方法与字典一致
`tag['class']`
tag的属性可以被添加,删除或修改

#### 遍历文档树 ####
得到所有的`<a>`标签
`soup.find_all('a')`

得到所有的`<a>`标签，并且`class='sister'`的标签
`soup.find_all("a", class_="sister")`

## 代码 ##
<a href="http://www.netbian.com/">目标网站</a>

建立网页的对象
并且提取图片的地址

```
def ana_web(url,header):
    response = requests.get(url,headers=header)
    response.encoding = 'gbk'
    soup = BeautifulSoup(response.text,'lxml')
    tags = soup.find_all('img')
    return tags
```

运用`os`库建立文件夹
```
def setDir():
    print("你正处于的路径：")
    print(os.path.abspath('.'))
    now_path = os.path.abspath('.')
    print('\n')
    dir_name = input('请输入你想保存的文件夹名称')
    os.mkdir(dir_name)
    os.chdir(now_path+'/'+dir_name)

```

下载图片并且保存到刚刚的文件夹中
```
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
```


