import math as mt
a=int(input("enter the a ="))
b=int(input("enter the b="))
c=int(input("enter the c="))
p=a+b+c
s=p/2
area=mt.sqrt(s*(s-a)*(s-b)*(s-c))
print(f"area of triangle = {area} & perimeter of triangle {p}")