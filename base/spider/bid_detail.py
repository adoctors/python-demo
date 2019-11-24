import sys
import re
import urllib.request
import urllib.error
import gzip
import time
from http import cookiejar
from bs4 import BeautifulSoup as bs
from threading import Timer
import random
sys.path.append('../config')
from mongodb import get_detail_header
from mongodb import coll_sm
from mongodb import coll_dtw
from mongodb import coll_jz
from mongodb import coll_ly


def get_str_money(strs):
  conditions = [
    '(成交|合同|中标|总中标)金额(：|:)',
    '(（\d）|\d、)成交金额(：|:)',
    '(（\d）|\d、)成交 金额(：|:)',
    '成交 金额(：|:)',
    '中标(金额（人民币）|\(成交\)金额)(：|:)',
    '合同总金|总成交金额：',
    '.{1,5}采购项目预算金额（元）：',
    '.{1,5}中标金额：',
    '.{1,15}金额：',
  ]

  for item in conditions:
    if re.match(item,strs):
      return re.sub(item,'',strs,1).strip()


def update_coll(query,coll_name,key,val):
  coll = coll_name.find_one(query)
  coll[key] = val
  coll_name.update_one(query,{'$set':coll})

def get_detail(url,cookie,coll_name,list_url):
  try:
    header = get_detail_header(url,cookie,list_url)
    response = urllib.request.Request(url, headers=header )
    html = urllib.request.urlopen(response)
    content = html.read()
    print(cookiejar.CookieJar())
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

      tag_list = ['p','div','li','tr','td']
      for tag in tag_list:
        for item in soup.select(tag):
          # print(item.string)
          if item.string and get_str_money(item.string):
            query = {'detail_url':url}
            update_coll(query,coll_name,key='hit_money',val=get_str_money(item.string))
            update_coll(query,coll_name,key='hit_money_res',val=item.string)
            print(get_str_money(item.string))


cookie = '__jsluid_h=43a8c9faf4062503f3295006bb521b09; client_login_info=a954Hx4YlHjUhyzlfx.e51vrNsJlRo61upp9wt1xWdl.OBBOMOgeJerCi1JknOwoSVyHyndVc1Di2QPPPw5UKH5u52nJ; Hm_lvt_93352b09c212b481a8db685016fa5723=1574430627,1574433222; Hm_lpvt_93352b09c212b481a8db685016fa5723=1574607514; clientlogin=fcc0YfSFvkFXg4j8uJTPq2SJCE3laBUPsEHJJkNDEIw8M9HvtZrC_yd8lfJGkD5qZkU7SwC3lX2D2jc9gka4Krd7oYivN0wavzuNuZEuBs62JHEB_cBq5g; __jsl_clearance=1574610624.558|0|vylPk13d3tbOulruFnTqxhfCDss%3D'
coll_name = coll_jz




i=1
skips = 0
limits = 50
n=1



def run():
  global i
  global n
  global skips
  global limits
  global limits

  for item in coll_name.find().skip(skips).limit(limits):
    start_time = time.time()
    url = item['detail_url']
    list_url = item['list_url']
    print(url)

    t = Timer(n+random.randint(2,5), get_detail,args=(url,cookie,coll_name,list_url,))
    if i+limits > coll_name.count():
      t.cancel()
    t.start()#定时执行
    # get_detail(url,cookie,coll_name,list_url)
    
    print('第%d个页面，耗时：%d' % (i,float(time.time()) - start_time))
    i+=1
    n+=1
    skips+=1
  


run()


