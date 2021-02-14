"""
    随机森林：
        是一个包含多个决策树的分类器，并且器输出的类别是由个别树输出的类别众数（投票,占比例大）决定的。

	单个树构建过程：数据集中有_ N个样本，M个特征：
		1. 重复N次， 随机在N个样本中选择一个样本， 注：样本可能存在重复。
		2. 随机在M个特征中选出m 个特征，  m取值范围   0<m<M
		3.因此建立10棵决策树，样本和特征大多不一样。
		4.抽样的方式：随机有返回的抽样， bootstrap 式。
		5.为什么随机抽样？保证每个树的样本及特征不一样。
		6.为什么有放回的抽样？ 保证数据有交集，导致后续无法投票进行决策。

"""
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import GridSearchCV
import pandas as pd


def forest():
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

    # 6.建立随机森林_ 使用参数调优_未使用超参数
    rf = RandomForestClassifier()
    param = {'n_estimators': [5, 10, 20, 40, 60, 100, 120, 200, 300, 500, 800, 1200],
             'max_depth': [5, 8, 15, 25, 30]}
    gs = GridSearchCV(rf, param_grid=param, cv=2)
    gs.fit(feature_train, target_train)

    print(f'精准率为:{gs.score(feature_test, target_test)}')
    print(f'最优参数: {gs.best_params_}')
    print(f'最优得分{gs.best_score_}')
    print(f'数据集大小： {df.shape}')


if __name__ == "__main__":
    forest()
