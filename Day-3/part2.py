import math

RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3

UP_RIGHT = 4
UP_LEFT = 5
DOWN_RIGHT = 6
DOWN_LEFT = 7

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
    return new_x != len(array)


def check_up(x, y):
    global array
    new_y = y - 1
    return not new_y < 0


def check_left(x, y):
    global array
    new_x = x - 1
    return new_x >= 0


def check_down(x, y):
    global array
    new_y = y + 1
    return new_y != len(array[0])


def right_empty(x, y):
    global array
    new_x = x + 1
    return new_x != len(array) and array[new_x][y] == EMPTY


def up_empty(x, y):
    global array
    new_y = y - 1
    return not new_y < 0 and array[x][new_y] == EMPTY


def left_empty(x, y):
    global array
    new_x = x - 1
    return new_x >= 0 and array[new_x][y] == EMPTY


def down_empty(x, y):
    global array
    new_y = y + 1
    return new_y != len(array[0]) and array[x][new_y] == EMPTY


def check_right_up(x, y):
    return check_right(x, y) and check_up(x, y)


def check_left_up(x, y):
    return check_left(x, y) and check_up(x, y)


def check_right_down(x, y):
    return check_right(x, y) and check_down(x, y)


def check_left_down(x, y):
    return check_left(x, y) and check_down(x, y)


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

    array[x][y] = get_around()


def get(direct):
    global array
    global x
    global y
    global current_num

    if direct == RIGHT:
        return array[x + 1][y]
    elif direct == UP:
        return array[x][y - 1]
    elif direct == LEFT:
        return array[x - 1][y]
    elif direct == DOWN:
        return array[x][y + 1]

    elif direct == UP_RIGHT:
        return array[x + 1][y - 1]
    elif direct == UP_LEFT:
        return array[x - 1][y - 1]
    elif direct == DOWN_RIGHT:
        return array[x + 1][y + 1]
    elif direct == DOWN_LEFT:
        return array[x - 1][y + 1]


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
        if up_empty(x, y):
            move(UP)
            change_direction()
        else:
            move(RIGHT)
    elif direction == UP:
        if left_empty(x, y):
            move(LEFT)
            change_direction()
        else:
            move(UP)
    elif direction == LEFT:
        if down_empty(x, y):
            move(DOWN)
            change_direction()
        else:
            move(LEFT)
    elif direction == DOWN:
        if right_empty(x, y):
            move(RIGHT)
            change_direction()
        else:
            move(DOWN)
    else:
        return


def get_around():
    global array
    global x
    global y
    global current_num

    current_num = 0
    if check_right(x, y):
        current_num += get(RIGHT)
    if check_down(x, y):
        current_num += get(DOWN)
    if check_left(x, y):
        current_num += get(LEFT)
    if check_up(x, y):
        current_num += get(UP)
    if check_right_up(x, y):
        current_num += get(UP_RIGHT)
    if check_left_up(x, y):
        current_num += get(UP_LEFT)
    if check_right_down(x, y):
        current_num += get(DOWN_RIGHT)
    if check_left_down(x, y):
        current_num += get(DOWN_LEFT)
    return current_num


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

for _ in range(maxNumber + 1):
    check()
    if get_around() > maxNumber:
        print("end = {0}".format(get_around()))
        # print_array()
        exit(1)