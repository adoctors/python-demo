

def verifyName():
  print('请输入当前使用的语言！')
  name = input()
  if (name == 'python'):
    print('ok!')
  else: 
    print('err!')
    verifyName()

verifyName()
# if (name == 'python'):
#   print('ok')
# else: 
#   print('err,请重新输入！')
#   name = input()
# print ('hello! 看 ', name)


# colors = ['yellow', 'green', 'red', 'blue', 'origin', 'pink']

# for color in colors:
#   print(color)

# s = set([1,1,2,3,4,5,1,2,4,3])
# print(s)
