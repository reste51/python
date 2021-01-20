"""
特征预处理
1. 归一化
    归一化首先在特征（维度）非常多的时候，可以防止某一维或某几维对数据影响过大，也是为了把不同来源的数据统一到一个参考区间下，这样比较起来才有意义，其次可以程序可以运行更快。


"""

from sklearn.preprocessing import MinMaxScaler

def normalization():
    """
    归一化
    :return: None
    """
    # 改变 标准化范围  默认 (0,1)
    scaler = MinMaxScaler(feature_range=(2,3))
    data = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]
    print(scaler.fit_transform(data))
    # 输出最大值
    print(scaler.data_max_,scaler.data_min_,scaler.data_range_)





if __name__=='__main__':
    normalization()









