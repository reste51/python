"""
    K 近邻算法：
    1，与邻居来判断类型（ 与最相近的人所在的区域）
    2.如何求距离？ 计算每个样本的特征值之间差的大小，从而影响 远近距离。
    3. 需对数据做 标准化处理， 防止某个特征异常值 影响计算后的距离.
-------------
   总结：
   1.缺点：
        1.1 k的取值(越小受异常点影响, 越大受最近数据太多导致比例变化)
        1.2 计算耗时长， 样本数 与时间成线性增长, 时间复杂度 n^2
   2. 优点： 算法简单，无需迭代训练优化，没有估计参数( 调用方法传递的参数)
        注：n_neighbors为超参数—> KNeighborsClassifier(n_neighbors=5);  创建类实例时，传递的参数。

"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from numpy.random import randn
from sklearn.preprocessing import StandardScaler

path = '../data/facebook-v-predicting-check-ins'  # 注： 显示全部列
pd.set_option('display.max_columns', None)
neighbor_num = 8

def k_neighbors():
    """
    k 近邻算法
    :return: None
    """
    # 1. 读取数据
    df = pd.read_csv(f'{path}/train.csv')
    # print(df.shape)            (29118021, 6)

    # 2.缩小数据范围
    df = df.query('x>1.0 & x< 1.25 & y>2.5 & y< 2.75')
    # 2.2 删除签到次数 小于3的
    #  df过滤前的条数:17710; 过滤后: 16918;   地点filter_df条数: 239
    g_df = df.groupby('place_id').count()  # return DF
    # 2.2.1 结构：place_id 作为索引，每个特征为 聚合后的数值
    # 2.2.2 过滤大于3，重置索引; 将place_id置为特征中, index从0计数
    filter_df = g_df[g_df['row_id'] > 3].reset_index()
    # 2.2.3 在原df中过滤_地点_
    df = df[df['place_id'].isin(filter_df['place_id'])]

    # 3. 处理日期格式, return Series
    df['format_time'] = pd.to_datetime(df['time'], unit='s')
    # 3.1 构建一些 时间的特征; 将日期转为字典,从而获取 年/ 月/ 日
    datetime = pd.DatetimeIndex(df['format_time'])
    df['day'] = datetime.day
    df['hour'] = datetime.hour
    # df['second'] = datetime.second
    # df['week'] = datetime.week

    # 4. 删除无用的特征， time, rowid,format_time 会影响 预测的位置
    df = df.drop('time', axis=1).drop('format_time', axis=1).drop('row_id', axis=1)

    # 5. 获取特征值和目标值 -> 划分训练和测试集
    # sample数：16918， 特征数:7
    target_all = df['place_id']
    feature_all = df.drop('place_id', axis=1)
    # print(target_all.shape, feature_all.shape)
    feature_train, feature_test, \
        target_train, target_test = train_test_split(feature_all, target_all, test_size=0.25)

    # 6. 标准化，注： 只处理特征值(test/train), 不处理目标值
    standard = StandardScaler()
    feature_train = standard.fit_transform(feature_train)
    # feature_test = standard.fit_transform(feature_test)
    # standard.fit(feature_test)
    feature_test = standard.transform(feature_test)

    # 7. 算法计算
    kn = KNeighborsClassifier(n_neighbors=neighbor_num)
    # fit predict score
    kn.fit(feature_train, target_train)  # 训练特征,训练目标;  有目标值为监督学习
    # 预测值, 传入测试特征
    target_predict = kn.predict(feature_test)
    print(f'预测的目标值位置为：{target_predict}')

    # 准确率_ 传入 测试特征，测试目标  与 训练后的值比较
    # 标准化前 3%, 标准化后38%;
    # 改进-> 删除row_id的特征后：43.3%
    # 改进2-> 日期特征只保留 day,hour 能达到 50%
    score = kn.score(feature_test, target_test)
    print(f'准确率为{score}')
    print(f'特征值的数量为{feature_all.shape[1]}, sample数量为: {feature_all.shape[0]}')


def df_query_test():
    """
    Query the columns of a frame with a boolean expression.
    :return: None 
    """
    # 10行 2列
    df = pd.DataFrame(randn(10, 2), columns=list('ab'))
    # query_ret_df = df.query('a>b')
    query_ret_df = df[df.a > df.b]  # same result
    print(query_ret_df)


if __name__ == '__main__':
    k_neighbors()
    # df_query_test()
