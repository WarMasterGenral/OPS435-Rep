stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
	print('Inventory:')
	total_item = 0
	for key in inventory.keys():
		print(inventory[key],key)
		total_item += inventory[key]
	print('Totoal number of items:',total_item)



'''
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))

displayInventory(stuff)
'''


'''
def list_to_dict(added_items):
        new_dict = {}
        for i in set(added_items):
                new_dict[i] = added_items.count(i)
        return new_dict
'''
def add_to_inventory(inventory,loot_list):
        for i in range(len(loot_list)):
                if loot_list[i] in inventory:
                        inventory[loot_list[i]] += 1
                else:
                        inventory.setdefault(loot_list[i],1)
        return inventory

inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
