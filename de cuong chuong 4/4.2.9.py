import re
s = input()
x = re.findall(r"\d+",s)
x = list(map(int, x))
luu = []
for i in x:
    if i % 2 != 0:
        luu.append(i)
print(" ".join(map(str, luu)))