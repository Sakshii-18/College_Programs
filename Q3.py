#Q3 Take a 3 sentences from the user ,split it into words, and store them in a list, print the longest word

s = input("enter any sentence :")
words = s.split(" ")
print(words)
max = ""

for i in words:
    if len(max) < len(i):
        max = i
print(max)