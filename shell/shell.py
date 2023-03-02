import os
import token
import scripts

exited = False


def printHelp():
    print("""
    exit to quit current session [-s to save all files]\n
    touch to create a new file\n
    """)


while exited != True:
    text = input('>>>')
    result, error = token.run('<stdin>', text)

    if (text == 'exit'):
        path = r"/workspaces/Max-Basic/shell/storage/"
        for file_name in os.listdir(path):
            # construct full file path
            file = path + file_name
        if os.path.isfile(file):
            os.remove(file)
        exited = True
    elif (text[:4] == 'exit' and text[5:] == '-s'):
        exited = False
    elif (text[:5] == 'touch'):
        scripts.createFile(text[6:])
    elif (text == 'help'):
        printHelp()
    elif (len(text) > 0 and error == None):
        print(result)
    elif (len(text) > 0):
        print(error.as_string())
