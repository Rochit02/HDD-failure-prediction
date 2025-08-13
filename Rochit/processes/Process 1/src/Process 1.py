# In this process, we are collecting all the rows of failures from each of the csv files from each quarter and combining it into one single quarter's failure data.
import pandas as pd
from datetime import datetime, timedelta

start_date = datetime.strptime('2021-01-01', '%Y-%m-%d')
end_date = datetime.strptime('2021-03-31', '%Y-%m-%d')

failures_list = []

current_date = start_date
while current_date <= end_date:
    filename = current_date.strftime('%Y-%m-%d') + '.csv'
    try:
        df = pd.read_csv(filename)
        if 'failure' in df.columns:
            filtered_df = df[df['failure'] > 0]
            if not filtered_df.empty:
                filtered_df['source_file'] = filename
                failures_list.append(filtered_df)
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Skipping...")
    except Exception as e:
        print(f"Error processing {filename}: {e}")
    current_date += timedelta(days=1)

if failures_list:
    all_failures = pd.concat(failures_list, ignore_index=True)
    all_failures.to_csv('failures.csv', index=False)
    print("Filtered failures saved to failures.csv.")
else:
    print("No failures found in the specified date range.")
