def get_reports():
    file = open("inputs.txt", "r")
    content = file.readlines()
    file.close()

    reports = list(map(get_levels, content))

    return reports


def get_levels(item):
    record = item.rstrip("\n").split(" ")

    return list(map(int, record))


def is_increasing(report):
    levels = []

    for level in report:
        if levels and level <= levels[-1]:
            return False

        levels.append(level)

    return True


def is_safe_increasing(report):
    if not is_increasing(report):
        return False

    levels = []

    for level in report:
        if levels:
            prev = levels[-1]

            if level - prev < 1:
                return False

            if level - prev > 3:
                return False

        levels.append(level)

    return True


def is_decreasing(report):
    levels = []

    for level in report:
        if levels and level >= levels[-1]:
            return False

        levels.append(level)

    return True


def is_safe_decreasing(report):
    if not is_decreasing(report):
        return False

    levels = []

    for level in report:
        if levels:
            prev = levels[-1]

            if prev - level < 1:
                return False

            if prev - level > 3:
                return False

        levels.append(level)

    return True


def safe_increasing_dampened_reports(report):
    for i in range(len(report)):
        if is_safe_increasing(report[:i] + report[i + 1 :]):
            return True

    return False


def safe_decreasing_dampened_reports(report):
    for i in range(len(report)):
        if is_safe_decreasing(report[:i] + report[i + 1 :]):
            return True

    return False


def get_safe_reports(reports):
    safe_increasing_reports = []
    safe_decreasing_reports = []

    for report in reports:
        if is_safe_increasing(report):
            safe_increasing_reports.append(report)
        elif safe_increasing_dampened_reports(report):
            safe_increasing_reports.append(report)

        if is_safe_decreasing(report):
            safe_decreasing_reports.append(report)
        elif safe_decreasing_dampened_reports(report):
            safe_decreasing_reports.append(report)

    return safe_increasing_reports + safe_decreasing_reports


get_safe_reports(get_reports())
