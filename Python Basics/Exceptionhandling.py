Itemincart = 0


if Itemincart != 2:
    #raise Exception("Product not in cart")
    pass


assert(Itemincart == 0)

#  try catch

try:
    with open("test1.txt", 'r') as reader:
        content = reader.readlines()
        for line in content:
            print(line)
except:            #  used for user exception
#except Exception as e:      #  used for python exception
    print("file not found")
#    print(e)

finally:
    print("gand mara bc")