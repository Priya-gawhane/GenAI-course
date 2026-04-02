#sending data to yield exp
def chai_customer():
    print("Welcome to the chai stall!")
    order = yield

    while True:
        print(f"preparing {order}.....")
        order = yield

stall = chai_customer()
next(stall)  # Start the generator

stall.send("Lemon Tea") #sends the order to the generator and passes the value to the yield expression, which is then printed as part of the preparation message.
stall.send("Masala Chai")