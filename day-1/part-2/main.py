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

    lists = [left, right]

    return lists


def find_number():
    lists = format_data()

    total = 0

    for item in lists[0]:
        count = lists[1].count(item)
        total += item * count

    return total


find_number()
