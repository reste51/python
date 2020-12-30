'''

    1. 值的修改   arr[0]=1,  第一行所有的值 赋值为1


    视频: 05-numpy读取本地数据和索引 ,03numpy中更多的索引方式
'''

import numpy as np

arr = np.arange(100,124).reshape(4,6)
print(arr)

# 第一行所有的值 赋值为1
arr[0]=1
print(arr)



