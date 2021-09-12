"""
 分词_ 将句子拆分有意义的小部分
"""

from nltk import data
import nltk

data.path.append('D:\soft\python\module_packages\\nlp_nltk\\nltk_data\\')

# 英文分词
sentence = 'Never underestimate the heart of a champion'
tokens = nltk.word_tokenize(sentence)
print(tokens)


# 中文分词
import jieba
seg_list = jieba.cut("我来到北京清华⼤学", cut_all=True)
print("全模式:", "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("我来到北京清华⼤学", cut_all=False)
print("精确模式:", "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("他来到了⽹易杭研⼤厦") # 默认是精确模式
print('新词识别:',", ".join(seg_list))

seg_list = jieba.cut_for_search("⼩明硕⼠毕业于中国科学院计算所，后在⽇本京都⼤学深造")
print('搜索引擎模式：',','.join(seg_list))

# 社交网络语言的分词
tweet = 'RT @angelababy: love you baby! :D http://ah.love #168cm'
print(nltk.word_tokenize(tweet))


