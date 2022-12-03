SCENARIOS = {
    ("A", "X"): 3,
    ("A", "Y"): 4,
    ("A", "Z"): 8,
    ("B", "X"): 1,
    ("B", "Y"): 5,
    ("B", "Z"): 9,
    ("C", "X"): 2,
    ("C", "Y"): 6,
    ("C", "Z"): 7
}

total_score = 0

with open("input/day-2.txt", "r") as file:
    for line in file:
        if len(line.strip()) == 0:
            continue

        scenario = tuple(line.split())

        total_score += SCENARIOS[scenario]

print(total_score)
