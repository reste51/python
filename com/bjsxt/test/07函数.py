'''
函数由四部分组成：
    名称
    函数体
    参数列表
    返回值
1.定义必须以 def 开头
2.名称+（参数列表） 调用
3.函数的参数列表不需要定义类型
4.python 没有重载， 重名的函数会覆盖前面的
5.函数的参数列表可以带默认值，调用不指定参数则使用默认值; 有参数则覆盖默认值
6.函数调用的时候，可以带参数名称传值， 按名称进行匹配，不是按照顺序
'''

def add():
    print('add')

add()

# 带参数的函数
def add(a,b):
    print('%d+%d=%d'%(a,b,a+b))

add(10,20)
# add()  # 覆盖了之前的函数声明

# 带默认值参数的函数
def add(a=100,b=200):
    print('%d+%d=%d'%(a,b,a+b))

add(1,2);

# 不定长参数
'''
*arg： 表示一组值的集合， 普通数据
**kwargs: k-v格式的数据, dict 字典; a1=12,b2=23
'''
def func(a,b,*args,**kwargs):
    print("a=", a)
    print("b=",b)
    print("*args=",args)
    print("**kwargs=",kwargs)
    for k,v in kwargs.items():
        print(k,v)

func(1,2,3,4,5,a1=12,b2=23)

# 带返回值的函数， 可以返回多个值(tuple)类型的
def func2(a,b):
    return a+b,a-b,a*b
# 分别赋值每个变量
ret1,ret2,ret3 = func2(10,20)
print(ret1,ret2,ret3)

print('[]'*200)

'''
全局变量： 定义方法外的变量
局部： 方法内的变量

全局变量可以在方法中使用
在方法中不可以改变全局变量的值（加上global可以改变值）
不能在global前定义同名的局部变量
'''

count=100
def fun():
    # count = 200  # 单独声明的局部变量
    # print(count)
    global count    # 使用global不能在前面 声明同名的局部变量
    print(count)
    count = 20
    print(count)
print(count)
fun()
print(count)

print('递归函数'*10)

'''
斐波那契数列
1，1，2，3，5，8，13，21，34，55
'''
def getNum(num):
    if(num<=2):  # 1和2 对应的数字均为1
        return 1
    else:
        return getNum(num-1)+getNum(num-2)

print(getNum(10))

# 输出序列
for i in range(1,11):
    print(getNum(i),end='\t')

print('匿名函数' * 10)
'''
lambda 参数列表: 函数体
用途：
    1.当作函数的参数
    2.当作内置参数使用
'''
sum = lambda a,b: a+b
print(sum(10,20))

def func(a,b, callback):
    print(a)
    print(b)
    print(callback(a,b))

# 作为参数 传递
func(1,2,lambda a,b:a+b)
func(1,2,lambda a,b:a-b)
func(1,2,lambda a,b:a/b)
func(1,2,lambda a,b:a*b)

dict = [ {"name":"zhangsan", "age":18}, {"name":"lisi", "age":19}, {"name":"wangwu", "age":17} ]
dict.sort(key=lambda item:item['age'],reverse=True)
print(dict)

