import os
import shutil

source = "C:/Users/Shree/Downloads"
#print(os.listdir(source))
dest = "C:/Users/Shree/Desktop/c112"
listOfFiles = os.listdir(source)

for fileName in listOfFiles:
    name,ext = os.path.splitext(fileName)
    #print(name) 
    if ext in ['.pdf']:
        shutil.move(source,dest)