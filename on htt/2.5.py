import math
n= int(input())
s=0
if(n<0):
    print("Error.")
else :
    for i in range(n-1):
        s=math.sqrt(2+s)
    print("{:.2f}".format(s))