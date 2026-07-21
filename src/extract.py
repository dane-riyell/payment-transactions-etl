import pandas as pd
from pathlib import Path
import json

# Path to the raw data folder
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = BASE_DIR / "data" / "raw"

def extract_csv(filename):
    try:
        df = pd.read_csv(RAW_DATA_DIR / filename)
        row_count = df.shape[0]
        column_count = df.shape[1]
        print(f"Loaded {row_count} rows and {column_count} columns from {filename}")
        return df
    except FileNotFoundError:
        # update this to log
        print("File not found")
        raise

def extract_mcc_json(filename):
    json_path = RAW_DATA_DIR / filename
    
    try:
        with json_path.open() as file:
            json_data = json.load(file)
    except FileNotFoundError:
        # update this to log
        print("File not found")
        raise

    mcc_df = pd.DataFrame(
        list(json_data.items()),
        columns=["mcc", "classification"]
    )
    row_count = mcc_df.shape[0]
    column_count = mcc_df.shape[1]
    print(f"Loaded {row_count} rows and {column_count} columns from {filename}")
    return mcc_df