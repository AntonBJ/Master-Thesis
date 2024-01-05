import plotly.express as px
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from scipy.stats import shapiro 
from scipy.stats import kstest
from scipy.stats import ttest_rel

df = pd.read_csv("C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/completeData/data.csv", sep=",")
print('Toatal Number of Samples: {}\n'.format(df['id'].size))
print('Total Number of Responses:')
print(df['id'].nunique())
#print('Numer of Samples: {}'.format())
#remove NaN
df = df[df['unac'].notna()]
#Only verified samples
df = df[df['verification']=='Yes']
#remove Trick Questions
df = df[df['sample']!='trickQuestion']

print('Toatal Number of Samples after verification: {}'.format(df['id'].size))
print('Total Number of Responses after verification:')
print(df['id'].nunique())

df_grouped = df.groupby('id')
df_grouped_first = df_grouped.first()
print('\n Age Statistics:')
print(df_grouped_first['age'].describe())

print('\n Gender Statistics:')
print(df_grouped_first.value_counts("gender"))

print('\n Language Statistics:')    #['Fluent' 'Advanced' 'Upper-Intermediate' 'Lower-Intermediate']
print(df_grouped_first.value_counts("english"))

print('\n Difficulties Understanding:')    
print(df_grouped_first.value_counts("difficulties"))

#Prior-/Post-Happyness
print('\n Prior Happyness')
print(df_grouped_first['pre_happy'].describe())
print('\n Post Happyness')
print(df_grouped_first['post_happy'].describe())

g = sns.histplot(data=df_grouped_first, x="pre_happy", color="#1f90cc", label="Pre Happy", kde=True)
g = sns.histplot(data=df_grouped_first, x="post_happy", color="#c40d1e", label="Post Happy", kde=True)
g.set(xlabel='Happyness', ylabel='Count')

plt.legend() 
plt.savefig('C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/images/happy_dist.png', bbox_inches='tight')
plt.show()

print('\nTest for Normal Distribution in pre_happy')
#print(shapiro(df_grouped_first['pre_happy']))
print(shapiro(df_grouped_first.loc[df_grouped_first["pre_happy"] > 30 , "pre_happy"]))
print(kstest(df_grouped_first['pre_happy'], 'norm'))

print('\nTest for Normal Distribution in post_happy')
print(shapiro(df_grouped_first['post_happy']))
print(kstest(df_grouped_first['post_happy'], 'norm'))

#t-Test:    This is a test for the null hypothesis that two related or repeated
#           samples have identical average (expected) values.
print('\nt-Test for pre_ and post_happy')
print(ttest_rel(df_grouped_first['pre_happy'],df_grouped_first['post_happy']))

print('\n Own Definitions:')    
print(df_grouped_first.value_counts("own_definition"))

print('\n Synthetic Voices Statistics:')
print(df_grouped_first.value_counts("synthetic_voices"))
print(df_grouped_first['synthetic_voices'].describe())

print('\n Daily Encounter Statistics:')
print(df_grouped_first['daily_encounter'].describe())   

print('\n Negative Experience Statistics:')    
print(df_grouped_first.value_counts("negative_experience"))

print('\n Difficulties Understanding Statistics:')    
print(df_grouped_first.value_counts("difficulties"))

print('\n Definition Statistics:')
print('Familiar with Definition:')     
print(df_grouped_first.value_counts("familiar_definition"))
print('Agree with Definition:')
print(df_grouped_first.value_counts("agree_definition"))

print('\n Verification Statistics:')    
print(df_grouped_first.value_counts("verification"))

print('\n User Comment Statistics:')    
print(df_grouped_first.value_counts("user_comment"))

print('\nNumber of participants with lower-intermediate english skill and understanding difficulties:')
print(df.loc[(df['difficulties']=='Yes') & (df['english']=='Lower-Intermediate'), ['id']].nunique())