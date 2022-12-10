# this counts the number of uppercase letters and lowercase letters in a phrase, ignoring spaces

def up_low(s):
    a = []
    b = []
    for x in s:
        if x.isupper() == True:
            a.append(1)
        elif x.islower() == True:
            b.append(1)
        else:
            pass

    up = len(a)
    low = len(b)
    print(f'No. of Upper case characters : {up}')
    print(f'No. of Lower case characters : {low}')




s = 'aaaa'
up_low(s)

