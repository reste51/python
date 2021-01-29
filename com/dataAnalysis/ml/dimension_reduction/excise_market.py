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

    2.

"""

import pandas as pd

# 使用merge通过关联的特征 合并一张表
aisles_df = pd.read_csv('../data/aisles.csv')
order_products_df = pd.read_csv('../data/order_products__prior.csv')
orders_df = pd.read_csv('../data/orders.csv')
products_df = pd.read_csv('../data/products.csv')


user_product_df = orders_df.merge(order_products_df,on='order_id')  # 3200万
# print(user_product_df[['order_id','user_id','product_id']], type(user_product_df))

# 关联 products表, 获取products_name 和 aisle_id
u_p_aisle = user_product_df.merge(products_df,on='product_id')
# 关联 aisles表, 获取物品类别
all_data_df = u_p_aisle.merge(aisles_df,on='aisle_id')
# 输出结果
print(all_data_df[['user_id','product_name','aisle']])

