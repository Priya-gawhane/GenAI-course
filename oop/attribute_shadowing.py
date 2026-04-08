class Chai:
    temperature ="hot"
    strength = "strong"

cutting = Chai()
print(cutting.temperature)

cutting.temperature = "mild"
cutting.cup = "cup of tea"
print("After changing", cutting.temperature)
print("cup", cutting.cup)
print("direct look", Chai.temperature)

del cutting.temperature
del cutting.cup
print("After deleting", cutting.temperature)