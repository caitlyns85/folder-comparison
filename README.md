# Folder Comparison Tool

A Python program to compare the contents of two folders and identify missing files. It can:

- Recursively scan directories and subdirectories.  
- Compare files between an old folder and a new folder.  
- Display missing files in a sorted, readable format.  
- Handle nested directories and maintain relative file paths.  

---

## Features

- Efficient file comparison using Python sets.  
- Modular design with separate functions for reading folder contents and comparing folders.  
- Supports user input validation for folder paths.  
- Can be extended to include additional file checks, such as file size or type.  

---

## File Structure

```
folder_comparison_tool/
│
├── src/
│   ├── main.py                # main program for user input and comparison
│   ├── compare_folders.py     # function to compare folder contents
│   └── read_folder_contents.py# function to recursively read folder files
│
└── README.md
```

---

## Setup and Installation

1. Clone the repository:

```bash
git clone <repo-url>
cd folder_comparison_tool
```

2. (Optional) Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

All dependencies are standard Python libraries (no external packages required).  

---

## Running the Program

Run the main program:

```bash
python3 src/main.py
```

- Follow the prompts to enter the paths of the old and new folders.  
- The program will display any files that are missing from the new folder.  

---

## Notes

- Compatible with Python 3.  
- Paths are case-sensitive and folder names must match exactly.  
- Can be extended to compare file sizes or other attributes.  
- No external dependencies required.  
