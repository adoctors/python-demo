# 并发方式

# 并发方法使用多线程来加速一般方法，
# 我们使用的并发模块为concurrent.futures模块，
# 设置多线程的个数为5个（实际是否能达到，视计算机而定）

import requests
import time
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED

def req_data(url):
   # 单个请求开始时间
  req_start_time = time.time()
  res = requests.get(url)
  print(url + '结束。 结果：' + res.text + '。 耗时：' + str(time.time() - req_start_time))


# 开始时间
start_time = time.time()

urls = []
for i in range(1,501):
  url = 'http://127.0.0.1:7001/other/req_list/%d' % i
  urls.append(url)

# 利用并发加速爬取
executor = ThreadPoolExecutor(max_workers=5)
# submit()的参数： 第一个为函数， 之后为该函数的传入参数，允许有多个
future_tasks = [executor.submit(req_data, url) for url in urls]
# 等待所有的线程完成，才进入后续的执行
wait(future_tasks, return_when=ALL_COMPLETED)

print('全部结束，总耗时：' + str(time.time() - start_time))

# 总耗时：14.856170892715454

# 顺序变了

# http://127.0.0.1:7001/other/req_list/1结束。 结果：--- res_con( 1 )---。 耗时：0.1515953540802002
# http://127.0.0.1:7001/other/req_list/3结束。 结果：--- res_con( 3 )---。 耗时：0.151594877243042
# http://127.0.0.1:7001/other/req_list/4结束。 结果：--- res_con( 4 )---。 耗时：0.1525897979736328
# http://127.0.0.1:7001/other/req_list/5结束。 结果：--- res_con( 5 )---。 耗时：0.1525897979736328
# http://127.0.0.1:7001/other/req_list/2结束。 结果：--- res_con( 2 )---。 耗时：0.15358710289001465
# http://127.0.0.1:7001/other/req_list/6结束。 结果：--- res_con( 6 )---。 耗时：0.1156916618347168
# http://127.0.0.1:7001/other/req_list/7结束。 结果：--- res_con( 7 )---。 耗时：0.11668944358825684
# http://127.0.0.1:7001/other/req_list/8结束。 结果：--- res_con( 8 )---。 耗时：0.11768651008605957
# http://127.0.0.1:7001/other/req_list/10结束。 结果：--- res_con( 10 )---。 耗时：0.11469411849975586
# http://127.0.0.1:7001/other/req_list/9结束。 结果：--- res_con( 9 )---。 耗时：0.11668777465820312
# http://127.0.0.1:7001/other/req_list/13结束。 结果：--- res_con( 13 )---。 耗时：0.135636568069458
# http://127.0.0.1:7001/other/req_list/11结束。 结果：--- res_con( 11 )---。 耗时：0.1436154842376709
# http://127.0.0.1:7001/other/req_list/15结束。 结果：--- res_con( 15 )---。 耗时：0.1386280059814453
# http://127.0.0.1:7001/other/req_list/12结束。 结果：--- res_con( 12 )---。 耗时：0.1436145305633545
# http://127.0.0.1:7001/other/req_list/14结束。 结果：--- res_con( 14 )---。 耗时：0.14162063598632812
# http://127.0.0.1:7001/other/req_list/16结束。 结果：--- res_con( 16 )---。 耗时：0.12765908241271973
# http://127.0.0.1:7001/other/req_list/18结束。 结果：--- res_con( 18 )---。 耗时：0.12167501449584961

# 假设单个接口延时200ms返回

# http://127.0.0.1:7001/other/req_list/2结束。 结果：--- res_con( 2 )---。 耗时：0.3171870708465576
# http://127.0.0.1:7001/other/req_list/4结束。 结果：--- res_con( 4 )---。 耗时：0.3171532154083252
# http://127.0.0.1:7001/other/req_list/1结束。 结果：--- res_con( 1 )---。 耗时：0.3181488513946533
# http://127.0.0.1:7001/other/req_list/5结束。 结果：--- res_con( 5 )---。 耗时：0.32117533683776855
# http://127.0.0.1:7001/other/req_list/3结束。 结果：--- res_con( 3 )---。 耗时：0.32117533683776855
# http://127.0.0.1:7001/other/req_list/6结束。 结果：--- res_con( 6 )---。 耗时：0.30315446853637695

# 总耗时：36.90632963180542