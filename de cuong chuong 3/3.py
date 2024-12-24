import math
def shh(n):
    if n <= 1:
        return False
    d = 1
    for i in range(2, int(math.sqrt(n)) + 1 ):
        if n%i==0:
            d += i
            if i != n // i:
                d += n // i
    return d == n
a, b = map(int, input().split())
for i in range(a, b+1):
    if shh(i) == True:
        print(i, end=' ')