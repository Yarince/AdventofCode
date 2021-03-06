import time

start_time = time.time()
with open("input.csv") as f:
    content = f.readlines()


def get_dict_by_key(search_key, search_dict):
    return next((dictvalue for key, dictvalue in enumerate(search_dict) if search_key in dictvalue), None)


puzzle_dict_array = []
instructions = []

for row in content:
    split = row.split()
    var_name = split[0]
    if not any(var_name in d for d in puzzle_dict_array):
        puzzle_dict = {var_name: 0}
        puzzle_dict_array.append(puzzle_dict)

    split.pop(3)  # remove 'if' from array.

    instructions.append(split)

for instruction in instructions:
    # instruction[0][0]
    check_var = instruction[3]
    dict_key = instruction[0]
    change_dict = get_dict_by_key(dict_key, puzzle_dict_array)
    change_value = int(instruction[2])
    check_dict = get_dict_by_key(check_var, puzzle_dict_array)
    if_operation = str(check_dict[check_var]) + ' ' + instruction[4] + ' ' + instruction[5]

    # Very wrong use of python :)
    if eval(if_operation):
        if instruction[1] == 'inc':
            change_dict[dict_key] += change_value
        elif instruction[1] == 'dec':
            change_dict[dict_key] -= change_value
        else:
            raise Exception('Not inc or dec, broken. Unexpected %s' % instruction[1][0])

max_var = 0
var_name = ''
for row in puzzle_dict_array:
    new_var = list(row.values())[0]
    if new_var > max_var:
        max_var = new_var
        var_name = list(row.keys())[0]

print(
    'Answer:\n'
    'Key: "%s"' % var_name, '- Max value: %s' % max_var
    + '\n\n' +
    'It took %s seconds to run' % str(time.time() - start_time)
)
