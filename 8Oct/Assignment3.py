#Q1 find all meaningful words from your name

name = "Sakshi"


#Q2 replace all the vowels from your name w 'z'


name2 = ""
vowels = "AEIOUaeiou"

for i in name:
    if i in vowels:
        name2 += 'z'
    else:
        name2 += i
print(name2)

#create a list of nums and strings accept the values from user separate the list from the max num display the names in list in sorted desc order

l = []

for i in range(0,5):
    num = input("enter any num or string : ")
    l.append(num)
print(l)
print("List in desc order : ", sorted(l,reverse=True))