all_guests = {'Alice':{'apples':5,'pretzels':12},
              'Bob':{'ham sandwich':3,'apples':2},
              'Carol':{'cups':3,'apple pies':1}}


def total_brought(guests,item):
    num_brought = 0
    for key,value in guests.items():
        num_brought += value.get(item,0)
    return num_brought

print('Number of things being brought:')
print(' - Apples ' + str(total_brought(all_guests, 'apples')))
print(' - Cups ' + str(total_brought(all_guests, 'cups')))
print(' - Cakes ' + str(total_brought(all_guests, 'cakes')))
print(' - Ham Sandwiches ' + str(total_brought(all_guests, 'ham sandwich')))
print(' - Apple Pies ' + str(total_brought(all_guests, 'apple pies')))
