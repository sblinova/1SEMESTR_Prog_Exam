import math

x = float(input('Ievadiet x vērtību --> '))

if x <= -7:
    skait = 1 + math.cos(x)
    sauc = 1 + math.sin(x)*math.sin(x)
    res = skait / sauc
elif x > -2.5 and x < 2.5:
    res = x*x*x + x*x
elif x >= 9:
    k = 1/7
    res = k * (math.log2(5) / math.log2(x))
else:
    print('x nav definīcijas apgabalā!')
    res = '-'
    
print(f'F(x)={res}')