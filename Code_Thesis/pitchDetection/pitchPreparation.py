import pandas as pd
import numpy as np

df = pd.read_csv('C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/outputPitch/pitchData.csv', sep=',')
names = pd.read_csv('C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/responses/sampleNames.csv', sep=',', header=None)

print(names)

#print(df['confidence']@df['frequency']/df['confidence'].sum())
#print(df['frequency'].mean())