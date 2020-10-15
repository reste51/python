'''
测试 多行注释
'''
print("hello python")


# 输出关键字
import  keyword
print(keyword.kwlist)

# 输出;  , 输出为 空格
print("hello", 113, "word")

print("--------------------")

# 格式化输出, %d 数字   %s字符串  %f小数
print('%d+%d=%d'%(100,200,300))
print('%s,world'%'Hello')
h = 'Hello '
print('%s , World'%h)

f = 10.672
# .2 为保留2位效数（四舍五入）
print('浮点数: %.1f' %f)