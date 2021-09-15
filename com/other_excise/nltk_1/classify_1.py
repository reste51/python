"""
 机器学习分类
"""
import nltk
from nltk.book import *


def gender_features(word):
    """
    生成特征: 最后一个单词
    :param word:
    :return:
    """
    return {'last_letter': word[-1]}

# 导入 学习的姓名和性别名单
from nltk.corpus import names
import random



