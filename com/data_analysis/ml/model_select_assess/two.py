"""
    模型的选择和评估
    1. 消除过拟合的现象，在训练集中(小范围,重复样本)表现很好，但在测试集中不行的现象。

"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm

# 导出莺尾花的数据
X, y = datasets.load_iris(return_X_y=True)
print(X.shape, y.shape)  # (150, 4) (150,), 4个feature, 150个samples

# 分为 训练和测试集, X为feature, y 为 target
X_train, X_test, \
    y_train, y_test = train_test_split(X, y)

print(X_train.shape, X_test.shape)  # train (112, 4) (38, 4)
print(y_train.shape, y_test.shape)  # target (112,) (38,)

clf = svm.SVC(kernel='linear',C=1).fit(X_train,y_train)
score = clf.score(X_test,y_test)
print(score)



