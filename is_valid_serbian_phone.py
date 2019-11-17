import re

valid_phone = r'\d\d\d/\d+-\d+'

print('Unesite vasu broj telefona: ')
user_phone = input()

if re.match(valid_phone, user_phone):
    print('Uneli ste broj u ispravnom formatu.')
else:
    print('Broj koji ste uneli nije u ispravnom formatu!')
