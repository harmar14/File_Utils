import os

def checkFiles(mainDirName, folderName):
    print(mainDirName)
    dirName = mainDirName + '/' + folderName
    for file in os.listdir(dirName):
        tmpDir = dirName + '/' + file
        print(tmpDir, os.path.isdir(tmpDir))
        if (os.path.isdir(tmpDir) == True):
            checkFiles(dirName, file)
        else:
            path = tmpDir.replace((directory + '/' + folder2), (directory + '/' + folder1))
            if (os.path.exists(path)):
                os.remove(path)

directory = str(input("¬ведите путь к расположению двух папок, которые будут сравниватьс€ (он должен быть одинаковым): "))
folder1, folder2 = [str(i) for i in input("¬ведите имена папок через пробел: ").split()]

#пример:
#directory = "C:/Users/julia/Desktop"
#folder1 = "dir1"
#folder2 = "dir2"
#тогда пути к папкам: C:/Users/julia/Desktop/dir1 и C:/Users/julia/Desktop/dir2
#в результате выполнени€ программы все файлы папки dir1, имеющие то же им€ и уровень вложенности в папке dir2, будут стерты 

checkFiles(directory, folder2)
print("done")