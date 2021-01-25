"""
数据降维：
    该维度是特征的数量， 降维则是  减少特征。

    特征选择：
        1. filter:  varianceFilter方差过滤( 过滤低于 指定方差值以下的特征， 删除相同值的特征)
            包名: feature_selection

          PCA：principal component analysis 主成分分析( 应用场景少)：
             包名: decomposition  ; 特征数量达到 上百个时使用
              1.2.1 将高维数据  降低低维, 数据不会损失很多。
              1.2.2 高维数据问题： 特征之间通常是相关的    - 22：31

        2. embed： 正则化、决策树






"""

from sklearn.feature_selection import VarianceThreshold

def varianceThreshold():
    """
    特征选择- 删除低于指定方差的特征
    :return:
    """
    var = VarianceThreshold(threshold=0.3)
    data = var.fit_transform([[0,2,0,3],[0,1,4,3],[0,1,1,3]])
    print(data)


if __name__ =='__main__':
    varianceThreshold()


