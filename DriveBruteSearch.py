import sys
import requests
import random

#URL Settings
urlIdSize = 33
baseUrl = "https://drive.google.com/"
urlFolderPrefix = "drive/folders/"
urlFilePrefix = "file/d/"
urlSuffix = "?usp=sharing"

#ID Generation
validChars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890-_'
generatedIds = []
generatedUrls = []

def intTryParse(value):
    try:
        return int(value)
    except:
        print("Could not parse " + value + " in int format")
        quit()
        
def generateId(count):
    generatedIds.clear()
    for i in range(count):
        id = ""
        for j in range(urlIdSize):
            id += random.choice(validChars)
        generatedIds.append(id)
        print(id)

def buildUrls(searchType):
    generatedUrls.clear()
    if searchType == "file":
        # Build file URL
        for id in generatedIds:
            thisUrl = baseUrl + urlFilePrefix + id + urlSuffix
            generatedUrls.append(thisUrl)
            print(thisUrl)
    elif searchType == "folder":
        # Build folder URL
        for id in generatedIds:
            thisUrl = baseUrl + urlFolderPrefix + id + urlSuffix
            generatedUrls.append(thisUrl)
            print(thisUrl)
    else:
        print("Type unrecognized")
        quit()
        
def testUrls():
    foundUrlsCount = 0
    for u in generatedUrls:
        print("Testing " + u)
        r = requests.get(u)
        status = r.status_code
        if status == 404:
            print("[-] Not found.\n")
        elif status == 400:
            print("[-] Bad Request\n")
        elif status == 200:
            print("[+] *** Server Found ! ***\n")
            foundUrlsCount += 1
    print("\n[*] Found URL count: " + str(foundUrlsCount))
    print("[*] Not found URL count: " + str(len(generatedUrls) - foundUrlsCount))

def main():
    if len(sys.argv) <= 2:
        print("Not enough args")
        print("Usage: test.py count type")
        print("type : file or folder")
        quit()
    
    count = intTryParse(sys.argv[1])
    searchType = sys.argv[2]
    print("----------Generating IDs----------\n")
    generateId(count)
    print("\n----------Building URLs----------\n")
    buildUrls(searchType)
    generatedIds.clear() # Clear IDs and keep only URLs
    print("\n----------Test URLs----------\n")
    testUrls()
    
if __name__ == "__main__":
    main()
