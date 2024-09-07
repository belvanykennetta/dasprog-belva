#length and width
Length1 = int(input('Enter length of rectangular 1 = '))
Width1 = int(input('Enter width of rectangular 1 = '))
Length2 = int(input('Enter length of rectangular 2 = '))
Width2 = int (input('Enter width of rectangular 2 = '))

#surface area
Surface_area1 = Length1 * Width1
Surface_area2 = Length2 * Width2

#total surface
Total_surface = Surface_area2 - Surface_area1

#time required to cut the grass
Duration = Total_surface / 2

print('The time required to cut the grass at the rate of two square feet a second is', Duration, 'seconds')