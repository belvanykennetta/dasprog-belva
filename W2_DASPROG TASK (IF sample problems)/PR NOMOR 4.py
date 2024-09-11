# MENENTUKAN GAS / ZAT BERDASARKAN HURUF AWAL WARNA SILINDER

#Memasukkan huruf awal warna silinder
color = input("Enter the first letter of the cylinder's color: ").strip().upper()

#Menentukan gas berdasarkan huruf awal warna silinder
if color == 'O' :
    contents = "ammonia"
elif color == 'B':
    contents = "carbon monoxide"
elif color == 'Y':
    contents = "hydrogen"
elif color == 'G':
    contents = "oxygen"
else:
    contents = "unknown"

print(f"The contents of the cylinder is: {contents}")
