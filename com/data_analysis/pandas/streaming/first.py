"""
    pandas_streaming aims at processing big files with pandas, too big to hold in memory,
    too small to be parallelized with a significant gain. The module replicates a subset of pandas API
    and implements other functionalities for machine learning.
"""
import pandas as pd
df = pd.DataFrame([dict(cf=0, cint=0, cstr="0"),
                       dict(cf=1, cint=1, cstr="1"),
                       dict(cf=3, cint=3, cstr="3")])

from pandas_streaming.df import StreamingDataFrame
sdf = StreamingDataFrame.read_df(df, chunksize=1)

for df in sdf:
    # process this chunk of data
    # df is a dataframe
    print(df, type(df))





pd.Series.where