"""
    Tokenize and tag some text
"""
import nltk

# nltk.download()


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
text1.generate()



