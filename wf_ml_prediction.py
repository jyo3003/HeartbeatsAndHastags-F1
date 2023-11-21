# wf_ml_prediction.py
import pandas as pd
import joblib

# Load the model
model = joblib.load('models/rf_model.joblib')

# Load the features from the test set
# Assuming the test set has been saved previously after running wf_ml_training.py
X_test = pd.read_csv('data_processed/X_test.csv')

# Make predictions
predictions = model.predict(X_test)

# Save predictions
predictions_df = pd.DataFrame(predictions, columns=['predictions'])
predictions_df.to_csv('evaluation/predictions.csv', index=False)
