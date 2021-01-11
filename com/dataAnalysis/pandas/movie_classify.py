"""
    电影的分类情况
    Horror: 恐怖片多少个, Thriller: 惊险小说多少个....

    注： Pd的重要思想:
    1.将去重的每个值作为 一个新的DF(df0)的列-col
    2. 创建一个新的全部标为0的DF shape(原df.shape[0], unique_val_list)
    3. 将每行出现过的value 在df0中对应的index的col 设置为1
    4. df0.sum(axis=0), 求和每列值, 得到结果
"""

import  pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv('./data/IMDB-Movie-Data.csv')
gnere_s = df['Genre']

# print(df['Genre'].head(10))

# 1.1 将每行 中的list 合并为一个 大list  <class 'list'>
row_list = df['Genre'].str.split(',').tolist()  # 结构为 [ ['Horror','Thriller'],[] ]
all_list = [i for j in row_list for i in j]

# 1.2 去重 再转为 list, 准备作为列
unique_val_list = list(set(all_list))

#  2.创建一个新的全部标为0的DFshape(原df.shape[0], unique_val_list)
#  2.1 创建一个二维数组. row_num作为原df.index的数量,  col_num为 unique_val的数量
two_arr= np.zeros((df.shape[0],len(unique_val_list)))
# print(two_arr,two_arr.shape,len(unique_val_list),sep="\n")

# 2.2 创建一个df对象, 列作为unique_val_list, data=two_arr
df0=pd.DataFrame(two_arr,columns=unique_val_list)
# print(df0)

# 2.3 遍历原row_list，依次将每行出现的值 赋值为df0对应行的1
# print(row_list)
# for row in row_list:  # row 为list
for i in gnere_s.index:
    row_val = row_list[i]
    # print(i,row_val)
    # loc_标签的筛选, 筛选行, 列(为一个列表，多个列的选择)
    df0.loc[i,row_val]=1

print(gnere_s.head(2))
# print(df0)

# 3 以每行_求和每列的值
ret_s = df0.sum(axis=0)
# print(ret_s.shape)  # (20,)

# 4.排序, 升序; 因为是Series 只有一列值,因此可以不指定排序的列
# 准备x 和y 轴的数据
ret_s = ret_s.sort_values()
# print(ret_s)
x_arr = ret_s.index
y_arr = ret_s.values

# print(type(x_arr),type(y_arr))

# 5. 绘制bar 图
plt.figure(figsize=(20,8),dpi=80)
plt.bar(x_arr,y_arr,width=0.4,color='orange')  # 传入x,y 轴的数组
# plt.xticks(range(len(x_arr)),x_arr)
plt.show()


