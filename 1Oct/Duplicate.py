#Remove Duplicate
list = [1,2,3,4,2,1,3,4]
newlist = []


for i in list :
    if i not in newlist:
        newlist.append(i)
print(newlist)