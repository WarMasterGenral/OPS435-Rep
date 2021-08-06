import random,sys

secret_number = random.randint(1,20)

print('I am thinking of a number between 1 and 20.')

remaining_shots = 6

for guess in range(1,7):
    print('You have {} shots.'.format(remaining_shots))
    your_guess = int(input('Take a guess: '))
    if your_guess == secret_number:
        print('Great job! You guessed my number in {} guesses!'.format(remaining_shots))
        sys.exit()
    else:
        remaining_shots = remaining_shots - 1
        if your_guess > secret_number:
            print('Your guess is higher than my number.')
        else:
            print('Your guess is lower than my number.')
            
