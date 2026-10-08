# String : methods
# strip
# to lower 
# to upper
# join 
# count
# replace
# partition vs split

# list :methods
# append()
# insert(pos,value) : inserts specific item
# remove : removes specific item
# pop : removes last item

# list :functions
# len()
# sum()
# sorted(numbers) : asc
# sorted(numbers, reverse=True)

#1 create a list of 10 nums print the sum of last 4 elements of the elements

l = [10,20,40,30,50,60,70,80,90,10]
suml = l[-4:]
print("Sum : ",sum(suml))


#2 find out the diff between max and min no. of list
print("Diff betn max and min : ", max(l)-min(l))

#3 insert a item/number in a list at 6th pos this num must be 1/3 of num stored at 4th position
num = l[4]
l.insert(6,(num/3))
print("insert vaue at 6th pos : ",l)

s = "Sakshi"
print("Max :", max(s), "min : ", min(s) )