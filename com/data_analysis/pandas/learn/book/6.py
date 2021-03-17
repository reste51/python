'''
    Data Loading, Storage
'''

import numpy as np
import  pandas as pd

path = '../../../data/example/ex1.csv'
df = pd.read_csv(path)
print(df)

df = pd.read_table(path,sep=',')
print(df)

print('*'*100)
print(pd.read_csv(path,header=None))

print('*'*100)

# 指定列名
print(pd.read_csv(path,names=['a1', 'b1', 'c1', 'd1', 'message']))

print('*'*100)

# writing data to text format
path = '../../../data/example/ex5.csv'
data = pd.read_csv(path)

writePath = '../../../data/example/out/out1.csv'
# data.to_csv(writePath)
# data.to_excel(writePath)


print('*'*100)

# JSON Data
obj = """
{"name": "Wes",
 "places_lived": ["United States", "Spain", "Germany"],
 "pet": null,
 "siblings": [{"name": "Scott", "age": 30, "pets": ["Zeus", "Zuko"]},
              {"name": "Katie", "age": 38,
               "pets": ["Sixes", "Stache", "Cisco"]}]
}
"""
import json
result = json.loads(obj)

# 提取json 数据作为DF
jsonDf = pd.DataFrame(result['siblings'],columns=['name','age'])
print(jsonDf)

asjson = json.dump(result)
print(asjson)
