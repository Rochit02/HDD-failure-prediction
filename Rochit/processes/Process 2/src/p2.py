import pandas as pd
import glob
import os

# List of files to combine
files = [
    "failures Q1 2021.csv",
    "failures Q1 2023.csv",
    "failures Q1 2024.csv",
    "failures Q2 2020.csv",
    "failures Q2 2021.csv",
    "failures Q2 2023.csv",
    "failures Q2 2024.csv",
    "failures Q2 2025.csv"
]

# Required columns
required_columns = [
    "date","serial_number","model","capacity_bytes","failure",
    "smart_1_normalized","smart_1_raw","smart_2_normalized","smart_2_raw","smart_3_normalized","smart_3_raw",
    "smart_4_normalized","smart_4_raw","smart_5_normalized","smart_5_raw","smart_7_normalized","smart_7_raw",
    "smart_8_normalized","smart_8_raw","smart_9_normalized","smart_9_raw","smart_10_normalized","smart_10_raw",
    "smart_11_normalized","smart_11_raw","smart_12_normalized","smart_12_raw","smart_13_normalized","smart_13_raw",
    "smart_15_normalized","smart_15_raw","smart_16_normalized","smart_16_raw","smart_17_normalized","smart_17_raw",
    "smart_18_normalized","smart_18_raw","smart_22_normalized","smart_22_raw","smart_23_normalized","smart_23_raw",
    "smart_24_normalized","smart_24_raw","smart_168_normalized","smart_168_raw","smart_170_normalized","smart_170_raw",
    "smart_173_normalized","smart_173_raw","smart_174_normalized","smart_174_raw","smart_175_normalized","smart_175_raw",
    "smart_177_normalized","smart_177_raw","smart_179_normalized","smart_179_raw","smart_180_normalized","smart_180_raw",
    "smart_181_normalized","smart_181_raw","smart_182_normalized","smart_182_raw","smart_183_normalized","smart_183_raw",
    "smart_184_normalized","smart_184_raw","smart_187_normalized","smart_187_raw","smart_188_normalized","smart_188_raw",
    "smart_189_normalized","smart_189_raw","smart_190_normalized","smart_190_raw","smart_191_normalized","smart_191_raw",
    "smart_192_normalized","smart_192_raw","smart_193_normalized","smart_193_raw","smart_194_normalized","smart_194_raw",
    "smart_195_normalized","smart_195_raw","smart_196_normalized","smart_196_raw","smart_197_normalized","smart_197_raw",
    "smart_198_normalized","smart_198_raw","smart_199_normalized","smart_199_raw","smart_200_normalized","smart_200_raw",
    "smart_201_normalized","smart_201_raw","smart_202_normalized","smart_202_raw","smart_206_normalized","smart_206_raw",
    "smart_210_normalized","smart_210_raw","smart_218_normalized","smart_218_raw","smart_220_normalized","smart_220_raw",
    "smart_222_normalized","smart_222_raw","smart_223_normalized","smart_223_raw","smart_224_normalized","smart_224_raw",
    "smart_225_normalized","smart_225_raw","smart_226_normalized","smart_226_raw","smart_231_normalized","smart_231_raw",
    "smart_232_normalized","smart_232_raw","smart_233_normalized","smart_233_raw","smart_234_normalized","smart_234_raw",
    "smart_235_normalized","smart_235_raw","smart_240_normalized","smart_240_raw","smart_241_normalized","smart_241_raw",
    "smart_242_normalized","smart_242_raw","smart_245_normalized","smart_245_raw","smart_247_normalized","smart_247_raw",
    "smart_248_normalized","smart_248_raw","smart_250_normalized","smart_250_raw","smart_251_normalized","smart_251_raw",
    "smart_252_normalized","smart_252_raw","smart_254_normalized","smart_254_raw","smart_255_normalized","smart_255_raw",
    "source_file"
]

# List to store all DataFrames
dfs = []

for file in files:
    if os.path.exists(file):
        df = pd.read_csv(file)
        
        # Add source file column
        df["source_file"] = os.path.basename(file)
        
        # Keep only columns that are in required_columns
        df = df[[col for col in required_columns if col in df.columns]]
        
        dfs.append(df)
    else:
        print(f"⚠ File not found: {file}")

# Combine all dataframes
combined_df = pd.concat(dfs, ignore_index=True)

# Save to CSV
combined_df.to_csv("combined_failures.csv", index=False)

print("Combined CSV saved as combined_failures.csv")

# Count occurrences of each model
model_counts = combined_df["model"].value_counts()

# Save counts to TXT
with open("model_counts.txt", "w") as f:
    for model, count in model_counts.items():
        f.write(f"{model}: {count}\n")

print("Model counts saved to model_counts.txt")
