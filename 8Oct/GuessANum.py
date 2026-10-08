import random

num = int(input("Guess a Number : "))
com = random.randint(0,100)

print("Your num : ",num, "Computer num :",com)


if(num == com):
    print("Yayy!! You've guessed the correct number")
   
print("Wrong Number !Please Try again!")