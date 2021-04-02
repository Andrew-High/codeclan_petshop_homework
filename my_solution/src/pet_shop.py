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
        if breed == "breed":
            number_of_breed.append(pet)
    return number_of_breed

# def find_pet_by_name (pet_shop_dictionary, name):
#     for pet in pet_shop_dictionary["pets"]:
#         if name == "name":
#             return pet

# def remove_pet_by_name(pet_shop_dictionary, name):
#     for pet in pet_shop_dictionary["pets"]:
#         if name == "name"
#         pet_shop_dictionary["pets"].pop(pet)