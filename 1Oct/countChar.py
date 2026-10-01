# s = "Sakshii"
# s = s.lower()
# for i in s:
#     count = 0

#     for j in s:
#         if i == j:
#             count += 1

#     print(i, "count is : ", count)

s = "Sakshii"
vowels = "aeiouAEIOU"
s = s.lower()
for i in s:
    count = 0

    for j in vowels:
        if i == j:
            count += 1

    print(i, "count is : ", count)