import math

def ktra(x):
    if(x<2):
        return False
    for i in range(2,int(math.sqrt(x)+1)):
        if(x%i==0):
            return False
    return True
a,b= map(int,input().split())
c=0
if(a>b):
    for i in range(a-1, b ,-1):
        if ktra(i):
            print(i, end=' ')
            c += 1

else:
    for i in range(a, b + 1):
        if ktra(i):
            print(i, end=' ')
            c += 1
if (c == 0):
    print("Khong co")
