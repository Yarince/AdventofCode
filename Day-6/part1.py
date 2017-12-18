import time

with open("input.csv") as f:
    content = f.readlines()
bank = [int(item) for item in (content[0].split("\t"))]


def divide_array(array):
    biggest_number = 0
    biggest_number_index = 0
    # Cannot sort the array or the pattern won't be visible
    for i in range(len(array)):
        if biggest_number < array[i]:
            biggest_number = array[i]
            biggest_number_index = i

    to_be_distributed = biggest_number
    array[biggest_number_index] = 0
    i = biggest_number_index

    while to_be_distributed > 0:
        i = i + 1 if i < len(array) - 1 else 0

        array[i] += 1
        to_be_distributed -= 1

    return array


start_time = time.time()

checked_banks = []
checked_banks += [bank]
print("Start            ", bank, " - ", len(bank), " t: ", sum(bank))
print()

new_bank = bank
found = False
iterations = 0
while not found:
    print("checked_banks = ", checked_banks[::-1])
    new_bank = divide_array([i for i in new_bank])  # Divide ints over new bank

    found = checked_banks.__contains__(new_bank)

    checked_banks += [new_bank]
    print("new_bank      =  ", new_bank, " t: ", sum(new_bank))
    print()

    iterations += 1

print("iterations = ", iterations)
print("Lol it took", time.time() - start_time, " seconds to run")
