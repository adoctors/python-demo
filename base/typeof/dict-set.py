import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

'''
dict
Python内置了字典：dict的支持，dict全称dictionary，
在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
'''

# obj = {'name':'adoctors','age':18,"adress":'洛阳'}
# print(obj['name'])
# obj['like']='eat'
# print(obj)

# 如果key不存在，dict就会报错：
# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
# print('a' in obj)  #False

# 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
# print(obj.get('b'),obj.get('c',404))   #None 404
# 注意：返回None的时候Python的交互环境不显示结果。

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
# obj.pop('age')
# print(obj.pop('age'),obj) #18 {...}

'''
和list比较，dict有以下几个特点：

查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。

而list相反：

查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法
'''


'''
set
set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
'''
#要创建一个set，需要提供一个list作为输入集合：

# arr = set([1,2,3])
# print(arr)    #{1,2,3}

# 重复元素在set中自动被过滤：
# print(set([1,2,3,5,1,2,6,3]))  #{1, 2, 3, 5, 6}

# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
# arr.add(4)
# print(arr) #{1, 2, 3, 4}

# 通过remove(key)方法可以删除元素：
# arr.remove(3)
# print(arr)  #{1, 2, 4}

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])

print(s1 & s2)  #{2, 3}
print(s1 | s2)  #{1, 2, 3, 4}


# 对于可变对象，比如list，对list进行操作，list内部的内容是会变化的，比如：

# 而对于不可变对象，比如str，对str进行操作呢：
a = 'abc'
a.replace('a', 'A') #'Abc'

# 当我们调用a.replace('a', 'A')时，实际上调用方法replace是作用在字符串对象'abc'上的，
# 而这个方法虽然名字叫replace，但却没有改变字符串'abc'的内容。
# 相反，replace方法创建了一个新字符串'Abc'并返回，
# 如果我们用变量b指向该新字符串，就容易理解了，变量a仍指向原有的字符串'abc'，但变量b却指向新字符串'Abc'了：