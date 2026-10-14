#Read all lines from a file into a list.Print the total number of lines and display the second and 4th line

f = open("sample.txt" , "r")
lines = f.readlines()

print("2nd line : ",lines[2])
print("4th line : ",lines[4])

        
f.close()