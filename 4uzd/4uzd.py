teik = 'Laimīgu   un panākumiem   bagātu       Jauno  2025. gadu!'
print(teik)

l = len(teik)
#print(l)
teikj = ''
v = ''
poz = l
for i in range(l-1, -1, -1):
    if teik[i] == ' ':
        p = i
        if teik[i] == teik[i+1]:
            poz = p
            continue
        else:
            for j in range(p+1, poz):
                v = v + teik[j]
            #print(v)
            teikj = teikj + v + ' '
            #print(teikj)
            v = ''
            poz = p
        
teikj = teikj + teik[0:poz]
print(teikj)