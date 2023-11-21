#### SER594: Experimentation
#### Title: Heartbeats and Hashtags: Sentiment Analysis in F1
#### Author: Jyothirmai Kantipudi
#### Date: 10/18/2023

## Explainable Records

### Record 1
**Raw Data:**
- user_name: Alex Papas
- user_location: Sydney, New South Wales
- user_description: F1/MotoGP/Horse Racing/MMA Enthusiast
- user_followers: 129
- user_friends: 650
- user_favourites: 8058
- user_verified: FALSE
- date: 8/1/21 23:49
- text: "He got what he deserved. Tifosi traitors always come off second best. Grazie ragazzi Seb." #F1 #HungarianGP
- hashtags: ['F1', 'HungarianGP']
- source: Twitter for Android
- is_retweet: FALSE

**Prediction Explanation:**
- The model predicts a negative sentiment based on the user's expressions like "He got what he deserved" and the mention of "Tifosi traitors." The use of hashtags like #F1 and #HungarianGP further supports the context of a Formula 1 event, possibly the Hungarian Grand Prix, where the user expresses dissatisfaction.

### Record 2
**Raw Data:**
- user_name: Kade Foster
- user_location: 
- user_description: 
- user_followers: 98
- user_friends: 139
- user_favourites: 583
- user_verified: FALSE
- date: 8/1/21 23:52
- text: "So Seb gets disqualified because they can't get a liter of fuel out, but mercedes gets a 10 second and a 5 place grid penalty for causing two MAJOR ACCIDENTS in back to back races???? oh wait..... it still doesn't make sense. #Vettel #HungarianGP #WTF1 #f1"
- hashtags: ['Vettel', 'HungarianGP', 'WTF1', 'f1']
- source: Twitter for iPhone
- is_retweet: FALSE

**Prediction Explanation:**
- The model predicts a negative sentiment as the user questions the decisions in Formula 1, expressing frustration over the perceived inconsistency in penalties. Hashtags like #Vettel, #HungarianGP, #WTF1, and #f1 emphasize the context of Formula 1, and the critical tone in the text contributes to the negative sentiment prediction.

## Interesting Features

Two features were identified as having a significant impact on the model's predictions:

1. **Feature A (user_followers)**: Indicates the reach and potential influence of the tweet, which can correlate with the spread of sentiment.
2. **Feature B (user_favourites)**: Reflects the user's engagement level, which can be related to the intensity of sentiment.

The model's reliance on these features is justified by the domain knowledge that influential and engaged users often express clearer sentiments.

## Experiments

The experiments manipulating Features A and B revealed:

- **Varying Feature A**: Showed a change in prediction confidence, suggesting the model considers user influence in sentiment prediction.
- **Varying Feature B**: Affected the predictions to a lesser extent, indicating a secondary role in sentiment analysis.
- **Varying Both Features**: Demonstrated complex interactions, where high influence combined with high engagement reinforced the sentiment prediction.

These trends confirm the model's sensitivity to user-related features in assessing tweet sentiments.
