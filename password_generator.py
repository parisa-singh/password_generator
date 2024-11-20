# Author: Parisa Singh
# Email: parisasingh@umass.edu
# Spire ID: 34751702

import random
from string import ascii_uppercase, ascii_lowercase, digits, punctuation
from math import floor

def password_generator(length):
    num_upper = floor(0.25 * length)
    num_lower = floor(0.25 * length)
    num_digits = floor(0.25 * length)
    num_special = length - (num_upper + num_lower + num_digits)
    
    upper_chars = random.choices(ascii_uppercase, k=num_upper)
    lower_chars = random.choices(ascii_lowercase, k=num_lower)
    digit_chars = random.choices(digits, k=num_digits)
    special_chars = random.choices(punctuation, k=num_special)
    
    password_list = upper_chars + lower_chars + digit_chars + special_chars
    random.shuffle(password_list)
    password = ''.join(password_list)
    return password

print(password_generator(10))  


