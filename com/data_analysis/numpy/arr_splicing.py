'''
    数组的拼接:
    06-numpy中的nan和常用方法_01数据的拼接
        垂直和 水平的拼接 与 分割的方式  相反

    常用的统计函数
        sum, mean , median ,max ,min ,ptp std
'''

import numpy as np

arr = np.arange(100,124).reshape(6,4)      # 6行4列
print(arr)
# 0为列,  1 为行
print(arr.sum(axis=1))

# 均值
print(arr.mean(axis=1))

# 中间值
print(np.median(arr,axis=1))

# 最大值
print(arr.max(axis=0))

# 最小值
print(arr.min(axis=0))


# 极值, 最大-最小值 ;Range of values (maximum - minimum) along an axis.
print(arr.ptp(axis=0))
print(np.ptp(arr,axis=0))

# 标准差, 判断点的波动情况与稳定性,
# 值越大:点越分散, 越小:稳定
print(arr.std(axis=1))




