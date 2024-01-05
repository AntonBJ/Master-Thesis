import plotly.express as px
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/completeData/data.csv", sep=",")
#remove NaN
df = df[df['unac'].notna()]
#remove Trick Questions
df = df[df['sample']!='trickQuestion']

df_grouped = df.groupby(['voice_gender', 'google_pitch'])[['unac', 'cons']].mean()
df_grouped = df_grouped.reset_index()
#print(df_grouped)

#sample means by pitch
df_pitch = df.groupby(['sample_id', 'google_pitch', 'voice_gender'])[['unac', 'cons']].mean()
df_pitch = df_pitch.reset_index()
#df_samples = df_samples.sort_values(by='unac')
df_pitch['google_pitch'] = df_pitch['google_pitch'].astype(str)
#print(df_pitch)

#sample means by voice_gender
df_gender = df.groupby(['sample_id', 'voice_gender'])[['unac', 'cons']].mean()
df_gender = df_gender.reset_index()

def plot_distribution():
    #g = sns.displot(data=d, x="unac", kde=True, hue = 'voice_gender', palette='Set1') # palette={'-10.0': 'navy', '10.0': 'red'}
    g = sns.displot(data=df_gender, x = 'cons' , kde=True, hue='voice_gender') # palette={'-10.0': 'navy', '10.0': 'red'}    
    #g.set_axis_labels("Unacceptability", "Demand for Consequences")
    #g.set_title("Female Voice")
    plt.show()

def plot_scatter():
    def scatter_pitch_unac_male():
        fig = px.scatter(df_pitch.loc[df_pitch['voice_gender']=='Male'], y="sample_id", x="unac", color="google_pitch", labels={"cons": "Mean", "unac": "Mean"})
        fig.update_traces(marker_size=10)
        fig.update_layout(title_text='Unacceptability in Male Voice', title_x=0.5)
        fig.show()

    def scatter_pitch_unac_female():
        fig = px.scatter(df_pitch.loc[df_pitch['voice_gender']=='Female'], y="sample_id", x="unac", color="google_pitch", labels={"cons": "Mean", "unac": "Mean"})
        fig.update_traces(marker_size=10)
        fig.update_layout(title_text='Unacceptability in Female Voice', title_x=0.5)
        fig.show()

    def scatter_pitch_cons_male():
        fig = px.scatter(df_pitch.loc[df_pitch['voice_gender']=='Male'], y="sample_id", x="cons", color="google_pitch", labels={"cons": "Mean", "unac": "Mean"})
        fig.update_traces(marker_size=10)
        fig.update_layout(title_text='Demand for Consequences in Male Voices', title_x=0.5)
        fig.show()

    def scatter_pitch_cons_female():
        fig = px.scatter(df_pitch.loc[df_pitch['voice_gender']=='Female'], y="sample_id", x="cons", color="google_pitch", labels={"cons": "Mean", "unac": "Mean"})
        fig.update_traces(marker_size=10)
        fig.update_layout(title_text='Demand for Consequences in Female Voices', title_x=0.5)
        fig.show()

    def scatter_gender_unac_high():
        fig = px.scatter(df_pitch.loc[df_pitch['google_pitch']=='10.0'], y="sample_id", x="unac", color="voice_gender", labels={"cons": "Mean", "unac": "Mean"})
        fig.update_traces(marker_size=10)
        fig.update_layout(title_text='Unacceptability in High Pitch Voices', title_x=0.5)
        fig.show()

    def scatter_gender_unac_low():
        fig = px.scatter(df_pitch.loc[df_pitch['google_pitch']=='-10.0'], y="sample_id", x="unac", color="voice_gender", labels={"cons": "Mean", "unac": "Mean"})
        fig.update_traces(marker_size=10)
        fig.update_layout(title_text='Unacceptability in Low Pitch Voices', title_x=0.5)
        fig.show()

    def scatter_gender_cons_high():
        fig = px.scatter(df_pitch.loc[df_pitch['google_pitch']=='10.0'], y="sample_id", x="cons", color="voice_gender", labels={"cons": "Mean", "unac": "Mean"})
        fig.update_traces(marker_size=10)
        fig.update_layout(title_text='Demand for Consequences in High Pitch Voices', title_x=0.5)
        fig.show()

    def scatter_gender_cons_low():
        fig = px.scatter(df_pitch.loc[df_pitch['google_pitch']=='-10.0'], y="sample_id", x="cons", color="voice_gender", labels={"cons": "Mean", "unac": "Mean"})
        fig.update_traces(marker_size=10)
        fig.update_layout(title_text='Demand for Consequences in Low Pitch Voices', title_x=0.5)
        fig.show()


    # scatter_pitch_unac_male()
    # scatter_pitch_unac_female()
    # scatter_pitch_cons_male()
    # scatter_pitch_cons_female()
    scatter_gender_unac_low()
    scatter_gender_unac_high()
    scatter_gender_cons_low()
    scatter_gender_cons_high()

#plot_distribution()
plot_scatter()