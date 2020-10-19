'''
异常:
    try -> except -> else ->finally

    其中 except 可以存在多个,  except XE as msg:
    else 与 except 是互斥的关系。

'''
f = None
try:
    print('-----test--1---')
    f = open('123.txt','r')
    print('-----test--2---')
# except IOError :
# 用as 可以使输出更看得懂,保存捕获到的错误信息
# 如果想通过一次except捕获到多个异常可以用一个元组的方式
except (IOError,FileExistsError) as msg:
    print('产生错误了，%s'%msg)
finally: # 类似java
    if(f):
        f.close()

print('-----test-3------')

