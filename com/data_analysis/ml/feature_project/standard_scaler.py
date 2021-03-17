"""
    特征工程：
        数据标准化， 去除异常值的影响
"""
from sklearn import preprocessing
import numpy as np

X_train = np.array([[1., -1, 2.],
                    [2.0, 0., 0.],
                    [0., 1., -1.]])

scaler = preprocessing.StandardScaler().fit(X_train)
print(scaler, sep='\n')

# 输出每个特征值的平均值，  sum(val) / count()
print(scaler.mean_)
print(scaler.scale_)

# 实际转换,zero mean and unit variance; 均值和方差均为0的数据
X_scaled = scaler.transform(X_train)
print(X_scaled)

print('*' * 100)

# 值的缩放; 一般是0-1 之间， 或者给定的最大和最小值之间.
# Here is an example to scale a toy data matrix(矩阵) to the [0, 1] range:

min_max_scaler = preprocessing.MinMaxScaler()
X_train_min_max = min_max_scaler.fit_transform(X_train)
print(X_train_min_max)

# 使用X_train的fit计算模型， 去转换测试集的数据
X_test = np.array([[-3., -1., 4.]])
X_test_min_max = min_max_scaler.transform(X_test)
print(X_test_min_max)  # 出现了-->  1.66666667, 可能是过拟合的现象


