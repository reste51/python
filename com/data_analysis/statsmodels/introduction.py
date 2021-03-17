"""
    下面是一个使用普通最小二乘的简单例子:
"""

import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

# load data
dat = sm.datasets.get_rdataset("Guerry",'HistData').data
# Fit regression model (using the natural log of one of the regressors)
results = smf.ols('Lottery ~ Literacy + np.log(Pop1831)',data=dat).fit()

# inspect the results
print(results.summary())




