menu = [
    "iced lemon tea",
    "masala chai",
    "iced Green tea",
    "sugary tea",
    "Salty tea"
]

iced_tea = [t for t in menu if "tea" in t]

print(iced_tea)

p = [a for a in  menu if len(a) > 10]

print(f"{p} is length tea")

#expression for item in iterable if condition