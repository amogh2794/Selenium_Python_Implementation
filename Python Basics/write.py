with open("test.txt", 'r') as reader:      #no need of file.close() when we use this method
    content = reader.readlines()
    reversed(content)
    with open("test.txt", 'w') as writer:
        for line in reversed(content):
            writer.write(line)


