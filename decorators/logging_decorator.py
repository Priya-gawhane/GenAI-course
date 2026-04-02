from functools import wraps
""" What is Wraps
    The functools.wraps decorator is used to preserve the metadata (such as __name__, __doc__, and __annotations__) 
    of a wrapped function when creating custom decorators in Python.  Without it, the wrapper function replaces
    the original function's identity, causing introspection tools like help() to display the wrapper's details 
    instead of the wrapped function's."""
def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"calling : {func.__name__}")
        result = func(*args, **kwargs)
        print(f"finished : {func.__name__}")
        return result
    return wrapper

@log_activity
def brew_coffee(coffee_type, milk= "no"):
    print(f"Brewing a cup of {coffee_type}... and milk status {milk}")

brew_coffee("Espresso", milk="yes")


