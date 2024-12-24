def DemKyTu(s):
    Luu={}
    for i in s:
        if i in Luu:
            Luu[i]+=1
        else:
            Luu[i]=1
    return Luu
s= input()
kq= DemKyTu(s)
ds= []
for KyTu,SL in kq.items():
    ds.append("{0}: {1}".format(KyTu,SL))
print(", ".join(ds))