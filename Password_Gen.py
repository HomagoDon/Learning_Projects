# this is my try at a password generator

import string
import secrets

upper = string.ascii_uppercase
lower = string.ascii_lowercase
punct = string.punctuation
letters = string.ascii_letters
digits = string.digits


def generate(length=25, upper = True,lower=True,punct=True,letters=True,digits=True):
    all = " "

    if upper:
        all += upper
    if lower:
        all += lower
    if punct:
        all += punct
    if letters:
        all += letters
    if digits:
        all += digits

    return''.join([secrets.choice(all)for i in range(length)])


print(generate)
