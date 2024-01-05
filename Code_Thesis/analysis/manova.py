from statsmodels.multivariate.manova import MANOVA
import pandas as pd

#load data
df = pd.read_csv('C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/completeData/data.csv')
#remove NaN
df = df[df['unac'].notna()]
#remove Trick Questions
df = df[df['sample']!='trickQuestion']

maov=MANOVA.from_formula('unac + cons ~ google_pitch + gender', data=df)
print(maov.mv_test())