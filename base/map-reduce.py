import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

from functools import reduce

'''
map()函数接收两个参数，
一个是函数，一个是Iterable，
map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
'''

def f(x):
    return x*x

r=map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))      #[1, 4, 9, 16, 25, 36, 49, 64, 81]


'''
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
这个函数必须接收两个参数，
reduce把结果继续和序列的下一个元素做累积计算，其效果就是
'''

def add(x,y):
    return x+y

print(reduce(add,[1,2,3]))      #6

'''
Python内建的filter()函数用于过滤序列
filter()也接收一个函数和一个序列。和map()不同的是，
filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
'''

def is_odd(n):
    return n%2==1

print(list(filter(is_odd,[1,2,5,6,8,7,9,4])))  #[1, 5, 7, 9]

'''
排序算法
Python内置的sorted()函数就可以对list进行排序：
'''

sortList = [36,5,9,-1,2,-6]
print(sorted(sortList))  #[-6, -1, 2, 5, 9, 36]


'''
此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
'''

print(sorted(sortList,key=abs))

