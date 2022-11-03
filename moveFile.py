import shutil


def moveFileFunction():
    file = input("What file do you want to move from PRIVATE? (Specifies the extension)")
    src = "C:\Documents\PRIVATE\\" + "" + file
    shutil.move(src, "C:\Documents\PRIVATE\Moved")
    return print("Success")
