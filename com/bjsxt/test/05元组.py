'''
元组通过（）来标识，元组中的数据不可变
'''

tuple = (1,2,True,'a',1.23)
print(tuple)

# 通过索引取值
print(tuple[1])

# 注: 当元组里 只有一个元素时, 使用(1,)
# tuple = (1) # <class 'int'>
tuple = (1,)
print(type(tuple))

'''
元素内的 引用地址不可改变， 但 如序列内的元素可以改变
'''
tuple = [1,2,3,['a','b','c']]

# 更改引用序列的 某个元素
tuple[3][1] = 'B'
print(tuple)

# 但不可改变 元素引用的地址
tuple[3] = [1,2,3,4,5]
print(tuple)

