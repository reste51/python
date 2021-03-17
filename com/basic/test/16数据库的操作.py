'''
操作mysql 数据库
'''

from pymysql import *

connection = None
try:
    connection = connect("localhost",'root','123456','test',3306)
    # 得到一个可以执行SQL语句的光标对象
    cursor = connection.cursor()

    # 插入多条记录,  注: 不能使用 %d 否则执行executemany 格式化会报错, 替换为 %s
    sql = 'insert into test1 (id,name,age,status) values(%s,%s,%s,%s)'
    data = [
        ("4","hive",32,1),
        ("5","spark",22,1),
        ("6","hbase",42,0)
    ]
    # insertCount = cursor.executemany(sql, data)
    # print(insertCount)



    # 查询数据
    sql = 'select * from test1 where age > 10'
    cursor.execute(sql)

    # 遍历结果集
    rowList = cursor.fetchall()
    print('查询总条数: %d'%len(rowList))
    for row in rowList:
        print(row)

    # 事务提交
    connection.commit()
    cursor.close()
except (Error,TypeError) as e:
    print('连接出错: %s', e)
finally:
    if(connection):
        connection.close()


