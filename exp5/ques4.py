lst=[]
n=int(input("Enter the number of element: "))

for i in range(n):
    lst.append(int(input()))
lst=list(set(lst))
lst.sort()
print("Sorted list =",lst)