
class NV:
    def __init__(self, id, ten, hsl, pc):
        self.id = id
        self.ten = ten
        self.hsl = hsl
        self.pc = pc
        self.luong_thang = self.luong()
    def luong(self):
        return self.hsl*2000000+self.pc
    def __str__(self):
        return f"{self.id} {self.ten} {self.hsl:.2f} {self.pc} {self.luong_thang:.2f}"
n = int(input())
nv_list = []
for _ in range(n):
    ten, id, hsl, pc = input().split()
    n_v = NV(int(id), ten, float(hsl), int(pc))
    nv_list.append(n_v)
nv_list.sort(key=lambda nv : nv.luong_thang, reverse=True)
print(f"Danh sach nhan vien da sap xep: {n}")
for nv in nv_list:
    print(nv)
