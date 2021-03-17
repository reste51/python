"""
    假设要解决一个时序问题：根据过往两年的数据（2012 年 8 月至 2014 年 8月），
        需要用这些数据预测接下来 7 个月的乘客数量
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error


def dataset():
    """
     1. 从 2012 年 8 月- 2013 年 12 月的数据中构造一个数据集。
     2. 创建 train and test 文件用于建模。前 14 个月（ 2012 年 8 月- 2013 年 10 月）用作训练数据，
        后两个月（2013 年 11 月 – 2013 年 12 月）用作测试数据。
    3.  以每天为单位聚合数据集。
    :return: 训练和测试集
    """
    # Subsetting the dataset
    df = pd.read_csv('../data/jet_rail/train.csv', nrows=11856)

    # create train and test set
    train = df[0:10392]
    test = df[10392:]  # 占比 12.3%

    # aggregating the dataset at daily level; 4位年用Y，2位年用y
    df['Timestamp'] = pd.to_datetime(df['Datetime'], format='%d-%m-%Y %H:%M')
    df.index = df['Timestamp']  # 以时间戳作为索引
    print(df.shape, df.info(), df.head(), sep='\n')

    # 训练和测试集的 索引更改
    train['Timestamp'] = pd.to_datetime(train['Datetime'], format='%d-%m-%Y %H:%M')
    train.index = train['Timestamp']
    train = train.resample('D').mean()  #

    test['Timestamp'] = pd.to_datetime(test['Datetime'], format='%d-%m-%Y %H:%M')
    test.index = test['Timestamp']
    test = test.resample('D').mean()

    # Plotting data
    train.Count.plot(figsize=(15, 8), title='Daily Ridership', fontsize=14)
    test.Count.plot(figsize=(15, 8), title='Daily Ridership', fontsize=14)
    plt.show()

    return train, test


def naive():
    """
    朴素法： 第一个预测点和上一个观察点相等的预测方法就叫朴素法。即 yt+1^=yt
    如果数据集在一段时间内都很稳定，我们想预测第二天的价格，
        可以取前面一天的价格，预测第二天的值。这种假设第一个预测点和上一个观察点相等的预测方法就叫朴素法。即 yt+1^=yt
    :return:
    """
    train, test = dataset()
    dd = np.asarray(train['Count'])
    y_hat = test.copy()
    y_hat['naive'] = dd[len(dd) - 1]
    plt.figure(figsize=(12, 8))
    plt.plot(train.index, train['Count'], label='Train')
    plt.plot(test.index, test['Count'], label='Test')
    plt.plot(y_hat.index, y_hat['naive'], label='Naive Forecast')
    plt.legend(loc='best')
    plt.title("Naive Forecast")
    plt.show()

    # 朴素法并不适合变化很大的数据集，最适合稳定性很高的数据集。我们计算下均方根误差，检查模型在测试数据集上的准确率
    cost = mean_squared_error(test['Count'], y_hat['naive'])
    print(f'均方误差值为： {cost}')


def simple_average():
    """
    简单平均法：
    物品价格会随机上涨和下跌，平均价格会保持一致。我们经常会遇到一些数据集，虽然在一定时期内出现小幅变动，但每个时间段的平均值确实保持不变。这种情况下，我们可以预测出第二天的价格大致和过去天数的价格平均值一致。
        这种将预期值等同于之前所有观测点的平均值的预测方法就叫简单平均法。即y^x+1=1x∑i=1xyi
    :return:
    """
    train, test = dataset()
    y_hat_avg = test.copy()
    y_hat_avg['avg_forecast'] = train['Count'].mean()
    plt.figure(figsize=(12, 8))
    plt.plot(train['Count'], label='Train')
    plt.plot(test['Count'], label='Test')
    plt.plot(y_hat_avg['avg_forecast'], label='Average Forecast')
    plt.legend(loc='best')
    plt.show()


if __name__ == '__main__':
    simple_average()
