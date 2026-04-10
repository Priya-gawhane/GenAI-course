chai_menu = {'elaichi': 20, 'ginger': 70}

try:
    chai_menu['masala']
except KeyError:
    print("Masala chai is not available")
    