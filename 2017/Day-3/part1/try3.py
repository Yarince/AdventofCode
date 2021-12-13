import math

RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3


def make_array(x, y):
    return [[0 for _ in range(x)] for _ in range(y)]


def check_right(x, y):
    global array
    new_x = x + 1
    if new_x != len(array):
        return array[new_x][y] == 0


def check_up(x, y):
    global array
    new_y = y - 1
    if not new_y < 0:
        return array[x][new_y] == 0


def check_left(x, y):
    global array
    new_x = x - 1
    if not new_x < 0:
        return array[new_x][y] == 0


def check_down(x, y):
    global array
    new_y = y + 1
    if new_y != len(array[0]):
        return array[x][new_y] == 0


def change_state(move):
    global direction
    if move > 0:
        if direction + 1 <= DOWN:
            direction += 1
        else:
            direction = RIGHT
    elif move < 0:
        if direction - 1 >= 0:
            direction -= 1
        else:
            direction = DOWN


maxNumber = 23

maxNumber_root = math.sqrt(maxNumber)

width = math.ceil(maxNumber_root)
height = math.ceil(maxNumber_root)

print(height)
print(width)

array = make_array(width, height)

direction = RIGHT

current_num = 1

center_x = math.floor(width / 2)
center_y = math.floor(height / 2)

array[center_x][center_y] = current_num
current_num += 1


def print_array():
    for row in array:
        print(row)
    print("----------------")


x = center_x
y = center_y
for _ in range(len(array)):

    for _ in range(len(array[x])):

        if direction == RIGHT:
            if check_right(x, y):
                array[x + 1][y] = current_num
                change_state(1)
            else:
                change_state(-1)
                continue

        elif direction == UP:
            if check_up(x, y):
                array[x][y - 1] = current_num
                change_state(1)
            else:
                change_state(-1)
                continue

        elif direction == LEFT:
            if check_left(x, y):
                array[x - 1][y] = current_num
                change_state(1)
            else:
                change_state(-1)
                continue
        elif direction == DOWN:
            if check_down(x, y):
                array[x][y + 1] = current_num
                change_state(1)
            else:
                change_state(-1)
                continue

        print_array()
        print(x, ' - ', y)
        current_num += 1

        if y + 1 < len(array[x]):
            y += 1
        else:
            y -= (len(array[x]) - center_y)

    if x + 1 < len(array):
        x += 1
    else:
        x -= (len(array) - center_x)
