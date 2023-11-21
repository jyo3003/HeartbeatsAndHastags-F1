# wf_ml_evaluation.py
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

def evaluate_model():
    # Load the model
    model = joblib.load('models/rf_model.joblib')

    # Load the test data and true labels
    X_test = pd.read_csv('data_processed/X_test.csv')
    y_test = pd.read_csv('data_processed/y_test.csv')

    # Make predictions using the model
    predictions = model.predict(X_test)

    # Evaluate the predictions
    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions, output_dict=True)

    # Prepare the summary text
    summary = (
        f"Model: {'Random Forest'}\n"
        f"Accuracy: {accuracy:.4f}\n"
        f"Precision: {report['weighted avg']['precision']:.4f}\n"
        f"Recall: {report['weighted avg']['recall']:.4f}\n"
        f"F1-score: {report['weighted avg']['f1-score']:.4f}\n"
    )
    print(summary)

    # Ensure the evaluation directory exists before writing the report
    evaluation_dir = 'evaluation'
    if not os.path.exists(evaluation_dir):
        os.makedirs(evaluation_dir)

    # Save the summary to a text file
    evaluation_report_path = os.path.join(evaluation_dir, 'summary.txt')
    with open(evaluation_report_path, 'a') as f:
        f.write(summary + "\n")

    # If additional models were evaluated, append their results to the summary file as well
    # ...

if __name__ == "__main__":
    evaluate_model()
