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

    exit()


    loop = True
    draw = TurtleSVG()


    print("\n\nEnter Option: ")
    print("1) Decode SVG")
    print("2) Run SVG")
    print("3) Decode and Run SVG")
    print("*) Any other Key to Exit")
    choice = input('Enter your Choice: ')
    if(choice == "1"):
        print("Only Decode")
        draw.runTurtle()
    elif(choice == "2"):
        print("Only Execute")
        draw.executeTurtle()   
    elif(choice == "3"):
        draw.runTurtle()
        draw.executeTurtle()
    else:
        loop = False
        print("\n====EXIT====")
