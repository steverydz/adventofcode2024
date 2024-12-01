def get_data():
    file = open("inputs.txt", "r")
    content = file.readlines()
    file.close()

    return content


def format_data():
    data = get_data()

    left = []
    right = []

    for item in data:
        items = item.split("   ")
        left.append(int(items[0]))
        right.append(int(items[1].rstrip("\n")))

    left.sort()
    right.sort()

    items = []

    for i in range(len(left)):
        items.append([left[i], right[i]])

    return items


def get_total_distance():
    data = format_data()

    total = 0

    for item in data:
        item.sort(reverse=True)

        distance = item[0] - item[1]

        if distance > 0:
            total += distance

    print(total)
    return total


get_total_distance()
