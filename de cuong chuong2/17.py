import math
a, b, c = map(int, input().split())
d = a + b + c
p = d/2
s = math.sqrt(p * (p-a) * (p-b) * (p-c))
if a+b>c and a+c>b and b+c>a:
    print(d, s)
else:
    print("Nhập bộ số khác")