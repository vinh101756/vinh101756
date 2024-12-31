n= int(input())
arr= list(map(int,input().split()))
c=0
min= None
vt=-1
for i in range (n):
    if(arr[i]%2!=0):
        c+=1
        if min is None or arr[i] <min:
            min = arr[i]
            vt = i
if(c==0):
    print("Khong co so le trong mang")
elif(c>0):
    print("So le nho nhat co vi tri {} gia tri {}".format(vt,min))

