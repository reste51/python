'''
How to create new columns derived from existing columns?

'''

import pandas as pd
air_quality = pd.read_csv('../../../data/air_quality_no2.csv',index_col=0,parse_dates=True)

print(air_quality.head())

# create new column
air_quality['london_new_col'] = air_quality['station_london']*1.882
print(air_quality.shape)


#
# air_quality_renamed = air_quality.rename(
#    ...:     columns={"station_antwerp": "BETR801",
#    ...:              "station_paris": "FR04014",
#    ...:              "station_london": "London Westminster"})
