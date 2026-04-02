def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

def imported_chai():
    yield "Matcha"
    yield "Latte"

def full_menu():
    yield from local_chai()  # Delegates to local_chai generator
    yield from imported_chai()  # Delegates to imported_chai generator

def chai_stall():
    try:
        while True:
            order = yield "Welcome stall! What would you like to order?"
    except:
        print("Closing the stall for the day. See you tomorrow!")

stall = chai_stall()
print(next(stall))  # Start the generator and get the welcome message
stall.close() # close the generator, it ll clean the memory