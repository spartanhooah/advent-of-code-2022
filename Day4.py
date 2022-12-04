# part 1
overlaps = 0

with open("input/day-4.txt", "r") as file:
    for line in file:
        if len(line.strip()) == 0:
            continue

        (elf1, elf2) = line.strip().split(",")
        (elf1_low, elf1_high) = [int(val) for val in elf1.split("-")]
        (elf2_low, elf2_high) = [int(val) for val in elf2.split("-")]
        elf1_range = range(elf1_low, elf1_high + 1)
        elf2_range = range(elf2_low, elf2_high + 1)

        if (elf1_low in elf2_range and elf1_high in elf2_range) \
                or (elf2_low in elf1_range and elf2_high in elf1_range):
            overlaps += 1

print(overlaps)

# part 2
overlaps = 0

with open("input/day-4.txt", "r") as file:
    for line in file:
        if len(line.strip()) == 0:
            continue

        (elf1, elf2) = line.strip().split(",")
        (elf1_low, elf1_high) = [int(val) for val in elf1.split("-")]
        (elf2_low, elf2_high) = [int(val) for val in elf2.split("-")]
        elf1_range = range(elf1_low, elf1_high + 1)
        elf2_range = range(elf2_low, elf2_high + 1)

        if (elf1_low in elf2_range or elf1_high in elf2_range) \
                or (elf2_low in elf1_range or elf2_high in elf1_range):
            overlaps += 1

print(overlaps)
