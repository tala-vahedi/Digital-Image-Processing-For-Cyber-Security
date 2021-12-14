# Script Purpose: EXIF Data Acquistion Example
# Script Version: 1.0 
# Script Author:  Tala Vahedi

# Script Revision History:
# Version 1.0 Sept 15, 2021, Python 3.x

# 3rd Party Modules
from datetime import datetime   # Python Standard Libary datetime method from Standard Library
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from prettytable import PrettyTable

# Python Standard Library : Operating System Methods
import os     
# Python Standard Library : System Methods
import sys                      

# Psuedo Constants
SCRIPT_NAME    = "Script: EXIF Data Acquistion Example"
SCRIPT_VERSION = "Version 1.0"
SCRIPT_AUTHOR  = "Author: Tala Vahedi"

def ExtractGPSDictionary(fileName):
    ''' Function to Extract GPS Dictionary '''
    try:
        pilImage = Image.open(fileName)
        exifData = pilImage._getexif()

    except Exception:
        # If exception occurs from PIL processing
        # Report the 
        return None, None
    
    imageTimeStamp = "NA"
    cameraModel = "NA"
    cameraMake = "NA"
    gpsData = False

    #creating a dictionary to hold the gps values
    gpsDictionary = {}

    if exifData:
        for tag, theValue in exifData.items():
            # obtain the tag
            tagValue = TAGS.get(tag, tag)

            if tagValue == 'DateTimeOriginal':
                imageTimeStamp = exifData.get(tag).strip()

            if tagValue == "Make":
                cameraMake = exifData.get(tag).strip()

            if tagValue == 'Model':
                cameraModel = exifData.get(tag).strip()

            # check the tag for GPS
            if tagValue == "GPSInfo":

                gpsData = True

                # Loop through the GPS Information
                for curTag in theValue:
                    gpsTag = GPSTAGS.get(curTag, curTag)
                    gpsDictionary[gpsTag] = theValue[curTag]

        basicExifData = [imageTimeStamp, cameraMake, cameraModel]    
        return gpsDictionary, basicExifData
    else:
        return None, None

# End ExtractGPSDictionary ============================


def ExtractLatLon(gps):
    ''' Function to Extract Lattitude and Longitude Values '''
    try:
        latitude     = gps["GPSLatitude"]
        latitudeRef  = gps["GPSLatitudeRef"]
        longitude    = gps["GPSLongitude"]
        longitudeRef = gps["GPSLongitudeRef"]

        # converting the gps attributes to degrees
        lat, lon = ConvertToDegreesV1(latitude, latitudeRef, longitude, longitudeRef)
        gpsCoor = {"Lat": lat, "LatRef":latitudeRef, "Lon": lon, "LonRef": longitudeRef}
        return gpsCoor

    except Exception as err:
        return None
# End Extract Lat Lon ==============================================

def ConvertToDegreesV1(lat, latRef, lon, lonRef):
    degrees = lat[0]
    minutes = lat[1]
    seconds = lat[2]
    try:
        seconds = float(seconds)
    except:
        seconds = 0.0

    latDecimal = float ( (degrees +(minutes/60) + (seconds)/(60*60) ) )
    if latRef == 'S':
        latDecimal = latDecimal*-1.0
    else:
        latDecimal == latDecimal
        
    degrees = lon[0]
    minutes = lon[1]
    seconds = lon[2]

    try:
        seconds = float(seconds)
    except:
        seconds = 0.0

    lonDecimal = float ( (degrees +(minutes/60) + (seconds)/(60*60) ) )

    if lonRef == 'W':
        lonDecimal = lonDecimal*-1.0
    else:
        lonDecimal = lonDecimal
    
    return(latDecimal, lonDecimal)
''' MAIN PROGRAM ENTRY SECTION '''

if __name__ == "__main__":
    # printing program details
    print("\nExtract EXIF Data from JPEG Files")
    print("Script Started", str(datetime.now()),"\n")

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

    ''' PROCESS EACH JPEG FILE SECTION '''
    # using the os.listdir() method to extract filenames from the directory path
    directory = os.listdir(fileDir)
    # creating a pretty table with the associated column names
    resultTable = PrettyTable(['File-Name', 'Lat','Lon', 'TimeStamp', 'Make', 'Model'])
    # looping through each filename and instantiating an object using the FileProcessor Class 
    for targetFile in directory: 
        if os.path.isfile(targetFile):
            gpsDictionary, exifList = ExtractGPSDictionary(targetFile)
            if exifList:
                TS = exifList[0]
                MAKE = exifList[1]
                MODEL = exifList[2]
            else:
                TS = 'NA'
                MAKE = 'NA'
                MODEL = 'NA'
            
            if (gpsDictionary != None):
                dCoor = ExtractLatLon(gpsDictionary)
                if dCoor:
                    lat = dCoor.get("Lat")
                    latRef = dCoor.get("LatRef")
                    lon = dCoor.get("Lon")
                    lonRef = dCoor.get("LonRef")
                    
                    if (lat and lon and latRef and lonRef):
                        # adding the variables to the pretty table when all criteria are met
                        resultTable.add_row([targetFile, lat, lon, TS, MAKE, MODEL])
                    else:
                        print("WARNING No GPS EXIF Data")
                else:
                    print("WARNING No GPS EXIF Data")                    
            else:
                print("WARNING", targetFile, "not a valid file")
    # printing out the pretty table results
    print(resultTable)