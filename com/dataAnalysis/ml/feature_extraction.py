"""
    样本的特征抽取， 将文本转为 数值( 使用字典标识)

    类似 YL1(0为未完成， 1已完成), ZJZLDM(证件种类代码_是一个字典)

    02-特征工程和文本特征提取 - 05_字典特征数据抽取  09：17

1. 生成的结果 sparse矩阵:  稀疏
    (0, 3)	100.0
    (1, 0)	1.0
原因:
   节约内存,  方便读取数据

2. 矩阵类型(ndarray, 二维数组):  sparse=False
[[  0.   1.   0. 100.]
 [  1.   0.   0.  60.]
 [  0.   0.   1.  30.]]


"""

from sklearn.feature_extraction import DictVectorizer

def dictvec():
    """
    字典数据抽取
    :return: None
    """
    # 实例化
    dict = DictVectorizer(sparse=False)

    # 特征化, 传入三份 样本
    data = dict.fit_transform([{'city': '北京','temperature':100},{'city': '上海','temperature':60},{'city': '深圳','temperature':30}])
    print(data)
    # 输出 特征列表;  ['city=上海', 'city=北京', 'city=深圳', 'temperature']
    print(dict.get_feature_names())


if __name__ == '__main__':
    dictvec()
