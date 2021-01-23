"""
pandas读写带变更的mysql数据

"""
import  pymysql
import pandas as pd
from sqlalchemy import create_engine

# 拼接语句  需要传入不同的变量的SQL写入或查询。遇到这种情况该如何解决呢？可以使用format函数来实现转化。
tablename='sdata'
startdate='2019-04-01'
endDate='2019-04-18'
sql = "delete from {} where str_to_date(ts,'%Y-%m-%d') between '{}' and '{}' "
sqlformat = sql.format(tablename, startdate, endDate)  # 会把fromat的大括号内容替换为变量内容
print(sqlformat)


# 就是有两个表：table1、table2。
# 需要将表1中的某个时间段的数据采集后写入表2，但表2中也有该时间段的数据（没有表1中的全），需要先删除表2中该时段的数据后，才执行写入

# 将数据库中的表读成数据框df（给定表名和起止时间）
def read_mysql(tablename,startdate,endDate):
    db = pymysql.connect("localhost", "root", "123456", "test")
    sqlcmd='select * from %s' % tablename+' where date_format(ts,"%Y-%m-%d") between'+"'"+startdate+"'"+' and '+"'"+endDate+"'"
    df=pd.read_sql(sqlcmd,db,index_col='index')
    return  df


# 将给定时间段的df写到数据库中的给定表
def write_df_to_table(df,tablename,startdate,endDate):
    db = pymysql.connect("localhost", "root", "123456", "test")# 数据库配置信息
    cursor = db.cursor()
# 先删除给定时间段的数据，防止重复，{}为变量占位符，下面三句是执行含有变量参数的核心代码
    sql="delete from {} where date_format(ts,'%Y-%m-%d') between '{}' and '{}' "
    sql1=sql.format(tablename,startdate,endDate)# sql语句动态变量转化函数
    cursor.execute(sql1)
# 执行删除操作后一定要提交，否则后面写入时会出现pymysql.err.InternalError1205报错
    db.commit()
    yconnect = create_engine('mysql+pymysql://root:123456@localhost:3306/test?charset=utf8')
    pd.io.sql.to_sql(df, '%s' % tablename, yconnect, schema='test', if_exists='append')
    db.commit()

# 将表user_test01时间段的数据读成数据框
# df1=read_mysql('user_test01','2019-04-01','2019-04-03')
#print(df1)

# 将上述数据框df1写到表user_test2（先删除该时间段数据后在写进）
# write_df_to_table(df1,'user_test2','2019-04-01','2019-04-03')

# 同样的，连时间参数我们也可以通过变量进行替换。比如我想要取三天前的日期和时间，代码如下：
import time
import datetime
# 先获得时间数组格式的日期
threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days = 3))
# 转换为时间戳
timeStamp = int(time.mktime(threeDayAgo.timetuple()))
# 转换为其他字符串格式
otherStyleTime = threeDayAgo.strftime("%Y-%m-%d %H:%M:%S")
print(otherStyleTime, timeStamp, type(threeDayAgo))
print(datetime.datetime.now(),datetime.timedelta(days = 3))


