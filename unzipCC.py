import zipfile
import os
import glob


def findZipFiles(folderPath):
    """Searches a folder for zip files.
    
    Args:
        folderPath: The path to the folder to search.
        
    Returns:
        A list of paths to zip files found in the folder.
    """

    zipFiles = glob.glob(os.path.join(folderPath, "*.zip"))
    return zipFiles

def unzipFile(zipFilePath, extractToPath):
    """
    Extracts all files from a zip archive.
    
    Args:
        zipFilePath (str): The path to the zip file.
        extractToPath (str): The directory to extract the contents to.
    """
    try:
        with zipfile.ZipFile(zipFilePath, 'r') as zipRef:
            zipRef.extractall(extractToPath)
        print(f"Successfully extracted '{zipFilePath}' to '{extractToPath}'")
    except FileNotFoundError:
        print(f"Error: '{zipFilePath}' was not found.")
    except zipfile.BadZipFile:
        print(f"Error: '{zipFilePath}' is not a valid zip file.")
    except Exception as e:
        print(f"An error occurred: {e}")



newFolder = str(input("Enter name of new folder: "))
if not os.path.exists(newFolder):
    os.mkdir(newFolder)
    print(f"Folder '{newFolder}' created.")
else:
    print(f"Folder '{newFolder}' already exists.")



folderPath = 'C:/Users/insan/SimsCCUnzip'
zipList = findZipFiles(folderPath)

if zipList:
    for filePath in zipList:
        subStrings = filePath.split("/")
        lastString = subStrings[-1]
        name = lastString.removeprefix("SimsCCUnzip\\")
        name = name.removesuffix(".zip")
        
        parentFolder = folderPath + "/" + newFolder
        tempFolder = os.path.join(parentFolder,name)
        os.mkdir(tempFolder)

        unzipFile(filePath, tempFolder)

        
else:
    print("No zip files found in the folder.")

print("\nUnzip Program Completed!")