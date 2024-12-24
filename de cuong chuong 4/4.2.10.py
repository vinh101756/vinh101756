
N, Q = map(int,input().split())
s = input()
for _ in range(Q):
    l, r, c = input().split()
    l = int(l) -1
    r = int(r)
    s1 = s[l:r]
    print(s1.count(c))
