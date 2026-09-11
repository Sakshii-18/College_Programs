num1= int(input("Enter any number : "))
num2= int(input("Enter any number : "))
answer = input("Enter a Operator :")

match answer :
    case '+':
        print("Addition : ",num1+num2)
    case '-':
        print("Subtraction : ",num1-num2)
    case '/':
        if num2 == 0:
              print("Number cannot be divided by zero")
        else:
              print("Division : ",num1//num2)
    case '*':
            print("Multiplication : ", num1*num2)
    case '%':
            print("Mod :" ,num1%num2)
    case _:
            print("Invalid")
        