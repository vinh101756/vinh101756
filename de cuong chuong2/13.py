import math
n = int(input())
s = 0
for i in range(n+1):
    x = 2*i + 1
    s = s + 1/(math.factorial(x))
print(s)