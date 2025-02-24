g = int(input('Ievadiet gadu --> '))

atl1 = g % 10
#print(atl)

match atl1:
    case 0:
        kr = 'Balts-metāls '
    case 1:
        kr = 'Balts-metāls '
    case 2:
        kr = 'Zils-ūdens '
    case 3:
        kr = 'Zils-ūdens '
    case 4:
        kr = 'Zaļš-koks '
    case 5:
        kr = 'Zaļš-koks '
    case 6:
        kr = 'Sarkans-uguns '
    case 7:
        kr = 'Sarkans-uguns '
    case 8:
        kr = 'Dzeltens-zeme '
    case 9:
        kr = 'Dzeltens-zeme '  
        
#print(kr)

atl2 = g % 12

match atl2:
    case 0:
        dz = 'pērtiķis '
    case 1:
        dz = 'gailis '
    case 2:
        dz = 'suns '
    case 3:
        dz = 'cūka '
    case 4:
        dz = 'žurka '
    case 5:
        dz = 'vērsis '
    case 6:
        dz = 'tiģeris '
    case 7:
        dz = 'trusis '
    case 8:
        dz = 'pūķis '
    case 9:
        dz = 'čūska '
    case 10:
        dz = 'zirgs '
    case 11:
        dz = 'kaza ' 
        
print(kr + dz + 'gads')
    