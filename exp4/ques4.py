num=int(input("enter a number : "))
sum=0
while num>0:
    digit=num%10
    sum+=digit
    num//=10
print("Sum of the digit : ",sum)