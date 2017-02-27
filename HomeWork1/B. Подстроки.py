# B. Подстроки
for _ in range(0, int(input())):
    string = input()
    for s in range(1, len(string) + 1):
        for i in range(0, len(string) - s + 1):
            print(string[i:i + s], end=' ')
    print()
