import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
#sns.set_style("white")
#pitch_palette = sns.color_palette({'Fri': "#F72585", 'Sun':  "#4CC9F0"})
#diverging_colors = sns.color_palette("RdBu", 10)
#sns.set_theme(style="ticks", palette=diverging_colors)

#load data
df = pd.read_csv('C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/completeData/data.csv')
#remove NaN
df = df[df['unac'].notna()]
#remove Trick Questions
df = df[df['sample']!='trickQuestion']

#df['HateSpeechfullness'] = (df['unac']+df['cons'])/200

dfhigh = df[df['google_pitch']==10]
dflow = df[df['google_pitch']!=10]
dfm = df[df['voice_gender']!='Female']
dff = df[df['voice_gender']=='Female']
dfm_low = dfm[dfm['google_pitch']!=10]
dfm_high = dfm[dfm['google_pitch']==10]
dff_low = dff[dff['google_pitch']!=10]
dff_high = dff[dff['google_pitch']==10]

def plot_jointplot(x = dfm):
    g = sns.jointplot(data=x, x="unac", y="cons", hue="google_pitch", palette="Spectral")
    g.set_axis_labels("Unacceptability", "Demand for Consequences")
    #g.set_titles("Female Voice")
    # g.figure.set_size_inches(6.5, 4.5)
    # g.ax.margins(.15)
    # g.despine(trim=True)
    #sns.color_palette("ch:s=.25,rot=-.25", as_cmap=True)
    #plt.figure(figsize=(10,7), dpi= 80)
    #sns.displot(x, color="dodgerblue", hue='google_pitch')
    #plt.xlim(50,75)
    #plt.legend()
    #ax.set(xlabel='Unacceptability', ylabel='Demand for Consequences')
    plt.show()

def plot_dist(d = dfm_low):
    #g = sns.displot(data=d, x="unac", kde=True, hue = 'voice_gender', palette='Set1') # palette={'-10.0': 'navy', '10.0': 'red'}
    g = sns.displot(data=d, x="unac", kde=True) # palette={'-10.0': 'navy', '10.0': 'red'}    
    #g.set_axis_labels("Unacceptability", "Demand for Consequences")
    #g.set_title("Female Voice")
    plt.show()

def plot_all_dist(d = df, hue = 'voice_gender', gender = 'Male', pitch=-10.0):
    g = sns.FacetGrid(d[d['google_pitch']==pitch], col='sample_id', col_wrap=4)
    g.map_dataframe(sns.histplot, x="unac", binwidth=10, kde = True, hue=hue) #, binwidth=2, binrange=(0, 60)
    #g.map_dataframe(sns.displot, x="unac", binwidth=10, kde = True) 
    plt.show()

g = df['sample'].unique()
g2 = [elem[-15:-4] for elem in g]

print(g2)

def plot_sampleCount(df):
    p = sns.countplot(data=df, x = 'sample', color="#1f90cc")
    p.set(ylabel='Count')
    p = p.set_xticklabels(g2, rotation=45, horizontalalignment='right', fontsize=5)
    plt.savefig('C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/images/sample_count.png', bbox_inches='tight')
    plt.show()

#sns.pairplot(df[['unac','google_pitch']], hue="google_pitch")
#plt.show()

#plot_all_dist(d = df, gender='Male')
#plot_all_dist(d = dfm_high)
#plot_all_dist(d = dff_low)
#plot_all_dist(d = dff_high)
#plot_jointplot(x = dfm)
#plot_dist(d = dff_high)

plot_sampleCount(df)


#for i in dfm_low['sample_id'].unique():
#    plot_dist(dfm_low[dfm_low['sample_id']== i])