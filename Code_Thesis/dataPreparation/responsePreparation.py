import pandas as pd

df_raw = pd.read_csv("data/responses/results-survey332483.csv", sep=",")
df_names = pd.read_csv("data/responses/sample_names.csv", sep=";", header=None)

data = []

for i in range(df_raw.shape[0]):
    for j in range(64, 170, 2):
        #Check for gender of the voice
        if df_names.iloc[0,j-64][-5] == 'f':
            voice_gender = 'Female'
        elif df_names.iloc[0,j-64][-5] == 'm':
            voice_gender = 'Male'
        else:
            voice_gender = None
        
        #Check for google tts pitch and sample name
        if 'wav' in df_names.iloc[0,j-64][-10:] and '-' not in df_names.iloc[0,j-64][-10:]:
            google_pitch = 10
            sample_id = df_names.iloc[0,j-64][10:-11]
        elif 'wav' in df_names.iloc[0,j-64][-10:] and '-' in df_names.iloc[0,j-64][-10:]:
            google_pitch = -10
            sample_id = df_names.iloc[0,j-64][10:-11]
        else:
            google_pitch = None
            sample_id = None

        #print(df_names.iloc[0,j-64][-5])
        data.append([df_raw.iloc[i,0],df_names.iloc[0,j-64],df_raw.iloc[i,j],
                     df_raw.iloc[i,j+1],df_raw.iloc[i,1],df_raw.iloc[i,2],
                     df_raw.iloc[i,3],df_raw.iloc[i,4],df_raw.iloc[i,5],
                     df_raw.iloc[i,5],df_raw.iloc[i,7],df_raw.iloc[i,8],
                     df_raw.iloc[i,9],df_raw.iloc[i,10],df_raw.iloc[i,170],
                     df_raw.iloc[i,171],df_raw.iloc[i,172],df_raw.iloc[i,173],
                     df_raw.iloc[i,174],df_raw.iloc[i,175],df_raw.iloc[i,176],
                     df_raw.iloc[i,177],df_raw.iloc[i,178],df_raw.iloc[i,179],
                     voice_gender, google_pitch, sample_id])

df = pd.DataFrame(data)

df = df.rename(columns={0: "id", 1: "sample", 2: "unac", 3: "cons", 4: "submitdate", 5: "lastpage", 6: "lan",
                         7: "seed", 8: "startdate", 9: "datestamp", 10: "gender", 11: "age", 12: "english",
                         13: "pre_happy", 14: "difficulties", 15: "post_happy", 16: "own_definition",
                         17: "synthetic_voices", 18: "daily_encounter", 19: "negative_experience",
                         20: "familiar_definition", 21: "agree_definition", 22: "verification",
                         23: "user_comment", 24: "voice_gender", 25: "google_pitch", 26: "sample_id"})

df.to_csv("data/responses/surveyData.csv", sep=",")

#print entire dataframe. pandas settings are local to with statement.   
# with pd.option_context('display.max_rows', None,
#                        'display.max_columns', None,
#                        'display.precision', 3,
#                        ):
#     print(df)   

