"""
    朴素贝叶斯:  朴素的含义_各个特征(条件)独立的概率
        该算法一般用于文档分类， 不像k近邻直接推导一个类别, 分析每个特征值的概率，取最大概率的类别。
    ---
    概率基础- P probability：
        1.联合概率：包含多个条件，且所有条件同时成立的概率
            P（A,B) ;  A和B事件同时生成的概率

        2。条件概率：事件B已经发生条件下，A 发生的概率
            P(A |B);  在B事件发生后，A的概率
            特性：P(A1,A2|B) = P(A1|B)P(A2|B)； 注意：此条件概率的成立，是由于A1,A2相互独立的结果

    ----
    通过 分析每篇文档的词汇， 获取重要性的词汇(需使用训练集的分析)， 再来计算每个词在该类别下出现的次数及 出现的总数。
    总结：
        优点:1.准确率高85%以上， 无需调参（alpha 不称为是超参数）。
        缺点： 受 训练集的 特征词汇影响大。
"""
from sklearn.naive_bayes import MultinomialNB
from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer


def naive_bayes():
    """
    朴素贝叶斯进行文本分类
    :return: None
    """
    # 1. 获取数据集
    news_ds = fetch_20newsgroups(data_home='../data/scikit_learn_data', subset='all')

    # 2. 划分训练和测试集
    # 2.1  x_代表特征值，其实就是一篇一篇的文章; y_代表特征值(一个数字， 对应一种类别)
    x_train, x_test, \
        y_train, y_test = train_test_split(news_ds.data, news_ds.target, test_size=0.25)

    # 3.特征处理- 词语重要性分析
    tf = TfidfVectorizer()
    # 3.1 使用训练集(特征)生成重要词汇(特征数据)
    x_train = tf.fit_transform(x_train)  # sparse.csr.csr_matrix 稀疏矩阵, 转为数据
    x_test = tf.transform(x_test)
    # print(f'训练特征值： {x_train.toarray()}, 特征值(重要词汇): {tf.get_feature_names()}')

    # 4. 算法应用, alpha即为拉普拉斯平滑系数，防止某个词(特征)概率为0的处理。
    bayes = MultinomialNB(alpha=1.0)
    # 4.1 fit predict score
    bayes.fit(x_train, y_train)  # fit 传入是 训练集的特征和目标
    # 4.2 生成预测结果，需传入 测试集的特征值  -> 预估 测试集的目标值
    predict_test = bayes.predict(x_test)
    print(f'预测值: {type(predict_test)}, {predict_test}')

    # 4.3 准确度,传入测试集的 特征和目标值来判断评分， 与相反;
    score = bayes.score(x_test, y_test)
    print(f'准确率为{score}')  # 85%


if __name__ == '__main__':
    naive_bayes()
