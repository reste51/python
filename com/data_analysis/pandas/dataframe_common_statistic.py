"""
    Pandas 的常用统计方法
"""
import pandas as pd
import numpy as np

df = pd.read_csv('./data/IMDB-Movie-Data.csv')
# print(df.info())

# 获取评分的 平均分
score_mean = df['Metascore'].mean()
print(score_mean)

# 导演的人数
#  col -> list集合 -> set 去重 --> len()  取长度
director_num = len( set(df['Director'].tolist()))
print(director_num)

# 09-统计方法和字符串离散化 --》 02padas的常用统计方法 (05:17)

# Return unique values of Series object
unique_s = df['Director'].unique()
print(len(unique_s))

# 获取 演员的人数_ 列值-> 每行转为一个list
row_actor_list = df['Actors'].str.split(',').tolist()


# 合并元素为list - 成为一个大list
# all_list = []
# 方法1： 初步的两次循环
# for row_list in row_actor_list:
#     for item in row_list:   # 遍历每行list中的每个元素
#         all_list.append(item)

# 方法2：列表方式双层循环(不怎么好理解)_ for j in row_actor_list;   for i in j
all_list = [i for j in row_actor_list for i in j]

# 方法3: numpy 操作;  返回一个一维数组: Return a copy of the array collapsed into one dimension.
# 注： 该方法不能应用, 不能打散为一个数组; [ list(['Topher Grace', ' Anna Faris']), list([])]
# all_list = list( np.array(row_actor_list).flatten())
# print(all_list,type(all_list),sep="\n")

print( np.array(row_actor_list))

unique_actor = set(all_list)
print(unique_actor,len(unique_actor),sep="\n")  # 2394



