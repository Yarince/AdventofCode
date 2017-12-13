from itertools import cycle

with open("input.txt") as f:
    content = f.readlines()

content = [row.strip() for row in content]
content = [word.split() for word in content]

wrong = 0
for row in content:
    row.sort()
    item_list = cycle(row)
    for i in range(len(row)):
        next_item = row[i + 1] if i + 1 < len(row) else None
        item = row[i]
        if item == next_item:
            print(item, " == ", next_item)
            print(row, " is wrong")
            wrong += 1
            break

print()
print("Wrong: ", wrong)
print("Right: ", len(content) - wrong)
