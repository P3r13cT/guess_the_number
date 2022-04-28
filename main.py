import random

number = random.randint(1, 100)
print('Welcome to "Guess the Number".')


def is_valid(num):
    if num.isdigit() is True and int(num) in range(1, 101):
        return True
    else:
        return False


flag = True
guess = input('Enter a number between 1 and 100: ')
while flag:
    if is_valid(guess) == True:
        if int(guess) == number:
            print('You won!')
            flag = False
        else:
            if int(guess) < number:
                guess = input('Try a higher number: ')
            else:
                guess = input('Try a lower number: ')
    else:
        guess = input('Enter a number between 1 and 100: ')
