year = int(input("Enter Year to Check Leap or not :"))

if(year!=0):
    if year%4==0 and year%100 != 0:
        print("Leap")
    else:
        print("Not Leap")