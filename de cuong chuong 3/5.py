import math
def bcnn(a, b):
    return math.lcm(a, b)
a, b = map(int, input().split())
print(bcnn(a, b))