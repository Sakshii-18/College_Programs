#Q4READ FILE AND SPLIT IT INTO LIST

file = open("sample.txt" , "r")
content = file.readline()
list1 = content.split(" ")

print(list1)

#1 print total no of words
count = len(list1)
print(count)

#2 print all unique words
s = []

for i in list1:
    if i not in s:
        s.append(i)
print("Unique Words : " ,s)

file.close()

