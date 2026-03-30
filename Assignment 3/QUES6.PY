#wap to remove all duplicates from a given string.
x=input("enter a string:")
result=""
for char in x:
    if char not in result:
        result=result+char
print(result)