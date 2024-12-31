def ktra_so_hhao(x):
    c=0
    if(x<1):
        return False
    for i in range (1,x):
        if(x%i==0):
            c+=i
    if(c==x):
        return True
    else:
        return False
a,b= map(int,input().split())
if(a>b):
    a,b=b,a
s=0
for i in range (a,b+1):
    if(ktra_so_hhao(i)):
        print(i,end=' ')
        s+=1
if(s==0):
    print("Khong co")

