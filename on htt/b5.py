def tim(arr):
    for i in range(len(arr)):
        if arr[i]>0:
            return i
    return -1
n = int(input())
x = list(map(float, input().split()))
m = int(input())
y = list(map(float, input().split()))
vtrix = tim(x)
if vtrix!=-1:
    print("{} {:.3f}".format(vtrix, x[vtrix]))
else :
    print("Khong co so duong trong mang.")
vtriy = tim(y)
if vtriy !=-1:
    print("{} {:.3f}".format(vtriy, x[vtriy]))
else :
    print("Khong co so duong trong mang.")