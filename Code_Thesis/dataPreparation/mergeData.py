import pandas as pd

df_outputPitch = pd.read_csv('C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/outputPitch/outputPitch.csv')
df_surveyData = pd.read_csv('C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/responses/surveyData.csv')

df_outputPitch['sample'] = df_outputPitch['sample'].str.replace('p10','p+10')

df = df_surveyData.merge(df_outputPitch, how='left', on='sample')

df = df.drop(['Unnamed: 0_x','Unnamed: 0_y'], axis='columns')

df['google_pitch'] = df['google_pitch'].astype(str) 

#remove NaN
df = df[df['unac'].notna()]

df.to_csv('C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/completeData/data.csv', sep=',')

#Check if merged correctly
# print('\n')
# print('df_outputPitch: {}\n'.format(df_outputPitch.shape))
# print('df_surveyData: {}\n'.format(df_surveyData.shape))
# print('df: {}\n'.format(df.shape))
