def tonguoc(x):
    c=0
    for i in range(1,x):
        if (x%i==0):
            c+=i
    return c
a,b= map(int,input().split())
if(tonguoc(a)==b and tonguoc(b)==a ):
    print("true")
else:
    print("false")