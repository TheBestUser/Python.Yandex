# F. Частоты букв
symbols = {}


def analysis(line):
    for j in line:
        if str.isalpha(j):
            j = str.lower(j)
            if j in symbols:
                symbols[j] += 1
            else:
                symbols[j] = 1


with open('input.txt') as f:
    for l in f.read():
        analysis(l)
for i in sorted(symbols.items(), key=lambda x: (int(-x[1]), x[0])):
    print(i[0] + ": " + str(i[1]))
