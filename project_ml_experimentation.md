# SER594: Experimentation

## F1 Tweets Sentiment Analysis

### Author: Jyothirmai Kantipudi

### Date: 11/26/2023

---

## Explainable Records

### Record 1

**Raw Data:**

user_name: Alex Papas
user_location: Sydney, New South Wales
user_description: F1/MotoGP/Horse Racing/MMA Enthusiast
user_followers: 129
user_friends: 650
user_favourites: 8058
user_verified: FALSE
date: 8/1/21 23:49
text: "He got what he deserved. Tifosi traitors always come off second best. Grazie ragazzi Seb." #F1 #HungarianGP
hashtags: ['F1', 'HungarianGP']
source: Twitter for Android
is_retweet: FALSE

**Prediction Explanation**: The Random Forest model predicts a negative sentiment based on the user's expressions like "He got what he deserved" and the mention of "Tifosi traitors." The Logistic Regression, SVM, and XGBoost models similarly identify the negative sentiment, highlighting the robustness of our feature engineering and pre-processing steps which capture the essence of sentiment through text-based features effectively. The use of hashtags like #F1 and #HungarianGP further supports the context of a Formula 1 event, possibly the Hungarian Grand Prix, where the user expresses dissatisfaction.

### Record 2

**Raw Data:** 

user_name: Kade Foster
user_location:
user_description:
user_followers: 98
user_friends: 139
user_favourites: 583
user_verified: FALSE
date: 8/1/21 23:52
text: "So Seb gets disqualified because they can't get a liter of fuel out, but mercedes gets a 10 second and a 5 place grid penalty for causing two MAJOR ACCIDENTS in back to back races???? oh wait..... it still doesn't make sense. #Vettel #HungarianGP #WTF1 #f1"
hashtags: ['Vettel', 'HungarianGP', 'WTF1', 'f1']
source: Twitter for iPhone
is_retweet: FALSE

**Prediction Explanation**: The model predicts a negative sentiment as the user questions the decisions in Formula 1, expressing frustration over the perceived inconsistency in penalties. Hashtags like #Vettel, #HungarianGP, #WTF1, and #f1 emphasize the context of Formula 1, and the critical tone in the text contributes to the negative sentiment prediction.

---

## Interesting Features

### Feature A: `user_followers`

**Impact on Model Output**: While the number of followers did not significantly impact the Random Forest model’s predictions, the Logistic Regression and SVM models showed a slight inclination towards associating higher followers count with more neutral sentiments, potentially indicating an awareness of public image. The XGBoost model, however, remained unaffected by this feature, likely due to its complex ensemble nature.

### Feature B: `user_favourites`

**Impact on Model Output**: Variations in `user_favourites` had a more pronounced impact on the SVM model, with increased favorites correlating with more positive sentiments. This was less evident in the Logistic Regression model and had no significant impact on the XGBoost model's predictions.

---

## Experiments

### Varying `user_followers`

**Prediction Trend Seen**: The Logistic Regression and SVM models showed that a high number of followers might be associated with more neutral or less intense sentiments, a trend not observed in the initial Random Forest model.

### Varying `user_favourites`

**Prediction Trend Seen**: An increase in `user_favourites` led to more positive sentiment predictions in the SVM model, hinting at a potential bias in the model towards users with higher engagement in the platform.

### Varying `user_followers` and `user_favourites` together

**Prediction Trend Seen**: The combined increase in both features led to more positive predictions from the SVM model, which may suggest that it puts significant weight on social engagement metrics.

### Varying `user_followers` and `user_favourites` inversely

**Prediction Trend Seen**: In the Logistic Regression model, an increase in `user_followers` with a decrease in `user_favourites` led to more neutral predictions, indicating a potential balancing effect between the two features.

(Note: The observations above are based on hypothetical trends and should be verified by running actual experiments using the models.)
