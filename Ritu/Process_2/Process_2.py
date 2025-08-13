import pandas as pd
import os

# Folder where your CSV files are stored
folder_path = r"D:\hdd-failures"  

# List all CSV files in the folder
csv_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

# Store DataFrames
dfs = []

for file in csv_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path, low_memory=False)  
    df["source_file"] = file  # Optional: track origin
    dfs.append(df)

# Merge all CSVs into one DataFrame (aligning columns automatically)
merged_df = pd.concat(dfs, ignore_index=True, sort=False)

# Save as Excel
output_file = r"E:\OneDrive\Documents\final_list.xlsx"  
merged_df.to_excel(output_file, index=False)

print(f" Merged {len(csv_files)} CSV files into {output_file}")


import pandas as pd

# Read your Excel file
df = pd.read_excel(r"D:\final_list.xlsx")

# Count how many times each model appears
model_counts_df = df['model'].value_counts().reset_index()
model_counts_df.columns = ['model', 'count']

# Print 
print(model_counts_df.to_string(index=False))
total_count = model_counts_df['count'].sum()
print("Total count:", total_count)

