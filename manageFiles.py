import os
import shutil
import zlib

def choseMainFolder():  # This function allows the user to choose which is the root folder where the archive will be contained
    mainFolder = input("Enter the path where your files will be managed \n")
    return mainFolder

def createFolder(mainFolder):  # This function allows the user to create a folder in which the files are to be saved
    folderName = input("What is the folder to create? \n")
    folder = os.path.join(mainFolder, folderName)
    if not os.path.exists(folder):
        os.mkdir(folder)
    else:
        print("The folder exist! \n")

def moveFileFunction(mainFolder):  # This function allows the user to move files into a folder
    file = input("What file do you want to move from " + mainFolder + "?\n")
    movingFolder = input("Where do you want to move the file into " + mainFolder + " ?\n")
    src = mainFolder + "\\" + file
    dst = mainFolder + "\\" + movingFolder
    shutil.move(src, dst)
    return print("The file " + file + " has been successfully moved!")
