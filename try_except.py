my_dict = {"name": "Alice", "age": 30, "city": "New York"}

def get_value(dictionary, key):
    try:
        value = dictionary[key]
        print(f"The value for '{key}' is: {value}")
    except KeyError:
        print(f'The key {key} was not found in the dictionary')

# Example usage
get_value(my_dict, "name")
get_value(my_dict, "occupation")

shopping_cart_items = []

def average_price(cart_items):
    
    average = 0

    for item in cart_items:
        average += item.price

   
    try:
        average = average / len(cart_items)
        return average
    except ZeroDivisionError:
        average = 0
        return average
            
         

average_price_of_cart_items = average_price(shopping_cart_items)

print(f"Your average cart item price is {average_price_of_cart_items} dollars")