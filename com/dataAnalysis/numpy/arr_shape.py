'''
1.numpy 的shape 是一个元组, 元组值的个数代表了 维度的数量
如： shape为(3,4) 代表了3行4列的数组,  因2个数值 代表了 该数组是 二维数组

2. reshape 修改arr的维度
    Returns an array containing the same data with a new shape.
    reshape的个数需要等于 原有数组元素的个数  3*4=12


'''
import  numpy as np

# 一维数组
# arr = np.arange(10)
# print(arr.shape,arr)

# 二维数组, dimensions 2 , shape 为(2, 2)
arr = np.array([[1,2], [3,4]])
print(arr,arr.shape)

arr = np.array([[1,2], [3,4]])
print(arr,arr.shape)

print('*'*50)

# reshape 修改arr的维度, 创建个数为12的数组
arr = np.arange(12)
# print(arr,arr.shape)
# 注: reshape的个数需要等于 原有数组的个数  3*4=12
arr = arr.reshape(3,4)    # reshape((3,4))
print(arr, arr.shape)

# 变为一维数组
arr = arr.reshape(12,)
print(arr, arr.shape)

