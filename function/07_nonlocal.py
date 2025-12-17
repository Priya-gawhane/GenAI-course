def update_order():
    chai_type = "elaichi"

    def kitchen():
        nonlocal chai_type #nonlocal means get authourity to change the outside func
        chai_type = "kesar"

    kitchen()
    print("after kitchen", chai_type)

update_order()