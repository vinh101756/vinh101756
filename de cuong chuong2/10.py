import math
n = int(input())
x = float(input())
s = 0
for _ in range(1, n+1):
    s = math.sqrt(x + s)
print(1 + s)

