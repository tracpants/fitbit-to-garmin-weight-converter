# Fitbit to Garmin Weight Data Converter

A Python script that converts Fitbit weight data JSON exports to a CSV format that can be imported into Garmin Connect.

## Purpose

This tool helps you migrate your historical weight data from Fitbit to Garmin Connect by:
1. Reading Fitbit weight data JSON files (from Fitbit data export)
2. Converting the data into a CSV format that Garmin Connect can import
3. Handling unit conversion (optional pounds to kilograms conversion)

## Features

- Converts Fitbit JSON weight data to Garmin-compatible CSV format
- Optional weight conversion from pounds to kilograms
- Sorts data chronologically
- Includes BMI and Fat percentage data
- Formats dates to Garmin's required format (DD-MM-YYYY)

## Usage

1. Export your Fitbit data and locate the weight data JSON files
2. Place the JSON files in a directory called `weight_files`
3. Run the script:
```bash
python weight_converter.py
```
4. Choose whether to convert weights to kilograms when prompted
5. Find the output in `weight_export.csv`
6. Import the generated CSV file into Garmin Connect

## Output Format

The script generates a CSV file in the format required by Garmin Connect:
```
Body
Date,Weight,BMI,Fat
"01-12-2015","113.44","32.44","0"
```

## Requirements

- Python 3.x
- Standard Python libraries (os, json, csv, datetime)

## Directory Structure
```
fitbit-to-garmin-weight-converter/
├── weight_converter.py
├── weight_files/      # Place your Fitbit JSON files here
└── README.md
```

## Importing to Garmin Connect

1. Log in to Garmin Connect
2. Go to Health Stats
3. Select Weight
4. Click the gear icon (⚙️)
5. Select "Import From File"
6. Choose the generated CSV file

## Notes

- Make sure your weight data is in the correct format before importing to Garmin Connect
- Back up your Garmin Connect data before importing new data
- The script will ignore any entries from Withings source to avoid duplicates
