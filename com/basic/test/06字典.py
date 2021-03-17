'''
字典通过{}来标识，字典中的数据可变
    字典中的key不可以重复，如果有重复，覆盖之前的值
    value可以重复
    value可以为空
set:没有值的dict
'''

'''
    不可变类型
        string
        tuple
    可变类型：
        dict
        list
        set
'''
# a 为500， value 也可有None值
dict={"a":100,"b":200,"c":300,"a":500,"f":None}
print(dict, type(dict))

# 取值       None --> NoneType
print(dict.get('a'), type(dict['f']))

# 修改值
dict['b'] = dict['b']*9
print(dict)

print('='*100)

# set 操作,  dict无 value
set = {1,2,3,4}
print(set, type(set))
# list -> set
# set = set([1,2,2,1,3,3,4])

set.add(5)
set.add('6')
print(set)

print('='*100)

# 删除操作
del dict['f']
print(dict)
dict.clear()
print(dict)
del dict
print(dict)

# 元素的方法
dict={"a":100,"b":200,"c":300,"a":500,"f":None}
print(len(dict))
print(dict.keys())
print(dict.values())
print(dict.items())

print('+'*100)
# 遍历
for k,v in dict.items():
    print(k,v)

for k in dict.keys():
    print(k,dict[k])












