#message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

while True:
    
    message = input('please enter a sentence: (Blank to exit)\n')
    if message == '':
        break
    else:
        count = {}
        for character in message:
            count.setdefault(character,0)
            count[character] += 1
        print(count)
    
