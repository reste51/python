"""
 pivot table 学习

参考学习的链接:
https://pbpython.com/pandas-pivot-table-explained.html




"""

import pandas as pd
import numpy as np

df = pd.read_excel('../data/sales-funnel.xlsx')

# print(df, df.info(), sep='\n')

# let’s define the status column as a category and set the order we want to view.
df['Status'] = df.Status.astype('category')
df.Status.cat.set_categories(["won","pending","presented","declined"],inplace=True)
print(df, df.info())

# The simplest pivot table must have a dataframe and an index
p_ret = pd.pivot_table(df, index=['Name'])
print(p_ret)

# ou can have multiple indexes as well. In fact, most of the pivot_table args can take multiple values via a list.
p_ret = pd.pivot_table(df,index=['Name','Rep','Manager'])
print(p_ret)

# easy to change the index
p_ret = pd.pivot_table(df, index=['Manager','Rep'])
print(p_ret)

# using values ,it can automatically averages the data,
# averages the data but we can do a count or a sum. Adding them is simple using aggfunc and np.sum .
p_ret = pd.pivot_table(df,index=['Manager','Rep'],values='Price',aggfunc= np.sum)
print(p_ret)

# aggfunc can take a list of functions. Let’s try a mean using the numpy mean function and len to get a count.
p_ret = pd.pivot_table(df,index=['Manager','Rep'], values='Price', aggfunc=[np.sum,len])
print(p_ret)

# I think one of the confusing points with the pivot_table is the use of columns and values .
# Remember, columns are optional - they provide an additional way to segment
# the actual values you care about. The aggregation functions are applied to the values you list.
p_ret = pd.pivot_table(df,index=['Manager','Rep'], values='Price' , columns='Product',aggfunc=[np.sum])
print(p_ret)

# remove the NaN
p_ret = pd.pivot_table(df,index=['Manager','Rep'], values='Price',
                       columns='Product',aggfunc=[np.sum], fill_value=0)
print(p_ret)





