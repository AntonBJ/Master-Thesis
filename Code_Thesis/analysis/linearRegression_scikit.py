import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

#load data
df = pd.read_csv('C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/completeData/data.csv')
#remove NaN
df = df[df['unac'].notna()]
#remove Trick Questions
df = df[df['sample']!='trickQuestion']
df['gender'].replace(['Female','Male'],[0,1],inplace=True)
df['synthetic_voices'].replace(['No','Yes'],[0,1],inplace=True)
df['negative_experience'].replace(['No','Yes'],[0,1],inplace=True)
df['agree_definition'].replace(['No','Yes'],[0,1],inplace=True)
df['voice_gender'].replace(['f','m'],[0,1],inplace=True)

x = df[['gender','age','pre_happy','post_happy','synthetic_voices','daily_encounter','negative_experience','agree_definition','voice_gender','google_pitch','pitch_weighted']]
y = np.sqrt((df['unac']**2)+(df['cons']**2))
x, y = np.array(x), np.array(y)

model = LinearRegression().fit(x, y)

r_sq = model.score(x, y)
print(f"coefficient of determination: {r_sq}")

print(f"intercept: {model.intercept_}")

print(f"coefficients: {model.coef_}")