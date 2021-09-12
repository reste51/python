"""
    nltk 自带的语料库
"""
from nltk.corpus import  brown
from nltk import  data

data.path.append('D:\soft\python\module_packages\\nlp_nltk\\nltk_data\\')

print(brown.categories())

# 信息描述
print(brown.readme())

# 单词: 输出前10个, 个数: 1161 192
print(brown.words()[:10])
print(len(brown.words()))

# 句子
print(brown.sents()[:10])
print(brown.sents().__len__())

# 词性标注
print(brown.tagged_words()[:10])
print(brown.tagged_words().__len__())

