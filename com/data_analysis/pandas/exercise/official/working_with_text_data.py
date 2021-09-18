"""
    pandas 处理 字符串的文本；
    文本的数据类型: object(numpy array),  StringDtype(extension type, this is recommend)

    使用 StringDtype的优势: numpy 的object 是混合的，什么类型都有， 不清晰

    参考文档: file:///D:/soft/python/module_package/pandas/doc/1.3.3/user_guide/text.html#text-string-methods
"""

import pandas as pd
import numpy as np


def string_type():

    # 显示指定 的数据类型:  StringDtype/"string"
    # s = pd.Series(['a','b','c'], dtype=pd.StringDtype())
    s = pd.Series(['a', 'b', 'c'], dtype='string')
    print(s, s.str.isdigit())

    # 创建后 可以转换类型
    s1 = pd.Series([1, 2, 3])
    s1 = s1.astype('string')
    print(s1, s1.str.isdigit())

def string_methods():
    """
    Series.str 拥有一些专门处理 这一组字符串的的便捷方法
    包含 Index 其实它就是一个数组
    :return:
    """
    s = pd.Series(
        ["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"], dtype="string"
    )
    print(s.str.lower())
    print(s.str.upper())
    print(s.str.len())


def concatenate_series():
    """
    .str.cat()   一列的字符连接
    :return:
    """
    s = pd.Series(["a", "b", "c", "d"], dtype="string")
    print(s.str.cat(sep=','))  # 使用分割符
    print(s.str.cat())  # 默认使用 '' 分割每个元素

    sa = pd.Series(['a','b',np.nan,1,1.0,'ccc'], dtype=pd.StringDtype())
    # 使用 na_rep处理空值
    print(sa.str.cat(na_rep = '空'))
    print(sa.str.cat(sep=',', na_rep='空值'))


def concatenate_list():
    """
    连接 一个数组
    :return:
    """
    s = pd.Series(["a", "b", "c", "d"], dtype="string")
    print(s.str.cat(['A','B','C','D']))

    s = pd.Series(["a", "a|b", np.nan, "a|c"], dtype="string")
    print(s.str.get_dummies(sep='|'))






if __name__ == '__main__':
    # string_methods()
    # concatenate_series()
    concatenate_list()