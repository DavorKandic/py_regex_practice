import re

valid_pin = r'\b\d{4}\b'
print('Enter your pin: ')
user_pin = input()
if re.match(valid_pin, user_pin):
    print('Valid PIN')
else:
    print('Invalid PIN')
