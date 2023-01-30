import os

def updateStructure(mainDirName, folderName):
    dirName = mainDirName + '/' + folderName
    for file in os.listdir(dirName):
        tmpDir = dirName + '/' + file
        # print(tmpDir, os.path.isdir(tmpDir))
        path = tmpDir.replace((directory + '/' + folder1), (directory + '/' + folder2))
        if not (os.path.exists(path)):
            os.rename(tmpDir, path)
        else:
            updateStructure(dirName, file)

directory = str(input("Введите путь к расположению двух папок, которые будут сравниваться (он должен быть одинаковым): "))
folder1, folder2 = [str(i) for i in input("Введите имена папок через пробел: ").split()]

# пример:
# directory = "C:/Users/julia/Desktop"
# folder1 = "dir1"
# folder2 = "dir2"
# тогда пути к папкам: C:/Users/julia/Desktop/dir1 и C:/Users/julia/Desktop/dir2
# в результате выполнения программы файлы и папки структуры dir1, которых нет в dir2, переместятся из dir1 в dir2 

updateStructure(directory, folder1)
print("done")
