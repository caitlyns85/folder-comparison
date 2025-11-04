import os
from pathlib import Path

def read_folder_contents(folder_path):
    """
    Recursively read contents from a folder and return a set of relative file paths.
    """
    files_set = set()
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            full_path = Path(root) / file
            # Store relative paths for comparison
            relative_path = full_path.relative_to(folder_path)
            files_set.add(str(relative_path))
    return files_set