age = int(input("enter your age : "))
ticket = 100

if age<12:
    print("For Children :",ticket-ticket*10/100)
else:
    print("For Adult :",ticket)