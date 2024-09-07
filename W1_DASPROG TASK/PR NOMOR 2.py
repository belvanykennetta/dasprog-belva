#Read the height of dam and speed of water
Height_of_dam = int(input('Enter the height of the dam: '))
Flow_rate = float(input('Enter the flow rate of the water: '))
Efficiency = float(input('Enter the efficiency: '))

#another constanta
Mass_of_one_cubic_meter_water = 1000 
Gravity = 9.8 

#First, we need to know the total mass of water
Total_water_mass = Flow_rate * 1000

#Second, we need to find work
Work = float(Total_water_mass * Gravity * Height_of_dam)

#Next, we're gonna find the watt power
Power_watt = Work * Efficiency

#The last is calculating the megawatt power
Power_megawatt = Power_watt / 10**6

print('The megawatts predicted are', Power_megawatt, 'MW')



