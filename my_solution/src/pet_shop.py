# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop_dictionary):
    return pet_shop_dictionary["name"]

def get_total_cash(pet_shop_dictionary):
    return pet_shop_dictionary["admin"]["total_cash"]

def add_or_remove_cash(pet_shop_dictionary, cash_difference):
    pet_shop_dictionary["admin"]["total_cash"] = pet_shop_dictionary["admin"]["total_cash"] + cash_difference
    