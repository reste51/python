"""
特征预处理
    数值型数据_针对每列（特征）处理_ 标准缩放

1. 归一化
    归一化首先在特征（维度）非常多的时候，可以防止某一维或某几维对数据影响过大，也是为了把不同来源的数据统一到一个参考区间下，这样比较起来才有意义，其次可以程序可以运行更快。
    受异常点 影响较大, 鲁棒性较差


2. 标准化：  常用_
    平均值 mean -》 方差 std  -》 标准差 σ = √std （根号 std）
    σ 越小：说明值越重合，集中；   越大： 说明离散

  其中\muμ是样本的均值，\sigmaσ是样本的标准差，它们可以通过现有的样本进行估计，在已有的样本足够多的情况下比较稳定，适合嘈杂的数据场景
  由于是使用了mean的平均值， 因此受异常点 影响较小, 鲁棒性较好
"""

from sklearn.preprocessing import MinMaxScaler,StandardScaler

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



def standardlization():
    """
    标准化：通过对原始数据进行变换把数据变换到均值为0,方差为1范围内
        均值为0：  所有特征值之和/ 样本数,  实际就是和为0

    注： 处理的是每列的特征值
    :return:
    """
    std_vector = StandardScaler()
    data = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]

    ret_arr = std_vector.fit_transform(data)  # numpy array of shape
    print(type(ret_arr), ret_arr,sep="\n")


if __name__=='__main__':
    # normalization()
    standardlization()








