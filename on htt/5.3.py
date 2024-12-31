n= int(input())
a=[]

for _ in range(n):
    row= list(map(int,input().split()))
    a.append(row)
max=a[0][0]
for i in range(n):
    if i+1<n:
        if a[i+1][i+1]>max:
            max= a[i+1][i+1]
print(max)
