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

# 动态获取二维数组的长度
arr_count = arr.shape[0] * arr.shape[1]
print('元素个数为{}'.format(arr_count))

# 转为一维数组的方式：
print(arr.reshape(arr_count,))
print(arr.flatten())  # Return a copy with the array collapsed into one dimension.

# 变为一维数组
# arr = arr.reshape(12,)
# print(arr, arr.shape)

print('*'*100)

# 数组的计算
arr2 = np.arange(24).reshape(4,6)
# print(arr2, arr2.shape)

# 1.与某个数值计算，广播机制(会与每个元素计算一次)_原数组的shape不会变
# print(arr2+20)
print(arr2/0)  # 元素0的为nan(not a number)， 不为0的是inf(infinite 无限)

# 2.与数组计算,
# 2.1 数组与数组的 shape 一样时, 矩阵的对应位置元素计算
arr3 = np.arange(100,124).reshape(4,6)
# print(arr3, arr3.shape)
print(arr2+arr3)


# 2.2 arr_row与arr3的每行shape 一致时,  对于每行的元素计算
arr_row = np.arange(6)
# print(arr3)
print(arr3 + arr_row)

# 2.3 列shape的计算    23：25



print('*'*100)


# 广播原则： 30：00_  trailing dimension





