import re

valid_email = r'[a-zA-Z]+@[a-zA-Z]+.com'

print('Unesite vasu mejl adresu: ')
email = input()

if re.match(valid_email, email):
    print('Uneli ste validnu mejl adresu.')
else:
    print('Mejl adresa nije validna!')
