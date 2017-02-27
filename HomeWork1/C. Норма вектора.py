# C. Норма вектора
power = float(input())
array = [float(x) for x in input().strip().split()]

x = 0
for a in array:
  x += abs(a**power)

print(float(x ** (1/power)))
