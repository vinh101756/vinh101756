import math
class dtron:
    def __init__(self,ma,tamx,tamy,bkinh):
        self.ma=ma
        self.tamx=tamx
        self.tamy=tamy
        self.bkinh=bkinh
    def kc(self):
        return math.sqrt((self.tamx ** 2) + (self.tamy ** 2))
    def nhap(self,data):
        parts=data.split()
        self.ma=int(parts[0])
        self.tamx=int(parts[1])
        self.tamy=int(parts[2])
        self.bkinh=float(parts[3])
    def xuat(self):
        print("{} {} {} {:.3f}".format(self.ma,self.tamx,self.tamy,self.bkinh))
n= int(input())
ds =[]
for _ in range(n):
    data=input()
    dtr=dtron(0,0,0,0)
    dtr.nhap(data)
    ds.append(dtr)
max=ds[0]
for i in ds:
    if i.kc()> max.kc():
        max=i
max.xuat()
