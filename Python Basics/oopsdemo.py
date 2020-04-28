# declare classes in python
# whenever we declare method inside class self variable is compulsory

class Calculator:
    num = 27  # class variable
    # default constructor
    def __init__(self,a,b):
        self.fstno = a  # instance variable
        self.sndno = b  # instance variable
        print("data in constructor")

    def getData(self):
        print("Executing as a method in class")

    def subtraction(self):
        return self.fstno - self.sndno + self.num  # we can use either self or class name for adding class variable

    def addition(self):
        return self.fstno + self.sndno + Calculator.num  # we can use either self or class name for adding class variable

obj = Calculator(2,3)  # syntax for creating object
obj.getData()
print(obj.subtraction())
print(obj.addition())
print(obj.num)

obj1 = Calculator(4,5)  # syntax for creating object
obj1.getData()
print(obj1.subtraction())
print(obj1.addition())
print(obj1.num)