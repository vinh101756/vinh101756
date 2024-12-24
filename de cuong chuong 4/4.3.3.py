m, n = map(int,input().split())
mt1 = []
mt2 = []
for _ in range(m):
    row1 = list(map(int,input().split()))
    mt1.append(row1)

for _ in range(m):
    row2 = list(map(int,input().split()))
    mt2.append(row2)
mtTich = [[0] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        mtTich[i][j] = mt1[i][j] * mt2[i][j]
for i in mtTich:
    print(' '.join(map(str,i)))