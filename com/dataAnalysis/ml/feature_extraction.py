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
from  sklearn.feature_extraction.text import CountVectorizer
import jieba

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

def text_vector(content):
    """
    文本特征化_ 统计出现词汇的次数
    去重单词作为特征列表(单个字母 i 则不统计_因为没有分类依据)
    :return: None
    """
    text_vec = CountVectorizer()
    ret = text_vec.fit_transform(content)
    # sparse矩阵(基于Numpy的)  -> 二维数组的格式
    print(ret.toarray())
    print(text_vec.get_feature_names())  # 特征列表

def cut_word(content):
    """
    使用jieba 分词处理
    jieba分词-> 迭代器 -> list -> str ' '.join(l) -> return array
    :return: array
    """
    ret = []
    for c in content:
        tmp_l = list(jieba.cut(c)) # 迭代器 -> list
        ret.append(' '.join(tmp_l)) # 以空格 分割的每个词汇
    return ret


if __name__ == '__main__':
    # 1.first
    # dictvec()

    # 2. 中英文
    # content = ["life is short short is life,i like python", "life is too long,i dislike python"]
    # 中文默认使用 , 及 空格分割词汇作为特征来统计。
    # content = ['人生苦短，我先java java 苦短','列表  分词 科技 科技']
    # text_vector(content)

    # 3.使用jieba 中文分词来特征统计
    content = ["今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。",
            "我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。",
            "如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。"]

    word_arr = cut_word(content)
    # print(word_arr)
    # 注： 单个汉字也无法统计
    text_vector(word_arr)





