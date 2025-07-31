# Activity Image Organizer Tool

This repository provides a utility to organize images related to activities (Points of Interest, or POIs) based on information from an Excel sheet. It ensures each activity (by `ActivityId`) has a minimum number of images, organizes images into folders, and outputs reviews and pending lists for easy content management.

---

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Configuration (`config.json`)](#configuration-configjson)
  - [Map Explanations & When to Use](#map-explanations--when-to-use)
- [File/Column Naming Conventions](#filecolumn-naming-conventions)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Excel-Driven Organization:** Reads an Excel file containing activity metadata.  
- **Image Mapping:** Matches images to activities using a naming convention.
- **Minimum Image Check:** Ensures each activity has at least a required number of images, flagging those that do not.
- **Folder Organization:** Images are moved or copied into folders named by `ActivityId`, or into a pending folder if insufficient images are found.
- **Review/Reporting:** Generates a CSV and Excel file showing which activities are pending review due to missing images.
- **Configurable Modes:** Supports "MOVE" or "COPY" for image files.

---

## How It Works

1. **Load Configuration:** Reads options from `config.json` (input/output paths, minimum images, mode, etc).
2. **Read Activity Data:** Loads the input Excel file and checks for required columns.
3. **Image Processing:** Counts how many images exist for each activity based on file naming (`ActivityId_*`).
4. **Pending Review:** Activities with fewer than the minimum required images are flagged for review.
5. **Organize Images:**
   - Activities with enough images: images are moved/copied into a folder named by `ActivityId`.
   - Activities lacking enough images: images are moved/copied into a `PENDING/ActivityId` folder.
6. **Outputs:**
   - Updated review CSV listing image counts per activity.
   - `PENDING_REVIEW.xlsx` in the output directory, listing all activities still pending (not enough images).
   - Images organized in the output directory as per the above logic.

---

## Setup Instructions

### 1. Prerequisites

- Python 3.8+
- pip (Python package manager)

### 2. Create a virtual environment & install Dependencies using the following command sequence

```sh
python -m venv venv

.\venv\scripts\activate

pip install pandas openpyxl
```

*(Or use the included `requirements.txt` if provided)*

### 3. Configuration

Edit `config.json` to set:

- `INPUT_EXCEL`: Path to the input Excel file with activity data.
- `IMAGES_DIR`: Path to the folder containing all images.
- `OUTPUT_DIR`: Path to where organized images and reports will be written.
- `REVIEW_CSV`: Name/path for the review CSV file.
- `MIN_IMAGES`: Minimum number of images required per activity.
- `MODE`: `"COPY"` or `"MOVE"` images.

---

## Usage

Run the script from the command line:

```sh
python main.py
```

- The tool will print progress and complete when done.
- Check your `OUTPUT_DIR` for organized images and the pending review file.

---

## Configuration (`config.json`)

This file controls all paths and thresholds for the tool.

```json
{
  "INPUT_EXCEL": "I:\\...\\FINAL Vancouver.xlsx",
  "IMAGES_DIR": "I:\\...\\Vancouver",
  "OUTPUT_DIR": "I:\\...\\Vancouver_OUTPUT",
  "REVIEW_CSV": "PENDING FOR REVIEW.csv",
  "MIN_IMAGES": 1,
  "MODE": "MOVE"
}
```

### Settings Explained

| Key           | Purpose                                                                                  | Example                                                          |
|---------------|------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| INPUT_EXCEL   | Path to the master Excel file containing activity info.                                   | `"I:\\...\\FINAL Vancouver.xlsx"`                                |
| IMAGES_DIR    | Directory containing all images to process.                                               | `"I:\\...\\Vancouver"`                                           |
| OUTPUT_DIR    | Where to put organized images and review files.                                           | `"I:\\...\\Vancouver_OUTPUT"`                                    |
| REVIEW_CSV    | Name of the output CSV listing activity image counts and pending activities.              | `"PENDING FOR REVIEW.csv"`                                       |
| MIN_IMAGES    | Minimum required images per activity.                                                     | `1`                                                              |
| MODE          | `"COPY"` to duplicate images, `"MOVE"` to move them (removes from original directory).    | `"MOVE"`                                                         |

#### When to use each `MODE` value:
- Use `"MOVE"` if you want to clear out the source image directory and only keep organized copies.
- Use `"COPY"` if you want to retain the original files and just make organized duplicates.

---

## File/Column Naming Conventions

- **Image Files:** Must begin with `{ActivityId}_`, e.g., `12345_Food_1.jpg`. Only files matching this pattern are processed.
- **Excel Columns:** Required columns in the input Excel:
  - `ActivityId`
  - `Type`
  - `Name`
  - `Website`
  - `Google_Map_Link`
  - `Total_reviews`

---

## Example Workflow

Suppose you have:

- Excel file: `FINAL Vancouver.xlsx`
- Images in: `Vancouver/`
- Output folder: `Vancouver_OUTPUT/`
- Minimum required images per activity: 2

1. Place all images in the `Vancouver/` folder, named like `12345_Type_1.jpg`.
2. Set `MIN_IMAGES` to `2` in `config.json`.
3. Run:
   ```sh
   python main.py
   ```
4. Result:
   - For every activity with 2 or more images, a folder `Vancouver_OUTPUT/12345/` will have its images.
   - For any activity with <2 images, images are moved/copied to `Vancouver_OUTPUT/PENDING/12345/`.
   - `PENDING_REVIEW.xlsx` and your review CSV will show which activities are still pending.

---

## Contributing

Yours truly
Subhojyoti :)
---