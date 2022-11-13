# class Uczen:
#     ocenyMat = []
#     ocenyInf = []
#     ocenyHis = []
#     def __init__(self,imie,nazw):
#         self.imie=imie
#         self.nazw=nazw
        
#     def srednia(self):
#         suma = 0
#         for i in self.ocenyMat:
#             suma += i
#         return suma / len(self.ocenyMat)
    
#     def najwiekszaOcena(self):
#         return max(self.ocenyMat)
    
#     def ilePiatek(self):
#         ile5 = 0
#         for ocena in self.ocenyMat:
#             if ocena == 5:
#                 ile5 += 1
#         return ile5
    
#     def info(self):
#         print(self.imie + " " + self.nazw)
#         print("matematyka:", end = ' ')
#         for i in self.ocenyMat: # WERSJA 1
#             print(i, end= ", ")
#         print()
#         print("informatyka: " + str(self.ocenyInf)[1:-1]) # WERSJA 2
#         print("historia:", end = ' ')
#         for i in self.ocenyHis:
#             print(i, end= ", ")

# uczen1 = Uczen("Jan","Kowal")
# uczen2 = Uczen("Ryszard","Nowak")

# uczen1.ocenyMat=[1,2,3,4,5]
# uczen2.ocenyMat=[5,5,5,5,5]
# uczen1.ocenyHis=[2,2,4,4,5]
# uczen1.ocenyInf=[5,2,1,4,5]

# # print(uczen1.imie)
# # print(uczen2.srednia())
# # print(uczen2.najwiekszaOcena())
# # print(uczen1.ilePiatek())

# while True:
#     print("i - informacje")
#     print("x - wyjscie")
#     print("p - ilosc piatek")
#     print("n - najwyzsza ocena")
#     a = input("Twoje działanie: ")
#     if a == 'i':
#         uczen1.info()
#     if a == 'x':
#         break
#     if a == 'p':
#         print(uczen1.ilePiatek())
#     if a == 'n':
#         print(uczen1.najwiekszaOcena())
#     input()
	
# # uczen1.info()



# with open("dane.csv") as plik:
#     # print(plik.readline())
#     for linia in plik:
#         print(linia.split(','))

# zapis = open("index.html","w")
# zapis.write("zapisalismy string")
# zapis.close()


def table_start():
    return "<table>\n"
def table_end():
    return "</table>"

tekst = ''
with open("dane.csv") as plik:
    tekst += table_start()
    for linia in plik:
        for column in linia.split(','):
            
    tekst += table_end()
    
zapis = open("index.html","w")
zapis.write("zapisalismy string")
zapis.close()