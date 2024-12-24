class Sach:
    def __init__(self, ten, so_trang, gia_tien):
        self.ten = ten
        self.so_trang = so_trang
        self.gia_tien = gia_tien

    def __str__(self):
        return f"{self.ten}, {self.so_trang}, {self.gia_tien}"
sach_list = []
with open('sach.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        ten, so_trang, gia_tien = line.strip().split(', ')
        sach = Sach(ten, int(so_trang), float(gia_tien))
        sach_list.append(sach)
filtered_sach = [sach for sach in sach_list if sach.gia_tien > 100000 and sach.so_trang < 200]
with open('ketqua.txt', 'w', encoding='utf-8') as file:
    for sach in filtered_sach:
        file.write(f"{sach}\n")