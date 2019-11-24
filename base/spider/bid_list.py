import sys
import urllib.request
import urllib.error
import gzip
import time
from bs4 import BeautifulSoup as bs
sys.path.append('../config')
from mongodb import getHeader
from mongodb import coll_sm
from mongodb import coll_dtw
from mongodb import coll_jz
from mongodb import coll_ly

def get_list(url,cookie,company_name,coll_name):
  try:
    header = getHeader(url,cookie)
    response = urllib.request.Request(url, headers=header )
    html = urllib.request.urlopen(response)
    content = html.read()
    result = gzip.decompress(content).decode("utf-8")
    soup = bs(result,'html.parser')

  except urllib.error.URLError as e:
      if hasattr(e, 'reason'):
          print('错误原因是' + str(e))
  except urllib.error.HTTPError as e:
      if hasattr(e, 'code'):
          print('错误状态码是' + str(e.code))
  else:
      print('请求成功通过。')
      for item in soup.select('.ul_list li'):
        area = item.select('span')[1].string
        title = item.select('a')[0].string
        detail_url = item.select('a')[0].get('href')
        time = item.select('b')[0].string
        data= {
          'company_name': company_name,
          'area': area,
          'project_name': title,
          'hit_time': time,
          'list_url': url,
          'detail_url':detail_url
        }

        # print(data)
        coll_name.insert_one(data)

# 获取列表




# get_list(url)

cookie = '__jsluid_h=43a8c9faf4062503f3295006bb521b09; client_login_info=a954Hx4YlHjUhyzlfx.e51vrNsJlRo61upp9wt1xWdl.OBBOMOgeJerCi1JknOwoSVyHyndVc1Di2QPPPw5UKH5u52nJ; Hm_lvt_93352b09c212b481a8db685016fa5723=1574430627,1574433222; __jsl_clearance=1574586309.14|0|7iAa5JbHZ%2FA4CeNIoO9vCvuzdy0%3D; Hm_lpvt_93352b09c212b481a8db685016fa5723=1574589133; clientlogin=0df8NDjx4QBNj8uPBxqZqlsvs0PLwErXMno3spk8JKn1hsg9QrQEd_W9JTrs_ceXfpMgcBgiaa3Il3ruW6oyEWqcbCyLrk2lbgsVknf7dUN8PD4y2pVwog'
company_name = '联奕科技有限公司'
coll_name = coll_ly

for i in range(1,55):
  start_time = time.time()
  # url = url = 'http://www.chinabidding.cc/search/index.html?page='+str(i)+'&keyword=南京迪塔维数据技术有限公司&h_lx=11&h_province=0&vague=0&date=365&search_field=0'
  url = url = 'http://www.chinabidding.cc/search/index.html?page='+str(i)+'&keyword=%E8%81%94%E5%A5%95%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&h_lx=11&h_province=0&vague=0&date=365&search_field=0'
  get_list(url,cookie,company_name,coll_name)
  print('第%d个页面，耗时：%d' % (i,float(time.time()) - start_time))
