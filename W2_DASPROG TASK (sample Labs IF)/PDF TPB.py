# MENGHITUNG BILANGAN PRIMA

bilangan_prima = int(input("Masukkan bilangan: "))

if bilangan_prima <= 1:
    print(f"{bilangan_prima} IT IS NOT A PRIME")
else:
    i = 2
    while i < bilangan_prima:
        if bilangan_prima % i == 0:
            print(f"{bilangan_prima} IT IS NOT A PRIME")
            i = bilangan_prima  
        elif bilangan_prima % i != 0:
            print(f"{bilangan_prima} IT IS A PRIME")
            i = bilangan_prima  
        else:
            i += 1
    
    # if i == bilangan_prima:
    #     print(f"{bilangan_prima} IT IS A PRIME")