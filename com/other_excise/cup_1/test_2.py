import gopup as gp

baidu_df = gp.covid_baidu(indicator='热搜谣言粉碎')
print(baidu_df, baidu_df.shape, sep='\n')



