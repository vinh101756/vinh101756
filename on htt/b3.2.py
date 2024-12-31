a, b = map(int, input().split())
mt = []
for _ in range(a):
    row = list(map(float, input().split()))
    mt.append(row)
min = mt[0][0]
vth = 0
vtc = 0
for i in range(a):
    for j in range(b):
        if mt[i][j] < min:
            min= mt[i][j]
            vth = i
            vtc = j
print("{} {} {:.2f}".format(vth, vtc, min))
