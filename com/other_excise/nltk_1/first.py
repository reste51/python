"""
    Tokenize and tag some text
"""
import nltk
from nltk import data



# 动态匹配 nltk的data 路径
data.path.append('D:\soft\python\module_packages\\nlp_nltk\\nltk_data\\')

sentence = """
At eight o'clock on Thursday morning Arthur didn't feel very good.
"""
tokens = nltk.word_tokenize(sentence)
print(tokens)

tagged = nltk.pos_tag(tokens)
print(tagged[0:6])


# from nltk.corpus import treebank
# t = treebank.parsed_sents('wsj_0001.mrg')[0]
# t.draw()

from nltk.book import *
text1.generate()
print('*'*100)

# Print random text
# text1.generate()

# print(text4.collocations())

print('*' * 100)

# the distribution of word lengths in a text

wl_list = [len(w) for w in text1]
print(len(wl_list))  # 每个词汇的 长度


# 统计的是  {字符长度: 单词频率个数}；
# 如 (4, 42345), (2, 38513)，  4个字符的单词有42325个
fdist = FreqDist(wl_list)
print(fdist.items())
# 查看 长度为3的单词数量,  占得百分比（频率）- TFw，  总单词数量,  样本数， 最大频率对应的 单词长度数
print(fdist[3],  fdist.freq(3),  len(text1), fdist.N(), fdist.max())


# 单词: 次数, ('Fellow', 24), ('-', 290), ('Citizens', 7), ('of', 7087)
fdist2 = FreqDist([w for w in text4])
print(fdist2.items())









