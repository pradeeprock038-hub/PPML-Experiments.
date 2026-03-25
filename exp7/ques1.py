first=int(input("enter the starting element: "))
last=int(input("enter the last number: "))
list1=[]
for i in range(first,last+1):
    list1.append(i)
print("the list 1 is :",list1)
print("Sum is : ",sum(list1))
print("Average is : ",sum(list1)/len(list1))
print("largesst is : ",max(list1))
print("Smallest is :",min(list1))
list2=[]
for i in list1:
    if i %3 !=0:
        list2.append(i)
print("except divisible by 3 : ",list2)