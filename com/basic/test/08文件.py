'''
文件操作
'''
path = 'E:\documents\spark_pom.xml'
f = open(path)
content =f .read()
print(content)

print(f.tell() ) # 指针位置
f.seek(0,0)  # 重置指针的位置

print('-'*100)

content = f.readline()
print(content)

f.seek(0,0)  # 重置指针的位置
content = f.readlines()
for line in content:
    print(line.replace('\n',''))
f.close()


# 创建 并能写入内容的文件
path = 'E:/documents/temp.xml'
f = open(path,mode='x',encoding='utf8')
f.write('这是测试内容\n')
f.write('这是第二行\n')
f.write('这是结尾')

f.close()

# import os
# 执行 shell命令
# os.system('dir')