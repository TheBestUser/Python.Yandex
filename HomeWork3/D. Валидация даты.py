import re


def is_valid(data):
    parts = re.split('[-./ ]', data)
    if len(parts) > 1:
        if parts[1].isdigit():
            return 5 <= len(parts[0]) + len(parts[2]) < 7
    parts = re.split('[\w]', data)
    # if len(parts) > 1:

    print(parts)
    # if len(parts) > 1:
    #     if len(parts[1])+len(parts[5]) > 5:
    #         return True
    return False


with open("input.txt") as f:
    for line in f:
        print("YES" if is_valid(line) else "NO")

        # ([0-9]+)?([ /.-])(\d{2}|[а-я]+)([ /.-])?([0-9]+)
