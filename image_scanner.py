# image_scanner.py

import os
import re
from config import IMAGES_SOURCE_DIR

def scan_images():
    """Scan the source directory and group image paths by ActivityId."""
    pattern = re.compile(r'^(?P<activityid>[^_]+)_.+\.jpg$', re.IGNORECASE)
    image_map = {}
    for filename in os.listdir(IMAGES_SOURCE_DIR):
        match = pattern.match(filename)
        if match:
            aid = match.group('activityid')
            path = os.path.join(IMAGES_SOURCE_DIR, filename)
            image_map.setdefault(aid, []).append(path)
    return image_map
