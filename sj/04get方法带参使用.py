import  requests
url = 'http://www.baidu.com'

p = {'id':1001}
p2 = {'id':'1001,1002'}   #%2c是asci值为逗号
p3 = {'id':1001,'kw':'北京'}
rq = requests.get(url,params=p)
print('请求：',rq.url)

#print(rq.text)

#获取相应状态码
print('响应状态码：',rq.status_code)

#获取响应信息 文本形式
print('响应信息',rq.text)


#或者
# 10
# 7-85uki nb b m



