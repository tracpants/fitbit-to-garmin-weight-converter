import os
import json
import csv
from datetime import datetime

# Define input/output paths
INPUT_DIR = "./weight_files"
OUTPUT_CSV = "weight_export.csv"

# Standard conversion factor
LBS_TO_KG = 0.453592


def convert_json_to_csv(input_dir, output_csv, convert_to_kg):
    """Convert Fitbit weight JSON files to CSV format."""
    data_entries = []

    for filename in os.listdir(input_dir):
        if filename.endswith(".json"):
            file_path = os.path.join(input_dir, filename)
            try:
                with open(file_path, "r") as json_file:
                    data = json.load(json_file)
                    for entry in data:

                        date_raw = entry.get("date", "")
                        weight = entry.get("weight", 0)
                        bmi = entry.get("bmi", "0")
                        fat = entry.get("fat", "0")

                        if not date_raw:
                            continue

                        # Convert date to DD-MM-YYYY format
                        try:
                            date = datetime.strptime(date_raw, "%m/%d/%y").strftime(
                                "%d-%m-%Y"
                            )
                        except ValueError:
                            print(f"Invalid date format in {filename}: {date_raw}")
                            continue

                        # Convert weight if necessary
                        if convert_to_kg:
                            weight = weight * LBS_TO_KG

                        # Create entry using exact field names
                        entry_data = {
                            "Date": date,
                            "Weight": f"{weight:.2f}",
                            "BMI": f"{float(bmi):.2f}" if bmi else "0",
                            "Fat": f"{float(fat):.0f}" if fat else "0",
                        }

                        data_entries.append(entry_data)

            except (json.JSONDecodeError, KeyError, ValueError) as e:
                print(f"Error processing {filename}: {e}")

    # Sort entries by Date
    data_entries.sort(key=lambda x: datetime.strptime(x["Date"], "%d-%m-%Y"))

    # Write to CSV with exact header format
    with open(output_csv, mode="w", newline="", encoding="utf-8") as csv_file:
        # Write the "Body" line first
        csv_file.write("Body\n")

        # Write the header and data using DictWriter
        fieldnames = ["Date", "Weight", "BMI", "Fat"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        # Write header without quotes
        csv_file.write(",".join(fieldnames) + "\n")
        writer.writerows(data_entries)


if __name__ == "__main__":
    if not os.path.exists(INPUT_DIR):
        print(f"Input directory '{INPUT_DIR}' not found.")
    else:
        user_input = (
            input("Do you want to convert weight to kilograms (kg)? (yes/no): ")
            .strip()
            .lower()
        )
        convert_to_kg = user_input == "yes"

        convert_json_to_csv(INPUT_DIR, OUTPUT_CSV, convert_to_kg)
        print(f"✅ Data has been converted and saved to '{OUTPUT_CSV}'.")
