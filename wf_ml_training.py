import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from xgboost import XGBClassifier
import joblib
import os

def train_models():
    # In wf_ml_training.py
    print("Executing wf_ml_training.py")

    # Load the dataset
    df = pd.read_csv('data_processed/processed_f1_tweets.csv')
    # Randomly sample a subset of the data
    df = df.sample(frac=0.1, random_state=42)

    # Handle NaN values in 'hashtags' column before applying string operation
    df['hashtags'] = df['hashtags'].fillna('[]')  # Replace NaN with empty list representation

    # Assuming the hashtags are stored as strings representing lists, like "['F1', 'Race']"
    df['target'] = df['hashtags'].apply(lambda x: 1 if 'F1' in eval(x) else 0)

    # Prepare feature variables X and target y here by selecting the appropriate columns
    X = df.drop(columns=['user_name', 'user_location', 'date', 'text', 'hashtags', 'target'])
    y = df['target']

    # Split the dataset into a training set and a test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Save the training and test sets
    data_processed_dir = 'data_processed'
    if not os.path.exists(data_processed_dir):
        os.makedirs(data_processed_dir)

    X_train.to_csv(os.path.join(data_processed_dir, 'X_train.csv'), index=False)
    X_test.to_csv(os.path.join(data_processed_dir, 'X_test.csv'), index=False)
    y_train.to_csv(os.path.join(data_processed_dir, 'y_train.csv'), index=False)
    y_test.to_csv(os.path.join(data_processed_dir, 'y_test.csv'), index=False)


    # Make sure the models directory exists
    models_dir = 'models'
    if not os.path.exists(models_dir):
        os.makedirs(models_dir)

    # Initialize and train the RandomForestClassifier
    rf_model = RandomForestClassifier(random_state=42)
    rf_model.fit(X_train, y_train)
    try:
        joblib.dump(rf_model, os.path.join(models_dir, 'rf_model.joblib'))
        print("RF model saved successfully")
    except Exception as e:
        print(f"Error saving RF model: {e}")


    # Initialize and train the Logistic Regression model
    logistic_model = LogisticRegression(random_state=42)
    logistic_model.fit(X_train, y_train)
    try:
        joblib.dump(logistic_model, os.path.join(models_dir, 'logistic_model.joblib'))
        print("Logistic model saved successfully")
    except Exception as e:
        print(f"Error saving Logistic model: {e}")

    # Initialize and train the SVM model
    svm_model = SVC(random_state=42)
    svm_model.fit(X_train, y_train)
    try:
        joblib.dump(svm_model, os.path.join(models_dir, 'svm_model.joblib'))
        print("SVM model saved successfully")
    except Exception as e:
        print(f"Error saving SVM model: {e}")
    

    # Initialize and train the XGBoost model
    xgb_model = XGBClassifier(random_state=42)
    xgb_model.fit(X_train, y_train)
    joblib.dump(xgb_model, os.path.join(models_dir, 'xgb_model.joblib'))
    try:
        joblib.dump(xgb_model, os.path.join(models_dir, 'xgb_model.joblib'))
        print("XGB model saved successfully")
    except Exception as e:
        print(f"Error saving XGB model: {e}")

