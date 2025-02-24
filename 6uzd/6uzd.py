def vesneneg(a): # pārbaude vai vesels nenegativs
    try:
        a = int(a)
        if a >= 0:
            paz = 't'
        else:
            paz = 'f'
    except:
        paz = 'f'
    return paz


def parbaude(a):
    sk = 1
    while sk <= 5:
        p = vesneneg(a)
        if p == 't':
            return int(a)
        else:
            if sk == 5:
                return 'f'
            else:
                sk = sk + 1
                a = input('Mēģiniet vēlreiz --> ')
    else:
        return 'f'   
    
    
x = input('Ievadiet argumentu x --> ')
#print(parbaude(x))

y = input('Ievadiet argumentu y --> ')
#print(parbaude(y))

def ackermann(a, b):
    if a == 0:
        return b + 1
    elif b == 0:
        return ackermann(a-1, 1)
    else:
        return ackermann(a-1, ackermann(a, b-1))
    
print(ackermann(parbaude(x), parbaude(y)))