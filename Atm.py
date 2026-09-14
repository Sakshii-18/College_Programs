option = int(input("Choose 1.Check Balance 2.Deposite 3.Withdraw 4.Exit : "))
balance = 7000

match option :
    case 1 :
        print("Balance : ", balance)
    case 2 :
        deposite = int(input("Enter Total amount to deposite :"))
        balance = balance + deposite
        print("Money Deposited! Total balance after deposite : ", balance)
    case 3 :
        withdraw = int(input("Enter amount to withdraw :"))
        if withdraw > balance :
            print("Insufficient Balance")
        else :
            balance = balance - withdraw
            print("Money Withdrew! Total balance after withdraw : ",balance )
    case 4 : 
        print("Exit")
    case _ :
        print("Invalid")
        