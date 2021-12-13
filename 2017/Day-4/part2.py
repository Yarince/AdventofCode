from itertools import cycle

with open("input.txt") as f:
    content = f.readlines()

content = [row.strip() for row in content]
content = [word.split() for word in content]

print(content)
for i in range(len(content)):
    for j in range(len(content[i])):
        item = list(content[i][j])
        item.sort()
        content[i][j] = ''.join(item)
    content[i].sort()
print(content)

# Practice
# str1 = "text"
# str2 = "xtet"
# str1 = list(str1)
# str1.sort()
# str2 = list(str2)
# str2.sort()
#
# print(str1 == str2)
# print(str(str1), " == ", str(str2))

wrong = 0
for row in content:
    item_list = cycle(row)
    for i in range(len(row)):
        next_item = list(row[i + 1]) if i + 1 < len(row) else []
        item = list(row[i])
        if ''.join(item) == ''.join(next_item):
            print(''.join(item), " == ", ''.join(next_item))
            print(row, " is wrong")
            wrong += 1
            break

print()
print("Wrong: ", wrong)
print("Right: ", len(content) - wrong)
