class Chaiorder:
    def __init__(self, name, tea, sugar):
        self.name = name
        self.tea = tea
        self.sugar = sugar

    @classmethod
    def from_string(cls, order_string):
        name, tea, sugar = order_string.split(',')
        return cls(name, tea, sugar)
    
order1 = Chaiorder.from_string("Alice,Green Tea,2")
order2 = Chaiorder.from_string("Bob,Black Tea,1")   
print(order1.name)  # Output: Alice
print(order1.tea)   # Output: Green Tea