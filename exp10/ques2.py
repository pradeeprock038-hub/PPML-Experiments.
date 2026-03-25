class addition:
    def add(self):
        print("Addition is :",self.a+self.b)

class multiplication:
    def mul(self):
        print("multiplication is :",self.a*self.b)

class division:
    def div(self):
        print("the division is : ",self.a/self.b)

class subtraction:
    def sub(self):
        print("the difference is :",self.a-self.b)

class calculator(addition,multiplication,subtraction,division):
    def __init__(self,a,b):
        self.a=a
        self.b=b

x=int(input("enter the number for a  : "))
y=int(input("enter the number for b : "))
obj=calculator(x,y)
obj.add()
obj.mul()
obj.div()
obj.sub()                                                                         