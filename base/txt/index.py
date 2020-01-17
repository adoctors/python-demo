# 一个普通的爬虫测试

import time
import requests
from bs4 import BeautifulSoup as bs

import sys

url_list = []
url = 'http://www.janpn.com/book/zuiqiangkuangbing2.html'
# file_path = './2292-d.txt'


def writ_cover(path, txt):
    f = open(path, 'w')    # w模式为覆盖
    f.write(txt + '\n')
    f.close()


def writ_append(path, txt):
    f = open(path, 'a', encoding='utf-8')    # a模式为追加
    f.write(txt + '\n')
    f.close()


def read(path):
    # 读取文件
    f = open(path)
    content_txt = f.read()
    f.close()
    return content_txt


def get_detail(url):
    try:
        res = requests.get(url)
        html = res.content                # 此时结果乱码
        result = bs(html, 'html.parser')   # 此时可获得utf8
        return result.select('#htmlContent')[0].text
    except:
        print('--------------------------------发生异常' + url)
        return url


def get_page_list(url):
    file_path = './2293-d.txt'
    res = requests.get(url)
    html = res.content                # 此时结果乱码
    result = bs(html, 'html.parser')   # 此时可获得utf8

    for item in result.select('.panel-chapterlist li'):
        try:
            href = item.select('a')[0].get('href')
            text = item.select('a')[0].text
            # 写入章节名
            print(text)
            writ_append(file_path, str(text) + '\n')
            # 写入章节内容
            detail = get_detail(href)
            print(str(detail))

            writ_append(file_path, str(detail) + '\n')

        except:
            print('写入异常')


get_page_list(url)

# get_detail('http://www.janpn.com/book/138/138590/63422386.html')

# print(read(file_path))
