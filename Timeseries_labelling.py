import pandas as pd
import numpy as np
import time

start_time = time.time()

# Load data csv file
data_file_name = r'E:\dataset\dataset\agout.csv'
data = pd.read_csv(data_file_name, encoding='utf-8')

# Load label csv file
label_file_name = r'E:\dataset\dataset\label.csv'
labels = pd.read_csv(label_file_name, encoding='utf-8')

# Define sample rate in seconds
sample_rate = 0.0001

# Create a list of tuples containing start and end times and corresponding labels
time_labels = [(row['start_time'], row['end_time'], row['label']) for index, row in labels.iterrows()]

# Create a new DataFrame to hold the labels for each sample
labels_df = pd.DataFrame()

# Loop through each time label tuple and generate corresponding labels for each sample
for (start, end, label) in time_labels:
    start_index = round(start / sample_rate)
    end_index = round(end / sample_rate)
    label_series = pd.Series([label] * (end_index - start_index), index=range(start_index, end_index))
    labels_df = pd.concat([labels_df, label_series])

# Add the labels column to the data DataFrame
data['labels'] = labels_df

# Save the labeled data to a new csv file
data.to_csv(data_file_name + " - LABELED.csv", index=False)

end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")