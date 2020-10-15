'''
字符串的相关操作
    切片， 及其他方法
'''

str = 'abcdefg'
# 索引值
print(str[4])
print(str[-1]) # 最后面的一个字符

# 切片
print(str[2:5:])  # cde
print(str[:4:2])  # ac, start=0

print(str[::-1]) # 从右向左输出  <-,  reverse

print(str[5:2:-1])  # <-  fed

print(str[4::-1])   # <-  包含end： a ( 闭区间)  edcba

print('='*200)

mystr = 'hello world and bjsxt yunshuxueyuan sxt beijing'

# 找不到会抛异常  raise
print(mystr.index('world'))
print(mystr.rindex('sxt'))  # Return the highest index

print(mystr.find("abc"))  # 找不到会返回-1


# 每个单词的首字母 大写
print(mystr.title())
print(mystr.upper())
