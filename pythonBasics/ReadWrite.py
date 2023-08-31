file = open('test.txt')
# read all the contents of a file
# if I don't specify any characters then it will read all the content
# If I specify characters then it will print out that specified number of characters
# print(file.read())
# print(file.read(2))
# print(file.read(5))

# to read a line then I can use read line method
# print(file.readline())  # it will read the first line of the text
# print(file.readline())  # it will go on reading the next line of the first line
# if I won't comment the above methods, then it will read the first line after them


# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

# print(file.readlines())  # it will store each line in an index of a list
for line in file.readlines():
    print(line)

file.close()
