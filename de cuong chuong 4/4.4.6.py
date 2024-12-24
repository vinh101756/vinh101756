class SV:
    def __init__(self, ten, id, dT, dTr, dLTC):
        self.ten = ten
        self.id = id
        self.dT = dT
        self.dTr = dTr
        self.dLTC = dLTC
        self.dtb = self.diem()
    def diem(self):
        return (self.dT+self.dTr+self.dLTC)/3
    def __str__(self):
        return f"{self.ten} {self.id} {self.dT:.2f} {self.dTr:.2f} {self.dLTC:.2f} {self.dtb:.2f}"
n = int(input())
sv_list = []
for _ in range(n):
    ten, id, dT, dTr, dLTC = input().split()
    s_v = SV(ten, int(id), float(dT), float(dTr), float(dLTC))
    sv_list.append(s_v)
sv_list.sort(key=lambda sv : sv.dtb, reverse=True)
print("Danh sach sinh vien hoc lai")
c = 0
for sv in sv_list:
    if sv.dtb < 4:
        print(sv)
        c+=1
print(f"Danh sach nay co {c} sinh vien phai hoc lai")