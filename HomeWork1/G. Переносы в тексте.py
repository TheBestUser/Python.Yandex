# G. Переносы в тексте
curr = 0
with open('input.txt') as f:
    all_str = f.read().split('\n')
    max_len = int(all_str[0])
    for l in all_str[1:]:
        if curr != 0:
            curr = 0
            print()
        if l == '':
            print()
            continue
        s = l.split(' ')
        for i in s:
            if (len(i) + curr <= max_len) or (curr == 0):
                if curr != 0:
                    print(end=' ')
                curr += (len(i) + 1)
            else:
                print('\n', end='')
                curr = len(i) + 1
            print(i, end='')
