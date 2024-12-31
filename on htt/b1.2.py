def ThapPhanSangNhiPhan(n):
    if n == 0:
        return "0"
    NhiPhan = ""
    while n > 0:
        NhiPhan = str(n % 2) + NhiPhan
        n //= 2
    return (' '.join(NhiPhan))
a,b = map(int, input().split())
if a>b:
    a,b=b,a
for i in range(a,b+1):
    print("{}: {}".format(i,ThapPhanSangNhiPhan(i)))