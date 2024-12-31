import math
def ktra(x):
    if(x<2):
        return False
    for i in range(2,int(math.sqrt(x)+1)):
        if(x%i==0):
            return False
    return True
a= int(input())
c=0
for i in range (1,int(math.sqrt(a)+1)):
    if ktra(i):
        if(a%(i*i)==0):
            print("true")
            c+=1
            break
if (c==0):
    print("false")