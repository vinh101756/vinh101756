def ss(n):
    s = 0
    while n!=0:
        d = n%10
        s = s + d
        n = n // 10
    return s
n = int(input())
print(ss(n))
