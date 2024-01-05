
#https://pandas.pydata.org/docs/user_guide/indexing.html#selection-by-label

import pandas as pd
import os

os.getcwd()

selection_td = [2994,3913,4382,5213,6037,7699,7809,9064,9093,22967]
selection_hasoc = [431,2157,3234]

df1 = pd.read_csv("data/processedData_t_davidson.csv")
df2 = pd.read_csv("data/processedDataHate.csv")

print(df1)

df1 = df1[df1['index'].isin(selection_td)]
df2 = df2[df2['index'].isin(selection_hasoc)]

d_td = {'index_old': df1["index"], 'text': df1["tweet"]}
df_td = pd.DataFrame(data=d_td)

d_hasoc = {'index_old': df2["_id"], 'text': df2["text"]}
df_hasoc = pd.DataFrame(data=d_hasoc)

df = df_td._append(df_hasoc, ignore_index = True)
df = df.reset_index()  # make sure indexes pair with number of rows

df.to_csv("data/selectedData.csv")

print("\n\n")



print(df)


