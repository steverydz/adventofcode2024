import re


def get_data():
    file = open("inputs.txt", "r")
    content = file.readlines()
    file.close()
    return content


def get_all_multipliers():
    data = get_data()
    multipliers_pattern = r"mul\(\d{1,3},\d{1,3}\)"
    multipliers = []

    for item in data:
        items = re.findall(multipliers_pattern, item)
        multipliers = multipliers + items

    return multipliers


def get_multiply_result(multiplier_function):
    arg_pattern = r"\d{1,3},\d{1,3}"
    args = re.findall(arg_pattern, multiplier_function)
    args_digits = args[0].split(",")

    return int(args_digits[0]) * int(args_digits[1])


def get_result():
    multipliers = get_all_multipliers()
    results = list(map(get_multiply_result, multipliers))

    return sum(results)


get_result()
