## Data Labeling

This Python script is designed to label time series data using a separate CSV file containing start and end times and corresponding labels. The labeled data is saved to a new CSV file.

## Dependencies

This script requires the following Python libraries:

-   pandas
-   numpy

## Usage

To use this script, you must have a CSV file containing your time series data and another CSV file containing start and end times and corresponding labels.

The data file should be formatted with each row representing a single data point and each column representing a different variable.

The label file should be formatted with each row representing a single labeled segment of the time series data. The file should contain three columns: "start_time", "end_time", and "label". The start and end times should be in seconds and the label should be an integer.

To use the script, modify the following variables at the beginning of the code:

-   `data_file_name`: the file path of your data CSV file
-   `label_file_name`: the file path of your label CSV file
-   `sample_rate`: the sample rate of your data in seconds

Then, run the script to generate a new CSV file with the same data as the original data file but with a new "labels" column containing the corresponding label for each data point.

The new CSV file will be saved in the same directory as the original data file with "- LABELED" appended to the file name.
