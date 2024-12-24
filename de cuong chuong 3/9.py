def convert(n):
    if n == 0:
        return "0"
    hc = "0123456789ABCDEF"
    hn = ""
    while n>0:
        r = n%16
        hn = hc[r] + hn
        n = n // 16
    return hn
n = int(input())
print(convert(n))