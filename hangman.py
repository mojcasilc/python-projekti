import random
from collections import Counter

word_list = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon
cherry papaya berry peach lychee muskmelon'''

word_list = word_list.split(' ')
#choose a random word from list words_list
word = random.choice(word_list)

print('Guess the word!')

for i in word:
    #print the empty spaces for letters of the word
    print('_', end=' ')
print()

playing = True
#list for storing the letters guessed
letter_guessed = ''
chances = len(word) + 5
correct = 0
flag = 0 


while chances != 0 and flag == 0:
    #if the word is guessed with chances left, flag will break the loop
    print()
    chances -= 1

    try:
        guess = str(input('Enter a letter to guess: '))
    except:
        print('Enter only one letter!')
        continue

    #validating the guess
    if not  guess.isalpha():
        print('Enter only a LETTER.')
        continue
    elif len(guess) > 1:
        print('Enter only a SINGLE letter.')
        continue
    elif guess in letter_guessed:
        print('You have already guessed that letter.')
        continue

    #letter guessed
    if guess in word:
        #n - number of times the guessed letter occurs in the word
        n = word.count(guess)
        for _ in range(n):
            #the guessed letter is added as many times as it occurs
            letter_guessed += guess
    
    #print the word
    for char in word:
        if char in letter_guessed and (Counter(letter_guessed) != Counter(word)):
            print(char, end=' ')
            correct += 1
        #guessed all the letters
        elif Counter(letter_guessed) == Counter(word):
            #the game ends even if chances remain
            print(f'The word is: {word}.', end=' ')
            flag = 1
            print('Congratulations, you won!')
            break #break out of for loop 
        else:
            print('_', end=' ')

#used all chances
if chances <= 0 and Counter(letter_guessed) != Counter(word):
    print()
    print('Game over! Try again.')
    print(f'The word was {word}.')


            
