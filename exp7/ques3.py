str1=input("enter an paragraph: ")
words=str1.split()
print("number of words are : ",len(words))

palindrome_cou0nt=0

for word in words:
    if word.lower()==word[::-1].lower():
        palindrome_cou0nt+=1

print("number of palindrome are : ",palindrome_cou0nt)

print("word in reverse :")

for word in words:
    print(word[::-1])