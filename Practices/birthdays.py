birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    name = input('Enter a name: (blank to quit)\n')
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I don\'t have birthday information for ' + name)
        bday = input('What is their birthday?\n')
        birthdays[name] = bday
        print('Birthday database updated.')
