print("Enter your choice :")
exit = False

while not exit:
    choice = input("+ , - , * , / ,%, !(factorial), exit : ")
    if choice == '+':
        num1 = int(input("Enter number 1 :"))
        num2 = int(input("Enter number 2 :"))

        print("Result : ", num1+num2)
    elif choice == '-':
        num1 = int(input("Enter number 1 :"))
        num2 = int(input("Enter number 2 :"))
    
        print("Result : ", num1-num2)
    elif choice == '*':
        num1 = int(input("Enter number 1 :"))
        num2 = int(input("Enter number 2 :"))
    
        print("Result : ", num1*num2)
    elif choice == '/':
        num1 = int(input("Enter number 1 :"))
        num2 = int(input("Enter number 2 :"))
    
        print("Result : ", num1/num2)
    elif choice == '%':
        num1 = int(input("Enter number 1 :"))
        num2 = int(input("Enter number 2 :"))
    
        print("Result : ", num1%num2)
    elif choice == '!':
        num1 = int(input("Enter number 1 :"))
        fact = 1 

        for i in range(1 , num1+1):
            fact = fact * i
        print("Result : ", fact)
    elif choice == "exit":
        exit = True
        print("Calculator Exited")
    else :
        print("Invalid choice")

    



