n = int(input())
for i in range(1, n + 1):
    s = input()
    KyTuTruoc = s[0]
    C = 1
    kq = ""
    for j in range(1,len(s)):
        if s[j] == KyTuTruoc:
            C = C + 1
        else:
            kq = kq + "{0}{1}".format(KyTuTruoc,C)
            KyTuTruoc = s[j]
            C = 1
    kq = kq + "{0}{1}".format(KyTuTruoc,C)
    print(kq)