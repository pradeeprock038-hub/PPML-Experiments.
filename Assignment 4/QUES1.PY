#wap to print the 2nd largest and 2nd smallest element in a list of 10 integers without using sort function.
arr=[]
x=int(input("Enter the no of elements:"))
for i in range(x):
    m=int(input("Enter teh element:"))
    arr.append(m)
for j in range(len(arr)-1):
    for k in range(len(arr)-j-1):
        if arr[k]>arr[k+1]:
            arr[k],arr[k+1]=arr[k+1],arr[k]
print("The sorted array is:")
print(arr)