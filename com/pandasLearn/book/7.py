'''
    Data cleaning and Preparation
'''

import numpy as np
import pandas as pd


# PREVIOUS_MAX_ROWS = pd.options.display.max_rows
# pd.options.display.max_rows = 20
# np.random.seed(12345)
# import matplotlib.pyplot as plt
# plt.rc('figure', figsize=(10, 6))
# np.set_printoptions(precision=4, suppress=True)

# Handling Missing Data
string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'])
print(string_data.isnull())

# 数据离散化 与 装箱
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]

# 根据18-25  2-35 等若干组
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages,bins)

print(cats.codes)
print(cats.categories)
