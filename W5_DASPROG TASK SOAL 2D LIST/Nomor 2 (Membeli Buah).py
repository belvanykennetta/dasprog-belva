N, K = (map(int, input('Masukkan jumlah buah dan uang yang anda miliki: ').split()))
Harga_buah = list(map(int, input().split()))
banyak_buah = []

for i in range(N):
    if Harga_buah[i] <= K:
        banyak_buah.append(i + 1)
        
bisa_beli_buah = len(banyak_buah)
if bisa_beli_buah > 0:
    banyak_jenis_buah = (f'jenis ke-{j}' for j in banyak_buah[:-1]) + f'dan jenis ke-{banyak_buah[-1]}'
    print (f"Dengan uang {K}, ia bisa membeli dengan kemungkinan {bisa_beli_buah} jenis buah, yaitu buah {banyak_jenis_buah}")
else:
    print ("Maaf uang tidak cukup!")