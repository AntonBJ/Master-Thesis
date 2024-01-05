import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import seaborn as sns
sns.set_style("white")

#load data
df = pd.read_csv('C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/completeData/data.csv')
#remove NaN
df = df[df['unac'].notna()]
#remove Trick Questions
df = df[df['sample']!='trickQuestion']

df['HateSpeechfullness'] = (df['unac']+df['cons'])/200

rng = np.random.default_rng(19680801)

dfm = df[df['voice_gender']!='Female']
dff = df[df['voice_gender']=='Female']
dfm_low = dfm[dfm['google_pitch']!=10]
dfm_high = dfm[dfm['google_pitch']==10]
dff_low = dff[dff['google_pitch']!=10]
dff_high = dff[dff['google_pitch']==10]

def plot_histogram(dataframe, feature = 'unac', num_bins = 40):
     # example data
     mu = dataframe[feature].mean()
     sigma = dataframe[feature].std()
     x = dataframe[feature]

     fig, ax = plt.subplots()

     # the histogram of the data
     n, bins, patches = ax.hist(x, num_bins, density=True)

     # add a 'best fit' line
     y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
          np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
     ax.plot(bins, y, '--')
     ax.set_xlabel('Value')
     ax.set_ylabel('Probability density')
     ax.set_title('Histogram of HateSpeech Responses')
     #sns.distplot(x , color="dodgerblue", axlabel='Ideal')

     # Tweak spacing to prevent clipping of ylabel
     fig.tight_layout()
     plt.show()

plot_histogram(dataframe=dfm_low)
plot_histogram(dataframe=dfm_high)
plot_histogram(dataframe=dff_low)
plot_histogram(dataframe=dfm_high)
