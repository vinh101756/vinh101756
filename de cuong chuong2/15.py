import math
a = float(input())
if(0<a<0.1):
    n = 0
    s = 0
    while 1/(2*n + 1) >= a:
        n += 1
        s += 1/(math.factorial(2*n + 1))
    print(s)
else:
    print("Error")