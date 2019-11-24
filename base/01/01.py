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

