from scipy.stats import mannwhitneyu
import pandas as pd
from tqdm import tqdm
from scipy.stats import false_discovery_control

df = pd.read_csv("C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/completeData/data.csv", sep=",")

#remove Trick Questions
df = df.loc[df['sample']!='trickQuestion']
#remove NaN
df = df[df['unac'].notna()]
df = df[df['cons'].notna()]

#select sample
sample_id = df['sample_id'].unique()

pitch = [10.0,-10.0]
gender = ['Female','Male']
feature = ['unac','cons']

sample_list = []
gender_list = []
p_value_list = []
test_result_list = []
feature_list = []

#test for difference in weeklyEncounters
for s in sample_id:
    for f in feature:
            _df = df.loc[(df['sample_id'] == s)]

            # data
            group1_data = _df.loc[df['daily_encounter'] < 37][f]
            group2_data = _df.loc[df['daily_encounter'] > 37][f]

            statistic, p_value = mannwhitneyu(group1_data, group2_data)

            alpha = 0.05  # Set significance level
            if p_value < alpha:
                test_result_list.append('difference')
            else:
                test_result_list.append('no difference')

            sample_list.append(s)
            p_value_list.append(p_value)
            feature_list.append(f)

df_mWUT = pd.DataFrame({'sample': sample_list, 'feature': feature_list,  'p_value': p_value_list})    #, 'mWUT_result': test_result_list})
df_mWUT['sample'] = df_mWUT['sample'].str[-4:]

fdr_kst = false_discovery_control(df_mWUT['p_value'], method='bh', axis=0)
df_mWUT['bh'] = fdr_kst 

print(df_mWUT)

#df_mWUT.to_csv('C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/outputTeststatistics/mWUTest_pitch.csv')

print(df_mWUT.to_latex(index=False,
                  formatters={"name": str.upper},
                  float_format="{:.4f}".format,
))  