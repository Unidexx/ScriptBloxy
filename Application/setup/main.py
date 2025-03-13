# Setup wizard for ScriptBloxy!

## ! IF YOU ARE SEEING THIS, THIS WAS NOT MADE FOR EDUBLOCKS. THIS IS JUST A DRAFT CODE!

# By The E-Coders

import time, os, requests


# URLS and stuff
fileURL = "https://github.com/Unidexx/sbInstallation3770/ScriptBloxy-V1.zip"

# Definitions
def load():
    fileNum = 85
    fileSize = 3758
    mfileSize = 2604

    totalSize = fileSize + mfileSize
    filesnum = fileNum

    return filesnum, totalSize

print("Welcome to the ScriptBloxy Setup Wizard!")
time.sleep(5)
print("Please wait...")
files = load()
time.sleep(14)

while True:
    dirEntry = input("Enter your directory where you want to install the file >> ")
    os.chdir(dirEntry)
    confirmation = input("Are you sure you want to download this file in this directory? Yes/No ... ")
    if confirmation == "Yes" or confirmation == "yes":
        print("Pending...")
        time.sleep(10)
        print("Downloading...")
        
        filename = os.path.basename(fileURL)
        
        response = requests.get(fileURL)
        
        file = open(filename, "wb")
        file.close()
        time.sleep(3120)
        print("Download complete! You may now exit this application...")
        break
    else:
        print()