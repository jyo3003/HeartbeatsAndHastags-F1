#### SERX94: Machine Learning Evaluation
#### Title: F1 Tweet Sentiment Analysis
#### Author: [Your Name]
#### Date: [Submission Date]

## Evaluation Metrics
### Metric 1
**Name:** Accuracy

**Choice Justification:** Accuracy is chosen as it provides a straightforward measure of the overall correctness of the sentiment predictions. In the context of sentiment analysis, accurately classifying tweets as positive, negative, or neutral is essential for understanding the effectiveness of the model.

**Interpretation:** The accuracy metric represents the percentage of correctly classified tweets out of the total tweets evaluated. A higher accuracy indicates better performance in predicting sentiment across the dataset.

### Metric 2
**Name:** F1 Score

**Choice Justification:** F1 Score is selected as it considers both precision and recall, providing a balanced measure that is especially valuable when dealing with imbalanced datasets. In sentiment analysis, achieving a balance between correctly identifying positive, negative, and neutral sentiments is crucial.

**Interpretation:** The F1 Score ranges from 0 to 1, with higher values indicating a better balance between precision and recall. It is particularly useful when there is an uneven distribution of sentiment classes, as it considers false positives and false negatives.

## Alternative Models
### Alternative 1
**Construction:** Use a different sentiment analysis algorithm, such as a Support Vector Machine (SVM), instead of the initially employed model (e.g., Naive Bayes).

**Evaluation:** Compare the accuracy and F1 Score of the SVM model with the baseline model to assess whether a different algorithm yields better sentiment predictions.

### Alternative 2
**Construction:** Implement sentiment analysis using a deep learning approach, such as a recurrent neural network (RNN) or long short-term memory (LSTM) network.

**Evaluation:** Evaluate the accuracy and F1 Score of the deep learning model and compare it with the baseline model's performance to determine if the complexity of the deep learning model improves sentiment analysis results.

### Alternative 3
**Construction:** Modify the feature set used for sentiment analysis by incorporating additional features, such as user engagement ratio and tweet length.

**Evaluation:** Assess the impact of the modified feature set on sentiment prediction accuracy and F1 Score compared to the baseline model.

## Visualization
### Visual 1
**Analysis:** TODO

### Visual 2
**Analysis:** TODO

### Visual 3
**Analysis:** TODO

## Best Model
**Model:** Random Forest Classifier with the default settings proved to be the best-performing model based on the accuracy and F1-score. Further tuning did not result in a significant performance gain.
