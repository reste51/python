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

print('~'*100)

'''
查找字符串的唯一要素
以下代码可用于查找字符串中所有的唯一要素。
我们使用其属性，其中一套字符串中的所有要素都是唯一的。
'''
my_string = "aavvccccddddeee"
# converting the string to a set, 去重每个字符
temp_set = set(my_string)
# stitching set into a string using join
new_string = '.'.join(temp_set)
print(new_string)

print('.'*100)

'''
将字符串拆分成子字符串列表
通过使用.split方法，可以将字符串分成子字符串列表。还可以将想拆分的分隔符作为参数传递。
'''
string_1 = "My name is Chaitanya Baweja"
string_2 = "sample/ string 2"
# default separator
print(string_1.split(' '))
# [ My , name , is , Chaitanya , Baweja ]
# defining separator as /
print(string_2.split( '/' ))
# [ sample , string 2 ]

'''
检查唯一性
以下函数将检查一个列表中的所有要素是否唯一。
'''
def unique(l):
    if len(l)==len(set(l)):   # 每个元素 无重复
        print("All elements are unique")
    else:           # 存在重复数据
        print("List has duplicates")
unique([1,2,3,4])
# All elements are unique
unique([1,1,2,3])
# List has duplicates





