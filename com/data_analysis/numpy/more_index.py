'''

    1. 值的修改   arr[0]=1,  第一行所有的值 赋值为1

    2. bool索引
         [ condition(返回boolean值) ] ; arr[arr>120] = 10

    3. np.where(condition,x,y)  三元运算符

    4.裁剪： arr.clip(108,118)   小于108 替换为108， 大于118 替换为118

    视频: 05-numpy读取本地数据和索引 ,03numpy中更多的索引方式
'''

import numpy as np

arr = np.arange(100,124).reshape(4,6)
print(arr)

# 第一行所有的值 赋值为1
# arr[0]=1
# print(arr)

# 布尔索引:  将大于 120的元素置为 10;   [ condition(返回boolean值) ]
# print(arr>120)
# arr[arr>120] = 10  # 会将 为True的元素置为10
# print(arr)

# 将大于 120的置为10， 小于 120的置为1
new_arr = np.where(arr>120,10,1)  # 三元运算符
print(new_arr)

# 小于108 替换为108， 大于122 替换为122
arr = arr.clip(108,118)
print(arr)



