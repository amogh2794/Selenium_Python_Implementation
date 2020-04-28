# example of list
# list is opened with a square bracket and contane values with multiple data types

values = [1, 2, "Amogh", 4.5]

print(values[0])
print(values[2])
print(values[-1])  # for printing last index of list

print(values[1:3])  # For printing between the index

values.insert(3,"Vaidya")  # for inserting values in a list
print(values)
values.append("last me add karega")
print(values)

values[2] = "AMOGH"  # for updating

print(values)

del values[0]  # delete marne k liye

print(values)



#-----------------------------------------------------------------------------------------------------------------------

# Tuple data type

# open with round bracket

# it is imutable which means it cannot be updated i.e values cannot be updated

tuples = ("hi", 5, 4.5)

print(tuples)
print(tuples[2])

#-----------------------------------------------------------------------------------------------------------------------

# Dictionary data type
# opens with { bracket
# contains key value pair
# key should not be in ""  if either key or value is string only then use ""

dic = {1: "Amogh", 2: 5, "c": "hello world"}
print(dic)
print(dic[1])
print(dic["c"])

# create dictionary at runtime

dict = {}

dict["Fname"] = "Amogh"
dict["lname"] = "Vaidya"
dict[1] = "one"
print(dict)