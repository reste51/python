'''
日期和时间：
    datetime模块， 提供datetime / date / time 类型
'''

from  datetime import  datetime,date,time
dt = datetime(2020,10,25,20,20,12)
print(dt.day,dt.minute)

print(dt.date(),  dt.time())

print('*'*100)
# 格式化字符串
str = dt.strftime('%Y-%m-%d %H:%M:%S')
print(str)


b = ['saw', 'small', 'He', 'foxes', 'six']
# 按照单词的长度进行排序
b.sort(key=len,reverse=True)
print(b)


