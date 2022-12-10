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


from random import randint

lista = []


def losowa_lista():
    for i in range(300):
        lista.append(randint(1, 100))


def ile_razy():
    wybor = input("podaj liczbe: ")
    licznik = 0
    for i in lista:
        if i == int(wybor): licznik += 1
    return licznik


losowa_lista()

print(ile_razy())


