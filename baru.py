#convertmoney
usd = float(input("Currency in US dollars : "))

#1 USD = 0.65 GDP
gbp = 0.65

#formula
convert = float(usd*gbp)
print(f"Currency in British pounds : {convert}")