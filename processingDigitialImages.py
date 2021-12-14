# Script Purpose: Searching For Digital Images in Python
# Script Version: 1.0 
# Script Author:  Tala Vahedi

# Script Revision History:
# Version 1.0 Sept 15, 2021, Python 3.x

# 3rd Party Modules
from PIL import Image
from prettytable import PrettyTable

# Python Standard Library
import os

# Psuedo Constants
SCRIPT_NAME    = "Script: Searching For Digital Images in Python"
SCRIPT_VERSION = "Version 1.0"
SCRIPT_AUTHOR  = "Author: Tala Vahedi"

if __name__ == '__main__':
    # Print Basic Script Information
    print()
    print(SCRIPT_NAME)
    print(SCRIPT_VERSION)
    print(SCRIPT_AUTHOR)
    print()

    # Setup Pretty Table with the appropriate column names
    pTable = PrettyTable(['File', 'Ext','Format', 'Width', 'Height', 'Mode'])    

    # prompting the user for a directory path continoulsy 
    while True:
        # prompting user to enter a path or enter 'exit' to end the program
        fileDir = input("Please enter a path (or enter 'exit' to stop the program): ")
        # condition that ends the program if user inputs 'exit'
        if fileDir == "exit":
            exit()
        # if path is not found, prompt the user to re-enter a path or exit the program
        elif os.path.exists(fileDir) == False:
            print("ERROR: Invalid file path, please try another path\n")
            continue
        # print processing the file path and break while statement to continue with code
        else:
            print("\nProcessing File, please wait...\n")
            # breaking out of the while look to proceed with script
            break
    
    # using the os.listdir() method to extract filenames from the directory path
    directory = os.listdir(fileDir)
    # looping through each filename and instantiating an object using the FileProcessor Class
    for fileName in directory:
        # using try except in order to filter out files that are not images
        try:
            # opening the file to examine its data
            im = Image.open(fileName)
            # variable to grab the file name
            imPath = im.filename
            # variable that uses splittext method to extract the ext
            imExtension = os.path.splitext(im.filename)[1]
            # variable to grab the image format
            imFormat = im.format
            # variable to grab the image width
            imWidth = im.width
            # variable to grab the image height
            imHeight = im.height
            # variable to grab the image mode
            imMode = im.mode
            # added each image's metadata to the table for pretty formatting
            pTable.add_row([imPath, imExtension, imFormat, imWidth, imHeight, imMode])
        # throwing an exception error to avoid files which are not images
        except IOError:
            # passing files that are not images
            pass
    
    # printing out the final results of the table
    print(pTable)