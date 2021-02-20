from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

"""
    使用线性回归的方式来波士顿房价预测：
    1. 获取数据集
    2. 分割数据集
    3. 数据标准化 - 分别实例化两个feature 和target的 scalar对象
    4. estimator - 正规方程(样本数小于100k)和 梯度下降(大于100k)

"""


def boston():
    """
    预测房价
    :return: None
    """
    # 1.获取数据集  (506, 13)
    lb = load_boston()


    # 2. 分割数据集
    x_train, x_test, \
     y_train, y_test = train_test_split(lb.data, lb.target, test_size=0.25)

    # 3. 标准化处理 - 分别实例化两个feature 和target(他们shape不同) scalar对象
    # 注; Expected 2D array, got 1D array instead:， 目标值需要1维 转为 2维处理; array.reshape(-1, 1) if your data has a single feature or array.reshape(1, -1) if it contains a single sample
    y_train = y_train.reshape(-1, 1)  # 注: -1 代表样本数无穷大， 1 代表列值为1个
    y_test = y_test.reshape(-1, 1)

    x_std = StandardScaler()
    x_train = x_std.fit_transform(x_train)  # 3.1 先处理 feature 值_ 均已train的目标计算 处理
    x_test = x_std.transform(x_test)

    y_std = StandardScaler()  # 3.2 再处理 target 值
    y_train = y_std.fit_transform(y_train)
    y_test = y_std.transform(y_test)

    # 4. estimator 估计器处理. 梯度下降
    sgd = SGDRegressor()
    sgd.fit(x_train, y_train)  # 4.1 传入 train

    # 4.2, 传入test的特征值;  注： 回归算法没有score精准率， 只有误差值
    y_predict = sgd.predict(x_test)

    # 5. 回归的评估_ 使用均方差的方式  需转为原始值比较， 如果使用标准化后的数据, 小数很难看清
    y_predict_origin = y_std.inverse_transform(y_predict)
    y_true_origin = y_std.inverse_transform(y_test)
    lost_value = mean_squared_error(y_test, y_predict)

    # 6 需要将标准化后的值还原为 之前的值格式; 看了下 误差值为3左右;  权重值与特征数一样
    print(f'梯度下降_预测的房价值为： {y_predict_origin}，'
          f' 真实值为:{y_true_origin}, 权重值: {sgd.coef_}，均方差值为：{lost_value}')

    # 7. 使用正规方程的方式评估
    lr = LinearRegression()
    lr.fit(x_train, y_train)

    y_predict_lr_origin = y_std.inverse_transform(lr.predict(x_test))
    lost_value_lr = mean_squared_error(y_true_origin, y_predict_lr_origin)
    print(f'正规方程_预测的房价值为： {y_predict_lr_origin}，'
          f' 权重值: {lr.coef_}，均方差值为：{lost_value_lr}')

    return None


if __name__ == '__main__':
    boston()
