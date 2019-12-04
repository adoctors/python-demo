# 基础概念测试

# import sys

# print(sys.version)
# print(sys.version_info)
# print(sys.api_version)

# -----------------------------------------------
# import turtle
    
# turtle.pensize(4)
# turtle.pencolor('green')

# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)

# turtle.mainloop()

# ------------------输入与占位------------------------

# a = int(input('a = '))
# b = int(input('b = '))
# print('%d + %d = %d' % (a, b, a + b))
# print('%d - %d = %d' % (a, b, a - b))
# print('%d * %d = %d' % (a, b, a * b))
# print('%d / %d = %f' % (a, b, a / b))
# print('%d // %d = %d' % (a, b, a // b))
# print('%d %% %d = %d' % (a, b, a % b))
# print('%d ** %d = %d' % (a, b, a ** b))

# ------------------输入与判断------------------------

# username = input('username:')
# password = input('password:')

# if username == 'admin' and password == '123':
# 	print('success!')
# else:
# 	print('fail')

# score = float(input('请输入成绩：'))
# if score >= 90:
# 	grade = 'A'
# elif score >= 80:
# 	grade = 'B'
# elif score >= 70:
# 	grade = 'C'
# else:
# 	grade = 'D'

# print('对应的等级是：',grade)

# ------------------循环------------------------

# sum = 0
# for x in range(101):
# 	sum +=x
# print(sum)

# x = int(input('请输入行数: '))
# for _ in range(x):     # _作为占位符，无意义
#   print('2')

# row = int(input('请输入行数: '))
# for i in range(row):
#     for _ in range(i + 1):
#         print('*', end='')   # print('*', end='2')
#     print()

# -----------------------------------------------

# import random

# answer = random.randint(1, 100)
# print(answer)
# counter = 0
# # 没有做空值处理所以回报错
# # 因为用的是while所以输错了会让重新输入
# 因为此处是一个死循环，在循环内条件结束循环
# while True:
#     counter += 1
#     number = int(input('请输入: '))
#     if number < answer:
#         print('大一点')
#     elif number > answer:
#         print('小一点')
#     else:
#         print('恭喜你猜对了!')
#         break
# print('你总共猜了%d次' % counter)
# if counter > 7:
#     print('你的智商余额明显不足')

# -----------------------------------------------

# import random
   
# money = 1000
# while money > 0:
#   print('你的总资产为:', money)
#   needs_go_on = False
#   while True:
#     debt = int(input('请下注: '))
#     if 0 < debt <= money:
#       break
#   first = random.randint(1, 6) + random.randint(1, 6)
#   print('玩家摇出了%d点' % first)
#   if first == 7 or first == 11:
#     print('玩家胜!')
#     money += debt
#   elif first == 2 or first == 3 or first == 12:
#     print('庄家胜!')
#     money -= debt
#   else:
#     needs_go_on = True
#   while needs_go_on:
#     needs_go_on = False
#     current = random.randint(1, 6) + random.randint(1, 6)
#     print('玩家摇出了%d点' % current)
#     if current == 7:
#       print('庄家胜')
#       money -= debt
#     elif current == first:
#       print('玩家胜')
#       money += debt
#     else:
#       needs_go_on = True
# print('你破产了, 游戏结束!')

# pre = 1
# nex = 1
# mid = 1

# leng = 1

# while leng < 21:
#   print(mid)
#   mid = pre+nex
#   # print(mid)
#   pre=nex
#   nex=mid
#   leng+=1


# while True:
#   print('start: %d' % leng)
#   leng+=1
#   if leng == 3:
#     # 此时直接跳过下面的内容直接进入下一个循环
#     continue
#   print('end: %d' % leng)

#   if leng == 5:
#     print('---')
#     break


# f = [x for x in range(1, 10)]
# print(f)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# f = [x + y for x in 'ABCDE' for y in '1234567']
# print(f)
# ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7']


# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#         yield a


# # print(fib(20))  <generator object fib at 0x0000020996F2EE58>

# def main():
#     # for val in fib(20):
#         # print(val)


# if __name__ == '__main__':
#     main()


# -------------------------------

class Student(object):

    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国爱情大电影.' % self.name)

def main():
    # 创建学生对象并指定姓名和年龄
    stu1 = Student('adoctors', 28)
    # 给对象发study消息
    stu1.study('Python程序设计')
    # 给对象发watch_av消息
    stu1.watch_movie()
    stu2 = Student('王大锤', 15)
    stu2.study('思想品德')
    stu2.watch_movie()


# if __name__ == '__main__':
#     main()

# ----------------------------------------