name = input('Masukkan nama pembeli : ')
n_toko = int(input('Masukkan barang dalam toko dan jumlahnya : '))

barang_di_toko = {}

for i in range(n_toko):
    item, amount = input().split()
    amount = int(amount)
    barang_di_toko[item] = amount

n_beli = int(input('Masukkan barang yang dibeli dan jumlahnya : '))
barang_yang_dibeli= []

for i in range(n_beli):
    charitem, charquantity = input().split()
    charquantity = int(charquantity)
    barang_yang_dibeli.append(charitem)
    
    barang_di_toko[charitem] -= charquantity

print(name)
print(' '.join(barang_yang_dibeli))
print("STORAGE")

for item, quantity in barang_di_toko.items():
    print(f"{item} {quantity}")