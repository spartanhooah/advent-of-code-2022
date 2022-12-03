elves = {}
current_calories = 0
current_elf = 0

with open("input/day-1.txt", "r") as file:
    for line in file:
        if len(line.strip()) == 0:
            elves[current_elf] = current_calories
            current_elf += 1
            current_calories = 0
        else:
            current_calories += int(line.strip())

    elves[current_elf] = current_calories

print(max(elves.values()))

sorted_elves = sorted(elves.values())

print(sum(sorted_elves[-3:]))
