import plotly.express as px
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from scipy.stats import shapiro 
from scipy.stats import kstest

df = pd.read_csv("C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/completeData/data.csv", sep=",")

#remove Trick Questions
df = df.loc[df['sample']!='trickQuestion']

#select sample
sample_id = df['sample_id'].unique()

pitch = [10.0,-10.0]
gender = ['Female','Male']

swt_list = []
kst_list = []
sample_list = []
swt_result_list = []
kst_result_list = []
pitch_list = []
gender_list = []
sample_name = []

#select pitch and voice_gender
for s in sample_id:
    for g in gender:
        for p in pitch:
            _df = df.loc[df['sample_id'] == s]
            _df1 = _df.loc[(_df['google_pitch'] == p) & (_df['voice_gender'] == g)]

            swt = shapiro(_df1['unac'])
            swt_list.append(swt[1])
            kst = kstest(_df1['unac'], 'norm')
            kst_list.append(kst[1])

            print()
            print(_df1['unac'])
            print(kst)

            sample_list.append(_df1['sample'].unique())
            pitch_list.append(p)
            gender_list.append(g)
            sample_name.append(s[-4:])


            if swt[1] < 0.05:
                swt_result_list.append('not normal')
            else:
                swt_result_list.append('normal')
            
            if kst[1] < 0.05:
                kst_result_list.append('not normal')
            else:
                kst_result_list.append('normal')
            
df_distribution = pd.DataFrame({'sample': sample_name, 'pitch': pitch_list, 'gender': gender_list, 'swt': swt_list, 'swt_result': swt_result_list, 'kst': kst_list,'kst_result': kst_result_list})
print(df_distribution)

#df_distribution.to_csv('C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/output_normalDistribution/distributionTests.csv')

#Test for Normality
#create Q-Q plot with 45-degree line added to plot

#print(df.loc[df['sample'] == '47_sample_9064_p+10_f.wav']['unac'])

# fig = sm.qqplot(data = df.loc[df['sample'] == '47_sample_9064_p+10_f.wav']['unac'], line='45')
# plt.show()

print(df_distribution.to_latex(index=False,
                  formatters={"name": str.upper},
                  float_format="{:.4f}".format,
))  