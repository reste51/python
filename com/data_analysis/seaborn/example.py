"""
our first seaborn plot
"""

import seaborn as sns

# apply the default theme
sns.set_theme()

# load an example dataset,  网络访问不通
tips = sns.load_dataset('tips')


# create a visualization
sns.relplot(
    data=tips,
    x='total_bill',y='tip', col='time',
    hue='smoker',style='smoker', size='size'
)

