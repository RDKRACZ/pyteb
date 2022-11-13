import random
class Czlowiek:
    zycie = 1000
    xp = 0
    walka = 0
    
    def lecz(self):
        Czlowiek.zycie += 50
    
    def walcz(self):
        Czlowiek.zycie -= random.randint(1,100)
        if Czlowiek.zycie > 0:
            Czlowiek.xp += 50
        if Czlowiek.zycie < 0 and Czlowiek.xp < 1000:
            print("umarles")
        if Czlowiek.zycie < 0 and Czlowiek.xp > 1000:
            print("wygrales")


gracz=Czlowiek()

while True:
    print()
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("s - statystyki")
    print("x - wyjscie")
    print("w - walka")
    print("l - leczenie")
    a = input("Twoje działanie: ")
    if a == 's':
        print("zycie:", gracz.zycie)
        print("xp:", gracz.xp)
    if a == 'x':
        break
    if a == 'w':
        gracz.walcz()
    if a == 'l':
        gracz.lecz()
        print("zycie:", gracz.zycie)
