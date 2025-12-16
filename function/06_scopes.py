def serve_chai():
    chai_type = "masala" #local scope
    print(f"inside func {chai_type}")

chai_type = "badam chai"
serve_chai()
print(f"outside func{chai_type}")

def chai_counter():
    chai_order = 'lemon' #enclosing scope

    def print_order():    #nested function
        chai_order= 'ginger'
        print("inner", chai_order)
    print_order()
    print("outer", chai_order)

chai_order = 'tulsi' #global scope
chai_counter()
print("global", chai_order)