# #you want this to be consistent and traceable 
# #logic should not be scattered

# your shop adds a 10 % vat on every orderw
# write add_vat(price, vat_rate)
# use it on 3 orders 

def add_vat(price, vat_rate):
    return price * (100 + vat_rate)/100


orders = [100, 150, 200]

for price in orders:
    final_amount = add_vat(price, 10)
    print(f"original : {price}, final with vat {final_amount}")