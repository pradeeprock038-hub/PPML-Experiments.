x=int(input("enter the number to reverse"))
temp=0
while(x > 0):
    digit=x%10
    temp=temp*10+digit
    x=x//10
print(temp)