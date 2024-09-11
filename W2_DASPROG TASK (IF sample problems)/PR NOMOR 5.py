# PERHITUNGAN PENGGUNAAN DATA DAN BIAYA YANG DITANGGUNG

#Masukkan data yang digunakan
data = float(input("Enter the amount of data used: "))
 
#Menentukan kategori data dan biaya yang ditanggung
if 0.0 <= data < 1.0:
    charges = 250
elif 1.0 <= data < 2.0:
    charges = 500
elif 2.0 <= data < 5.0:
    charges = 1000
elif 5.0 <= data < 10.0:
    charges = 1500
elif data >= 10.0:
    charges = 2000
    
else:
    charges = "bad data"

if charges == "bad data":
    print("Bad data entered.")
else:
    print(f"The charges for {data} Gbs of data usage is: ${charges}")
