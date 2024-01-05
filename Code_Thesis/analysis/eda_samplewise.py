import plotly.express as px
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from scipy.stats import shapiro 

df = pd.read_csv("C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/completeData/data.csv", sep=",")

#remove Trick Questions
df = df.loc[df['sample']!='trickQuestion']

#select sample
sample_id = df['sample_id'].unique()
#_df = df.loc[df['sample_id'] == sample_id[0]]
_df = df.loc[df['sample'] == '47_sample_9064_p+10_f.wav']

pitch = [10.0,-10.0]
gender = ['Female','Male']

#select pitch and voice_gender
#_df = _df.loc[df['voice_gender'] == gender[0]]
#_df = _df.loc[df['google_pitch'] == pitch[0]]

g = sns.displot(data=_df, x=_df['unac'], kde=True, hue='google_pitch', bins = [0,10,20,30,40,50,60,70,80,90,100]) # palette={'-10.0': 'navy', '10.0': 'red'}    
#g.set_axis_labels("Unacceptability", "Demand for Consequences")
#g.set_title("Female Voice")
plt.show()

#print(_df['unac'])
#print(np.log(_df['unac']))


