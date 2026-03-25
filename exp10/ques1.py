class employee:
    def __init__(self,empid,name,basicpay):
        self.empid=empid
        self.name = name
        self.basicpay=basicpay
        
    def disp(self):
        print("\nEmployee Details: ")
        print("\nEmployee id:",self.empid)
        print("\nName of employee:",self.name)
        print("\nEmployee basic pay:",self.basicpay)
        print("\nTA:",self.ta)
        print("\nDA:",self.da)
        print("\nEmployee gross pay: ",self.grosspay)
    def calc(self):
        self.ta=self.basicpay*0.1
        self.da=self.basicpay*0.4
        self.grosspay=self.ta+self.basicpay+self.da

id=int(input("enter the empolyee id :"))
name=input("enter the name of employee: ")
bp=int(input("enter the basic pay : "))
obj=employee(id,name,bp)
obj.calc()
obj.disp()