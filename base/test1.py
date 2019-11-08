import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')



str='im python! 看'
print(str)					#直接输出

name = input()				#可输入变量

print(name)					#输出可输入变量

'''
像这样的为
多行注释
'''

"""
这里也是多行注释
使用三个 单引号/双引号都行
"""

_vars = '变量名开头石字母或者_开头'

colors = ['green','blue','yellow','gray','read']