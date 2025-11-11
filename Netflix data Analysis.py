import pandas as pd
import os

#Column Names
''''show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added',
       'release_year', 'rating', 'duration', 'listed_in', 'description'''


if os.name=='nt':
    _= os.system('cls')

#Loads info into a dataframe
df = pd.read_csv("netflix_titles.csv")

#Cleaning data
df.iloc[int(0)]
df['date_added']= pd.to_datetime(df['date_added'], errors='coerce')
df.columns= ['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added',
       'release_year', 'rating', 'duration', 'listed_in', 'description']
for c in df.columns:
    c.replace(' ','_')


#Displays data
#df.info()
df.describe(include='all').T
print(df.head())

