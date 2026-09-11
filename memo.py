# a=int(input("Enter age: "))
# b=a*365
# print(f"{a} years = {b} days")

# min=int(input("Enter minutes: "))
# hr=min//60
# rhr=min%60
# print(f"{min} minutes is {hr} hours and {rhr} mins")

role=str(input("Enter role(Student or Teacher): "))
age=int(input("Enter age: "))
print("Eligible : ", age<=21 and role.lower()=="student")