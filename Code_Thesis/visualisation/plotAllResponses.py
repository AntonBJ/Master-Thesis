import plotly.express as px
import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/completeData/data.csv", sep=",")
#remove NaN
df = df[df['unac'].notna()]
#remove Trick Questions
df = df[df['sample']!='trickQuestion']

def scatter(color: str, colorLabel: str, title ="Hate Speech Data", data = df, all = True, sample_id = '22967'):
    #Scatterplot
    if all == False:
        df = data.loc[data['sample_id'] == sample_id]
    else:
        df = data

    fig = px.scatter(df, x="cons", y="", color=color,
                    labels={
                        "unac": "Unacceptability",
                        "cons": "Demand for Consequences",
                        color: colorLabel
                    },
                    title=title)
    # add annotation
    fig.add_annotation(dict(font=dict(color='black',size=12),
                                        x=0,
                                        y=-0.12,
                                        showarrow=False,
                                        text="{} #: {}".format(sample_id,df.shape[0]),
                                        textangle=0,
                                        xanchor='left',
                                        xref="paper",
                                        yref="paper"))

    fig.show()

#Plot sample wise
for index, row in df.drop_duplicates(subset='sample_id').iterrows():
    print(row['sample_id'])
    scatter(color="pitch_weighted", colorLabel='Mean Weighted Pitch (HZ)', all=False, sample_id=row['sample_id'])

#Plot sample wise
# for index, row in df.drop_duplicates(subset='sample_id').iterrows():
#     print(row['sample_id'])
#     scatter(color="voice_gender", colorLabel='Gender Google TTS Voice', all=False, sample_id=row['sample_id'])


#Plot all
#scatter(color="sample_id", colorLabel='Sample ID')
#scatter(color="pitch_weighted", colorLabel='Mean Weighted Pitch (HZ)')
#scatter(color="voice_gender", colorLabel='Gender Google TTS Voice')

