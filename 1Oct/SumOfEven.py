#Sum of 1st 10 even no
n = 20;
sum =0;
for i in range(1,n+1):
    if(i%2 == 0):
        sum += i;
print(sum)