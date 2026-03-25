num=int(input("enter the number palindrome"))
temp=0
ori=num
while(num> 0):
    digit=num%10
    temp=temp*10+digit
    num=num//10
if temp==ori:
    print("the number is palindrome")
else:
    print("the number is not palindrome")