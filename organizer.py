import os
import shutil
import pandas as pd
from utils import ensure_dir_exists, print_progress, log_console

def organize_images(review_df, images_dir, output_dir, min_images, mode, review_csv):
    pending_list = []
    total = len(review_df)
    for idx, row in review_df.iterrows():
        aid = str(row['ActivityId'])
        img_count = int(row['ImageCount'])
        subdir = os.path.join(output_dir, 'PENDING' if img_count < min_images else aid)
        if img_count < min_images:
            subdir = os.path.join(output_dir, 'PENDING', aid)
            pending_list.append(row)
        else:
            subdir = os.path.join(output_dir, aid)
        ensure_dir_exists(subdir)
        # Move or copy images
        for file in os.listdir(images_dir):
            if file.startswith(f"{aid}_"):
                src = os.path.join(images_dir, file)
                dst = os.path.join(subdir, file)
                if mode == "MOVE":
                    shutil.move(src, dst)
                else:
                    shutil.copy2(src, dst)
        print_progress(idx+1, total, prefix='Organizing:', suffix=f"({aid})")
    # Only pending entries remain in the csv
    pending_df = pd.DataFrame(pending_list)
    pending_df.to_csv(review_csv, index=False)
    return pending_df