import os
from pathlib import Path


fileList = []

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            if not file[0] == '.':
                fileList.append(file)
                os.rename(file, '.' + file)
    return fileList

def main():
    print(files('.'))

main()




