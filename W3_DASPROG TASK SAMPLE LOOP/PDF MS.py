banyak = int(input("Masukkan jumlah sepatu : "))
sepatu = [] 

for _ in range(banyak):
    masuk = input('Masukkan id sepatu yang terkena virus: ') 
    temp = "" 
    
    for i in range(len(masuk)):
        if masuk[i].isdigit():
            temp += masuk[i]
        elif masuk[i]=="L" or masuk[i]=="R": 
            temp += masuk[i]
    sepatu.append(temp) 
    
sama = 0 
i = 0
while i<len(sepatu)-1:
    j = i+1
    while j<len(sepatu):
        if sepatu[i][:-1]==sepatu[j][:-1]:
            if sepatu[i][-1]=="L" and sepatu[j][-1]=="R":
                sama += 1
            elif sepatu[i][-1]=="R" and sepatu[j][-1]=="L":
                sama += 1
        j += 1
    i += 1

print(sama)