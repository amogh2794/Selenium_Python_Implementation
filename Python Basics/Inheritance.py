from oopsdemo import Calculator

class ChildImpl(Calculator):
    num2 = 200
    def __init__(self):
        Calculator.__init__(self, 8, 9)

    def getCompleteData(self):
        return self.num2 + self.addition()

obj = ChildImpl()
print(obj.getCompleteData())