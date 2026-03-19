def serve_chai():
    yield "Cup1 : Masala Chai"
    yield "Cup2 : ginger aaaaaaaa"
    yield "cup3 : lemon tea"

stall = serve_chai()
for chai in stall:
    print(chai)

def get_chai_fun():
    return ["Cup1", "Cup2", "Cup3"]

def get_chai_gen():
    yield "Cupa"
    yield "Cupb"
    yield "cupc"

function = get_chai_fun()
print(function)

generator = get_chai_gen()
print(generator) #IT WILL NOT PRINT THE VALUES IN GENERATOR, it will point to the object or reference address
print(next(generator)) #it will print the first value in generator
print(next(generator)) #it will print the second value in generator
print(next(generator)) #it will print the third value in generator