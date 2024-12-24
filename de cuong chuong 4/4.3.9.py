
m, n = map(int, input().split())
m1 = []
for _ in range(m):
    m1.append(list(map(int, input().split())))
mm = []
for i in range(m):
    if sum(m1[i]) % 7 == 0:
        mm.append(i+1)
if mm:
    for i in mm:
        print(i+1)
else:
    print("NO")
