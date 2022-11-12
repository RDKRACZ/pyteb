while True:
    print("---------------------------------------")
    print()
    a=str(input("wprowadź typ działania, lub 'x' aby zakończyć: "))
    if a == 'x':
        break
    # if not a == "-" or "+" or "/" or "*" or "**" or "%":
    #     print("Niepoprawny znak działania")
    #     continue
    try:
        b = float(input("liczba nr jeden: "))
    except ValueError as e:
        print("To nie liczba")
        continue
    try:
        c = float(input("liczba nr dwa: "))
    except ValueError as e:
        print("To nie liczba")
        continue

    if a == '-':
        print(b - c)
    if a == '+':
        print(b + c)
    if a == '/':
        print(b / c)    
    if a == '*':
        print(b * c)
    if a == '**':
        print(b ** c)
    if a == '%':
        print(b % c)