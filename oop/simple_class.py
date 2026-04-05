class Chai:
    pass
class ChaiTime:
    pass

print(type(Chai))

ginger_tea = Chai()
print(type(ginger_tea))
print(type(ginger_tea is Chai))
print(type(ginger_tea is ChaiTime))

#Class is a blueprint for creating objects.
#It defines a set of attributes and methods that the created objects will have. 
#In this case, we have defined a class called "Chai" which currently does not have any attributes or methods. 
#We can create instances of this class to represent different types of chai.