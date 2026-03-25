a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
i=1
gcd=1

while i<=a and i<=b and i<=c:
    if a%i==0 and b%i==0 and c%i==0:
        gcd=i
    i+=1

print("GCD :",gcd)