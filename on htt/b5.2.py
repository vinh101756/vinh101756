def tim_phan_tu_dac_biet(matrix, n, m):
    hang_chung = set(matrix[0])
    for i in range(1, n):
        hang_chung &= set(matrix[i])
    ket_qua = []
    for x in hang_chung:
        if all(x in [matrix[i][j] for i in range(n)] for j in range(m)):
            ket_qua.append(x)
    return ket_qua
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
phan_tu_dac_biet = tim_phan_tu_dac_biet(matrix, n, m)
if phan_tu_dac_biet:
    print(" ".join(map(str, phan_tu_dac_biet)))
else:
    print()
