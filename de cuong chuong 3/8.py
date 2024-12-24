def convert(n):
    if n<0:
        return False
    np = ""
    while n > 0:
        r = n%2
        np = str(r) + np
        n = n // 2
    return np
n = int(input())
print(convert(n))