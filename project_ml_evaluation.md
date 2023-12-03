#### SER594: Exploratory Data Munging and Visualization
#### Title: Heartbeats and Hashtags: Sentiment Analysis in F1
#### Author: Jyothirmai Kantipudi
### Date: 11/26/2023

---

## Evaluation Metrics

### Metric 1

**Name:** Accuracy

**Choice Justification:** Accuracy is chosen because it provides a straightforward indication of the model's overall performance in correctly classifying the tweets.

**Interpretation:** The Random Forest model achieved an accuracy of 0.8889, indicating that it correctly predicted the sentiment of F1 tweets 88.89% of the time.

### Metric 2

**Name:** F1-Score

**Choice Justification:** The F1-score is a harmonic mean of precision and recall, offering a balance between the two in cases where there is an uneven class distribution.

**Interpretation:** The weighted average F1-score for the model is 0.8728, suggesting a high degree of precision and recall balance in the model's predictions.

---

## Alternative Models

### Alternative 1 - Logistic Regression Model

- **Construction**: A Logistic Regression model was constructed as a baseline model with default hyperparameters.
- **Evaluation Metrics**:
  - Accuracy: 0.8511 
  - F1-Score: 0.7826 
- The Logistic Regression model performed reasonably well, achieving an accuracy of 0.8511 and an F1-Score of 0.7826.

### Alternative 2 - Support Vector Machine (SVM) Model

- **Construction**: An SVM model with a radial basis function (RBF) kernel was trained on the dataset.
- **Evaluation Metrics**:
  - Accuracy: 0.8511 
  - F1-Score: 0.7826 
- The SVM model showed performance comparable to the Logistic Regression model with an accuracy of 0.8511 and an F1-Score of 0.7826.

### Alternative 3 - XGBoost Model

- **Construction**: An XGBoost model was built with tuned hyperparameters for maximum performance on the classification task.
- **Evaluation Metrics**:
  - Accuracy: 0.8796 
  - F1-Score: 0.8481 
- The XGBoost model outperformed the Logistic Regression and SVM models, achieving an accuracy of 0.8796 and an F1-Score of 0.8481.

---
## Visualization

### Visual 1

**Analysis:** The histogram of user locations indicates the geographic distribution of the users tweeting about F1, which could be used to tailor the model's feature set to include location-based insights.

## Best Model

**Model:** The Random Forest model emerged as the best-performing model, demonstrating the highest accuracy (0.8889) and a competitive F1-Score (0.8728).

