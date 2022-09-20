import sys
from datetime import datetime
from utils.file import readFile
from utils.regex import extractDim
from utils.turtle import compileSVG


#Regex Test
if(__name__ == "__main__"):

    if(len(sys.argv) <= 1):
        print("About Project")

    else:
        command = sys.argv[1]

        if command in ['run','0']:
            inPath = input("Enter SVG Input Path: ")
            outPath = input("Enter Output Path: ")
            if(len(outPath) == 0):
                timeUID = str(datetime.time(datetime.now())).replace(':','')
                outPath = f"new-file-{timeUID}.txt"
            val = readFile(inPath)
            extractDim(val, outPath)
            compileSVG(outPath)

        
        elif command in ['decode','1']:
            inPath = input("Enter SVG Input Path: ")
            outPath = input("Enter Output Path: ")
            if(len(outPath) == 0):
                timeUID = str(datetime.time(datetime.now())).replace(':','')
                outPath = f"new-file-{timeUID}.txt"
            val = readFile(inPath)
            extractDim(val, outPath)

        elif command in ['draw', '2']:
            filePath = input("Enter File Path: ")
            compileSVG(filePath)

        else:
            print('About Project')
