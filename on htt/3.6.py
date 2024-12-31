def ktra_chu_so_le(x):
    c=0
    if(x<0) :
        print("Error")
        return
    digits = str(x)
    odd_digits = [d for d in digits if int(d) % 2 != 0]
    if odd_digits:
        print(' '.join(odd_digits))
    else:
        print("No")
a,b,c= map(int,input().split())
ktra_chu_so_le(a)
ktra_chu_so_le(b)
ktra_chu_so_le(c)

