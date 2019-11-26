# 测试基于协程的异步爬虫程序

import time
import aiohttp
import asyncio


# 内部具体逻辑
async def fetch(session,url):
  async with session.get(url) as response:
    return await response.text(encoding='gb18030')

async def run(url):
  with(await sem):
    print(url + '开始-----')
    req_start_time = time.time()
    # async with是异步上下文管理器
    async with aiohttp.ClientSession() as session: # 获取session
      res = await fetch(session, url)
      print(url + '结束。 结果：' + res + '。 耗时：' + str(time.time() - req_start_time))


sem = asyncio.Semaphore(10) # 信号量，控制协程数，防止爬的过快

# 开始时间
start_time = time.time()

urls = []
for i in range(1,501):
  url = 'http://127.0.0.1:7001/other/req_list/%d' % i
  urls.append(url)


loop = asyncio.get_event_loop()   # 获取事件循环
tasks = [run(url) for url in urls]  # 把所有任务放到一个列表中
loop.run_until_complete(asyncio.wait(tasks)) # 激活协程
loop.close()  # 关闭事件循环

print('全部结束，总耗时：' + str(time.time() - start_time))


# 延时200ms,全部结束，总耗时：16.77814269065857

# http://127.0.0.1:7001/other/req_list/373开始-----
# http://127.0.0.1:7001/other/req_list/466开始-----
# http://127.0.0.1:7001/other/req_list/374开始-----
# http://127.0.0.1:7001/other/req_list/467开始-----
# http://127.0.0.1:7001/other/req_list/375开始-----
# http://127.0.0.1:7001/other/req_list/468开始-----
# http://127.0.0.1:7001/other/req_list/376开始-----
# http://127.0.0.1:7001/other/req_list/469开始-----
# http://127.0.0.1:7001/other/req_list/377开始-----
# http://127.0.0.1:7001/other/req_list/470开始-----
# http://127.0.0.1:7001/other/req_list/373结束。 结果：--- res_con( 373 )---。 耗时：0.5714821815490723
# http://127.0.0.1:7001/other/req_list/378开始-----
# http://127.0.0.1:7001/other/req_list/375结束。 结果：--- res_con( 375 )---。 耗时：0.5734684467315674
# http://127.0.0.1:7001/other/req_list/376结束。 结果：--- res_con( 376 )---。 耗时：0.5744731426239014
# http://127.0.0.1:7001/other/req_list/470结束。 结果：--- res_con( 470 )---。 耗时：0.5754668712615967
# http://127.0.0.1:7001/other/req_list/377结束。 结果：--- res_con( 377 )---。 耗时：0.5784587860107422
# http://127.0.0.1:7001/other/req_list/374结束。 结果：--- res_con( 374 )---。 耗时：0.5834488868713379
# http://127.0.0.1:7001/other/req_list/471开始-----
# http://127.0.0.1:7001/other/req_list/379开始-----
# http://127.0.0.1:7001/other/req_list/472开始-----
# http://127.0.0.1:7001/other/req_list/380开始-----
# http://127.0.0.1:7001/other/req_list/473开始-----
# http://127.0.0.1:7001/other/req_list/467结束。 结果：--- res_con( 467 )---。 耗时：0.6043915748596191
# http://127.0.0.1:7001/other/req_list/468结束。 结果：--- res_con( 468 )---。 耗时：0.6063857078552246
# http://127.0.0.1:7001/other/req_list/469结束。 结果：--- res_con( 469 )---。 耗时：0.609379768371582
# http://127.0.0.1:7001/other/req_list/466结束。 结果：--- res_con( 466 )---。 耗时：0.617351770401001



