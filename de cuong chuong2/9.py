x = int(input())
n = int(input())
s = 0
for i in range(1, n+1):
    s = s + x**i
print(1 + s)