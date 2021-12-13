import math


def make_array(x, y):
    return [['*' for _ in range(x)] for _ in range(y)]


def check_right(check_array, x, y):
    new_x = x + 1
    if new_x != len(check_array):
        return check_array[new_x][y] == '*'


def check_up(check_array, x, y):
    new_y = y - 1
    if not new_y < 0:
        return check_array[x][new_y] == '*'


def check_left(check_array, x, y):
    new_x = x - 1
    if not new_x < 0:
        return check_array[new_x][y] == '*'


def check_down(check_array, x, y):
    new_y = y + 1
    if new_y != len(check_array[0]):
        return check_array[x][new_y] == '*'


def change_state():
    global direction
    if state + 1 < 3:
        state += 1
    else:
        state = 1


maxNumber = 23

maxNumber_root = math.sqrt(maxNumber)

width = math.ceil(maxNumber_root)
height = math.ceil(maxNumber_root)

print(height)
print(width)

array = make_array(width, height)
direction = 0

current_num = 1
# for i in range(len(array)):
#     for j in range(len(array[i])):
#         if state == 0 and check_right(array, i, j):
#             array[i][j] = current_num
#             change_state()
#
#         elif state == 1 and check_up(array, i, j):
#             array[i][j] = current_num
#             change_state()
#
#         elif state == 2 and check_left(array, i, j):
#             array[i][j] = current_num
#             change_state()
#
#         elif state == 3 and check_down(array, i, j):
#             array[i][j] = current_num
#             change_state()
#
#     current_num += 1

center_x = math.ceil(width / 2) - 1
center_y = math.ceil(height / 2) - 1
print(center_x)

for i in range(len(array)):
    if i + center_x < len(array):
        i += center_x
    else:
        i -= (len(array) - center_x)

    for j in range(len(array[i])):
        if j + center_y < len(array[i]):
            j += center_y
        else:
            j -= (len(array[i]) - center_y)

        array[i][j] = 1
        for row in array:
            print(row)
        print("----------------")

        continue
        # if state == 0 and check_right(array, i, j):
        #     array[i][j] = current_num
        #     change_state()
        #
        # elif state == 1 and check_up(array, i, j):
        #     array[i][j] = current_num
        #     change_state()
        #
        # elif state == 2 and check_left(array, i, j):
        #     array[i][j] = current_num
        #     change_state()
        #
        # elif state == 3 and check_down(array, i, j):
        #     array[i][j] = current_num
        #     change_state()

        # current_num += 1

for row in array:
    print(row)


