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
        item = {item[0]: item[1]}
        for key, value in item.items():
            item = {key: value.split(',')}
            array.append(item)

for item in array:
    print(item)
iterations = 0
i = 0
j = 0
array_sorted = False
while not array_sorted:
    if j < len(array) - 1:
        j = j + 1
    else:
        i = i + 1 if i < len(array) - 1 else 0
        j = 0

    i_row = array[i]
    j_row = array[j]
    next_row = next(iter(j_row))
    for row_key, next_value in i_row.items():
        for k in range(len(next_value)):
            iterations += 1
            if next_value[k] == next_row:
                i_row[row_key][k] = array[j]
                disk = array[j]
                array.remove(array[j])
                continue

    # print(array[i])

    array_sorted = len(array) == 1


def print_crazy_array(array):
    print("{")
    for item in array:
        for key, value in item.items():
            print("\"%s\":{" % key)
            for item1 in value:
                print("    %s," % item1)
            print("   }")
    print("}")


print_crazy_array(array)
print("iterations %d" % iterations)
print("Lol it took", time.time() - start_time, " seconds to run")
