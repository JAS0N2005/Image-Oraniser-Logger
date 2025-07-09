# image_processor.py

import os
import shutil
from concurrent.futures import ThreadPoolExecutor
from config import OUTPUT_BASE_DIR, MAX_WORKERS

def copy_images_for_activity(activityid, image_paths):
    """Copy all images for a given ActivityId into its output folder."""
    target_dir = os.path.join(OUTPUT_BASE_DIR, activityid)
    os.makedirs(target_dir, exist_ok=True)
    def copy_file(src):
        dest = os.path.join(target_dir, os.path.basename(src))
        if not os.path.exists(dest):
            shutil.copy2(src, dest)
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        executor.map(copy_file, image_paths)
