# 一个普通的爬虫测试

import time
import requests
from bs4 import BeautifulSoup as bs

import sys
sys.path.append('../../config') # 模块所在目录加入到搜素目录中

from mongodb import coll_qiubai


def get_page_list(url):
  res = requests.get(url)
  html = res.content                # 此时结果乱码
  result = bs(html,'html.parser')   # 此时可获得utf8

  for item in result.select('.ui-module .mala-text'):
    title = item.select('.mtitle a')[0].text      
    # title = item.select('.mtitle a')[0].string    # BeautifulSoup的方法
    img_src = item.select('div a img')[0].get('src')
    data = {
      'web_url':url,
      'img_src': img_src,
      'title': title
    }
    coll_qiubai.insert_one(data)
    print(title, img_src, end='\n\n',)

# url = 'http://www.qiubaichengnian.com/index_1.html'
url = 'http://www.qiubaichengnian.com/index.html'

# get_page_list(url)

for i in range(1,11):
  start_time = time.time()
  target_url = 'http://www.qiubaichengnian.com/index_%d.html' % i
  get_page_list(target_url)

  print('第%d个页面，耗时：%d' % (i,float(time.time()) - start_time))


