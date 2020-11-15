'''
内建数据结构， 函数及文件
'''

# 拆包 中遍历元组的应用
seq = [(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in seq:
    # 使用 {index} _format()
    print('a={0},b={1},c={2}'.format(a,b,c))

# *rest 任意长度的 拆包
a,b,c,*rest = (1,2,3,4,5,6,7,8)
print(rest) # rest 为余下的参数 [4, 5, 6, 7, 8]

# 二分法使用
import bisect
arr = [1,2,2,2,3,4,7]

# 第二个参数为 插入的值，  返回待插入的索引值
insertIndex = bisect.bisect(arr,2)
print(insertIndex)

# 将元素插入指定的位置
# Return the index where to insert item x in list a, assuming a is sorted.
bisect.insort(arr,5)
print(arr)

# 列表切片  slice
seq = [7, 2, 3, 7, 5, 6, 0, 1]
print(seq[1:5],len(seq) )  # 2-5

# 切片的更改
seq[3:4] = [66,6]    # 其实只更新了7的值为66,  6为新增的值
print(seq,len(seq))

print(seq[-4:])  # [5,6,0,1]
print(seq[-6:-2])   # [66, 6, 5, 6]

# 遍历获取索引值, enumerate
for index,value in enumerate(seq):
    print(index,value)

#  zip 列表或序列 依次配对组成一个新的元组
a = [1,2,3]
b = ['a','b','c']
print(list(zip(a,b)))

# dict
dict1 = {'a':'hello','b':'world'}
print(dict1['a'])
dict1['c']='python'
del dict1['a']

print(list(dict1.keys()), list(dict1.values()))

# update 两个字典的合并
dict1.update({'d':'hhh'})
print(dict1)

print('*'*100)

# 从序列中生成字典
mapping = {}
tuple = list( zip(list(range(0,5)),list(range(5,0,-1))) )
for k,v in tuple:
    mapping[k] = v
print(mapping)

# zip 可以接收 range
dict2 = dict(zip(range(0,6), reversed(range(0,6))))
print(dict2)

# 如果存在k则返回值， 没用则返回默认值
defaultVal = dict2.get('a','defaultVal')
print(defaultVal)

print('*'*100)

words = ['apple','bat','bar','atom','book']
by_letter = {}
for word in words:
    letter = word[0]
    # 有letter的key 则无需设置value为[], 默认初始化时添加生效
    by_letter.setdefault(letter,[]).append(word)
print(by_letter)

from collections import  defaultdict
# 设置 默认的value为 List集合
by_letter = defaultdict(list)
for word in words:
    by_letter[word[0]].append(word)
# {'a': ['apple', 'atom'], 'b': ['bat', 'bar', 'book']}
print(dict(by_letter))

print('*'*100)

# 有效 字典的键类型
print(hash('string'))
print(hash((1,2 )))
# print(hash((1,2 ,[1,2]))       # unhashable type: 'list',list 为可变的

# 列表推导式  [expr for val in collection if condition]
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']

# 筛选字符数大于2， 并且转为大写
arr = [word.upper() for word in strings if len(word)>2]
print(arr)

# set,dict 推导式: {key-expr: val-expr for val in collection if condition}
# set
set1 = { len(word) for word in strings}
print(set1)

set2 = set( map(len,strings))
print(set2)

print('*'*100)

loc_mapping = { val:index  for val,index in enumerate(strings)}
print(loc_mapping)




