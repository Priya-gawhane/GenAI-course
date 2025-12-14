# instead of writing formulas use function
def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup

my_bill = calculate_bill(3, 15)
print(my_bill)

print("Order for table to:", calculate_bill(2, 50))