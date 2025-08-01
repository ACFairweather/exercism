"""Functions to keep track and alter inventory."""


def create_inventory(items):
    inventory = {}
    for item in items:
        inventory[item] = inventory.setdefault(item, 0) + 1
    return inventory

def add_items(inventory, items):
    for item in items:
        inventory[item] = inventory.setdefault(item, 0) + 1
    return inventory


def decrement_items(inventory, items):
    for item in items:
        if item in inventory and inventory[item] > 0:
            inventory[item] = inventory[item] - 1
    return inventory


def remove_item(inventory, item):
    if item in inventory:
        inventory.pop(item)
    return inventory


def list_inventory(inventory):
    list = []
    for item in inventory.items():
        if item[1] > 0:
            list.append(item)
    return list

