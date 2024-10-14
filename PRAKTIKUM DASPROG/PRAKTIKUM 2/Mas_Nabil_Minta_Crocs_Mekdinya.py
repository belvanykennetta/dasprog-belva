N = int(input())
angka_dipilih = list(map(int, input().split()))

flag = 0

for i in range(len(angka_dipilih)-1):
    if flag == 1:
        break
    
    for j in range(i + 1, len(angka_dipilih)):
        if angka_dipilih[i] ^ angka_dipilih[j] == 0:
            hasil_xor = 0
            flag = 1
            break
        
        if i == 0 and j == 1:
            hasil_xor = angka_dipilih[i] ^ angka_dipilih[j]
        else:
            hasil_xor *= angka_dipilih[i] ^ angka_dipilih[j]
            
        
print(hasil_xor)