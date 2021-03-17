'''
模块：
    模块就好比是工具包，要想使用这个工具包中的工具(就好比函数)，就需要导入这个模块
    三种方式的导入：
        1.import module1,mudule2...
        2.from modname import name1[, name2[, ... nameN]]
        3.from module1 import *

    定位模块
    当你导入一个模块，Python解析器对模块位置的搜索顺序是：
    1、当前目录
    2、如果不在当前目录，Python则搜索在shell变量PYTHONPATH下的每个目录。
    3、如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/
    4、模块搜索路径存储在system模块的sys.path变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。

'''

import  math
print(math.sqrt(2))

#有时候我们只需要用到模块中的某个函数，只需要引入该函数即可，此时可以用下面方法实现：from…import
from os import listdir
print(listdir())     # Return a list containing the names of the files in the directory.

# from  com.bjsxt.test.test import add,division
import  basic.test.test as test

print(test.add(10, 20))
print(test.division(10, 20))


# from distutils.core import setup

