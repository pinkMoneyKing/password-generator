#!/usr/bin/python3

"""
    Password Generator
    
    by Pink Money King
"""

import string
import random
import sys
import itertools

def get_password_length():
    """
    Get random length for password
    """
    if len(sys.argv) > 1:
        passwd_length = sys.argv[1]
        return passwd_length
    else:
        passwd_length = 19
        return int(passwd_length)

def pwd():
    length = get_password_length()
    chars = list(itertools.chain.from_iterable(
        [random.choices(string.ascii_uppercase, k=20),
             random.choices(string.ascii_lowercase, k=20),
             random.choices(string.digits, k=20),
             random.choices(string.punctuation, k=20)]))

    passwd = ''.join(random.sample(chars, k=length))

    print(f'\n\n\t    Password : {passwd}\n\n')
    return passwd

def main():
    print('\n\n\t    PINK MONEY PASSWORD GENERATOR\n')
    print('\t$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print('\t$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print('\t$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    pwd()
    print('\t$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print('\t$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print('\t$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n\n')


if __name__ == "__main__":
    main()
