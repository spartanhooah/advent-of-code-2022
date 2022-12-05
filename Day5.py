import collections

stacks = []

with open("input/day-5.txt", "r") as file:
    for line in file:
        if len(line.strip()) == 0:
            continue

        if "[" in line:
            crates = line[1::4]

            for index, crate in enumerate(crates):
                if len(stacks) < len(crates):
                    stacks.append(collections.deque())

                # append to "right"/"bottom" of deque
                if crate != " ":
                    stacks[index].append(crate)

        if "move" in line:
            instructions = line.split()
            count = int(instructions[1])
            source = int(instructions[3]) - 1
            target = int(instructions[5]) - 1

            # pop things from the "left"/"top" of the deque
            for i in range(count):
                crate = stacks[source].popleft()
                stacks[target].appendleft(crate)

answer = ""

for stack in stacks:
    answer += stack.popleft()

print(answer)
