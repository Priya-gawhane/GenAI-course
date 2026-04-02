from functools import wraps

def require_auth(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied")
        else:
            return func(user_role)
    return wrapper

@require_auth
def access_tea_inventory(role):
    print("Accessing tea inventory...")

access_tea_inventory("user")
access_tea_inventory("admin") 