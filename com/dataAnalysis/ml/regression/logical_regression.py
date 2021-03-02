"""
    逻辑回归-输入线性值 - 癌症预测_ 输出二分类。
    损失函数： 对数似然函数
    sigmoid函数输出 [0-1]的值 也是正例的概率值

    正例和反例，  判断依据是 数量大小， 小的为正例

"""

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import numpy as np
import pandas as pd


def read_data():
    """
    读取数据- 返回特征值和目标值
    target: 2 为良性， 4 为恶性
    :return: None
    """
    colums = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size',
              'Uniformity of Cell Shape', 'Marginal Adhesion', 'Single Epithelial Cell Size',
              'Bare Nuclei', 'Bland Chromatin', 'Normal Nucleoli', 'Mitoses', 'Class']
    # 注：如果不指定列名，默认会使用第一行作为列; names 指定列名
    df = pd.read_csv('../data/wisconsin/breast-cancer-wisconsin.data',
                     names=colums)

    # 空值处理 ? -> np.nan;
    # null_feature = df[colums[-5]]    # 注： 不能通过引用判断,因为删除时使用 inplace更换新引用值
    print(f'删除前的shape{ df[colums[-5]].shape}') # null_feature.isin(["?"])   注:isin 不能传递str,只能传递array like []
    df.replace('?', np.nan, inplace=True)
    df.dropna(axis=0,inplace=True)
    print(f'删除后的shape{ df[colums[-5]].shape}')

    return df[colums[1:10]], df[colums[10]]


if __name__ == '__main__':
    X, y = read_data()

    X_train, X_test, \
        y_train, y_test = train_test_split(X, y)

    # 标准化处理特征值， target 由于是分类类别无需处理
    x_std = StandardScaler()
    X_train_scaled = x_std.fit_transform(X_train)
    X_test_scaled = x_std.transform(X_test)

    lr = LogisticRegression(penalty='l2')
    lr.fit(X_train_scaled,y_train)

    # 由于是分类问题，因此可以有 精确率(无参考价值)/ 召回率(是否查的全)等因素
    score = lr.score(X_test_scaled,y_test)
    # print(f' 逻辑回归预测精准率为:{score}')
    y_predict = lr.predict(X_test_scaled)
    # 以 恶性作为正例， 召回率为 0.97, 有3个人没有识别出来。
    report = classification_report(y_test,y_predict,labels=[2,4],target_names=['良性','恶行'])
    print(report)


