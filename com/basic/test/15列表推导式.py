'''
指的轻量级循环创建列表

'''

a = [i for i in range(1,11)]
print(a)

# 在循环的过程中使用if 来确定 列表中元素的条件
a2 = [i for i in range(1,11) if i%2==0]
print(a2)

# 多个 条件的筛选
a3 = [i for i in range(1,11) if i%2==0 if i<6]
print(a3)

# 两个 for 循环
a4 = [(i,j) for i in range(0,10) for j in range(0,100)]
print(a4)
print(len(a4))

# 三个 for 循环
a5 = [(i,j,k) for i in range(0,10) for j in range(0,20)  for k in range(0,30)]
print(len(a5))
print(a5)

# 使用set 自动去重
a6 = [{i,j,k} for i in range(0,10) for j in range(0,20)  for k in range(0,30)]
print(len(a6))
print(a6)

# 使用字典自动去重
a6 = [{i:j,j:k} for i in range(0,10) for j in range(0,20)  for k in range(0,30)]
print(len(a6))
print(a6)


