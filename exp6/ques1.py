fruits=["apple","banana","mango","orange","grapes"]
for fruit in reversed(fruits):
    print(fruit,"-length",len(fruit))
reversefruit=[]
for fruit in fruits:
    reversefruit.append(fruit[::-1])

print("original list :",fruits)
print("list with reversed elements:",reversefruit)