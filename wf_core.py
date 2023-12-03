# wf_core_modified.py
import wf_dataprocessing
import wf_visualization
import wf_ml_training
import wf_ml_evaluation
import wf_ml_prediction 

def main():
    # Call the data processing function in wf_dataprocessing
    wf_dataprocessing.process_data()

    # Call the visualization function in wf_visualization
    wf_visualization.generate_statistics_and_visuals()
    
    # Train the model and save the datasets
    wf_ml_training.train_models()

    # Evaluate the model
    wf_ml_evaluation.evaluate_model()

    # Make predictions using the trained models
    wf_ml_prediction.make_predictions()  # New function

if __name__ == "__main__":
    main()
