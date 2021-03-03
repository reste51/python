"""
    非监督学习： k-means;  k代表类别的数量， Means 是距离的平均值
    一般用于 分类操作前处理

    聚类评估： 使用 轮廓系数  [-1,1] ;   族群内部距离小，外部距离大 最优。
"""
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
from com.dataAnalysis.ml.feature_project.dimension_reduction.excise_market import pca_data
import os
import matplotlib.pyplot as plt

if __name__ == '__main__':
    print(f'k路径：{os.getcwd()}')
    # 样本数减少111个_注： 使用的是绝对路径,相对路径不知道为啥存在问题
    user_data = pca_data(root_path='E:\excise\python/new_project01\com\dataAnalysis\ml\data\instacart/')
    # 假定给用户分为4个类别, 预测的label为 [0,1,2,3]
    km = KMeans(n_clusters=4)

    # 随机找4个中心点来 聚类
    km.fit(user_data)

    predict_labels = km.predict(user_data)
    # print(predict_labels, predict_labels.shape)

    # 绘制散点图
    color = ['red', 'yellow', 'green', 'gray']
    # 根据对应的索引值来区别不同的类别
    data_color = [color[label] for label in predict_labels]
    plt.figure(figsize=(10, 10))
    # 由于是平面图，x ,y 任选两个特征 [shape_1的选择, shape_2选择];  data[:,10] -> 所有样本, 取第10个特征
    plt.scatter(user_data[:, 1], user_data[:, 10], color=data_color)

    plt.xlabel('one feature')
    plt.ylabel('ten feature')

    plt.show()

    # 聚类评估  [-1,1];  0.6 算比较优质的， 一般不会大于0.7
    silhouette_score = silhouette_score(user_data, predict_labels)
    print(f'轮廓系数为: {silhouette_score}')