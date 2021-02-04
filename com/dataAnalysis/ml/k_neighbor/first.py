"""
    K 近邻算法：
    1，与邻居来判断类型（ 与最相近的人所在的区域）
    2.如何求距离？ 计算每个样本的特征值之间差的大小，从而影响 远近距离。
    3. 需对数据做 标准化处理， 防止某个特征异常值 影响计算后的距离.
-------------
    开发流程：
    1. 定义特征： x,y 坐标; 定位准确率;  格式化后的时间戳(年月日时分秒)
    2. 数据缩减: x,y的范围减小, 减少签到人数量的 位置(如：排除100人以下)
        2.1 pandas 缩小范围， df.query()
    3.标准化_
"""

from  sklearn.neighbors  import  KNeighborsClassifier


# KNeighborsClassifier(n_neighbors=)

