N, M = map(int, input('Masukkan nilai N dan M: ').split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))

total_harga = []
total_uang = []

for i in range (len(P)):
    if P[i] > 0:
        total_harga.append(P[i])
        
for i in range (M):
    if C[i] < 0:
        total_uang.append(C[i])

total_harga_final = sum(total_harga)
total_uang_final = sum(total_uang)

total_hutang = total_uang_final - total_harga_final

print(total_hutang) 