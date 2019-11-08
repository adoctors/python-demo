import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')


'''
变量
# 这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。
# 静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。
# 和静态语言相比，动态语言更灵活，就是这个原因。
'''

# a = 'ABC'
# b = a
# a = 'XYZ'
# print(b + a)        #ABCXYZ

'''
常量
所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量。在Python中，通常用全部大写的变量名表示常量：
PI = 3.14159265359
但事实上PI仍然是一个变量，Python根本没有任何机制保证PI不会被改变，
所以，用全部大写的变量名表示常量只是一个习惯上的用法，如果你一定要改变变量PI的值，也没人能拦住你。
'''





# '''
# number 数字类型
# 包括：整数、布尔、浮点数、复数
#     int
#     bool
#     float
#     complex
# '''

'''
整数
Python可以处理任意大小的整数，当然包括负整数，在程序中的表示方法和数学上的写法一模一样，例如：1，100，-8080，0，等等。
'''

# start = -200
# end = 201
# print(start + end)  # 1

#解释一下整数的除法为什么也是精确的。在Python中，有两种除法，一种除法是/：
# /除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数：
# print(10 / 3) #3.3333333333333335

# 还有一种除法是//，称为地板除，两个整数的除法仍然是整数：
# 整数的地板除//永远是整数，即使除不尽。因为//除法只取结果的整数部分.
# print(10 // 3)   #3

# Python还提供一个余数运算，可以得到两个整数相除的余数：
# print(10 % 3)      #1


'''
浮点数
浮点数也就是小数，之所以称为浮点数，是因为按照科学记数法表示时，一个浮点数的小数点位置是可变的。
整数和浮点数在计算机内部存储的方式是不同的，整数运算永远是精确的（除法难道也是精确的？是的！），
而浮点数运算则可能会有四舍五入的误差。
Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）。
'''

'''
布尔值
布尔值和布尔代数的表示完全一致，一个布尔值只有True、False两种值。
在Python中，可以直接用True、False表示布尔值（请注意大小写）
布尔值可以用and、or和not运算。
非零数值、非空字符串、非空list等，就判断为True，否则为False
'''
# print(3>2) # True
# age = 20
# if age >= 18:
#     print('adult')
# else:
#     print('teenager')

'''
空值
空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。
'''


'''
string 字符串
    单引号和双引号使用完全相同
    使用三引号(使用三个-单引号/双引号都行)可以指定一个多行字符串
    字符串可以用 + 运算符连接在一起
    用 * 运算符重复  
    Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
    Python中的字符串不能改变
    Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
    字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
'''
strs = 'adoctors!'
# print(strs)                 # 输出字符串   adoctors!
# print(strs[0:-1])           # 输出第一个到倒数第二个的所有字符      adoctors
# print(strs[0])              # 输出字符串第一个字符      a
# print(strs[2:5])            # 输出从第三个开始到第五个的字符    oct
# print(strs[2:])             # 输出从第三个开始的后的所有字符    octors!
# print(strs * 2)             # 输出字符串两次    adoctors!adoctors!
# print(strs + '你好')        # 连接字符串    adoctors!你好
# print('hello \nworld!')      # 使用反斜杠(\)+n转义特殊字符
# print(r'hello \nworld!')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义     hello \nworld!
# print('this' 'is' 'a' 'line')   #   thisisaline

# Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
# print(ord('A'))     #65
# print(ord('B'))     #66
# print(chr(66))      #B
# print(chr(20013))   #中
# print('\u4e2d\u6587')   #中文

    
# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。
# 如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
# Python对bytes类型的数据用带b前缀的单引号或双引号表示：
x = b'ABC'

# 要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。

# 格式化
# 最后一个常见的问题是如何输出格式化的字符串。
# 我们经常会输出类似'亲爱的xxx你好！你xx月的话费是xx，余额是xx'之类的字符串，
# 而xxx的内容都是根据变量变化的，所以，需要一种简便的格式化字符串的方式。用%实现
# %运算符就是用来格式化字符串的。
# 在字符串内部，%s表示用字符串替换，%d表示用整数替换，%f浮点数；%x十六进制整数。
# 有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。
# 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：

# print('hello,%s' % 'world') #hello,world
# print('%d' % 3)        #3
# print('%d-%2d' % (3, 1)) #3- 1
# print('%2d-%2d' % (3, 1)) # 3- 1
# print('%.2f' % 3.1415926) #3.14

# 有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：
# print('rate: %d %%' % 7) #rate: 7 %
# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.xx%'，只保留小数点后2位：
s1=72
s2=85
# print('percentum: %.2f %%' % ((s2-s1)/s1*100)) # 18.06 %

'''
list
Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
'''

# 用len()函数可以获得list元素的个数：
colors = ['green','blue','yellow','gray','red']

# print(len(colors))       #5 获取list的长度
# 用索引来访问list中每一个位置的元素，记得索引是从0开始的：
# print(colors[0])    #green
# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
# print(colors[-1])   #red
# list是一个可变的有序表，所以，可以往list中追加元素到末尾：
# colors.append('pink')
# print(colors)
# 也可以把元素插入到指定的位置，比如索引号为1的位置：
# colors.insert(1, 'adoctors')
# print(colors)
# 要删除list末尾的元素，用pop()方法：
# colors.pop()
# print(colors)   #输出删除后的list
# print(colors.pop())     #输出删除的元素
# print(colors)   #输出删除后的list
# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
# print(colors.pop(2))
# print(colors)

# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
# colors[4]='shanks'

'''
tuple
另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
'''
# classmates = ('Michael', 'Bob', 'Tracy')
# 现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。
# 其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。
# 不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。


# t=('a', 'b', ['A', 'B'])
# t[2][0]='X'
# t[2][1]='Y'
# print(t)

# 表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。
# tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
# 即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！


'''
条件判断
'''

score = 18

if score < 60:
    print('成绩：', score , '差')
elif score <=80:
    print('成绩：', score , '良')
else:
    print('成绩：', score , '优')