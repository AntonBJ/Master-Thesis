import crepe
import pandas as pd
from scipy.io import wavfile

sample = pd.read_csv('C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/responses/sampleFileNames.csv', sep=',', header=None)

df_sample = pd.DataFrame(sample)

#list for rowwise cacheing of results. Will be saved to dataframe later
a_list = []
b_list = []
c_list = []
d_list = []
e_list = []

for index, row in df_sample.iterrows():
    print('Starting {}'.format(row[0]))
    #Compute CREPE frequency
    sr, audio = wavfile.read('C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/outputVoices/neural2/{}'.format(row[0][3:]))
    time, frequency, confidence, activation = crepe.predict(audio, sr, viterbi=False)

    # Save all values for each sample if needed
    # d1.to_csv('C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/outputPitch/{}.csv'.format(row[0][3:]), sep=',')

    #Calculate pitch
    d1 = pd.DataFrame(data = {'time': time, 'frequency': frequency, 'confidence': confidence})
    pitch_weighted = d1['confidence']@d1['frequency']/d1['confidence'].sum()
    pitch_mean = d1['frequency'].mean()
    pitch_median = d1['frequency'].median()
    pitch_std = d1['frequency'].std()

    #cache results
    a_list.append(row[0])
    b_list.append(pitch_weighted)
    c_list.append(pitch_mean)
    d_list.append(pitch_median)
    e_list.append(pitch_std)

    print('Row {} completed'.format(index))

data = pd.DataFrame({'sample': a_list, 'pitch_weighted': b_list, 'pitch_mean': c_list, 'pitch_median': d_list, 'pitch_std': e_list})
del a_list, b_list, c_list, d_list, e_list

data.to_csv('C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/outputPitch/outputPitch.csv', sep=',')

print('\n')
print(data)
