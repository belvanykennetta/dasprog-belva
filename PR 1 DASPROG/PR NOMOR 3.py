#how long of the power failure
duration = float(input('Enter duration: '))

#temperature
temperature = ((4*(duration)**2) / (duration + 2)) - 20

print(temperature)