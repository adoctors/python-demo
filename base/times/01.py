# Python中通过线程实现定时器timer,其使用非常简单

import threading
from datetime import datetime
 
# def fun_timer():
#      print(datetime.now().strftime("%Y-%m-%d  %H:%M:%S"))
#     print('Hello Timer!')
 
# timer = threading.Timer(1, fun_timer)
# timer.start()
# 注意，只输出了一次，程序就结束了

# ---------------------------------------------------------------------

# 循环调用该函数(递归)

def fun_timer():
    print('Hello Timer!')
    print(datetime.now().strftime("%Y-%m-%d  %H:%M:%S"))
    global timer
    timer = threading.Timer(1, fun_timer)
    timer.start()
 
timer = threading.Timer(2, fun_timer)
# 定时器间隔单位是秒，可以是浮点数，如5.5，0.02等
# timer.start()

# threading 模块中的Timer 是一个非阻塞函数，比sleep好一点，


# timer.cancel() 停止定时器

# ---------------------------------------------------------------------

# 循环sleep


import time
# 每n秒执行一次
def timer(n):
    while True:
        print(datetime.now().strftime("%Y-%m-%d  %H:%M:%S"))
        time.sleep(n)

# timer(5)
# 这个方法的缺点是，只能执行固定间隔时间的任务，
# 如果有定时任务就无法完成，比如固定每天上午6点钟执行，
# 并且sleep是一个阻塞函数，也就是说sleep着段时间，什么都不能做。

# ---------------------------------------------------------------------------

# 使用sched模块
# sched 模块是Python内置模块，它是一个调度（延时处理机制），每次想要定时执行任务都必须写入一个调度。
import sched

# 初始化sched模块的scheduler类
# 第一个参数是一个可以返回时间戳的函数，第二参数可以在定时未到达之前阻塞
schdule = sched.scheduler(time.time, time.sleep)
# 被周期性调度触发函数
def printTime(inc):
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    schedule.enter(inc, 0, printTime, (inc,))
# 默认参数60s
def main(inc=60):
    # enter四个参数分别为：间隔事件,优先级（用于同时到达两个事件同时执行的顺序），被调度触发的函数
    # 给该触发器函数的参数（tuple形式）
    schedule.enter(0, 0, pirntTime, (inc,))
    schedule.run()
# 5秒输出一次
main(5)

# sched使用步骤如下：
# （1）生成调度器：
# s = sched.scheduluer(time.time, time.sleep)
# 第一个参数是一个可以返回时间戳的函数，第二个参数可以在定时未到达之前阻塞。

# （2）加入调度事件
# 其实有 enter、enterabs 等等，我们以 enter 为例子。
# s.enter(x1,x2,x3,x4)
# 四个参数分别为：间隔事件、优先级（用于同时间到达的两个事件同时执行时定序）、被调用触发的函数，给触发函数的参数（注意：一定要以 tuple 给，如果只有一个参数就(xx,)）

# （3）运行
# s.run()
# 注意 sched 模块不是循环的，一次调度被执行后就 Over 了，如果想再执行，请再次 enter(循环调用）
