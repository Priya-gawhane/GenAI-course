favourate = [
    "masala chai", "lemon tea", "green tea",
    "green tea", "elaichi chai", "lemon tea"
]

unique = {chai for chai in favourate if "tea" in chai}
u = {chai for chai in favourate}
print(u)
print(unique)

