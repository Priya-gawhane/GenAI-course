def serve_chai():
    chai_type = "masala" #local scope
    print(f"inside func {chai_type}")

chai_type = "badam chai"
serve_chai()
print(f"outside func{chai_type}")