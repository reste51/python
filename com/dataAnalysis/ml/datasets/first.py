"""
    从Sklearn 获取数据， 进而通过 sklearn.model_selection.train_test_split的 数据集划分。
    1. 分类数据集： 目标值为 离散的(前50个为0, 中50个为1,xxxx;  1 和0 代表一个类别,通过 DESCR属性来获取)
    2. 回归数据集:  目标值为 连续的(房价, 每个房子_特征值 都对应一个 房价_目标值, 50-100万)

    注： train_test_split的划分数据集时，顺序是无序，乱序的。
"""
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris,fetch_20newsgroups

# 1.离散_鸢尾花的_获取小规模数据集，数据包含在datasets里
# 特征为4， 样本数:150;    类别：3，每个类别的目标值为 50个
# ds = load_iris()

# 特征数据数组，是 [n_samples * n_features] 的二维numpy.ndarray 数组
# print(f'特征值数据：{ds.data}')

# 目标值数组，是 n_samples 的一维 numpy.ndarray 数组
# print(f'目标值数据：{ds.target}')
# print(f'鸢尾花描述信息：{ds.DESCR}')

# 训练和测试集划分; 传入 特征值,目标值, 测试集的比例
# 训练集特征值，测试集特征值，训练目标，测试目标(默认随机取)
# train_features,test_features,\
#     train_target,test_target = train_test_split(ds.data,ds.target,test_size=0.25)

# print(f'特征值:{train_features}\n ************ {test_features}')
# print(f'目标值:{train_target}\n {test_target}')


# 2.目标值连续_适合回归算法_ 房价预测;
#   注：会从网络下载, 先会从网络下载*.tar.gz->解压 -> 抽取内容到20news-bydate_py3.pkz; 比较智能
# subset: 'train'或者'test','all'，可选，选择要加载的数据集.
# datasets.clear_data_home(data_home=None)  清除目录下的数据

ds_continually = fetch_20newsgroups(data_home='../data/scikit_learn_data',subset='all')

print(f'特征值： {ds_continually.data}')
print(f'目标值： {ds_continually.target}')
print(f'描述信息: {ds_continually.DESCR}')


