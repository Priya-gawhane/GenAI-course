# # (exp for ite in iterable if condition)
# [x for x in item] makes the entire list in the memory
# (x for x in item) It generates one item at a time and does not store the entire list in memory.
# It is more memory efficient than list comprehension, especially when working with large datasets.
# its like a stream

daily_sales = [100, 200, 300, 400, 500, 89, 1290, 212, 345]

total_cups = sum(sale for sale in daily_sales if sale > 200)

print(total_cups)