from scipy.stats import wilcoxon
import pandas as pd
from tqdm import tqdm
from scipy.stats import false_discovery_control

df = pd.read_csv("C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/completeData/data.csv", sep=",")

#remove Trick Questions
df = df.loc[df['sample']!='trickQuestion']

#select sample
sample_id = df['sample_id'].unique()

pitch = [10.0,-10.0]
gender = ['Female','Male']
feature = ['unac','cons']

sample_list = []
pitch_list = []
p_value_list = []
test_result_list = []
feature_list = []

#test for difference in pitch
for s in sample_id:
    for f in feature:
        for p in pitch:
            _df = df.loc[(df['sample_id'] == s) & (df['google_pitch'] == p)]

            # data
            group1_data = _df.loc[df['voice_gender'] == gender[0]][f]
            group2_data = _df.loc[df['voice_gender'] == gender[1]][f]

            print(len(group1_data))
            print(len(group2_data))

            statistic, p_value = wilcoxon(x = group1_data, y = group2_data)

            alpha = 0.05  # Set significance level
            if p_value < alpha:
                test_result_list.append('difference')
            else:
                test_result_list.append('no difference')

            sample_list.append(s)
            pitch_list.append(p)
            p_value_list.append(p_value)
            feature_list.append(f)

df_wT = pd.DataFrame({'sample': sample_list, 'feature': feature_list, 'pitch': pitch_list, 'p_value': p_value_list, 'wilcoxon_result': test_result_list})


fdr_kst = false_discovery_control(df_wT['p_value'], method='bh')
print(fdr_kst)

#df_wT.to_csv('C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/outputTeststatistics/wilcoxonTest_gender.csv')