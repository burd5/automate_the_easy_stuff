# Strong Password Detection
import re
"""
Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit. You may need to test the string against multiple regex patterns to validate its strength.

"""
password = input('Please enter a strong password: ')

length = re.compile(r'.{8,}')
upper = re.compile(r'[A-Z]+')
lower = re.compile(r'[a-z]+')
digit = re.compile(r'\d+')

regexes = [length, upper, lower, digit]

def strongPassword(password):
    count = 0
    for regex in regexes:
        if regex.search(password): count += 1

    if count == 4:
        return('Congrats. Your password is strong enough.')
    else:
        return('Password does not meet all requirements. Try again.')

print(strongPassword(password))


    

