letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


# part 1
total = 0

with open("input/day-3.txt", "r") as file:
    for line in file:
        line = line.strip()
        length = len(line)
        left = line[:int(length / 2)]
        right = line[int(length / 2):]

        for letter in left:
            if letter in right:
                total += letters.index(letter) + 1
                break

print(total)

total = 0
elves = []
# part 2
with open("input/day-3.txt", "r") as file:
    for line in file:
        line = line.strip()

        elves.append(line)

        # group of 3 finished
        if len(elves) % 3 == 0:
            for letter in elves[0]:
                if letter in elves[1] and letter in elves[2]:
                    total += letters.index(letter) + 1
                    elves = []
                    break

print(total)
