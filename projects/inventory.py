stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for key, value in inventory.items():
        # FILL IN THE CODE HERE
        item_total += value
        print(f"{value} {key}")
    print("Total number of items: " + str(item_total))


displayInventory(stuff)

print()


def addToInventory(inventory, addedItems):
    # your code goes here
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return(inventory)


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)