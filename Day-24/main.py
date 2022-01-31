# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()
#
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

FILE_PATH = 'files/'

with open(FILE_PATH+"new_file.txt", 'r+') as file:
    for letter in file.read():
        file.write(letter + " ")

