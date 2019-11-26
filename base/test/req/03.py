# 异步方式

# 异步方法在爬虫中是有效的速度提升手段，
# 使用aiohttp可以异步地处理HTTP请求，使用asyncio可以实现异步IO，
# 需要注意的是，aiohttp只支持3.5.3以后的Python版本

import time
import aiohttp
import asyncio

async def fetch(session,url):
  async with session.get(url) as response:
    return await response.text(encoding='gb18030')

async def run(url):
  print(url + '开始-----')
  req_start_time = time.time()
  async with aiohttp.ClientSession() as session:
    res = await fetch(session, url)
    print(url + '结束。 结果：' + res + '。 耗时：' + str(time.time() - req_start_time))


# 开始时间
start_time = time.time()

urls = []
for i in range(1,501):
  url = 'http://127.0.0.1:7001/other/req_list/%d' % i
  urls.append(url)


# 利用asyncio模块进行异步IO处理
loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(run(url)) for url in urls]
tasks = asyncio.gather(*tasks)
loop.run_until_complete(tasks)

print('全部结束，总耗时：' + str(time.time() - start_time))


# 全部结束，总耗时：16.77814269065857

# http://127.0.0.1:7001/other/req_list/363结束。 结果：--- res_con( 363 )---。 耗时：16.11192560195923
# http://127.0.0.1:7001/other/req_list/110结束。 结果：--- res_con( 110 )---。 耗时：16.227615118026733
# http://127.0.0.1:7001/other/req_list/364结束。 结果：--- res_con( 364 )---。 耗时：16.11292266845703
# http://127.0.0.1:7001/other/req_list/111结束。 结果：--- res_con( 111 )---。 耗时：16.229609489440918
# http://127.0.0.1:7001/other/req_list/365结束。 结果：--- res_con( 365 )---。 耗时：16.113919496536255

# 假设单个接口延时200ms返回

# http://127.0.0.1:7001/other/req_list/363结束。 结果：--- res_con( 363 )---。 耗时：17.267564296722412
# http://127.0.0.1:7001/other/req_list/102结束。 结果：--- res_con( 102 )---。 耗时：17.407190799713135
# http://127.0.0.1:7001/other/req_list/364结束。 结果：--- res_con( 364 )---。 耗时：17.269558668136597
# http://127.0.0.1:7001/other/req_list/103结束。 结果：--- res_con( 103 )---。 耗时：17.40818762779236
# http://127.0.0.1:7001/other/req_list/104结束。 结果：--- res_con( 104 )---。 耗时：17.40918493270874
# http://127.0.0.1:7001/other/req_list/365结束。 结果：--- res_con( 365 )---。 耗时：17.27155303955078

# 总耗时：17.819050550460815


# 小结
# 500次请求

# 一般
# 不延时      总耗时：19.72829842567444
# 延时200ms   总耗时：126.0974280834198
# 顺序        保持

# 并发
# 不延时      总耗时：13.159818172454834
# 延时200ms   总耗时：34.75210666656494
# 顺序        不保持

# 异步
# 不延时      总耗时：17.416436910629272
# 延时200ms   总耗时：17.31770086288452
# 顺序        不保持
