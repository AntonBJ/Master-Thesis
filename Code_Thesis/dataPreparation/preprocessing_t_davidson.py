
#https://pandas.pydata.org/docs/user_guide/indexing.html#selection-by-label

import pandas as pd
import os

os.getcwd()

df = pd.read_csv("data/t-davidson_labeled_data.csv", delimiter=',', quotechar='"')

df = df[df["hate_speech"]==1]

#ignore entries with  #, http, @
df = df[df["tweet"].str.contains('#|http') == False]

#remove emojis
df = df.astype(str).apply(lambda x: x.str.encode('ascii', 'ignore').str.decode('ascii'))

#df = df.astype(str).apply(lambda x: x.str.encode('""', 'ignore').str.decode('ascii'))

df = df.reset_index()  # make sure indexes pair with number of rows

#for index, row in df.iterrows():
#    print(df.loc[index,'tweet'])
#    print('\n')

for index, row in df.iterrows():
    a = row['tweet']
    a.split()                          # split, splits the string on delimiter, by default its whitespace
    df.loc[index,'tweet'] = " ".join(filter(lambda x:x[0]!='@', a.split()))

print(df.head())
print(df.info)

df.to_csv("data/processedData_t_davidson.csv")