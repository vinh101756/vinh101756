def fibonacci(n):
    if n <= 0:
        return False
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_s = [0, 1]
        for i in range(2, n):
            d =  fib_s[-1] + fib_s[-2]
            fib_s.append(d)
        return fib_s
n = int(input())
if isinstance(fibonacci(n), str):
    print(fibonacci(n))
else:
    print(' '.join(map(str, fibonacci(n))))
    print(sum(fibonacci(n)))