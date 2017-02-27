# A Числа Фибоначчи
a = [0, 1]
n = int(input())
for i in range(0, n):
    a[i % 2] = a[0] + a[1]
print(a[n % 2])
