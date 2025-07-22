import pandas as pd
import os

def read_input_excel(input_excel):
    df = pd.read_excel(input_excel)
    required_cols = ["ActivityId", "Type", "Name", "Website", "Google_Map_Link", "Total_reviews"]
    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        raise ValueError(f"Missing columns in input Excel: {missing}")
    return df[required_cols]

def write_pending_to_excel(pending_data, output_dir):
    output_excel = os.path.join(output_dir, 'PENDING_REVIEW.xlsx')
    pending_data.to_excel(output_excel, index=False)