#VBTI and duration
VBTI = int(input('Enter volume to be infused : '))
duration = int(input('Enter duration: '))

#infusion rate calculation
infusion_rate = VBTI / (duration / 60)

print('The infusion rate is=', infusion_rate, "ml")

