import sys
sys.path.append('../../config')
import requests
import time
from mongodb import coll_req_list

base_url = 'http://127.0.0.1:7001'

# 开始时间
start_time = time.time()


for item in coll_req_list.find():
  # 单个请求开始时间
  req_start_time = time.time()

  url = base_url + item['req_url']
  # print(url)
  res = requests.get(url)
  print(res.text)
  print(url + '结束。 结果：' + res.text + '。 耗时：' + str(time.time() - req_start_time))

print('全部结束，总耗时：' + str(time.time() - start_time))