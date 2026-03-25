sentence=input("enter a sentence")
list1=sentence.split()
for index,word in enumerate(list1):
    print(index,":",word)
list2=[1,2,3,4]
list3=[10,20,30,40]
combined=list(zip(list2,list3))
print("first number list:",list2)
print("second number list:",list3)
print("combined list using zip():",combined)