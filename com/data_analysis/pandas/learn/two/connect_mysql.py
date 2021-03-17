'''
连接 mysql 处理
'''

import  pandas as pd
from sqlalchemy import create_engine

con = create_engine('mysql+pymysql://root:123456@localhost:3306/test')

sql = ' select * from person'
df = pd.read_sql(sql,con)

print(df)
print(df.shape)

