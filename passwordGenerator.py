#Generates a random password...

import random

lst_digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lst_symbols = ['@', '#', '$', '%', '&']

char_lst = []
digits_lst = []
digits_lst2 = []
symbols_lst = []

def get_input():
    '''Validates and returns the length of a password
      Between Min: 7 & Max: 16 chars...'''
    psw_length = 0
    while psw_length < 7 or psw_length > 16:
        try:
            psw_length = int(input('Enter a password length between 7 and 16  -->>    '))
        except ValueError:
            print('ERROR! Please enter a valid integer...')
    return psw_length

password_length = get_input()   # stores the password length(from the user)...


num_chars = random.randint(2, (password_length - 2))   # stores number of letters...
num_digits = random.randint(2, (password_length - 1 - num_chars))   # stores number of digits...
num_symbols = (password_length - num_chars - num_digits)   # stores number of symbols...

print()
print(f'Computer will generate a password of {num_chars} letters, {num_digits} digit(s), and {num_symbols} symbol(s)...')

def generate_letters(length):
    for _ in range(length):
        lst = random.choice(lst_letters)
        char_lst.append(lst)
    return char_lst

def generate_digits(length):
    for _ in range(num_digits):
        lst = random.choice(lst_digits)
        digits_lst.append(lst)
    return digits_lst

def generate_symbols(length):
    for _ in range(num_symbols):
        lst = random.choice(lst_symbols)
        symbols_lst.append(lst)
    return symbols_lst

print()
picked_letters = generate_letters(num_chars)
picked_digits = generate_digits(num_digits)

def int_to_str(digits):
    for _ in digits:
        digits_lst2.append(str(_))
    return digits_lst2

picked_digits2 = int_to_str(picked_digits)

picked_symbols = generate_symbols(num_symbols)
print('Letters Picked: ', picked_letters)
print('Digits Picked: ',  picked_digits2)
print('Symbols Picked: ', picked_symbols)

whole_list = char_lst + digits_lst2 + symbols_lst   # holds the list of joined all choices...
#print(whole_list)

# __________________________________
# Shuffles the list ...
shuffled_list= random.sample(whole_list, len(whole_list))
print()
print('Shuffled List: ', shuffled_list, '\n')


# Randomly converts letters to uppercase & converts list to a string...
final_psswrd = ''.join( random.choice([k.upper(), k ]) for k in shuffled_list )
print('Your new password: ', final_psswrd)


