Number = list(map(int, input('Masukkan bilangan: '.split())))
Move = int(input('Masukkan jumlah angka belakang yang bergerak ke depan: '))
How_many_times = int(input('Masukkan berapa kali angka tersebut berpindah: '))

for i in range(0,How_many_times):
    cats_jump = Number[-move]
    cats_remaining = Number[:-Move]
    Number = cats_jump,cats_remaining
    
print(f"Urutan kucing menjadi = ", Number )
    
