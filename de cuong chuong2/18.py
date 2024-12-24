import math
def ktra(x, x1, y, y1):
    return math.sqrt((math.pow(x-x1,2)) + (math.pow(y-y1,2)))
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
x3, y3 = map(float, input().split())
a = ktra(x1, x2, y1, y2)
b = ktra(x1, x3, y1, y3)
c = ktra(x2, x3, y2, y3)
if(a+b>c and a+c>b and b+c>a):
    d = a+b+c
    p = c/2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(d, s)
else:
    print("Error")