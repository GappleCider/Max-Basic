def createFile(fileName):
    file = open(f'shell/storage/{fileName}', "w")
    return file
