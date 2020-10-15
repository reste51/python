'''
通过 符号来标识各种数据结构
    使用[] 标识列表

    增加：
        append
        insert
        extend

    删除：
        pop
        remove
        del
    sort 使用元素的类型要一致

'''
list=["abcd",123,True,123.345]
list2=["q","w",["e","r"]]

# 取尾部的元素
print(list[-1])

# 切片 ,  reverse 反转
print(list[::-1])

# 遍历每个元素
for i in list:
    print(i)

print('=======================')

# 遍历每个元素 和  索引
for k,v in enumerate(list):
    print(k,v)

# print(type(enumerate(list)))
# print(type(list))

print('=======================')

# 添加
list.append("qwer")
list.insert(2,'hello')

list.extend(list2) # 相当于java的addAll 添加集合到尾部

# 修改集合内的元素
list[0] = 'world'
print(list)

print('=======================')

# index, 查找的值,start(闭),end(开)
# 如果没有找到则 ValueError: 123 is not in list
print(list.index(123,0,2))

# 查找 字符串出现的个数
print(list.count('hello'))

# 删除元素
list.remove(True)
print(list)

popVal = list.pop(2)
print(popVal, list)

del  list[-1]
print(list)

list.reverse()
print(list)

# 排序
list=[5,2,4,3,1]
list.sort(reverse=True)
print(list)

# 符号的相加
list = [1,2,3]
list += list
print(list)
