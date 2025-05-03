#lab2
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

df_can = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.csv')

df_can.head()

df_can.set_index('Country', inplace=True)
df_can.index.name = None
years = list(map(str, range(1980, 2014)))

# LINE CHARTS

haiti = df_can.loc['Haiti', years] # passing in years 1980 - 2013 to exclude the 'total' column
haiti.index = haiti.index.map(int) 
haiti.plot(kind='line')
plt.title('Immigration from Haiti')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
plt.text(2000, 6000, '2010 Earthquake') # see note below
plt.show() 

CandI = df_can.loc[['China','India'],years]
CandI = CandI.transpose()
CandI.plot(kind='line')
CandI.index = CandI.index.map(int)
plt.title('Immigrants from China and India')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
plt.show()

df_top5 = df_can.nlargest(5, 'Total')
df_top5 = df_top5[years].transpose()
df_top5.index = df_top5.index.map(int)
df_top5.plot(kind='line', figsize=(14, 8))
plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
plt.show()

#Area Plots, Histograms, and Bar Charts


           
           
           
           
           
        
        











