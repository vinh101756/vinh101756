class KhachHang:
    def __init__(self, ten, ma, dau, cuoi):
        self.ten = ten
        self.ma = ma
        self.dau = dau
        self.cuoi = cuoi

    def luong_dien_tieu_thu(self):
        return self.cuoi - self.dau

    def don_gia(self):
        if self.ma[0] == 'D':
            return 1000 * 1.05  # Doanh nghiệp
        elif self.ma[0] == 'K':
            return 1000 * 1.07  # Hộ kinh doanh
        else:
            return 1000  # Khách hàng thông thường

    def tien_tra(self):
        return self.luong_dien_tieu_thu() * self.don_gia()

    def la_ho_kinh_doanh(self):
        return self.ma[0] == 'K'

    def xuat(self):
        print("{} {} {} {} {} {}".format(self.ten,self.ma,self.dau,self.cuoi,self.luong_dien_tieu_thu()))


# Đọc input
n = int(input())
ds = []

for _ in range(n):
    data = input().split()
    ten = data[0]
    ma = data[1]
    dau = int(data[2])
    cuoi = int(data[3])
    khach_hang = KhachHang(ten, ma, dau, cuoi)
    ds.append(khach_hang)

# Tìm khách hàng là hộ kinh doanh phải trả nhiều tiền nhất
ho_kinh_doanh_max = None

for kh in ds:
    if kh.la_ho_kinh_doanh():
        if ho_kinh_doanh_max is None or kh.tien_tra() > ho_kinh_doanh_max.tien_tra():
            ho_kinh_doanh_max = kh

# In kết quả
if ho_kinh_doanh_max:
    print(ho_kinh_doanh_max.xuat())
else:
    print("Khong co khach hang la ho kinh doanh.")
