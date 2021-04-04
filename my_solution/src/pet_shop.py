# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop_dictionary):
    return pet_shop_dictionary["name"]

def get_total_cash(pet_shop_dictionary):
    return pet_shop_dictionary["admin"]["total_cash"]

def add_or_remove_cash(pet_shop_dictionary, cash_difference):
    pet_shop_dictionary["admin"]["total_cash"] += cash_difference
    
def get_pets_sold(pet_shop_dictionary):
    return pet_shop_dictionary["admin"]["pets_sold"]

def increase_pets_sold(pet_shop_dictionary, pets_difference):
    pet_shop_dictionary["admin"]["pets_sold"] += pets_difference

def get_stock_count(pet_shop_dictionary):
    return len(pet_shop_dictionary["pets"])

def get_pets_by_breed(pet_shop_dictionary, breed):
    number_of_breed = []
    for pet in pet_shop_dictionary["pets"]:
        if breed == pet["breed"]:
            number_of_breed.append(pet)
    return number_of_breed

def find_pet_by_name (pet_shop_dictionary, name):
    for pet in pet_shop_dictionary["pets"]:
        if name == pet["name"]:
            return pet

def remove_pet_by_name(pet_shop_dictionary, name):
    for pet in pet_shop_dictionary["pets"]:
        if name == pet["name"]:
            pet_shop_dictionary["pets"].remove(pet)

def add_pet_to_stock (pet_shop_dictionary, pet_to_add):
    pet_shop_dictionary["pets"].append(pet_to_add)

def get_customer_cash (customer):
    return customer["cash"]

def remove_customer_cash (customer, cash_difference):
    customer["cash"] -= cash_difference

def get_customer_pet_count (customer):
    return len(customer["pets"])

def add_pet_to_customer (customer, pet_to_add):
    customer["pets"].append(pet_to_add)

def customer_can_afford_pet (customer, pet_to_add):
    if customer["cash"] >= pet_to_add["price"]:
        return True
    else:
        return False

def sell_pet_to_customer (pet_shop_dictionary, pet_to_sell, purchasing_customer):
    if pet_to_sell is None:
        return None
    elif purchasing_customer["cash"] < pet_to_sell["price"]:
        return None
    else:
        purchasing_customer["pets"].append(pet_to_sell)
        pet_shop_dictionary["admin"]["pets_sold"] += 1
        purchasing_customer["cash"] -= pet_to_sell["price"]
        pet_shop_dictionary["admin"]["total_cash"] += pet_to_sell["price"]
 
    
