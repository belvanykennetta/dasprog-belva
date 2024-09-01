#how many gallons
gallons_of_oil = int(input('Enter the number of gallons= '))
efficiency = float(input('Enter effeciency= '))

#btu calculation
BTU = round(gallons_of_oil / 42 * 5800000 * efficiency / 100, 3)

print('Result of BTU= ', BTU, "btu")