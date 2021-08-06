cat_names = []
while True:
    name = input('Enter the name of cat {} (Or enter nothing to stop.) '.format(len(cat_names)+1))
    if name == '':
        break
    cat_names.append(name)
print()
print('The cat names are: ')
for cat in cat_names:
    print(cat)
