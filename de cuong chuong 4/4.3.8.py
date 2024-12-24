n = int(input())
m = []
for _ in range(n):
    m.append(list(map(int, input().split())))
tgt = True
tgd = True
for i in range(n):
    for j in range(n):
        if m[i][j] !=0:
            tgt = False
    for j in range(i+1, n):
        if m[i][j] !=0:
            tgd = False
if tgt:
    print("UPPER TRIANGLE")
elif tgd:
    print("LOWER TRIANGLE")
else:
    print("NONE")