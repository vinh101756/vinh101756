import math
def ptb2(a, b, c):
    delta = (b*b) - (4*a*c)
    if(delta < 0):
        return "VN"
    elif(delta == 0):
        x1 = -b/(2*a)
        return x1
    elif(delta > 0):
        x1 = (-b-math.sqrt(delta))/(2*a)
        x2 = (-b+math.sqrt(delta))/(2*a)
        if(x1 > x2):
            return x1, x2
        else:
            return x2, x1
a, b, c = map(int, input().split())
print(ptb2(a, b, c))