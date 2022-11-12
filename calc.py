while True:
    print("---------------------------------------")
    print()
    a=str(input("wprowadź typ działania, lub 'x' aby zakończyć: "))
    if a == 'x':
        break
    b = float(input("liczba nr jeden: "))
    c = float(input("liczba nr dwa: "))
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
