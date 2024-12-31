import re
def ktra(xau):
    kqua= re.sub(r'[^a-zA-Z0-9]', '',xau).lower()
    return kqua== kqua[::-1]
s1= input()
s2= input()
print("true"if ktra(s1) else"false")
print("true"if ktra(s2) else"false")