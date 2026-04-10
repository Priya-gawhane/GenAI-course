def serve_chai(flavor):
    try:
        print(f"Serving {flavor} chai for you!")
        if flavor == "unknown":
            raise ValueError ("Sorry, we don't have that flavor.")
    except ValueError as e:
        print("Error", e)
    else:
        print("Enjoy your chai!")
    finally:
        print("Thank you for visiting our chai shop!")
    
serve_chai("elaichi")