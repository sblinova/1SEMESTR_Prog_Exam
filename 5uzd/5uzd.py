def pirmskaitlis(b):
    if b > 1:
        for i in range(2, b//2+1):
            if b % i == 0:
                return 'f'
        else:
            return 't'
    else:
        return 'f'
    

def summa(a):
    s = 0
    for i in range(len(a)):
        s = s + int(a[i])   
    return s


def pirmreiz(a):
    pirm = ''
    for i in range(2, a//2+1):
        if pirmskaitlis(i) == 't':
            while a % i == 0:
                pirm = pirm + str(i)
                a = a / i 
    return pirm



for i in range(1, 1000000):
    if i == 1:
        print(1)
    else:
        s1 = summa(str(i))
        pirm = pirmreiz(i)
        #print(pirm)
        s2 = summa(str(pirm))
        if s1 == s2:
            print(i)
                