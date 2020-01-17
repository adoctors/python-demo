import time
filename = 'a.txt'


def read_file0(file_name):
    f = open(file_name, 'r', encoding='utf-8')
    print(f.read())
    f.close()

# 请注意上面的代码，如果`open`函数指定的文件并不存在或者无法打开，那么将引发异常状况导致程序崩溃。
# 为了让代码有一定的健壮性和容错性，我们可以使用Python的异常机制对可能在运行时发生状况的代码进行适当的处理，如下所示。

def read_file01(file_name):
    f = None
    try:
        f = open(file_name, 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()

# `finally`块的代码不论程序正常还是异常都会执行到


# 也可以使用上下文语法，通过`with`关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源

def read_file02(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')

# read_file0('b.js')
# read_file01('b.js')


# 通过for-in循环逐行读取
# with open(filename, 'r', encoding='utf-8') as f:
#   for line in f:
#     print(line, end='')
#     time.sleep(0.5) # 延时0.5S
# print()



# 读取文件按行读取到列表中
# with open(filename, 'r', encoding='utf-8') as f:
#   lines = f.readlines()
# print(lines)

def write_file():
  filenames = ('wa.txt', 'wb.txt', 'wc.txt')
  fs_list = []
  try:
    for filename in filenames:
      fs_list.append(open(filename, 'w', encoding='utf-8'))
    for number in range(1, 10000):
      if number < 100:
        fs_list[0].write(str(number) + '\n')
      elif number < 1000:
        fs_list[1].write(str(number) + '\n')
      else:
        fs_list[2].write(str(number) + '\n')
  except IOError as ex:
    print(ex)
    print('写文件时发生错误!')
  finally:
    for fs in fs_list:
      fs.close()
  print('操作完成!')



write_file()