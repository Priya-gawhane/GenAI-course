from functools import wraps
def decorator(func):
    @wraps(func)
    def wrapper():
        print("Before the function call.")
        func()
        print("After the function call.")
    return wrapper

@decorator
def greet():
    print("Hello from the decorator class from outside")
greet()
print(greet.__name__)