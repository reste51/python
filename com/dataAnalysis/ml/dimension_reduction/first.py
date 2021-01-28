"""
数据降维：
    该维度是特征的数量， 降维则是  减少特征。

    特征选择：
        1. filter:  varianceFilter方差过滤( 过滤低于 指定方差值以下的特征， 删除相同值的特征)
            包名: feature_selection   ; removes all low-variance features

          PCA：principal component analysis 主成分分析( 应用场景少)： 降低维度，数据量尽量减少损失
             包名: decomposition  ; 特征数量达到 上百个时使用
              1.2.1 将高维数据  降低低维, 数据不会损失很多。
              1.2.2 高维数据问题： 特征之间通常是相关(通过缩放比例是重复的)

        2. embed： 正则化、决策树






"""

from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import  PCA

def varianceThreshold():
    """
    特征选择- 删除低于指定方差的特征
    :return:
    """
    var = VarianceThreshold(threshold=0.3)
    data = var.fit_transform([[0,2,0,3],[0,1,4,3],[0,1,1,3]])
    print(data)

def pca():
    """
    主成分分析
    n_components 特征信息损失量：
        1. 小数( 0-1,  0% - 100%): 损失率， 常用 ( 0.9 - 0.95)
        2. 整数:保留的特征个数; 一般不会用
    :return:
    """
    pca = PCA(n_components=0.9)  # 原4个特征 减少为2, 损失量 10%
    # pca = PCA(n_components=1)  # 原4个特征 减少为1
    reduce_data = pca.fit_transform([[2,8,4,5],[6,3,0,8],[5,4,9,1]])
    print(reduce_data)

if __name__ =='__main__':
    # varianceThreshold()
    pca()

