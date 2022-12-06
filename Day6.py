def find_marker(marker_length):
    start = 0

    for end in range(marker_length, len(line.strip()) - 1):
        marker_set = set(line[start:end])
        if len(marker_set) == marker_length:
            print(end)
            break

        start += 1


with open("input/day-6.txt", "r") as file:
    for line in file:
        find_marker(4)
        find_marker(14)
