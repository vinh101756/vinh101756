def DemKyTu(s):
    Luu={}
    for i in s:
        if i in Luu:
            Luu[i]+=1
        else:
            Luu[i]=1
    return Luu
n= int(input())
ds= []
for i in range(1,n+1):
    s= input()
    kq=DemKyTu(s)
    for KyTu, SL in kq.items():
        ds.append("{0}{1}".format(KyTu, SL))
    print(''.join(ds))
    ds.clear()
