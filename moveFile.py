import shutil


def moveFileFunction():
    file = input("Quale file vuoi muovere dalla cartella PRIVATE?")
    src = "C:\Documents\AntonioDelrio\PRIVATE\\" + "" + file
    shutil.move(src, "C:\Documents\AntonioDelrio\PRIVATE\Sposta")
    return print("Success")
