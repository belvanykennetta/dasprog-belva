#JARAK LOMPATAN B DI TIAP PILLAR

input_distance = int(input('Masukkan jarak lompatan tiap pillar: '))

#Mengubah inputan menjadi rapih
input_distance_str = str(input_distance)
distances_pillars = list(map(int,input_distance_str.split("-")))
print (distances_pillars)
    
B_max_jump = int(input_distance_str[0])
distances_pillars = input_distance_str[1:]

#Menentukan apakah B bisa melompati pillar atau tidak
if len(distances_pillars) > 0 and int (distances_pillars[0]) > B_max_jump:
    print("NO HE CAN'T")
elif len(distances_pillars) > 1 and int (distances_pillars[1]) > B_max_jump:
    print("NO HE CAN'T")
elif len(distances_pillars) > 2 and int(distances_pillars[2]) > B_max_jump:
    print("NO HE CAN'T")
elif len(distances_pillars) > 3 and int(distances_pillars[3]) > B_max_jump:
    print("NO HE CAN'T")

else:
    print("YES HE CAN")