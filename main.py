from random import randint


def is_valid(num):
    if str(num).isdigit() is True and int(num) in range(1, limit + 1):
        return True
    else:
        return False


print('Welcome to "Guess the Number".')
response = input('Do you want to change the upper limit of the range? (100 by default) (y/n) ')

if response.lower() == 'y':
    entering = True
    while entering is True:
        limit = (input('Enter any number greater than 1: '))
        if limit.isdigit() and int(limit) > 1:
            entering = False
            limit = int(limit)
else:
    limit = 100

answer = randint(1, limit)
attempts = 1
playing = True
guess = input(f'Enter a number between 1 and {limit}: ')
while playing:
    while is_valid(guess) is False:
        guess = input(f'Enter a number between 1 and {limit}: ')
    guess = int(guess)
    if guess == answer:
        print('You won!')
        print(f'Number of attempts: {attempts}')
        response = input('Do you want to play again? (y/n) ')
        if response.lower() == 'y':
            answer = randint(1, limit)
            attempts = 1
            guess = None
            continue
        else:
            print('Thanks for playing!')
            break
    if guess < answer:
        guess = input('Try a higher number: ')
        if not is_valid(guess):
            continue
        attempts += 1
        guess = int(guess)
    if guess > answer:
        guess = input('Try a lower number: ')
        if not is_valid(guess):
            continue
        attempts += 1
        guess = int(guess)
