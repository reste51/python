#get put post delete head options
#要使用head options方法，必须开发在代码中有这个方法
#注释的快捷键：ctrl+/

#导包
import requests

#调用get
url = 'http://www.baidu.com'
rq = requests.get(url)

#获取请求地址
# print('这是我练习的url：%s , my salary is : %.2f' % (url, 5600.5864))
# print('这是我练习的url：%s'.format( url))
# print(f'这是我练习的url：{url}') #3.6

print('请求：',rq.url)

#print(rq.text)

#获取相应状态码
print('响应状态码：',rq.status_code)

#获取响应信息 文本形式
print('响应信息',rq.text)
