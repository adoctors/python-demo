import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

# print ('测试')

# name = input('请输入姓名: ')


# if(name):
#     age = input('请输入年龄: ')
# else:
#     name = input('请输入姓名: ')

# print('姓名：',name , 'age:', age)

# colors = ['green','blue','yellow','gray','red']


'''
循环
    for in
    while
    在循环中，break语句可以提前退出循环
    在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。
'''


# for color in colors:
#     print(color)

# 如果要计算1-100的整数之和，从1写到100有点困难，
# 幸好Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。
# 比如range(5)生成的序列是从0开始小于5的整数：
# lists = list(range(5))
# print(lists)

# 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。
# 比如我们要计算100以内所有奇数之和，可以用while循环实现：

# sum = 0
# n=99
# while n>0:
#     sum+=n
#     n-=2
# print(sum)

