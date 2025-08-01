"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    for item in items_to_add:
        current_cart[item] = current_cart.setdefault(item, 0) + 1
    return current_cart


def read_notes(notes):
    return dict.fromkeys(notes, 1)


def update_recipes(ideas, recipe_updates):
    for name, new_ingredients in recipe_updates:
        ideas[name] = new_ingredients
    return ideas


def sort_entries(cart):
    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    fulfillment_cart = {}
    for item, quantity in cart.items():
        aisle, refrigeration = aisle_mapping[item]
        fulfillment_cart[item] = [quantity, aisle, refrigeration]
    return dict(sorted(fulfillment_cart.items(), reverse=True))


def update_store_inventory(fulfillment_cart, store_inventory):
    for k, v in fulfillment_cart.items():
        store_inventory[k][0] -= v[0]
        if store_inventory[k][0] < 1:
            store_inventory[k][0] = 'Out of Stock'
    return store_inventory

