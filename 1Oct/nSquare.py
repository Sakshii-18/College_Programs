#Accept 2 val N and S print square of N numbers starting from S

s = int(input("Enter First Value :"))
n = int(input("Enter Last Value :"))

sum =0
for i in range(s,n+1):
    sqr = i*i
    sum += sqr
print(sum)