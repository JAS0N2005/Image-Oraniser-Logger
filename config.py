# config.py

# Path to the input Excel file containing the rows to process
INPUT_EXCEL_PATH = r"H:\My Drive\HireThen\Internal - Flyberg Content\Location Scrapping Info\Subhojyoti\Hashtags Completed Data\FINAL Albuquerque.xlsx"

# Directory containing the source images named {activityid}_{type}_{sl_no}.jpg
IMAGES_SOURCE_DIR = r"C:\Users\User.WTPL-KOL-0948\Desktop\Test"

# Base directory where output folders for each ActivityId will be created
OUTPUT_BASE_DIR = r"C:\Users\User.WTPL-KOL-0948\Desktop\Sorted Images"

# Name of the subdirectory under OUTPUT_BASE_DIR to store pending activity folders
PENDING_SUBDIR_NAME = 'PENDING'

# Path to the Excel file for pending reviews
PENDING_REVIEW_FILE = r"C:\Users\User.WTPL-KOL-0948\Desktop\Image Scraping Review.xlsx"

# Number of photos threshold to trigger pending review
PHOTO_THRESHOLD = 3

# Path to the state JSON file for tracking last processed row index
STATE_FILE = r"C:\Users\User.WTPL-KOL-0948\Desktop\Sorted Images\state.json"

# Number of threads for concurrent file copying
MAX_WORKERS = 4

# Optional row range for processing (0-based indices)
# Set PROCESS_START_ROW to the first row to process (inclusive),
# and PROCESS_END_ROW to the last row to process (inclusive)
# Use None for no limit on PROCESS_END_ROW
PROCESS_START_ROW = 0
PROCESS_END_ROW = 300

# Number of pending records to buffer before automatic flush to Excel
PENDING_FLUSH_INTERVAL = 50
