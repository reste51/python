'''
标准输入, 注：输入的都是字符串，匹配时需要转化类型
'''
# age = input("请输入年龄")
# age = int(age)
# if(age<=12):
#     print("少年")
# elif(age <=20):
#     print("青年")
# else:
#     print("老年")


'''
累加 1-100 的和
'''
sum = 0
# for i in range(1,101):
#     sum += i
# print(sum)

# temp = 0
# while (temp<=100):
#     sum += temp
#     temp+=1

# print(sum)

# for , 第三个参数为 步长
# for i in range(0,10,2):
#     print(i)

# 字符串的字符遍历
# for i in "Hello":
#     print(i)

# 九九乘法表
# i =1
# while i<10:
#     j=1
#     while j<=i:
#         # 手工设置分隔符, 默认为 \n
#         print('%d*%d=%d'%(i,j,i*j),end='\t')
#
#         if i==j: # 相等 换行
#             print()
#         j+=1
#     i+=1

for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
        if i==j:  # 相等 换行
            print()




