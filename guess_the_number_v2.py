import random

print("""Welcome! This is a number guessing game. \nYou will start by setting the desired range. \nThen you will have 7 chances to guess the random number.\nStart guessing!""")

#input desired range
lower = int(input('Please input the lower limit of the range (must be 0 or more): '))
upper = int(input('Please input the upper limit of the range (must me 1 or more): '))
#random number in the given range
number = random.randrange(lower, upper)
#number of chances and number of guesses
chances = 7
guess_count = 0

#while loop for guessing
while guess_count < chances:
    #input you guess, guess count +1
    guess_count += 1
    my_guess = int(input('Please enter your guess: '))
    #you guessed the number, exit out of loop
    if my_guess == number:
        print(f'you are correct, the number is {number}, and you guessed it in {guess_count} attempts')
        break
    #you did not guess correctly in 7 tries, game over
    elif guess_count >= chances and my_guess != number:
        print(f'Better luck next time. The number was {number}.')
    #you guessed too high
    elif my_guess > number:
        print('Try again! You guessed too high.')
    #you guessed too small
    elif my_guess < number:
        print('Try again! You guessed too small.')