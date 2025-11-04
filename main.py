"""
This program prompts the user to enter the paths of an old folder and a new folder and
identifies any files that exist in the old folder but are missing from the new folder.
Results are printed to console.

Caitlyn Stuart
"""

from pathlib import Path
from compare_folders import compare_folders

while True:
    old_folder = input("Enter the old folder path: ")
    old_path = Path(old_folder)
    if old_path.is_dir():
        break
    else:
        print("Invalid folder path. Try again.")

while True:
    new_folder = input("Enter the new folder path: ")
    new_path = Path(new_folder)
    if new_path.is_dir():
        break
    else:
        print("Invalid folder path. Try again.")

missing = compare_folders(old_path, new_path)
if missing:
    print("Files missing from new folder:")
    for missing_file in missing:
        print(missing_file)
else:
    print("No missing files in new folder.")