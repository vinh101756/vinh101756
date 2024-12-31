
n= int(input())
c=0
tong =0
if(n>=0):
    while n!=0:
        tong +=n%10
        n=int(n/10)
        c+=1
    print("{} {}".format(c,tong))
else:
    print("Du lieu sai")
