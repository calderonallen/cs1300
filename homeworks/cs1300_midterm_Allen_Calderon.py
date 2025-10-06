problem 2: resturant bill calculator

food_total = 45.50
drinks_total = 18.75
dessert_total = 12.25

subtotal = food_total + drinks_total + dessert_total
tax = subtotal * 0.08 
total_with_tax = subtotal + tax 

if total_with_tax >= 50:
    tip = total_with_tax * 0.20
elif total_with_tax >= 30:
    tip = total_with_tax * 0.18
elif total_with_tax >= 15:
    tip = total_with_tax * 0.15
else: 
    tip = total_with_tax * 0.10
    
final_total = total_with_tax + tip

print("Subtotal: $", round(subtotal, 2))
print("tax amount: $", round(tax, 2))
print("Tip amount: $", round(tip, 2))
print("Final total: $", round(final_total, 2))