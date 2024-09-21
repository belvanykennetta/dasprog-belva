n = int(input('Masukkan jumlah elemen dalam kedua array: '))

arrayA = list(map(int, input('Masukkan deret bilangan A: ').split()))
arrayB = list(map(int, input('Masukkan deret bilangan B: ').split()))

arrayA = arrayA[:n]
arrayB = arrayB[:n]

true_false = []

m = int(input('Masukkan jumlah query yang akan diproses:  '))

for i in range(m):
    a, b = map(int, input('Masukkan index awal dan akhir untuk menjumlahkan array: ').split())
    x = sum(arrayA[a:b+1])
    y = sum(arrayB[a:b+1])
    if x == y:
        true_false.append(1)
    else:
        true_false.append(0)

for i in range(len(true_false)):
    if true_false[i] == 1:
        print("YA")
    else:
        print("TIDAK")