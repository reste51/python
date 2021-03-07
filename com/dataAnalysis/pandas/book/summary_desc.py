"""
    常用数学和统计学方法的集合。  归约和汇总统计的类别，从DF的行或列抽取一个Series 或单个值

"""
import numpy as np
import pandas as pd

df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]],
                  index=['a','b','C','D'],columns=['Q','W'])
print(df)

print('*'*100)

# 以列分组，合并每行的数据; 返回 Series; 每列名作为index
sum_df = df.sum()
print(sum_df)

# 以每行分组， 合并每列
rows_df = df.sum(axis=1)
print(rows_df)

# 积累型, 最后一行是之前所有行的合计
cum_ret = df.cumsum()
print(cum_ret)

# 多种合计_ 适合数值类型的列
print(df.describe())
print('*'*100)

# 非数值的汇总信息
# count     16
# unique     3
# top        a
# freq       8   频率_不清楚怎么计算的
s = pd.Series(['a', 'a', 'b', 'c']*4)
print(s.describe(), s)

print('*0'*100)

# 相关性和协方差
# 注:需要安装 pip install pandas-datareader 从yahoo下载数据
import pandas_datareader as web
# 生成{'AAPL':data,'IBM':data2, 'GOOG':data3 }
all_data = {ticker:  web.get_data_yahoo(ticker) for ticker in ['AAPL','IBM','MSFT','GOOG']}

# 生成{'AAPL':data['Adj Close'],'IBM':data2['Adj Close'], 'GOOG':data3['Adj Close'] }
price = pd.DataFrame( {ticker: data['Adj Close'] for ticker,data in all_data.items()})
volume = { ticker: data['Volume'] for ticker,data in all_data.items()}

# 股价百分比
returns = price.pct_change()
print(returns.tail())
