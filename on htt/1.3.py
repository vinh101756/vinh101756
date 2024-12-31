a,b= map(int,input().split())
if(1<=a,b<=9):
    for i in range(a,b+1):
        for j in range(i,10):
            print("{}x{}={}".format(i,j,i*j))