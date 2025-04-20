#dv lab 1
import numpy as np
import pandas as pd

df_can = pd.read_excel(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx',
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)

print('Data read into a pandas dataframe!')

df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)

df_can['Total'] = df_can.sum(axis=1, numeric_only=True)

df_can.head()


df_can.set_index('Country', inplace=True)
df_can.index.name = None
    
df_can.columns = list(map(str, df_can.columns))

years = list(map(str, range(1980, 2014)))

condition = df_can.loc[:,'1980':]==16
#condition = df_can['1980']==16
print(condition)
df_can[condition]

#show any columns with a number == to somethign i want
df_can[(df_can.loc[:,'1980':'2013']>22000).any(axis=1)]

df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)
df_can.head(5)
