for a in range(-99, 100):
    for b in range(-99, 100):
        for c in range(-99, 100):
            if a*a - b*b == c*c*c:
                print(f'({a},{b},{c})')