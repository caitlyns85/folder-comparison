# Folder Comparison Tool

A Python program that compares the contents of two folders and identifies files that are missing in the new folder.  
The tool recursively scans directories, stores relative file paths, and outputs any missing files, making it useful for backups, migrations, or version control.

## Features
- Recursively scans folders and subfolders
- Compares files based on relative paths
- Outputs missing files in a clear list
- Cross-platform: works on Mac, Windows, Linux

## Technical Details
- Python 3
- Uses `os` and `pathlib` modules for file system operations
- Modular design with separate files for scanning and comparing folders
- Designed for clarity and easy extension

## Usage
Run the program in the terminal:

```bash
python main.py
