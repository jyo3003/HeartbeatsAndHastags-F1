import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from xgboost import XGBClassifier
import os



def evaluate_model():
    # In wf_ml_training.py
    print("Executing wf_ml_eval.py")

    # File paths
    DATA_PATH = 'data_processed/'
    MODEL_PATH = 'models/'
    EVAL_PATH = 'evaluation/'

    # Create directories if they don't exist
    os.makedirs(MODEL_PATH, exist_ok=True)
    os.makedirs(EVAL_PATH, exist_ok=True)

    # Load training and test data
    X_train = pd.read_csv(os.path.join(DATA_PATH, 'X_train.csv'))
    y_train = pd.read_csv(os.path.join(DATA_PATH, 'y_train.csv')).values.ravel()
    X_test = pd.read_csv(os.path.join(DATA_PATH, 'X_test.csv'))
    y_test = pd.read_csv(os.path.join(DATA_PATH, 'y_test.csv')).values.ravel()

    # Initialize models
    rf_model = RandomForestClassifier()
    logistic_model = LogisticRegression()
    svm_model = SVC()
    xgb_model = XGBClassifier()

    # List of models
    models = [
        ('Random Forest', rf_model),
        ('Logistic Regression', logistic_model),
        ('SVM', svm_model),
        ('XGBoost', xgb_model)
    ]

    # Train and evaluate each model
    for name, model in models:
        try:
            # Train model
            model.fit(X_train, y_train)

            # Make predictions
            predictions = model.predict(X_test)

            # Evaluate model
            accuracy = accuracy_score(y_test, predictions)
            f1 = f1_score(y_test, predictions, average='weighted')

            # Print the evaluation metrics
            print(f"{name} Model - Accuracy: {accuracy:.4f}, F1-Score: {f1:.4f}")

            # Append evaluation metrics to the summary file
            with open(os.path.join(EVAL_PATH, 'summary.txt'), 'a') as file:
                file.write(f"{name} Model - Accuracy: {accuracy:.4f}, F1-Score: {f1:.4f}\n")


        except Exception as e:
            print(f"Error in {name} model: {e}")
