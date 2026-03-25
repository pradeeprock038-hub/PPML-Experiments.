a=int(input("enter the a value to swap:"))
b=int(input("enter the b value to swap:"))
print(f"before swap value a={a} & b={b}")
a=a+b
b=a-b
a=a-b
print(f"after swap value a={a} & b={b}")