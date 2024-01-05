import pandas as pd
import numpy as np
#from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from scipy import stats

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

#agree definion has only one value. Only use variables which have different values otherwise ols fails
X = df[['gender','age','pre_happy','post_happy','synthetic_voices','daily_encounter','negative_experience','agree_definition','voice_gender','google_pitch','pitch_weighted']]
y = np.sqrt((df['unac']**2)+(df['cons']**2))
X, y = np.array(X), np.array(y)

X2 = sm.add_constant(X)
est = sm.OLS(y, X2)
est2 = est.fit()
print(est2.summary())

print(est2.params)

# # range of data
# max_x = data['x'].max()
# min_x = data['x'].min()
 
# # range of values for plotting
# # the regression line
# x = np.arange(min_x, max_x, 1)