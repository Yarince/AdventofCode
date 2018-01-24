import time
with open("input.csv") as f:
    content = f.readlines()
jumps = [int(row.strip()) for row in content]
# jumps = [0, 3, 0, 1, -3]

start_time = time.time()

steps = 0
i = 0
while i <= len(jumps):
    old_i = i

    if jumps[i] != 0:
        i += jumps[i]

    if jumps[old_i] >= 3:
        jumps[old_i] -= 1
    else:
        jumps[old_i] += 1

    steps += 1

    if i >= len(jumps):
        break

print("Amount of steps: ", steps)
print("Lol it took", time.time() - start_time, " seconds to run")
