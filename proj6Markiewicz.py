# Anna Markiewicz Photo Albums
# Write a script that renames and organizes image files into photo albums

# Import os and shutil modules
import os
import shutil

# Open index file, call the file object file_handle
# Read first line of input file
file_handle = open("index.txt", 'r')

def make_folders(folder_name):
    """Takes folder_name as parameter, creates folder name """
    print("Creating folder: ", folder_name)
    os.mkdir(folder_name)

def get_folder_name(line):
    """Takes line as parameter, returns folder name """
    folder = line.split(",")
    # Assign zeroth field to folder_name
    return folder[0]

def get_file_name(line):
    """Takes line as parameter, returns file name """
    # Use split to obtain fields
    object_list = line.split(",")
    file_name = object_list[1].strip( )
    # print(file_name)
    return file_name

def copy_file(folder_name, counter, original_photo_name):
    new_photo_name = "{:s}/{:03d}-{:s}". \
    format(folder_name, counter, original_photo_name)
    print(f"Copying original file {original_photo_name} to original {new_photo_name}")
    shutil.copy("originals/" + original_photo_name, new_photo_name)


line = file_handle.readline( )
# Assign previous_album to the empty string ("")
remember_album = ""
# While input file not empty
while line != "":
    folder_name = get_folder_name(line)
    #if previous_album != folder_name
    if remember_album != folder_name:
        make_folders(folder_name)
        remember_album = folder_name
        # Initialize counter to 1
        counter = 1
    original_photo_name = get_file_name(line)
    copy_file(folder_name, counter, original_photo_name) 
    counter += 1
    line = file_handle.readline( ).lower()
    
file_handle.close( )
