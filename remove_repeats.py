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

directory = str(input("������� ���� � ������������ ���� �����, ������� ����� ������������ (�� ������ ���� ����������): "))
folder1, folder2 = [str(i) for i in input("������� ����� ����� ����� ������: ").split()]

#������:
#directory = "C:/Users/julia/Desktop"
#folder1 = "dir1"
#folder2 = "dir2"
#����� ���� � ������: C:/Users/julia/Desktop/dir1 � C:/Users/julia/Desktop/dir2
#� ���������� ���������� ��������� ��� ����� ����� dir1, ������� �� �� ��� � ������� ����������� � ����� dir2, ����� ������ 

checkFiles(directory, folder2)
print("done")