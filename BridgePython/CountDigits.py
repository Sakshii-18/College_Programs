n = int(input("Enter any number :"))
count = 0


while(n>0):
    rem = n%10
    count = count + 1
    n = n//10
print(count)