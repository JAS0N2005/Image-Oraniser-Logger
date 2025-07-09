# main.py

import os
import shutil
import pandas as pd
from config import (
    INPUT_EXCEL_PATH, PHOTO_THRESHOLD,
    PROCESS_START_ROW, PROCESS_END_ROW,
    OUTPUT_BASE_DIR, PENDING_SUBDIR_NAME
)
from state_manager import load_state, save_state
from image_scanner import scan_images
from image_processor import copy_images_for_activity
from pending_review import add_pending_review

def process_rows():
    last_processed = load_state()
    df = pd.read_excel(INPUT_EXCEL_PATH, dtype=str)
    required_cols = ['Name','Type','Website','Total_reviews','Google_Map_Link','ActivityId']
    for col in required_cols:
        if col not in df.columns:
            print(f"ERROR: Column {col} not found in input Excel.")
            return

    image_map = scan_images()

    for idx, row in df.iterrows():
        if idx < PROCESS_START_ROW:
            continue
        if PROCESS_END_ROW is not None and idx > PROCESS_END_ROW:
            continue
        if idx <= last_processed:
            continue

        activityid = row['ActivityId']
        paths = image_map.get(activityid, [])
        copy_images_for_activity(activityid, paths)
        count = len(paths)

        if count < PHOTO_THRESHOLD:
            # Buffer for pending review
            add_pending_review({
                'ActivityId': activityid,
                'Name': row['Name'],
                'Type': row['Type'],
                'Website': row['Website'],
                'Google_Map_Link': row['Google_Map_Link'],
                'PhotoCount': count
            })
            # Move folder to Pending subdirectory
            pending_base = os.path.join(OUTPUT_BASE_DIR, PENDING_SUBDIR_NAME)
            os.makedirs(pending_base, exist_ok=True)
            src = os.path.join(OUTPUT_BASE_DIR, activityid)
            dst = os.path.join(pending_base, activityid)
            if os.path.exists(dst):
                shutil.rmtree(dst)
            shutil.move(src, dst)

        save_state(idx)
        print(f"Processed row {idx} (ActivityId={activityid}): {count} images.")

def main():
    try:
        process_rows()
    except KeyboardInterrupt:
        print("Interrupted, exiting early.")
    except Exception as e:
        print(f"Error: {e}, exiting early.")
    print("Done.")

if __name__ == '__main__':
    main()
