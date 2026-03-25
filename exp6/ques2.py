dict={}
n=int(input("enter number of elements:"))
for i in range(n):
    key=input("enter the key:")
    value=input("enter value:")
    dict[key]=value

dict2={}
for key,value in dict.items():
    dict2[key]=value

for key,value in dict.items():
    print(f"{key}:{value}",end="\n")

for key,value in dict2.items():
    print(f"{key}:{value}",end="\n")