"""
特征预处理
    数值型数据_标准缩放：

1. 归一化
    作用于每列特征， 首先在特征（维度）非常多的时候，可以防止某一维或某几维对数据影响过大，也是为了把不同来源的数据统一到一个参考区间下，这样比较起来才有意义，其次可以程序可以运行更快。
    受异常点 影响较大, 鲁棒性较差


2. 标准化：  常用_
    平均值 mean -》 方差 std  -》 标准差 σ = √std （根号 std）
    σ 越小：说明值越重合，集中；   越大： 说明离散

  其中\muμ是样本的均值，\sigmaσ是样本的标准差，它们可以通过现有的样本进行估计，在已有的样本足够多的情况下比较稳定，适合嘈杂的数据场景
  由于是使用了mean的平均值， 因此受异常点 影响较小, 鲁棒性较好

 3. 空置处理：
    删除（不建议），  填充（建议 ，使用平均值/ 中位数 每列填补）
    pandas 也可以处理


"""
import  numpy as np
from sklearn.preprocessing import MinMaxScaler,StandardScaler,Imputer

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

def nan_process():
    """
    空值处理 - 详情参考源码
    0计算过程： 0为列， nan =  (1+8)/2 =4.5

     missing_values:
      For missing values encoded as np.nan, use the string value "NaN".  float类型

     - If `axis=0`, then impute along columns.
     - If `axis=1`, then impute along rows.

    strategy
     - If "mean", then replace missing values using the mean along
      the axis.
    - If "median", then replace missing values using the median along
      the axis.
    - If "most_frequent", then replace missing using the most frequent
      value along the axis.
    :return:
    """
    nan_process = Imputer(missing_values='NaN',strategy='mean',axis=0)
    data = [[1, 2], [np.nan, 3], [8, 6]]  # np.nan 为float
    print(nan_process.fit_transform(data))

if __name__=='__main__':
    # normalization()
    # standardlization()
    nan_process()








