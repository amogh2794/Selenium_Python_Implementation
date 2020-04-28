#file = open("test.txt")
#print(file.read())  # read all content of file
#rint(file.read(2))  # read n no. of characters
#print(file.readline())  # will print first line
#print(file.readline())  # will print 2nd line

#file.close()



#  print all lines using readline method

#file = open("test.txt")

#line = file.readline()
#while line != "":
#    print(line)
#   line = file.readline()
#file.close()

#  using for loop

file = open("test.txt")

for line in file.readlines():       #  use readlines method in for loop
    print(line)


file.close()