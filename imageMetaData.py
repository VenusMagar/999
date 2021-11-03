from PIL import Image
from PIL.ExifTags import TAGS

def getImageMetaData(imgName):
    try:
        metaData = {}
        imgFile = Image.open(imgName)
        print("Obtaining Metadata From the Image")
        imageMetaData = imgFile._getexif()
        
        if imageMetaData:
            print("Metadata Obtained")

            for(tag, value) in imageMetaData.items():
                tagname = TAGS.get(tag, tag)
                metaData[tagname] = value
                print(tagname, value)
        
    except:
        print("Failed To Obtain The Metadata")

def executeProgram():
    imageFilePath = input("Enter the full path of the image : ")
    getImageMetaData(imageFilePath)

executeProgram()
