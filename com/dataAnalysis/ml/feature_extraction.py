"""
    特征抽取， 将文本转为 数值( 使用字典标识)

    类似 YL1(0为未完成， 1已完成), ZJZLDM(证件种类代码_是一个字典)
"""

from sklearn.feature_extraction import DictVectorizer

def dictvec():
    """
    字典数据抽取
    :return: None
    """
    # 实例化
    dict = DictVectorizer()

    # 特征化
    data = dict.fit_transform([{'city': '北京','temperature':100},{'city': '上海','temperature':60},{'city': '深圳','temperature':30}])
    print(data)


if __name__ == '__main__':
    dictvec()
