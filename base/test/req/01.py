# 一般的简单方式

# 使用同步方法
# 一般方法虽然思路简单，容易实现，但效率不高，耗时长

import requests
import time

def req_data(url):
   # 单个请求开始时间
  req_start_time = time.time()
  res = requests.get(url)
  print(url + '结束。 结果：' + res.text + '。 耗时：' + str(time.time() - req_start_time))


# 开始时间
start_time = time.time()

for i in range(1,501):
  url = 'http://127.0.0.1:7001/other/req_list/%d' % i
  req_data(url) 

print('全部结束，总耗时：' + str(time.time() - start_time))
# 总耗时：22.513701677322388

# 因为同步，顺序固定
# http://127.0.0.1:7001/other/req_list/1结束。 结果：--- res_con( 1 )---。 耗时：0.048836469650268555
# http://127.0.0.1:7001/other/req_list/2结束。 结果：--- res_con( 2 )---。 耗时：0.038895606994628906
# http://127.0.0.1:7001/other/req_list/3结束。 结果：--- res_con( 3 )---。 耗时：0.039893150329589844
# http://127.0.0.1:7001/other/req_list/4结束。 结果：--- res_con( 4 )---。 耗时：0.03789854049682617
# http://127.0.0.1:7001/other/req_list/5结束。 结果：--- res_con( 5 )---。 耗时：0.0359039306640625
# http://127.0.0.1:7001/other/req_list/6结束。 结果：--- res_con( 6 )---。 耗时：0.037897586822509766
# http://127.0.0.1:7001/other/req_list/7结束。 结果：--- res_con( 7 )---。 耗时：0.03590273857116699
# http://127.0.0.1:7001/other/req_list/8结束。 结果：--- res_con( 8 )---。 耗时：0.03590583801269531
# http://127.0.0.1:7001/other/req_list/9结束。 结果：--- res_con( 9 )---。 耗时：0.046872854232788086

# 假设单个接口延时200ms返回

# http://127.0.0.1:7001/other/req_list/1结束。 结果：--- res_con( 1 )---。 耗时：0.26329565048217773
# http://127.0.0.1:7001/other/req_list/2结束。 结果：--- res_con( 2 )---。 耗时：0.24135708808898926
# http://127.0.0.1:7001/other/req_list/3结束。 结果：--- res_con( 3 )---。 耗时：0.24733662605285645
# http://127.0.0.1:7001/other/req_list/4结束。 结果：--- res_con( 4 )---。 耗时：0.23640131950378418

# 总耗时：123.99135088920593