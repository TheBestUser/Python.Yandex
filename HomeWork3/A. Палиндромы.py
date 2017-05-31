import re

for i in range(int(input())):
    string = re.sub(r'[^a-zA-Zа-яА-Я]', '', str(input()).replace('ё', 'е').lower())
    res = True
    for a, b in zip(string, reversed(string)):
        res = res and a == b
    if res and string.isalpha():
        print('yes')
    else:
        print('no')
