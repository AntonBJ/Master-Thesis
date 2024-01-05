import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/completeData/data.csv", sep=",")
#remove NaN
df = df[df['unac'].notna()]
#remove Trick Questions
df = df[df['sample']!='trickQuestion']
df['sample_id'] = df['sample_id'].str[-4:]

df_grouped = df.groupby(['voice_gender', 'google_pitch'])[['unac', 'cons']].mean()
df_grouped = df_grouped.reset_index()
#print(df_grouped)

#sample means by pitch
df_pitch = df.groupby(['sample_id', 'google_pitch', 'voice_gender'])[['unac', 'cons']].mean()
df_pitch = df_pitch.reset_index()
#df_samples = df_samples.sort_values(by='unac')
df_pitch['google_pitch'] = df_pitch['google_pitch'].astype(str)
#print(df_pitch)

# Create an array with the colors
colors = ["#1f90cc", "#c40d1e"]  #TU red, TU blue, TU green "#49cb40"
# Set custom color palette
sns.set_palette(sns.color_palette(colors))
sns.set_theme(style="whitegrid")

def mean_male_unac():
    # Initialize the figure
    f, ax = plt.subplots()
    sns.despine(bottom=True, left=True)

    # Show each observation with a scatterplot
    sns.stripplot(
        data=df.loc[df['voice_gender']=='Male'], x="unac", y="sample_id", hue="google_pitch",
        dodge=0.25, alpha=.5, jitter=False, legend=False, palette=sns.color_palette(colors)
    )

    # Show the conditional means, aligning each pointplot in the
    # center of the strips by adjusting the width allotted to each
    # category (.8 by default) by the number of hue levels
    sns.pointplot(
        data=df.loc[df['voice_gender']=='Male'], x="unac", y="sample_id", hue="google_pitch",
        dodge=0.25, palette=sns.color_palette(colors), errorbar='ci',
        markers="D", markersize=4, linestyle="none", 
    )

    # Set axis labels
    ax.set(
        xlabel='Unacceptability', ylabel='Sample Id')

    # Improve the legend
    sns.move_legend(
        ax, loc="upper left", ncol=3, frameon=True, columnspacing=1, handletextpad=0, title = 'Google Pitch'
    )
    plt.savefig('C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/images/mean_male_unac.png', bbox_inches='tight')
    plt.show()

def mean_male_cons():
    # Initialize the figure
    f, ax = plt.subplots()
    sns.despine(bottom=True, left=True)

    # Show each observation with a scatterplot
    sns.stripplot(
        data=df.loc[df['voice_gender']=='Male'], x="cons", y="sample_id", hue="google_pitch",
        dodge=0.25, alpha=.5, jitter=False, legend=False, palette=sns.color_palette(colors)
    )

    # Show the conditional means, aligning each pointplot in the
    # center of the strips by adjusting the width allotted to each
    # category (.8 by default) by the number of hue levels
    sns.pointplot(
        data=df.loc[df['voice_gender']=='Male'], x="cons", y="sample_id", hue="google_pitch",
        dodge=0.25, palette=sns.color_palette(colors), errorbar='ci',
        markers="D", markersize=4, linestyle="none", 
    )

    # Set axis labels
    ax.set(
        xlabel='Demand for Consequences', ylabel='Sample Id')

    # Improve the legend
    sns.move_legend(
        ax, loc="upper left", ncol=3, frameon=True, columnspacing=1, handletextpad=0, title = 'Google Pitch'
    )
    plt.savefig('C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/images/mean_male_cons.png', bbox_inches='tight')
    plt.show()

def mean_female_unac():
    # Initialize the figure
    f, ax = plt.subplots()
    sns.despine(bottom=True, left=True)

    # Show each observation with a scatterplot
    sns.stripplot(
        data=df.loc[df['voice_gender']=='Female'], x="unac", y="sample_id", hue="google_pitch",
        dodge=0.25, alpha=.5, jitter=False, legend=False, palette=sns.color_palette(colors)
    )

    # Show the conditional means, aligning each pointplot in the
    # center of the strips by adjusting the width allotted to each
    # category (.8 by default) by the number of hue levels
    sns.pointplot(
        data=df.loc[df['voice_gender']=='Female'], x="unac", y="sample_id", hue="google_pitch",
        dodge=0.25, palette=sns.color_palette(colors), errorbar='ci',
        markers="D", markersize=4, linestyle="none", 
    )

    # Set axis labels
    ax.set(
        xlabel='Unacceptability', ylabel='Sample Id')

    # Improve the legend
    sns.move_legend(
        ax, loc="upper left", ncol=3, frameon=True, columnspacing=1, handletextpad=0, title = 'Google Pitch'
    )
    plt.savefig('C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/images/mean_female_unac.png', bbox_inches='tight')
    plt.show()

def mean_female_cons():
    # Initialize the figure
    f, ax = plt.subplots()
    sns.despine(bottom=True, left=True)

    # Show each observation with a scatterplot
    sns.stripplot(
        data=df.loc[df['voice_gender']=='Female'], x="cons", y="sample_id", hue="google_pitch",
        dodge=0.25, alpha=.5, jitter=False, legend=False, palette=sns.color_palette(colors)
    )

    # Show the conditional means, aligning each pointplot in the
    # center of the strips by adjusting the width allotted to each
    # category (.8 by default) by the number of hue levels
    sns.pointplot(
        data=df.loc[df['voice_gender']=='Female'], x="cons", y="sample_id", hue="google_pitch",
        dodge=0.25, palette=sns.color_palette(colors), errorbar='ci',
        markers="D", markersize=4, linestyle="none", 
    )

    # Set axis labels
    ax.set(
        xlabel='Demand for Consequences', ylabel='Sample Id')

    # Improve the legend
    sns.move_legend(
        ax, loc="upper left", ncol=3, frameon=True, columnspacing=1, handletextpad=0, title = 'Google Pitch'
    )
    plt.savefig('C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/images/mean_female_cons.png', bbox_inches='tight')
    plt.show()

