import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')


'''
切片
迭代
列表生成器
生成器
迭代器
'''

'''
切片

取一个list或tuple的部分元素是非常常见的操作。
记住倒数第一个元素的索引是-1。
什么都不写，只写[:]就可以原样复制一个list：
'''
colors = ['red','green','yellow','blue']

#要求：取前三个元素
# 方法一：使用下标
# print(colors[0],colors[1],colors[2])

# 方法二：使用循环
# arr = []
# n = 3
# for i in range(n):
#     arr.append(colors[i])
# print(arr)      #['red', 'green', 'yellow']

# 对这种经常取指定索引范围的操作，用循环十分繁琐
# Python提供了切片（Slice）操作符，能大大简化这种操作

# print(colors[0:3])      #['red', 'green', 'yellow']

#tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
# print((0, 1, 2, 3, 4, 5)[:3])   #(0, 1, 2)

# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。
# 因此，字符串也可以用切片操作，只是操作结果仍是字符串：
# Python没有针对字符串的截取函数，只需要切片一个操作就可以完成

# print('adoctors'[:3])  #ado



'''
迭代

如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
在Python中，迭代是通过for ... in来完成的

list这种数据类型虽然有下标，但很多其他数据类型是没有下标的
，但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代：
'''

# obj = {'a':1,'b':2,'c':3}
# for key in obj:
#     print(key,obj[key])

#因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，
# 如果要同时迭代key和value，可以用for k, v in d.items()。
# 由于字符串也是可迭代对象，因此，也可以作用于for循环：

# 所以，当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，
# 而我们不太关心该对象究竟是list还是其他数据类型。
# 那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：


# from collections.abc import Iterable    #注意.abc必须带，否则报错，版本原因
# print(isinstance('abc', Iterable)) # str是否可迭代    True
# print(isinstance([1,2,3], Iterable)) # list是否可迭代   True
# print(isinstance(123, Iterable)) # 整数是否可迭代  False

# isinstance(x, str)    判断x是否为字符串




# 如果要对list实现类似Java那样的下标循环怎么办？
# Python内置的enumerate函数可以把一个list变成索引-元素对，
# 这样就可以在for循环中同时迭代索引和元素本身：

# for i, value in enumerate(['A', 'B', 'C']):
#     print(i, value)
# 0 A
# 1 B
# 2 C


'''
列表生成器
列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
'''

#举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
arr=list(range(1,11))
print(arr)   #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



# 但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？
# 方法一是循环：
l=[]
for x in range(1,11):
    l.append(x*x)
# print(l)   #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 方法二：使用列表生成器
# print([x * x for x in range(1,11)])   #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：

# print([x * x for x in range(1, 11) if x % 2 == 0])   #[4, 16, 36, 64, 100]

# 还可以使用两层循环，可以生成全排列：
# print([m + n for m in 'ABC' for n in 'XYZ'])  #['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

#三层和三层以上的循环就很少用到了。

# 运用列表生成式，可以写出非常简洁的代码。
# 例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os # 导入os模块，模块的概念后面讲到
print([d for d in os.listdir('.')])   # os.listdir可以列出文件和目录   ['.vscode', 'defs.py', 'others.py', 'test1.py', 'typeof']



# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)

e = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in e.items()])   # ['y=B', 'x=A', 'z=C']

# 最后把一个list中所有的字符串变成小写：
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])   # ['hello', 'world', 'ibm', 'apple']





# 列表生成式也可以使用两个变量来生成list：




'''
生成器

在Python中，这种一边循环一边计算的机制，称为生成器：generator
'''

'''
迭代器
'''
