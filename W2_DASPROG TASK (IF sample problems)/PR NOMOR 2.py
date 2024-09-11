# PERHITUNGAN DAN PEMBAGIAN KATEGORI BODY MASS INDEX (BMI)

#Memasukkan weight in pounds (wt_lb) and height in inches (ht_in)
wt_lb = float(input('Enter weight in pounds: '))
ht_in = float(input('Enter height in inches: '))

#Perhitungan of Body Mass Index (BMI)
BMI = (703 * wt_lb) / ht_in**2

#Membagi dalam kategori
if BMI < 18.5:
    print('Weight status: Underweight')
elif 18.5 <= BMI <= 24.9:
    print('Weight status: Normal')
elif 25.0 <= BMI <= 29.9:
    print('Weight status: Overweight')
elif BMI >= 30.0:
    print('Weight status: Obese')