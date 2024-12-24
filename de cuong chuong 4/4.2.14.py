
import re
n = input()
so = re.findall(r"-?\d+",n)
chu = re.findall(r"[a-z]+",n)
x = list(map(int,so))
x.sort()
kq = []
i = 0
j = 0
while i < len(chu) or j < len(x):
    if i < len(chu):
        kq.append(chu[i])
        i = i + 1
    if j < len(x):
        kq.append(str(x[j]))
        j = j + 1
print(''.join(kq))
