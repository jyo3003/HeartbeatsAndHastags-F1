# wf_ml_prediction.py
import pandas as pd
import joblib

def make_predictions():

    # In wf_ml_training.py
    print("Executing wf_ml_prediction.py")

    # Load the features from the test set
    # Assuming the test set has been saved previously after running wf_ml_training.py
    X_test = pd.read_csv('data_processed/X_test.csv')

    # Load the Random Forest model
    rf_model = joblib.load('models/rf_model.joblib')

    # Load the Logistic Regression model
    logistic_model = joblib.load('models/logistic_model.joblib')

    # Load the SVM model
    svm_model = joblib.load('models/svm_model.joblib')

    # Load the XGBoost model
    xgb_model = joblib.load('models/xgb_model.joblib')

    # Make predictions using each model
    rf_predictions = rf_model.predict(X_test)
    logistic_predictions = logistic_model.predict(X_test)
    svm_predictions = svm_model.predict(X_test)
    xgb_predictions = xgb_model.predict(X_test)

    # Print or use the predictions as needed
    print("Random Forest Prediction:", rf_predictions)
    print("Logistic Regression Prediction:", logistic_predictions)
    print("SVM Prediction:", svm_predictions)
    print("XGBoost Prediction:", xgb_predictions)

    # Save predictions
    rf_predictions_df = pd.DataFrame(rf_predictions, columns=['rf_predictions'])
    logistic_predictions_df = pd.DataFrame(logistic_predictions, columns=['logistic_predictions'])
    svm_predictions_df = pd.DataFrame(svm_predictions, columns=['svm_predictions'])
    xgb_predictions_df = pd.DataFrame(xgb_predictions, columns=['xgb_predictions'])

    rf_predictions_df.to_csv('evaluation/rf_predictions.csv', index=False)
    logistic_predictions_df.to_csv('evaluation/logistic_predictions.csv', index=False)
    svm_predictions_df.to_csv('evaluation/svm_predictions.csv', index=False)
    xgb_predictions_df.to_csv('evaluation/xgb_predictions.csv', index=False)

