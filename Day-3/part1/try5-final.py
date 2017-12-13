import math

RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3

EMPTY = 0


def make_array(x, y):
    return [[EMPTY for _ in range(x)] for _ in range(y)]


def print_array():
    for row in array:
        print(row)
    print("----------------")


def check_right(x, y):
    global array
    new_x = x + 1
    if new_x != len(array):
        return array[new_x][y] == EMPTY


def check_up(x, y):
    global array
    new_y = y - 1
    if not new_y < 0:
        return array[x][new_y] == EMPTY


def check_left(x, y):
    global array
    new_x = x - 1
    if not new_x < 0:
        return array[new_x][y] == EMPTY


def check_down(x, y):
    global array
    new_y = y + 1
    if new_y != len(array[0]):
        return array[x][new_y] == EMPTY


def move(direct):
    global array
    global x
    global y
    global current_num

    if direct == RIGHT:
        x += 1
    elif direct == UP:
        y -= 1
    elif direct == LEFT:
        x -= 1
    elif direct == DOWN:
        y += 1

    array[x][y] = current_num


def change_direction():
    global direction
    if direction + 1 <= DOWN:
        direction += 1
    else:
        direction = RIGHT


def check():
    global direction
    global current_num

    if direction == RIGHT:
        if check_up(x, y):
            move(UP)
            change_direction()
        else:
            move(RIGHT)
    elif direction == UP:
        if check_left(x, y):
            move(LEFT)
            change_direction()
        else:
            move(UP)
    elif direction == LEFT:
        if check_down(x, y):
            move(DOWN)
            change_direction()
        else:
            move(LEFT)
    elif direction == DOWN:
        if check_right(x, y):
            move(RIGHT)
            change_direction()
        else:
            move(DOWN)
    else:
        return
    current_num += 1


maxNumber = 368078
maxNumber_root = math.sqrt(maxNumber)
width = math.ceil(maxNumber_root)
height = math.ceil(maxNumber_root)

array = make_array(width, height)

direction = RIGHT
current_num = 1

center_x = math.floor(width / 2)
center_y = math.floor(height / 2)

x = center_x
y = center_y

array[int(center_x)][center_y] = current_num

for current_num in range(maxNumber + 1):
    check()

# print_array()

midden = [center_x, center_y]

for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j] == maxNumber:
            num_index = [i, j]
            break

print(midden)
print(num_index)
print("-----------------")
print(num_index[0], "-", midden[0])
dif1 = abs(num_index[0] - midden[0])
print("= \n", dif1)
print(num_index[1], "-", midden[1])
dif2 = abs(num_index[1] - midden[1])
print("= \n", dif2)

print("Answer = ", dif1 + dif2)
