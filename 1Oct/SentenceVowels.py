sentence = input("enter the sentence :")
vowels = ['a' , 'e','i','o','u','A','E','I','O','U']
count =0 

for i in sentence :
    if (i == 'a' or i == 'e'or i =='i'or i =='o'or i =='u'or i =='A'or i =='E'or i =='I'or i =='O'or i =='U'):
        count = count + 1
print(count)