# Comparison for Voice Gender
def mean_high_unac_gender():
    # Initialize the figure
    f, ax = plt.subplots()
    sns.despine(bottom=True, left=True)

    # Show each observation with a scatterplot
    sns.stripplot(
        data=df.loc[df['google_pitch']==10.0], x="unac", y="sample_id", hue="voice_gender",
        dodge=0.25, alpha=.5, jitter=False, legend=False, palette=sns.color_palette(colors)
    )

    # Show the conditional means, aligning each pointplot in the
    # center of the strips by adjusting the width allotted to each
    # category (.8 by default) by the number of hue levels
    sns.pointplot(
        data=df.loc[df['google_pitch']==10.0], x="unac", y="sample_id", hue="voice_gender",
        dodge=.25, palette=sns.color_palette(colors), errorbar='ci',
        markers="D", markersize=4, linestyle="none", 
    )

    # Set axis labels
    ax.set(
        xlabel='Unacceptability', ylabel='Sample Id')

    # Improve the legend
    sns.move_legend(
        ax, loc="upper left", ncol=3, frameon=True, columnspacing=1, handletextpad=0, title = 'Gender Voice'
    )
    plt.savefig('C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/images/mean_high_unac_gender.png', bbox_inches='tight')
    plt.show()

def mean_high_cons_gender():
    # Initialize the figure
    f, ax = plt.subplots()
    sns.despine(bottom=True, left=True)

    # Show each observation with a scatterplot
    sns.stripplot(
        data=df.loc[df['google_pitch']==10.0], x="cons", y="sample_id", hue="voice_gender",
        dodge=0.25, alpha=.5, jitter=False, legend=False, palette=sns.color_palette(colors)
    )

    # Show the conditional means, aligning each pointplot in the
    # center of the strips by adjusting the width allotted to each
    # category (.8 by default) by the number of hue levels
    sns.pointplot(
        data=df.loc[df['google_pitch']==10.0], x="cons", y="sample_id", hue="voice_gender",
        dodge=.25, palette=sns.color_palette(colors), errorbar='ci',
        markers="D", markersize=4, linestyle="none", 
    )

    # Set axis labels
    ax.set(
        xlabel='Demand for Consequences', ylabel='Sample Id')

    # Improve the legend
    sns.move_legend(
        ax, loc="upper left", ncol=3, frameon=True, columnspacing=1, handletextpad=0, title = 'Gender Voice'
    )
    plt.savefig('C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/images/mean_high_cons_gender.png', bbox_inches='tight')
    plt.show()

def mean_low_unac_gender():
    # Initialize the figure
    f, ax = plt.subplots()
    sns.despine(bottom=True, left=True)

    # Show each observation with a scatterplot
    sns.stripplot(
        data=df.loc[df['google_pitch']==-10.0], x="unac", y="sample_id", hue="voice_gender",
        dodge=0.25, alpha=.5, jitter=False, legend=False, palette=sns.color_palette(colors)
    )

    # Show the conditional means, aligning each pointplot in the
    # center of the strips by adjusting the width allotted to each
    # category (.8 by default) by the number of hue levels
    sns.pointplot(
        data=df.loc[df['google_pitch']==10.0], x="unac", y="sample_id", hue="voice_gender",
        dodge=.25, palette=sns.color_palette(colors), errorbar='ci',
        markers="D", markersize=4, linestyle="none", 
    )

    # Set axis labels
    ax.set(
        xlabel='Unacceptability', ylabel='Sample Id')

    # Improve the legend
    sns.move_legend(
        ax, loc="upper left", ncol=3, frameon=True, columnspacing=1, handletextpad=0, title = 'Gender Voice'
    )
    plt.savefig('C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/images/mean_low_unac_gender.png', bbox_inches='tight')
    plt.show()

def mean_low_cons_gender():
    # Initialize the figure
    f, ax = plt.subplots()
    sns.despine(bottom=True, left=True)

    # Show each observation with a scatterplot
    sns.stripplot(
        data=df.loc[df['google_pitch']==10.0], x="cons", y="sample_id", hue="voice_gender",
        dodge=0.25, alpha=.5, jitter=False, legend=False, palette=sns.color_palette(colors)
    )

    # Show the conditional means, aligning each pointplot in the
    # center of the strips by adjusting the width allotted to each
    # category (.8 by default) by the number of hue levels
    sns.pointplot(
        data=df.loc[df['google_pitch']==10.0], x="cons", y="sample_id", hue="voice_gender",
        dodge=.25, palette=sns.color_palette(colors), errorbar='ci',
        markers="D", markersize=4, linestyle="none", 
    )

    # Set axis labels
    ax.set(
        xlabel='Demand for Consequences', ylabel='Sample Id')

    # Improve the legend
    sns.move_legend(
        ax, loc="upper left", ncol=3, frameon=True, columnspacing=1, handletextpad=0, title = 'Gender Voice'
    )
    plt.savefig('C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/images/mean_low_cons_gender.png', bbox_inches='tight')
    plt.show()

mean_male_unac()
mean_male_cons()
mean_female_unac()
mean_female_cons()



mean_high_unac_gender()
mean_high_cons_gender()
mean_low_unac_gender()
mean_low_cons_gender()
