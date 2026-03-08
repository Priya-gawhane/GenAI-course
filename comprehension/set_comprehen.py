favourate = [
    "masala chai", "lemon tea", "green tea",
    "green tea", "elaichi chai", "lemon tea"
]

unique = {chai for chai in favourate if "tea" in chai}
u = {chai for chai in favourate}
print(u)
print(unique)

RECIPES = {
    "masala chai": ["tea leaves", "milk", "sugar", "spices"],
    "lemon tea": ["tea leaves", "lemon", "sugar"],
    "green tea": ["green tea leaves", "water"],
    "elaichi chai": ["tea leaves", "milk", "sugar", "elaichi"]
}

unique_spices = {spice for ingredients in RECIPES.values() for spice in ingredients}
print(unique_spices)
#expression for item in iterable if condition