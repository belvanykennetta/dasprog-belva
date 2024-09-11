# PERHITUNGAN LAMPU MERAH

Mobil_di_depan = int(input('Ada berapa mobil di depan: '))
Mobil_di_belakang = int(input('Ada berapa mobil di belakang: '))
Detik = int(input('Apakah kita bisa melalui lampu merah setelah detik ke: ', ))

#Lama lampu menyala (5 detik di lampu hijau untuk 1 mobil)
Lampu_merah = 20
Lampu_kuning = 5
Lampu_hijau = 60
Lama_siklus = Lampu_merah + Lampu_kuning + Lampu_hijau

#Berapa kali siklus traffic berjalan dalam detik yang diinput tadi
Jumlah_siklus = Detik // Lama_siklus

#Sisa waktu setelah diketahui jumlah siklus yang bisa dilakukan
Sisa_waktu = Detik % Lama_siklus

#Berapa kali lampu hijau dan berapa mobil yang lewat
Total_lampu_hijau = Jumlah_siklus * Lampu_hijau
Mobil_lewat =  Total_lampu_hijau // 5

if Jumlah_siklus > Lampu_merah + Lampu_kuning:
    Total_lampu_hijau = Total_lampu_hijau + (Sisa_waktu - (Lampu_merah + Lampu_kuning))
else:
    waktu_hijau_tersisa = 0
    
#Perhitungan sisa mobil dan mengecek apakah kita sudah bisa melewati lampu merah
Sisa_mobil_depan = Mobil_di_depan - Mobil_lewat
Sisa_mobil_belakang = Mobil_di_belakang - Sisa_mobil_depan

if Sisa_mobil_depan < 0:
    Sisa_mobil_depan = 0
    
if Mobil_lewat > Mobil_di_depan:
    print('YES!', 0)
else:
    print('NO!', Sisa_mobil_belakang)