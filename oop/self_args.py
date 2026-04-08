class Chaicup:
    size = 150 #ml

    def describe(self):
        return f"A{self.size} ml cup of chaicup"
    
cup = Chaicup()
print(cup.describe())
print(Chaicup.describe(cup))

cuptwo = Chaicup()
cuptwo.size = 200
#print(cuptwo.describe(cuptwo))