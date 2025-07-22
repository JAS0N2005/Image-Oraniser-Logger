import os
import pandas as pd
from collections import defaultdict
from utils import print_progress

def process_images(data_df, images_dir, review_csv):
    image_files = os.listdir(images_dir)
    img_map = defaultdict(list)
    for img in image_files:
        # Format: "{ActivityId}_{Type}_{slno}.ext"
        fragments = img.split('_')
        if len(fragments) < 3:
            continue
        activity_id = fragments[0]
        img_map[activity_id].append(img)
    
    # Add ImageCount to data
    data_df = data_df.copy()
    data_df['ImageCount'] = data_df['ActivityId'].astype(str).map(lambda aid: len(img_map.get(str(aid), [])))
    
    # Save to CSV
    data_df.to_csv(review_csv, index=False)
    return data_df