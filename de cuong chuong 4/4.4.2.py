class Sach:
    def __init__(self, ten, st, gt):
        self.ten = ten
        self.st = st
        self.gt = gt
    def tbc(self):
        return self.gt/ self.st
    def nhap(self):
        self.ten = input("Nhap ten sach: ")
        self.st = int(input("Nhap so trang: "))
        self.gt = float(input("Nhap gia tien: "))
    def xuat(self):
        print(f"Ten sach: {self.ten}, So trang: {self.st}, Gia tien: {self.gt}")
n = int(input("Nhap so luong sach: "))
a = []
for _ in range(n):
    sach = Sach("", 0, 0.0)
    sach.nhap()
    a.append(sach)
a.sort(key = lambda  s: s.tbc())
for i in a:
    i.xuat()