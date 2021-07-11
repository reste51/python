"""
 pivot table 学习



"""

import pandas as pd
import numpy as np

df = pd.read_excel('../data/sales-funnel.xlsx')

# print(df, df.info(), sep='\n')

# let’s define the status column as a category and set the order we want to view.
df['Status'] = df.Status.astype('category')
df.Status.cat.set_categories(["won","pending","presented","declined"],inplace=True)
# print(df, df.info())

# The simplest pivot table must have a dataframe and an index
p_ret = pd.pivot_table(df, index=['Name'])
print(p_ret)

# ou can have multiple indexes as well. In fact, most of the pivot_table args can take multiple values via a list.
p_ret = pd.pivot_table(df,index=['Name','Rep','Manager'])
print(p_ret)

# easy to change the index
p_ret = pd.pivot_table(df, index=['Manager','Rep'])
print(p_ret)



