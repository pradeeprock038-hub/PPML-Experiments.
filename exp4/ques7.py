num=int(input("enter the n terms of fibonacci series: "))
a,b=0,1
for i in range(num):
    temp=a+b
    a=b
    b=temp
    print(temp)