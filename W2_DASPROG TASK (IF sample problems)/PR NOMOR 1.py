#Read total purchase
total_purchase = float(input("Enter the total purchase: $"))

#Read option whether student or not
student_options = input("Is the purchaser a student? (yes/no): ").strip().lower() == 'yes'

#Discount and tax rates
discount_rate = 0.20
tax_rate = 0.05

#Calculate the discount if the purchaser is a student or not
if student_options:
    discount = total_purchase * discount_rate
else:
    discount = 0

#Calculate the price after discounted
price = total_purchase - discount

#Calculate the sales tax
sales_tax = price * tax_rate

#Calculate the final total price
total = price + sales_tax

print(f"Total purchases: ${total_purchase:.2f}")
if student_options:
    print(f"Student's discount (20%%): ${discount:.2f}")
print(f"Discounted total: ${price:.2f}")
print(f"Sales tax (5%%): ${sales_tax:.2f}")
print(f"Total: ${total:.2f}")