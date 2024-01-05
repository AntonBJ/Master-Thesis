library(tidyr)

data <- read.csv("C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/completeData/data.csv", header=TRUE, stringsAsFactors=FALSE)

data <- drop_na(data)

y <- sqrt((data[c("unac")]**2)*(data[c("cons")]**2))
y <- (y-min(y))/(max(y)-min(y))

X = data[c('gender','age','pre_happy','post_happy','synthetic_voices','daily_encounter','negative_experience','agree_definition','voice_gender','google_pitch','pitch_weighted')]          
X$y <- y

# Estimate the model and same the results in object "ols"
ols <- lm(y$unac ~ gender + age + voice_gender + google_pitch + pitch_weighted, data = X) 

# pre_happy + post_happy + synthetic_voices + daily_encounter + negative_experience   

summary(ols)

# Print the result in the console
#ols
