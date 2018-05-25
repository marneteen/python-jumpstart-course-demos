import random

print('**********************************')
print('         Guess The Number')
print('**********************************')
print('')

number = random.randint(1,100)
guess = -1

name = input('Player, what is your name? ')

while guess != number:
    guess_text = input('Guess a number between 1 and 100. ')
    guess = int(guess_text)

    if guess > number:
        print('Sorry {}, the number {} is too high'.format(name,guess))
    elif guess < number:
        print('Woops! {}, the number {} is too low'.format(name, guess))
    else:
        print('Hurray! {}, you guessed it! The number is {}'.format(name, guess))

print('done')

