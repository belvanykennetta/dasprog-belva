#TAXI FARE CALCULATION

#distances
beginning_odometer= float(input('Enter beginning odometer: '))
ending_odometer= float(input('Enter ending odometer: '))

#total distance
Total_distance = ending_odometer - beginning_odometer

#total taxi fare
Taxi_fare_per_mile = 1.50
Total_taxi_fare = round(ending_odometer - beginning_odometer,1) * Taxi_fare_per_mile

print('You traveled a distance of', round(Total_distance), 'miles. At $1.50 per mile, your fare is $', round(Total_taxi_fare))

