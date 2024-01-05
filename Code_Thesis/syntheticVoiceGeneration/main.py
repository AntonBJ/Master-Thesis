import pandas as pd
import callAPI

df = pd.read_csv('data/selectedData.csv')

#x = "This is not a Hate Speech Sample. Please move the Slider for Unacceptability to the very left. And the Slider for Demand of Consequences to the very right."#df.iloc[12]
#print(x["text"])
counter = 0

pit = [-10, 10]
gen = ["m","f"]
for g in gen:
    for p in pit:
        for i in range(len(df.index)):
            callAPI.synthesize_text(_id = df['index_old'][i], text = df['text'][i], pitch = p, gender = g)


#callAPI.synthesize_text(_id = x["_id"], text = x["text"], pitch = 0, gender = "m")
#callAPI.synthesize_text(_id = "TrickQuestion", text = x, pitch = 0, gender = "m")

#print(g)
#print(p)
#print(df['index_old'][i])
#print(df['text'][i])
#print()
#counter = counter + 1