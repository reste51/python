'''
numpy 学习的进阶
'''

import numpy as np

arr = np.random.randint(1,10,20).reshape(4,5)
# 获取每个轴上面的元素总数, 行为4个，列为5个
# print(arr.shape[0],  arr.shape[1])
print(arr)

# 遍历元素
# for i in range(0,arr.shape[0]):
#     for j in range(0,arr.shape[1]):
#         print(arr[i][j],end='\t')
#     print()

# 基本运算

# 每个元素的求和
print(arr.sum())

# 每列求和  -  一元数组- 5
print(arr.sum(0))
# 每行求和，  个数为 行的个数
print(arr.sum(1))
# print(arr.sum(2))  # 会报错

print('*'*1000)

# + - * /的运算
arr2 = np.ones(20,dtype=int).reshape(5,4)

# 每个元素的累加
# print(arr + arr2)
# print(arr-arr2)

# 乘积不能使用 arr * arr2
# arr的 行 * arr2的列（必须相等）, arr列=arr2行
print(np.dot(arr,arr2))

# 转置， 行转列
print(arr.T)


