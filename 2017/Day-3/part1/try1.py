import math


def make_array(x, y):
    return [[0 for j in range(x)] for i in range(y)]


maxNumber = 23

maxNumber_root = math.sqrt(maxNumber)

width = math.ceil(maxNumber_root)
height = math.floor(maxNumber_root)

print(height)
print(width)

array = make_array(width, height)

# Print a clear version of the array
# for row in array:
#     print(row)

center_x = int(width / 2)
center_y = int(height / 2)


# center = array[center_x][center_y]

# array[center_x][center_y] = 1


def check_right(check_array, x, y):
    new_x = x + 1
    return (not new_x != len(check_array[0])) and check_array[new_x][y] == 0


def check_up(check_array, x, y):
    new_y = y - 1
    return (not new_y < 0) and check_array[x][new_y] == 0


def check_left(check_array, x, y):
    new_x = x - 1
    return (not new_x < 0) and check_array[new_x][y] == 0


def check_down(check_array, x, y):
    new_y = y + 1
    return (new_y != len(check_array)) and check_array[x][new_y] == 0


current_state = 0
current_number = 1


def iterate(x, y):
    global array
    global current_number
    global current_state
    if current_state == 0:
        if check_left(array, x, y):
            array[x][y] = current_number
            current_state = 0
            return
    elif current_state == 1:
        if check_right(array, x, y):
            array[x][y] = current_number
            current_state = 0
            return
    elif current_state == 2:
        if check_up(array, x, y):
            array[x][y] = current_number
            current_state = 0
            return
    elif current_state == 3:
        if check_down(array, x, y):
            array[x][y] = current_number
            current_state = 0
            return

    if current_state + 1 < 3:
        current_state += 1
    else:
        current_state = 0

    current_number += 1


for row in range(len(array)):
    for item in range(len(array[row])):
        iterate(row, item)

for row in array:
    print(row)

# Cheat
# array = [
#     [17, 16, 15, 14, 13],
#     [18, 5, 4, 3, 12],
#     [19, 6, 1, 2, 11],
#     [20, 7, 8, 9, 10],
#     [21, 22, 23]
# ]
# for row in array:
#     print(row)

# def manhattan_distance(start, end):
#     sx, sy = start
#     ex, ey = end
#     return abs(ex - sx) + abs(ey - sy)
#
#
#
# # Some online example
# from collections import namedtuple
# from itertools import count
#
# Step = namedtuple("Step", ["dx", "dy"])
# RIGHT = Step(1, 0)
# DOWN = Step(0, 1)
# LEFT = Step(-1, 0)
# UP = Step(0, -1)
#
#
# def steps_from_center():
#     for n in count(start=1):
#         if n % 2:
#             yield RIGHT
#             for i in range(n):
#                 yield DOWN
#             for i in range(n):
#                 yield LEFT
#         else:
#             yield LEFT
#             for i in range(n):
#                 yield UP
#             for i in range(n):
#                 yield RIGHT
