#dataset link: https://www.kaggle.com/datasets/hasibalmuzdadid/asia-cup-cricket-1984-to-2022?resource=download
#importing pandas lib to support dataframes and plotting graphs
import pandas as pd
import numpy as np
#read data from csv
asia_cup_cricket_data = pd.read_csv("asiacup.csv")
#print top 5 rows
asia_cup_cricket_data.head()
#transform the year column to increase the year by 1
asia_cup_cricket_data['Year'] = asia_cup_cricket_data['Year']+1
# describe all the number fields
asia_cup_cricket_data.describe(include=[np.number])
#plot year and run rate
asia_cup_cricket_data.plot(x ='Year', y='Run Rate')
#plot year and fours in scatter
asia_cup_cricket_data.plot(x='Year', y='Fours', kind = 'scatter')
