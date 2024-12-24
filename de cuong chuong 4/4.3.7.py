n = int(input())
m = []
for _ in range(n):
    m.append(list(map(int, input().split())))
tcc = 0
tcp = 0
for i in range(n):
    tcc += m[i][i]
    tcp += m[i][n-i-1]
print(tcc, tcp)