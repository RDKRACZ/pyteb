# while True:
#     a = int(input("liczba: "))
#     try:
#         print(float(a) / 2)
#     except ValueError as e:
#         print(e)


# from random import randint
# proba = 0
# y = 0
# a = randint(1, 10)
# while a != y:
#     y = int(input('zgadnij liczbe: '))
#     if type(y) is not int:
#         print('test') 
#     print('pudlo')
#     proba += 1
# print(f'zgadles za {proba} razem')


# from random import randint
# def wypiszLiczby(a):
#     print(a)
#     print(a+10)

# wypiszLiczby(2)


# from random import randint

# def czy_zgadles(a):
#     if a == randint(0,3):
#         return True
#     else:
#         return False

# x=False
# while x == False:
#     a=input()
#     x=czy_zgadles(a)


# lista = "zwykly,, tekst,   zwykly tekst"
# print(lista[0])
# print(lista.split(","))
# print(lista[:-1])
# print(lista.replace(',,',','))

# kolekcja = ['a','b','c']
# for i in range(len(kolekcja)):
#     if i == 2:
#         kolekcja[i] = 'tekst'

# print(kolekcja)


# zero =  ["  xx  ",
#          " x  x ",
#          "x    x",
#          "x    x",
#          "x    x",
#          " x  x ",
#          "  xx  "]
# for i in zero:
#     print(i)


# jeden = ["    xx ",
#          "   xxx ",
#          "  x xx ",
#          "    xx ",
#          "    xx ",
#          "    xx ",
#          "   xxxx"]


# a = input("podaj liczbe: ")
# for i in range(len(a)):
#     if a[i] == "1":
#         tekst += jeden[j]    


l0 = ["###",
      "# #",
      "# #",
      "# #",
      "###"]

l1 = [" # ",
      "## ",
      " # ",
      " # ",
      "###"]

l2 = ["###",
      "  #",
      "###",
      "#  ",
      "###"]

l3 = ["###",
      "  #",
      " ##",
      "  #",
      "###"]

l4 = ["# #",
      "# #",
      "###",
      "  #",
      "  #"]

l5 = ["###",
      "#  ",
      "###",
      "  #",
      "###"]

l6 = ["###",
      "#  ",
      "###",
      "# #",
      "###"]

l7 = ["###",
      "  #",
      "  #",
      "  #",
      "  #"]

l8 = ["###",
      "# #",
      "###",
      "# #",
      "###"]

l9 = ["###",
      "# #",
      "###",
      "  #",
      "###"]

liczba = input("podaj wartość: ")
for i in range(5):
    tekst = ''
    for j in range(len(liczba)):
        if liczba[j] == '0':
            tekst += str(l0)
print(tekst)
