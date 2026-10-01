a = int(input("Enter number 1 :"))
b = int(input("Enter number 2 :"))
c = int(input("Enter number 3 :"))

if a==b and b==c:
    print("All are Equal")
elif a >= b and a>= c:
    print(a, "is greater")
elif b>=c and b>=a:
    print(b,"is greater")
else:
    print(c,"is greater")
