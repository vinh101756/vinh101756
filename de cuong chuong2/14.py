def  tk():
    n = 1
    while (n * (n + 1)) // 2 <= 1000:
        n += 1
    return n
n = tk()
print(n)