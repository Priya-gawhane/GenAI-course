class Chai:
    origin = "India"

print(Chai.origin)

Chai.is_hot = True
print(Chai.is_hot)

#creating objects
masala = Chai()
print(masala.origin)
print(masala.is_hot)

masala.is_hot = False
print(Chai.is_hot)
print(masala.is_hot)

masala.flavor = "spicy"
print(masala.flavor)