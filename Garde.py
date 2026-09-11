marks = int(input("Enter your marks out of 100 :"))

if marks<100 and marks>0 :
    if marks > 90 :
        print("Grade : O")
    elif marks > 80:
        print("Grade : A")
    elif marks > 65:
        print("Grade : B")
    elif marks > 35:
        print("Grade : C")
    else:
        print("Grade : F")
else:
    print("Invalid Marks")