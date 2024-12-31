class tiendien:
    def __init__(self,ma,ten, dau, cuoi):
        self.ma= ma
        self.ten=ten
        self.daui=dau
        self.cuoi=cuoi
    def sodien(self):
        return self.cuoi-self.dau
    def tinhtien(self):
        tien=0
        if(self.sodien()>=100):
            tien+=100*1000
        if (self.sodien() >=200):
            tien += 100 * 1500
        tien+=(self.sodien()-200)*2000
        return tien
    def nhap(self,data):
        parts=data.split()
        self.ten=parts[0]
        self.ma=int(parts[1])
        self.dau = int(parts[2])
        self.cuoi = int(parts[3])
    def xuat(self):
        print("{} {} {} {} {} {}".format(self.ma,self.ten,self.dau,self.cuoi,self.sodien(),self.tinhtien()))
n= int(input())
a=[]
for _ in range(n):
    data=input()
    td=tiendien(0,"",0,0)
    td.nhap(data)
    a.append(td)
max=a[0]
vt=0
for i in range(0,n-1):
    if a[i].tinhtien()>max.tinhtien():
        max= a[i]
        vt=i
print("khach hang phai tra tien nhieu nhat: {}".format(i))
max.xuat()

