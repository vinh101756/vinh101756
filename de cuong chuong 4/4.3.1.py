m,n,k= map(int,input().split())
mt=[]
c=0
for i in range(m):
    row = list(map(int,input().split()))
    mt.append(row)
for i in range(m):
    for j in range(n):
        if mt[i][j]== k:
            c+=1
print(c)