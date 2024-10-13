r, c, N = map(int, input('Masukkan jumlah baris & kolom, serta jumlah pergerakan: ').split())
arah = []
posisi_awal = [0, 0]

for i in range (r):
    arah.append(list(map(int, input().split())))
    
if len(arah[i]) != c:
    print("Arahnya kepanjangan cuy.")
    
gerakan = input('Masukkan arah gerakan: ')
if len(gerakan) != r:
    print("Gerakanmu salah bung!")
    exit()
    
emas = arah[posisi_awal[0]][posisi_awal[1]]

for g in gerakan:
    if g == 'U':
        emas += 3
        posisi_awal[0] -= 1
    elif g == 'D':
        emas -= 2
        posisi_awal[0] += 1
    elif g == 'L':
        emas -= 2
        posisi_awal[1] -= 1
    elif g == 'R':
        emas += 3
        posisi_awal[1] += 1
    if posisi_awal[0] < 0 or posisi_awal[0] >= r or posisi_awal[0] < 0 or posisi_awal[0] >= c:
        print("Gerakan keluar peta, tidak valid")
        exit()
    emas += arah[posisi_awal[0]][posisi_awal[1]]
print(f"total emas yang didapat adalah {emas}")
    