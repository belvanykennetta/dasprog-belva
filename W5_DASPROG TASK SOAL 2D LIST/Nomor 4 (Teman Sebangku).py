N, r, c = map(int, input("Masukkan jumlah murid dan urutan baris kolom kursi di kelas: ").split())
duduk_murid = {} 

for i in range (N):
    xi, a,  b = map(int, input('Masukkan nomor urut, duduk di kursi pada baris ke berapa, dan kolom ke berapa:  ').split())
    duduk_murid[a, b] = xi

for i in range (1, N + 1):
    ada = False
    for (a, b), murid in duduk_murid.items():
        if murid == i:
            if (a, b - 1) in duduk_murid:
                print(duduk_murid[(a, b - 1)])
                ada = True
            elif (a, b + 1) in duduk_murid:
                print(duduk_murid[(a, b + 1)]) 
                ada = True
            break
        
    if not ada:
        print (0)