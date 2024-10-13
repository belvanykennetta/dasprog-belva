# CREATE STRING (MEMBUAT STRING)
string_0 = "Belvany Virginia Kenetta Setiawan"
string_1 = "5054241011"
string_2 = "Surabaya"


# PRINT STRING (MENCETAK STRING)
print("PRINT STRING : ")
print("Nama saya " + string_0)
print("NRP saya " + string_1)
print("Asal saya dari " + string_2)


# ACCESS CHARACTER IN STRING (MENGAKSES KARAKTER DALAM STRING)
print("\nACCESS CHARACTER IN STRING : ")
print ("Inisial saya ", string_0[0], string_0[8], string_0[17], string_0[25])


# SLICING (PENGIRISAN INDEX)
print("\nSLICING : ")
print ("Nama depan saya ", string_0[:16])
print ("Nama belakang saya ", string_0[16:33])
print ("Nama panggilan saya ", string_0[0:5])


# REVERSE STRING (DIBALIK URUTANNYA)
print("\nREVERSE : ")
print ("Reverse dari NRP saya, yaitu ", string_1[::-1])


# UPDATE STRING
print("\nUPDATE STRING : ")
string_3 = "Saya adalah mahasiswa RKA"
print(string_3)


# CHANGE STRING TO "SAYA BUKAN MAHASISWA RPL" (MENGUBAH STRING MENJADI "SAYA BUKAN MAHASISWA RPL")
print("\nCHANGE (MENGUBAH) STRING : ")
string_4 = string_3.replace("adalah mahasiswa RKA", "bukan mahasiswa RPL")
print(string_4)

# TUGAS IMPLEMETASI 
# DELETTING A CHARACTER (MENGHAPUS KARAKTER)
print("\nDELETING CHARACTER : ")
print("Kota asal saya tanpa huruf s menjadi ", string_2[1:8])


# ESCAPE SEQUENCING IN PYTHON (supaya penulisan lebih rapih, harus bisa pake enter, tab, dll)
# - baris baru (new line) -
print ("\nESCAPE SEQUENCING (BARIS BARU) : ")
print("Sura\nbaya")

# - tab -
print ("\nESCAPE SEQUENCING (TAB) : ")
print("Sura\tbaya")

# - backlash (slash yang terbalik) -
print ("\nESCAPE SEQUENCING (BACKLASH) : ")
print("Sura\\baya")

# - tanda kutip tunggal & ganda
print ("\nESCAPE SEQUENCING (TANDA KUTIP TUNGGAL DAN GANDA) : ")
print("Sura\'baya")
print("Sura\"baya")


# PYTHON STRING FORMATTING
print ("\nPYTHON STRING FORMATTING : ")
print (f"Nama Saya {string_0}, NRP Saya {string_1}, Asal saya dari {string_2}")