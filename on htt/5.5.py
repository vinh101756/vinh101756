class NV:
    def __init__(self, ma, ten, hsl, pc):
        self.ma = ma
        self.ten = ten
        self.hsl = hsl
        self.pc = pc
    def luong(self):
        return self.hsl * 2000000 + self.pc
    def nhap(self,data):
        parts = data.split()

        self.ten = parts[0]
        self.ma = int(parts[1])
        self.hsl = float(parts[2])
        self.pc = int(parts[3])
    def xuat(self):
        print("{} {} {:.2f} {} {:.2f}".format(self.ma, self.ten, self.hsl, self.pc, self.luong()))
n = int(input())
a = []

for _ in range(n):
    data = input()
    nv = NV(0, "", 0, 0)
    nv.nhap(data)
    a.append(nv)
luongmax = a[0]
for i in a:
    if i.luong() > luongmax.luong():
        luongmax = i
print("Nhan vien co luong lon nhat")
luongmax.xuat()
