from read_folder_contents import read_folder_contents

def compare_folders(old_folder, new_folder):
    """
    Compares contents from 2 folders and returns a set of files that exist in
    the old folder but not in the new folder.
    Note: all folder names and path names must match exactly (case-sensitive).
    """
    old_files = read_folder_contents(old_folder)
    new_files = read_folder_contents(new_folder)

    missing_files = old_files - new_files
    return missing_files