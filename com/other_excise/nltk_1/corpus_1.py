"""
    词袋语义分析
"""

import nltk
from nltk.corpus import stopwords

def unusual_words(text):
    """
    获取 不常用的词 或 拼写错误的词汇
    :param text:   一组单词
    :return:
    """
    # 获取 是单词并去重
    text_vocab = set(s.lower() for s in text if s.isalpha())
    english_vocab = set(s.lower() for s in nltk.corpus.words.words())
    unusual = text_vocab.difference(english_vocab)
    print(len(unusual))
    return sorted(unusual)

def stop_words():
    """
    停用词， 常用的 a the  啊 这 那， 没有实际语义，只是增加连贯性
    :return:
    """
    print(stopwords.words('english'))



if __name__ == '__main__':
    unusual_word = unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt'))
    print(unusual_word)
    print(unusual_words(nltk.corpus.nps_chat.words()))




