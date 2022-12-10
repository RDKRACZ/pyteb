# list = [1, 2, 3, 4, 5]
# print(list)
# list.pop(2)
# print(list)
# list.pop(2)
# print(list)

# print()
# for i in range(len(list)):
#     print(list[i])

# print()
# for i in list:
#     print(i)

# print()
# for i in list:
#     if i % 2 == 0:
#         print(i)

# def sum_of_list(list):
#     suma = 0
#     for i in list:
#         suma += i
#     return suma

# list = [3, 3, 3, 3, 33]
# print("suma: ", sum_of_list(list))

# def mniejsze_niz_10(list):
#     for i in list:
#         if i < 10:
#             return i

# list = [3, 10, 20, 10, 33, 2, 7, 6]

# def najm(list):
#     lmin = list[0]
#     for i in list:
#         if lmin > i: lmin = i
#     return lmin

# def najw(list):
#     lmax = list[0]
#     for i in list:
#         if lmax < i: lmax = i
#     return lmax

# print(najm(list))
# print(najw(list))


# def najm_i_najw(list):
#     lmin2, lmax2 = list[0], list[0]
#     for i in list:
#         if lmin2 > i: lmin2 = i
#         if lmax2 < i: lmax2 = i
#     return lmin2, lmax2

# print("kolejno najmniejsza i najwieksza:", najm_i_najw(list))


# from random import randint

# lista = []


# def losowa_lista():
#     for i in range(300):
#         lista.append(randint(1, 100))


# def ile_razy():
#     wybor = input("podaj liczbe: ")
#     licznik = 0
#     for i in lista:
#         if i == int(wybor): licznik += 1
#     return licznik


# losowa_lista()

# print(ile_razy())


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def get_even_odd_lists(numbers):
#     print("pełna lista", numbers)

#     even_numbers = [x for x in numbers if x % 2 == 0]

#     odd_numbers = [x for x in numbers if x % 2 != 0]

#     print("tylko parzyste: ", even_numbers)
#     print("tylko nieparzyste:", odd_numbers)

# get_even_odd_lists(numbers)
# #######################################


# even= []
# odd = []

# def even_odd(numbers):
#     for i in numbers:
#         even.append(i) if i % 2 == 0 else odd.append(i)

# even_odd(numbers)
# print(even)
# print(odd)

# import random

# def add_digits(number_list):
#     # Initialize the sum of digits to 0
#     sum_of_digits = 0

#     # Iterate over the numbers in the list
#     for number in number_list:
#         # Convert the number to a string
#         number_str = str(number)

#         # Iterate over the digits in the number
#         for digit in number_str:
#             # Convert the digit to an integer and add it to the sum
#             sum_of_digits += int(digit)

#         # Print the number and the sum of its digits
#         print(f"{number}: {sum_of_digits}")

#         # Reset the sum of digits to 0
#         sum_of_digits = 0

#     # Return the sum of digits
#     return sum_of_digits

# # Generate a list of random numbers from 100 to 100000
# number_list = [random.randint(100, 100000) for _ in range(10)]

# # Test the function with the list of random numbers
# print(add_digits(number_list))


# from random import randint
# lista = []
# for _ in range(100):
#     lista.append(randint(100, 100000))

# def suma_cyfr(liczba):
#     suma = 0
#     while liczba > 0:
#         suma += liczba % 10
#         liczba = liczba // 10
#     return suma

# for _ in lista:
#     print(_, ' = ', suma_cyfr(_))


# from random import randint
# lista = []
# for _ in range(100):
#     lista.append(randint(100, 100000))

# def ile_cyfr(liczba,cyfra):
#     licznik = 0
#     while liczba > 0


# list = input("podaj 6 imion: ")
# licznik = 0
# lista = list.split()
# litera = input("podaj litere: ")
# for i in lista:
#     if i[-1] == litera:
#         licznik += 1
# print(licznik)

list = []
licznik = 0
for a in range(6):
    list.append(input("imie: "))
litera = input("podaj litere: ")
for i in list:
    for x in i:
        if x == litera:
            licznik += 1
print(licznik)


names = []
counter = 0

for i in range(6):
    name = input("Enter a name: ")
    names.append(name)

letter = input("Enter a letter: ")

for name in names:
    for c in name:
        if c == letter:
            counter += 1

print(counter)
