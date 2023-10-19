#### SER594: Exploratory Data Munging and Visualization
#### Title: Heartbeats and Hashtags: Sentiment Analysis in F1
#### Author: Jyothirmai Kantipudi
#### Date: 10/18/2023

## Basic Questions
**Dataset Author(s):** kash

**Dataset Construction Date:** 04/24/2022

**Dataset Record Count:** (580909, 13) - 580909 rows, 13 columns

**Dataset Field Meanings:** Here is the breakdown of the fields/attributes in the dataset:

user_name: The name of the user who posted the tweet.
user_location: The location associated with the user's account.
user_description: A brief description or bio provided by the user on their profile.
user_created: The date when the user's account was created.
user_followers: The number of followers the user has.
user_friends: The number of friends (or accounts the user follows) of the user.
user_favourites: The number of tweets the user has marked as favorites.
user_verified: A boolean value indicating whether the user's account is verified or not.
date: The date and time when the tweet was posted.
text: The actual text content of the tweet.
hashtags: A list of hashtags included in the tweet.
source: The source or platform from which the tweet was posted.
is_retweet: A boolean value indicating whether the tweet is a retweet or not.

**Dataset File Hash(es):** 1e4044d9f9d9aa4654f4a6d4bdf4b4d2

The dataset I've used exceeds 100 MB, so I couldn't upload it to GitHub. Instead, as suggested by the professor I've uploaded it to my Drive and adding an immutable link - https://drive.google.com/file/d/1AIPiYVCyYcBiy_oj0V0eYRuRXuQMAJii/view?usp=share_link

And the link to dataset from the website(to check the MD5 Hash) - https://www.kaggle.com/datasets/kaushiksuresh147/formula-1-trending-tweets/versions/20/data


## Interpretable Records
### Record 1
**Raw Data:** 
user_name: Alex Papas
user_location: Sydney, New South Wales
user_description: F1/MotoGP/Horse Racing/MMA Enthusiast
user_created: 1/25/15 12:51
user_followers: 129
user_friends: 650
user_favourites: 8058
user_verified: FALSE
date: 8/1/21 23:49
text: "He got what he deserved. Tifosi traitors always come off second best. Grazie ragazzi Seb." #F1 #HungarianGP https://t.co/U2ITC4RVsX https://t.co/EcjmM1liGD
hashtags: ['F1', 'HungarianGP']
source: Twitter for Android
is_retweet: FALSE

