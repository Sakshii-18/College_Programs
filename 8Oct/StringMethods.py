#strip

s = " sakshi "
print("Strip : " , s.strip())
print("Normal : ", s)

#to upper
print("To Upper : ", s.upper())

#to lower
print("To Lower : ", s.lower())

#count
print("Count s : ",s.count('s'))

#join
l = ["Python" , "is", "awesome"]
print("Join : " , " ".join(l))
print("Join string: " , " ,".join(s))

# replace
print("Replace : ", s.replace('i' , 'h'))

#split
print("Split :", s.split())

#partition 
print("After partition :", s.partition("hi"))