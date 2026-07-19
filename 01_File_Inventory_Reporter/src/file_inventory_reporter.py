#Uses pathlib.Path instead of string paths.
#Uses a main() function.
#Checks that the folder exists before continuing.
#Loops through files correctly.
#Uses item.stat() only once per file.
#Converts timestamps into readable dates.
#Stores data in variables before using them.
#Creates a dictionary for each file.
#Stores everything in a list.
#Writes a CSV using csv.DictWriter.
#Creates the Output folder automatically.
#Has clear comments.

import csv
from datetime import datetime
from pathlib import Path


def main() -> None:
    # Create a Path object pointing to the folder that will be scanned.
    folder = Path("Sample_Files")

    # Create an empty list to store information about every file.
    inventory = []

    # Stop the program if the folder does not exist.
    if not folder.exists():
        print("The Sample_Files folder was not found.")
        return

    print("Scanning folder...\n")

    # Loop through each item inside the Sample_Files folder.
    for item in folder.iterdir():

        # Only process items that are files.
        if item.is_file():
            # Retrieve the file metadata once.
            stats = item.stat()

            # Convert the file timestamps into readable dates.
            created_date = datetime.fromtimestamp(stats.st_ctime).strftime(
                "%Y-%m-%d %H:%M:%S"
            )
            modified_date = datetime.fromtimestamp(stats.st_mtime).strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            # Store the file information in variables.
            name = item.name
            extension = item.suffix
            size_bytes = stats.st_size
            size_kb = size_bytes / 1024
            size_mb = size_bytes / (1024 * 1024)
            parent_folder = item.parent.name
            absolute_path = str(item.resolve())

            # Assign a review category based on file size.
            if size_bytes < 10 * 1024:
                review_category = "Very Small"
            elif size_bytes > 100 * 1024 * 1024:
                review_category = "Large"
            else:
                review_category = "Normal"

            # Print the file information in the terminal.
            print(f"Name: {name}")
            print(f"Extension: {extension}")
            print(f"Size: {size_bytes:,} bytes")
            print(f"Size: {size_kb:.2f} KB")
            print(f"Size: {size_mb:.2f} MB")
            print(f"Created: {created_date}")
            print(f"Modified: {modified_date}")
            print(f"Absolute Path: {absolute_path}")
            print(f"Parent Folder: {parent_folder}")
            print(f"Review Category: {review_category}")
            print()

            # Create one dictionary containing the current file's information.
            file_record = {
                "Name": name,
                "Extension": extension,
                "Size (Bytes)": size_bytes,
                "Size (KB)": round(size_kb, 2),
                "Size (MB)": round(size_mb, 2),
                "Parent Folder": parent_folder,
                "Absolute Path": absolute_path,
                "Created": created_date,
                "Modified": modified_date,
                "Review Category": review_category,
            }

            # Add the file record to the inventory list.
            inventory.append(file_record)

    print(f"Files recorded: {len(inventory)}")

    # Create the Output folder if it does not already exist.
    output_folder = Path("Output")
    output_folder.mkdir(exist_ok=True)

    # Define the location and name of the CSV report.
    output_file = output_folder / "file_inventory.csv"

    # Define the CSV column names.
    fieldnames = [
        "Name",
        "Extension",
        "Size (Bytes)",
        "Size (KB)",
        "Size (MB)",
        "Parent Folder",
        "Absolute Path",
        "Created",
        "Modified",
        "Review Category",
    ]

    # Open the CSV file and write the inventory data.
    with output_file.open(
        "w",
        newline="",
        encoding="utf-8-sig",
    ) as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(inventory)

    print(f"CSV report created: {output_file.resolve()}")


if __name__ == "__main__":
    main()