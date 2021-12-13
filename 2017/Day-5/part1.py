import time
with open("input.csv") as f:
    content = f.readlines()
jumps = [int(row.strip()) for row in content]

start_time = time.time()

steps = 0
i = 0
while i <= len(jumps):
    old_i = i

    if jumps[i] != 0:
        i += jumps[i]

    jumps[old_i] += 1
    steps += 1
    if i >= len(jumps):
        break

print("Amount of steps: ", steps)
print("Lol it took", time.time() - start_time, " seconds to run")
