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


def change_state():
    global direction
    if direction + 1 <= DOWN:
        direction += 1
    else:
        direction = RIGHT


maxNumber = 23

maxNumber_root = math.sqrt(maxNumber)

width = math.ceil(maxNumber_root)
height = math.ceil(maxNumber_root)

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


side_width = 1
cur_index = 0
side_counter = 0
x = center_x
y = center_y


def move_y():
    global y
    if y + 1 < len(array[x]):
        y += 1
    else:
        y -= (len(array[x]) - center_y)
    return y


def move_x():
    global x
    if x + 1 < len(array):
        x += 1
    else:
        x -= (len(array) - center_x)
    return x


for _ in range(maxNumber):

        if cur_index < side_width:

            if direction == RIGHT:
                array[x + 1][y] = current_num
                x = move_x()

            elif direction == UP:
                array[x][y - 1] = current_num
                y = move_y()

            elif direction == LEFT:
                array[x - 1][y] = current_num
                x = move_x()

            elif direction == DOWN:
                array[x][y + 1] = current_num
                y = move_y()
            cur_index += 1

        elif cur_index == side_width:
            cur_index = 0
            side_width += 2
            change_state()

        print_array()
        print(x, ' - ', y)
        current_num += 1
