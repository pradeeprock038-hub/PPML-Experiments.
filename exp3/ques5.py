s1= int(input("enter the 1st marks "))
s2=int(input("enter the 2nd marks "))
s3=int(input("enter the 3rd marks "))
s4=int(input("enter the 4th marks "))
s5=int(input("enter the 5th marks "))
total=s1+s2+s3+s4+s5
percentage=(total/250)*100

if percentage >= 90:
    print("grade is O")
elif percentage >= 80:
    print("grade is E")
elif percentage >= 70:
    print("grade is A")
elif percentage >= 60:
    print("grade is B")
elif percentage >= 50:
    print("grade is C")
elif percentage >= 0:
    print("grade is F")
else:
    print("invalid grade")