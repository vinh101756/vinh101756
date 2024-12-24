import re
s = input()
x = re.findall(r"\d+",s)
x = list(map(int,x))
print(sum(x))