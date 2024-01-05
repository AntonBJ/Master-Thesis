
#https://pandas.pydata.org/docs/user_guide/indexing.html#selection-by-label

import pandas as pd
import os

os.getcwd()

df = pd.read_csv("data/rawData.csv", delimiter=',', quotechar='"')

df = df[df["task_2"]=="HATE"]

#ignore entries with  #, http, @
df = df[df["text"].str.contains('#|http') == False]

#remove emojis
df = df.astype(str).apply(lambda x: x.str.encode('ascii', 'ignore').str.decode('ascii'))

df = df.reset_index()  # make sure indexes pair with number of rows

#for index, row in df.iterrows():
#    print(df.loc[index,'text'])
#    print('\n')

for index, row in df.iterrows():
    a = row['text']
    a.split()                          # split, splits the string on delimiter, by default its whitespace
    df.loc[index,'text'] = " ".join(filter(lambda x:x[0]!='@', a.split()))

print(df.head())

df.to_csv("data/processedDataHate.csv")