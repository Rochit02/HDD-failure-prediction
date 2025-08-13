# In this, extracted all the rows of failures from all of the csv files of single quarter and same process repeated for all quaters.

# Step 1: Mount Google Drive and unzip the dataset
from google.colab import drive
drive.mount('/content/drive')

!unzip "/content/drive/MyDrive/data_Q1_2020.zip" -d "/content/hdd_data"

# Step 2: Import libraries
import os
import pandas as pd
from google.colab import files

# Step 3: Define the folder path
folder_path = '/content/hdd_data_2020Q1'

# Step 4: Iterate over all CSV files and collect rows where failure == 1
failure_rows = []
for root, dirs, files_list in os.walk(folder_path):
    for filename in files_list:
        if filename.endswith('.csv'):
            file_path = os.path.join(root, filename)
            try:
                # Try UTF-8, fallback to latin1 for special characters
                try:
                    df = pd.read_csv(file_path, encoding='utf-8', low_memory=False)
                except UnicodeDecodeError:
                    df = pd.read_csv(file_path, encoding='latin1', low_memory=False)

                # Check for failure column
                if 'failure' in df.columns:
                    failed = df[df['failure'] == 1]
                    if not failed.empty:
                        failed['source_file'] = filename  
                        failure_rows.append(failed)

            except Exception as e:
                print(f" Error reading {filename}: {e}")

# Step 5: Combine all failure rows and save to CSV
if failure_rows:
    final_df = pd.concat(failure_rows, ignore_index=True)
    final_df.to_csv("/content/hdd_failures.csv", index=False)
    print("File with failures saved as 'hdd_failures.csv'")

    # Step 6: Download the file (optional)
    files.download("/content/hdd_failures.csv")
else:
    print(" No rows with failure = 1 were found.")
