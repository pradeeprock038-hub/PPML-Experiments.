class product:
    def __init__(self,id,name,p,q):
        self.product_id=id
        self.product_name=name
        self.price=p
        self.quantity=q
        self.total_amount=0
    def calculate_total(self):
        self.total_amount=self.price*self.quantity


    def display(self):
        print("\nThe product details :")
        print("The product id is : ",self.product_id)
        print("The product Name is :",self.product_name)
        print("The price is : ",self.price)
        print("\nThe quantity is :",self.quantity)
        print("the total amount is : ",self.total_amount)
id=int(input("enter the id : "))
name=input("enter the name of product: ")
p=float(input("enter the price of the product : "))
q=int(input("enter the quantity:"))
obj=product(id,name,p,q)
obj.calculate_total()
obj.display()