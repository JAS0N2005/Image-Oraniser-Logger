import os
from config import load_config
from excel_handler import read_input_excel, write_pending_to_excel
from image_processor import process_images
from organizer import organize_images
from utils import log_console

def main():
    # Load config
    config = load_config()
    INPUT_EXCEL = config['INPUT_EXCEL']
    IMAGES_DIR = config['IMAGES_DIR']
    OUTPUT_DIR = config['OUTPUT_DIR']
    REVIEW_CSV = config['REVIEW_CSV']
    MIN_IMAGES = config['MIN_IMAGES']
    MODE = config['MODE']  # "COPY" or "MOVE"

    log_console("Loading input Excel data...")
    data = read_input_excel(INPUT_EXCEL)
    log_console(f"Loaded {len(data)} activity entries.")

    log_console("Processing images and counting for each ActivityId...")
    review_data = process_images(data, IMAGES_DIR, REVIEW_CSV)
    log_console(f"Image count for activities written to {REVIEW_CSV}")

    log_console("Organizing images into folders based on ActivityId...")
    pending_data = organize_images(
        review_data, IMAGES_DIR, OUTPUT_DIR, MIN_IMAGES, MODE, REVIEW_CSV
    )
    log_console("Image organization complete.")

    log_console("Writing pending data to Excel...")
    write_pending_to_excel(pending_data, OUTPUT_DIR)
    log_console("All done!")

if __name__ == "__main__":
    main()