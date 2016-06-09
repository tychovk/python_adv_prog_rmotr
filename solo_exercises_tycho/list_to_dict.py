
def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory.update({item: 1})
    return inventory
    
def displayInventory(inventory):
    print ("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print ("{k}: {v}".format(k = k, v = v))
        item_total += v
    print ("Total number of items: {}".format(item_total))
    
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)



displayInventory(inv)