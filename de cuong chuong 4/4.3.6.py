n= int(input())
mt =[]
c=0
for i in range (n):
    row = list(map(int,input().split()))
    mt.append(row)
for i in range (n):
    for j in range(n):
        if mt[i][j]== mt[j][i]:
           c+=1
if c<n:
    print("NO")
else:
    print("YES")



