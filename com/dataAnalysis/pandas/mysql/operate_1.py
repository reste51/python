"""
    如何在Python中使用Pandas库实现MySQL数据库的读写

    SQLAlchemy提供了SQL工具包及对象关系映射（ORM）工具,模块提供了create_engine()函数用来初始化数据库连接

      三个库：pandas， sqlalchemy，pymysql
      pandas模块提供了pd.read_sql_query（）函数实现了对数据库的查询，df.to_sql（）函数实现了对数据库的写入。并不需要实现新建MySQL数据表。
      sqlalchemy模块实现了与不同数据库的连接，而pymysql模块则使得Python能够操作MySQL数据库。

     参考连接： http://www.361way.com/pandas-myql/6416.html
"""


import  pandas as pd
from  sqlalchemy import create_engine
import  pymysql

# 初始化数据库连接，使用pymysql模块
# MySQL的用户：root, 密码:147369, 端口：3306,数据库：test
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/test')

sql = 'select * from test1'
# Read SQL query into a DataFrame.
df = pd.read_sql_query(sql,engine)

print(df.shape,df.head(2))


# 添加
d = {'id':[17,18], 'name':['scala','python'], 'age':[50,22], 'status':[1,0]}
df_d = pd.DataFrame(data=d)
# print(df_d.dtypes)
df_d.to_sql('test1',engine,index=False,if_exists='append')


# 修改
# update_data = {'id':8, 'name':'Vue','age':20}
# update_data.to_sql('test1',engine,index=False,if_exists='replace')


