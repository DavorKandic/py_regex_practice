import string

def is_pangram(s):
    if len(s) < 26:
        return False
    low_s = s.lower()
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
    'u','v','w','x','y','z']
    flag = True
    for letter in alphabet:
        if letter not in low_s:
            flag = False
    return flag


pangram = "The quick, brown fox jumps over the lazy dog!"
assert is_pangram(pangram) == True