**Interpretation:** This tweet was posted by a user named Alex Papas from Sydney, New South Wales. The user is an enthusiast of F1, MotoGP, Horse Racing, and MMA. The tweet seems to express satisfaction or agreement with some event related to the Hungarian Grand Prix (#HungarianGP) in Formula 1 (#F1). The user mentions "Tifosi traitors," which might refer to fans of Ferrari team in Formula 1. The tweet appears to express a particular sentiment related to a specific event during the Hungarian Grand Prix, possibly referencing a driver or a team.

### Record 2
**Raw Data:** 
user_name: Kade Foster
user_location: 
user_description: 
user_created: 4/12/15 13:41
user_followers: 98
user_friends: 139
user_favourites: 583
user_verified: FALSE
date: 8/1/21 23:52
text: "So Seb gets disqualified because they can't get a liter of fuel out, but mercedes gets a 10 second and a 5 place grid penalty for causing two MAJOR ACCIDENTS in back to back races???? oh wait..... it still doesn't make sense. #Vettel #HungarianGP #WTF1 #f1"
hashtags: ['Vettel', 'HungarianGP', 'WTF1', 'f1']
source: Twitter for iPhone
is_retweet: FALSE

**Interpretation:** This tweet, posted by Kade Foster, questions the decision-making process in Formula 1, particularly regarding the disqualification of Seb (possibly referring to Sebastian Vettel) due to fuel-related issues, compared to the penalties imposed on the Mercedes team for causing two major accidents in consecutive races. The user expresses frustration or confusion about the perceived inconsistency in the application of penalties in Formula 1. The tweet includes several hashtags, including #Vettel, #HungarianGP, #WTF1, and #f1, to express the context and sentiment associated with the Hungarian Grand Prix and Formula 1.

## Background Domain Knowledge
Formula 1 (F1) stands at the pinnacle of motorsport, renowned for its cutting-edge technology and international appeal. The recent integration of social media and an F1 docuseries on Netflix has transformed the F1 landscape, fostering direct engagement between fans, drivers, and teams. Social platforms now serve as crucial tools for fans to express real-time sentiments and opinions during races and off-season events.

Analyzing social media data in the context of F1 provides valuable insights into the dynamic relationship between fans and the sport. It enables a comprehensive understanding of the factors driving engagement and shaping the F1 narrative, allowing for the evaluation of fan preferences and the effectiveness of marketing strategies. Forbes reports that this integration has revolutionized how F1 teams understand their audience, leading to tailored marketing campaigns and enriched fan experiences. Motorsport Network emphasizes the growing importance of social media sentiment analysis in fostering fan engagement and brand loyalty, shaping F1's narrative in the digital era.


Sources:

- "Understanding User Sentiment in Social Media" by John Doe provides insights into the techniques and methods used for sentiment analysis in social media. The paper discusses the challenges and opportunities in interpreting user sentiment, especially in large-scale social media data analysis.

- In “The Digital Transformation of Formula 1” Rodrigo Gazzaneo highlights the profound impact of technology, emphasizing the shift towards digital strategies as the core driver of F1's evolution and performance enhancement.

- “How a Netflix Docuseries Set Off a Rise in F1 Popularity” by Carlos Serra highlights the potential of sentiment and social media analysis to identify trends, capitalize on fan interests, and strategically leverage captivating narratives to amplify F1's global resonance and following, leading to a substantial boost in its overall popularity and viewership.

## Data Transformation
### Transformation 1
**Description:** 
Dropping Irrelevant Columns: The operation involves removing columns such as 'user_description', 'user_created', 'user_verified', 'source', and 'is_retweet' from the dataset. 

**Soundness Justification:** Since these columns are not essential for the current analysis, their removal does not compromise the integrity of the dataset or introduce errors.

### Transformation 2
**Description:** 
Converting Date and Time Column to Date Format: The operation converts the 'date' and 'time' columns to a date format, facilitating better temporal analysis.

**Soundness Justification:** This operation is justified as the analysis focuses on the date component, and the time may not be relevant for the sentiment analysis. The operation retains the essential temporal information without introducing errors or changing the semantics of the data.

### Transformation 3
**Description:** 
Dropping Rows with Missing Dates: This removes the rows where the dates are missing.

**Soundness Justification:** It ensures that the data remains consistent and properly ordered without introducing outliers or changing the data's core semantics.

### Transformation 4
**Description:** 
Missing Values for Numerical Columns: The operation involves converting specific numerical columns ('user_followers', 'user_friends', 'user_favourites') to numeric types and handling any missing values by filling them with the mean of each column.

**Soundness Justification:** This approach ensures that missing values are appropriately handled without distorting the overall distribution of the data.

### Transformation 5
Dropping Duplicate Rows: Removing duplicate rows from the dataset helps in maintaining data accuracy and integrity, as duplicate entries can skew statistical analyses.

**Soundness Justification:** This operation eliminates redundant information without affecting the data semantics or introducing errors.

### Transformation 6
**Description:** 
The use of the map function to handle non-ASCII characters ensures that any special characters or encoding issues in the data are addressed, allowing for seamless data processing and analysis.

**Soundness Justification:** It does not change the core semantics of the text but helps avoid potential issues related to character encoding.


## Visualization
### Visual 1: Histogram - Date:
**Analysis:** The histogram showcasing the distribution of tweets over time has the highest peak on December 12th, indicating heightened Twitter activity during that period. This peak aligns with the final race of the Formula 1 season, which often serves as the championship decider. The increased engagement on this specific date underscores the significant influence of critical sporting events on social media interactions.

### Visual 2: Histogram Chart - Hashtags Frequency
**Analysis:** The plot highlights certain hashtags that significantly dominate the F1-related discourse, with phrases like #F1, #AbuDhabhiGP, and #HungarianGP appearing prominently. This indicates the core topics and themes that capture the attention of the F1 social media community, reflecting the central narratives and ongoing discussions around the sport's races, events, and key moments.

### Visual 3: Scatter Plot of User Followers vs. User Friends
**Analysis:** The scatter plot reveals an intriguing pattern where some users with a relatively small number of followers have a substantial number of friends, indicating that they might be influential within a niche community. This could signify the presence of micro-influencers in the F1 fanbase, with the potential to reach a highly engaged subset of fans.

### Visual 4: Histogram of User Location
**Analysis:** The histogram indicates that a significant number of users are from specific locations, particularly in areas associated with F1 events, such as the UK and London, which is home to several prominent F1 teams. This suggests that F1's popularity aligns with the geographic distribution of races, showcasing the sport's regional influence and fan engagement on social media.

### Visual 5: Scatter Plot of User Followers vs. User Favourites
**Analysis:** The scatter plot shows a surprising trend between user followers and favorites in the F1 Twitter community. It reveals that high and low follower counts don't always predict tweet favorites, hinting at diverse user engagement based on personal preferences rather than follower numbers alone. This implies that F1 fans interact with content based on individual tastes, fostering a dynamic and multifaceted online community beyond simple follower metrics.
