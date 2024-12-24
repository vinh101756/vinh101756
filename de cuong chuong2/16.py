import math
ep = float(input())
x = int(input())
if(0<ep<1):
    s = 0
    n = 0
    while math.fabs(x**n/math.factorial(n)) >= ep:
        n += 1
        s = s + (x**n)/(math.factorial(n))
    print(s)
else:
    print("Error")