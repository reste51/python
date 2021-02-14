"""
    决策分类树： 信息增益，作为分类依据之一。

"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier, export_graphviz


def test():
    # 1. 读取数据
    df = pd.read_csv('../data/titanic/titanic.csv')

    # 2. 获取 特征值和目标值
    feature_df = df[['Age', 'Pclass', 'Sex']]
    target_series = df['Survived']

    # 3. 特征值age 使用平均值填补空值
    feature_df.fillna(df['Age'].mean(), inplace=True, axis=1)
    # print(feature_df.head(10), target_series.head(10), feature_df.info(), sep='\n')

    # 4. 分割数据集
    feature_train, feature_test, \
    target_train, target_test = train_test_split(feature_df, target_series, test_size=0.25)

    # 5.特征工程， 将 sex字符串的类别转为one-hot编码: sex=male,sex=female ; 1为是， 0为否
    dv = DictVectorizer(sparse=False)  # 设置 ndarray数值矩阵类型， sparse 打印是一个 tuple
    feature_train = dv.fit_transform(feature_train.to_dict(orient='records'))
    feature_test = dv.transform(feature_test.to_dict(orient='records'))
    print(dv.get_feature_names(), feature_train, sep='\n')

    # 6. 定位决策树
    dtc = DecisionTreeClassifier(criterion='gini')
    dtc.fit(feature_train, target_train)

    score = dtc.score(feature_test, target_test)
    print(f'决策树精准率为: {score}')  # 84.7%

    # 7.树的可视化展示
    # 7.1 生成 tree.dot 文件
    export_graphviz(dtc, out_file='./tree.dot',feature_names=['Age', 'Pclass', 'Sex=female', 'Sex=male']) # 注:生成不支持中文
    # 7.2 先安装graphviz, 运行命令: dot -Tpng tree.dot -o tree.png ; 详情参考: dot -help


if __name__ == '__main__':
    test()
