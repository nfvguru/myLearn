#!/usr/bin/env python3

import random

def make_password_generator(s):
    def make_password(n):
        output = ''
        for i in range(n):
            output += random.choice(s)
        return output
    return make_password

make_alpha_password = make_password_generator('abcdefghij')
make_symbol_password = make_password_generator('abcde12345!@#$%')

new_alpha_password = make_alpha_password(5)  # new 5-character alphabetic pw
new_symbol_password = make_symbol_password(12)  # new 12-character symbolic pw


print(new_alpha_password)
print(new_symbol_password)
