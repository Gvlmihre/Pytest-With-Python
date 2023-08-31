# I don't need to add the close line if I use in this way
# I need to read the file and store all the lines in list
# reverse the list
# write the list back to the file

# with 'r' in the open block, I am specifying I am opening the file in a reading mode.
with open('test.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
