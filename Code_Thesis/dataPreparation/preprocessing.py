
#https://pandas.pydata.org/docs/user_guide/indexing.html#selection-by-label

import pandas as pd
import os

os.getcwd()

df = pd.read_csv('data/rawData.csv', delimiter=',', quotechar='"')

#ignore entries with  #, http, @
new_df = df[df["text"].str.contains('#|http|@') == False]

#remove emojis
new_df = new_df.astype(str).apply(lambda x: x.str.encode('ascii', 'ignore').str.decode('ascii'))

print(df.size)
print(df.head())

print(new_df.size)
print(new_df.head())

print(new_df.loc[[319]])

new_df.to_csv("data/processedData.csv")
#print(df.info()) 
#print(df.describe(include=["object", "bool"]))

