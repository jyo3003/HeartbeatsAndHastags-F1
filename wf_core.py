# Import the data processing and visualization modules
import wf_dataprocessing
import wf_visualization

def main():
    # Call the data processing function in wf_dataprocessing
    wf_dataprocessing.process_data()

    # Call the visualization function in wf_visualization
    wf_visualization.generate_statistics_and_visuals()

if __name__ == "__main__":
    main()
