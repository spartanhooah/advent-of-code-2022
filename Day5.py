import collections


def build_stacks(stacks):
    crates = line[1::4]
    for index, crate in enumerate(crates):
        if len(stacks) < len(crates):
            stacks.append(collections.deque())

        # append to "right"/"bottom" of deque
        if crate != " ":
            stacks[index].append(crate)


def parse_instructions(line):
    instructions = line.split()
    count = int(instructions[1])
    source = int(instructions[3]) - 1
    target = int(instructions[5]) - 1

    return count, source, target


def show_answer(stacks):
    answer = ""
    for stack in stacks:
        answer += stack.popleft()
    print(answer)


# part 1
with open("input/day-5.txt", "r") as file:
    stacks = []

    for line in file:
        if len(line.strip()) == 0:
            continue

        if "[" in line:
            build_stacks(stacks)

        if "move" in line:
            (count, source, target) = parse_instructions(line)

            # pop things from the "left"/"top" of the deque
            for i in range(count):
                crate = stacks[source].popleft()
                stacks[target].appendleft(crate)

show_answer(stacks)

# part 2
with open("input/day-5.txt", "r") as file:
    stacks = []

    for line in file:
        if len(line.strip()) == 0:
            continue

        if "[" in line:
            build_stacks(stacks)

        if "move" in line:
            (count, source, target) = parse_instructions(line)

            moving = collections.deque()

            for i in range(count):
                moving.append(stacks[source].popleft())

            while len(moving) > 0:
                stacks[target].appendleft(moving.pop())


show_answer(stacks)
