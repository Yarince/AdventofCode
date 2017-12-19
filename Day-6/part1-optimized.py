import time

with open("input.csv") as f:
    content = f.readlines()
bank = [int(item) for item in (content[0].split("\t"))]

total_iterations = 0


def divide_array(array):
    global total_iterations
    biggest_number = 0
    biggest_number_index = 0
    # Cannot sort the array or the pattern won't be visible
    for i in range(len(array)):
        if biggest_number < array[i]:
            biggest_number = array[i]
            biggest_number_index = i
        # Debug info
        total_iterations += 1

    to_be_distributed = biggest_number
    array[biggest_number_index] = 0
    i = biggest_number_index

    while to_be_distributed > 0:
        # Set I to next position in circular array like a loop
        i = i + 1 if i < len(array) - 1 else 0

        # Debug info
        total_iterations += 1

        array[i] += 1
        to_be_distributed -= 1

    return array


start_time = time.time()

checked_banks = []
checked_banks += [bank]

new_bank = bank
found = False
iterations = 0
while not found:
    new_bank = divide_array([i for i in new_bank])  # Divide ints over new bank

    found = checked_banks.__contains__(new_bank)

    checked_banks += [new_bank]
    # Debug info
    total_iterations += 1

    iterations += 1

print("Answer is %i iterations " % iterations)

print("And it took %f seconds to run" % (time.time() - start_time))
print("For %i iterations in total" % total_iterations)
