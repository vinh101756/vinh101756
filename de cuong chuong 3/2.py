import math
def snt(n):
    if n<2:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n%i==0:
                return False
                break
        return True
n = int(input())
for i in range(1, n+1):
    if snt(i) == True:
        print(i, end=' ')