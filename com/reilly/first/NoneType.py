"""
动物书， 基本类型的操作
"""
a = None
print( a is  None)

b = 6
print(b is not  None)

# None 作为常用函数的默认值参数
def add_maybe_multipy(a,b,c=None):
    result = a +b
    if c is not  None:
        result = result *c
    return  result

ret = add_maybe_multipy(2,10,10)
print(ret)
