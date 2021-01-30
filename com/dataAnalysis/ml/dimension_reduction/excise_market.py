"""
    用户类别的分析(用户喜好， 下次会购买哪些商品？)：
    目标值-- >
               类别
    userId  1   土豪
    userId  2   贫民

    1. 合并所需表 为一张表  , pandas.merge( rel_id)
    products.csv                         商品信息   （product_id_name，aisle_id）
    order_products__prior.csv           订单与商品信息 (order_id,product_id)
    orders.csv                          用户的订单信息 (order_id,user_id)
    aisles.csv                          商品所属具体物品类别  (aisle_id_  name)

    2. 建立类似行和列的数据
        使用交叉表(特殊的分组工具); 指定行和列的分组字段 pd.crosstab(index_col, col)

"""

import pandas as pd
from sklearn.decomposition import PCA

pd.set_option('display.max_columns', None)
root_path = '../data/instacart/'

# 1. 使用merge通过关联的特征 合并一张表
aisles_df = pd.read_csv(f'{root_path}aisles.csv')
order_products_df = pd.read_csv(f'{root_path}order_products__prior.csv')
orders_df = pd.read_csv(f'{root_path}orders.csv')
products_df = pd.read_csv(f'{root_path}products.csv')


user_product_df = orders_df.merge(order_products_df,on='order_id')  # 3200万
# print(user_product_df[['order_id','user_id','product_id']], type(user_product_df))

# 关联 products表, 获取products_name 和 aisle_id
u_p_aisle = user_product_df.merge(products_df,on='product_id')
# 关联 aisles表, 获取物品类别
all_data_df = u_p_aisle.merge(aisles_df,on='aisle_id')
# 输出结果
# print(all_data_df[['user_id','product_name','aisle']])


# 2. 建立类似行和列的数据
#   使用交叉表(特殊的分组工具); 指定行和列的分组字段 pd.crosstab(index_col, col)
cross_tab = pd.crosstab(all_data_df['user_id'],all_data_df['aisle'])
# print(cross_tab,cross_tab.shape)   # [206209 rows x 134 columns], 有134个特征

# 3. 数据稀疏，特征数过多，  值大部分为0 -> 使用主成分分析
pca = PCA(n_components=0.9)  # 信息损失率 90%

# 4. 主成分分析 - 数据降维(特征减少， 适用于 大量的特征数据)
data = pca.fit_transform(cross_tab)
print(data,data.shape)  # 特征值将为  27 个





