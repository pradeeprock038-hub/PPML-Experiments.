import math as mt
a=float(input("enter the co-efficient of a:"))
b=float(input("enter the co-efficient of b:"))
c=float(input("enter the co-efficient of c:"))
d=b**2 + 4*a*c
if d > 0:
    r1=(-b + mt.sqrt(d)/2*a)
    r2=(-b - mt.sqrt(d)/2*a)
    print("two real roots are : ",r1," and ",r2)
elif d==0:
    r=-b/(2*a)
    print("one real root is : ",r)
else:
    print("no real root ")