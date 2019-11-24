# 定时器，全局变量
from threading import Timer
import random



i=1


def fun(name,age):
  global i
  i+=1

  


  t = Timer(random.randint(1,3), fun,args=('abc',14,))
  if i > 5: 
    t.cancel()
  t.start()
  # i=unpdate_i()
  
  print('fun',name,age,i)

# fun()


# t = Timer(random.randint(5,30), fun,args=('abc',14,))


# t.start()
#  tmr.cancel()
fun('xxx',18)

