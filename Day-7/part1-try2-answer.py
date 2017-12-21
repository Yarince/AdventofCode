import re
import time

start_time = time.time()
with open("input.csv") as f:
    content = f.readlines()

array = []

for item in content:
    item = re.sub(r'(\([0-9]*\))|(\s)', '', item)
    item = item.strip()

    if len(item.split("->")) > 1:
        item = item.split("->")
        item = [[item[0], True]] + item[1].split(',')
        array.append(item)

for item in array:
    for item2 in array:
        if item[0][0] in item2:
            item[0][1] = False
            continue

for item in array:
    if item[0][1]:
        print("Answer =", item[0][0])

print("Lol it took", time.time() - start_time, " seconds to run")
