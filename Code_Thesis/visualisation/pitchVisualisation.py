import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv('C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/outputPitch/pitchData.csv', sep=',')

fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(go.Scatter(x=df['time'], y=df['frequency'],
                    mode='lines',
                    name='Frequency',
                    line=dict(color='royalblue', width=2)
                    ),
                    secondary_y=False
)

fig.add_trace(go.Scatter(x=df['time'], y=df['confidence'],
                    mode='lines',
                    name='Confidence',
                    line=dict(color='firebrick', width=1)
                    ),
                    secondary_y=True
)

# Add figure title
fig.update_layout(
    title_text="Pitch Sample"
)

# Set x-axis title
fig.update_xaxes(title_text="<b>Time</b> in 10ms")

# Set y-axes titles
fig.update_yaxes(title_text="<b>Frequency</b> Frequency in HZ", secondary_y=False)
fig.update_yaxes(title_text="<b>Confidence</b> Confidence in %", secondary_y=True)

fig.show()