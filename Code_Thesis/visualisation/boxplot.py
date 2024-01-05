import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#load data
df = pd.read_csv('C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/completeData/data.csv')
#remove NaN
df = df[df['unac'].notna()]
#remove Trick Questions
df = df[df['sample']!='trickQuestion']

print(df['sample_id'].unique())

#print((df['unac']+df['cons'])/200)

#df = df.insert(1, 'HateSpeechfullness', (df['unac']+df['cons'])/200)

df['HateSpeechfullness'] = (df['unac']+df['cons'])/200

print(df['HateSpeechfullness'])

#boxplot = df.boxplot(column='HateSpeechfullness', by='google_pitch')
#boxplot = df.boxplot(column='HateSpeechfullness', by='voice_gender')
#boxplot = df.boxplot(column='unac', by='google_pitch')
#boxplot = df.boxplot(column='cons', by='google_pitch')

#boxplot = df.boxplot(column=['unac', 'cons'], by=['voice_gender', 'google_pitch'])
df = df.sort_values(by='voice_gender')

boxplot = df.boxplot(column=['unac'], by=['sample_id', 'voice_gender'])


# #Histogram
# fig, axs = plt.subplots(1, 1, sharey=True, tight_layout=False)
# n_bins = 40
# # We can set the number of bins with the *bins* keyword argument.
# axs.hist(df['HateSpeechfullness'], bins=n_bins) 
# # histogram.plot()

plt.show() 

