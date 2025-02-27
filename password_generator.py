import random

#generate 2 random uppercase letters
uppercase1 = chr(random.randint(65,90))
uppercase2 = chr(random.randint(65,90))

#generate 2 random lowercase letters
lowercase1 = chr(random.randint(97, 122))
lowercase2 = chr(random.randint(97, 122))
lowercase3 = chr(random.randint(97, 122))

#generate 2 random digits between 0 and 9
digit1 = str(random.randint(0,9))
digit2 = str(random.randint(0,9))
digit3 = str(random.randint(0,9))

#generate 2 random punctation signs
punct = "! ? + * - _ . : , ; ' = # $ % & @"
punct = punct.split(' ')
punct1 = punct[random.randrange(17)]
punct2 = punct[random.randrange(17)]

def shuffle(string):
    '''shuffles the list of random characters in your password'''
    temp_list = list(string)
    random.shuffle(temp_list) 
    return ''.join(temp_list)

password = uppercase1 + uppercase2 + lowercase1 + lowercase2 + lowercase3 + digit1 + digit2 + digit3 + punct1 + punct2
password = shuffle(password)

print(password)