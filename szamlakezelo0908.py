#SZÁMLAKEZELÉS

#GLOBAL VALTOZOK
egyenleg=0
pin=1234
hasznalatidij=1000
adatfajl="szamla.txt"
jogosult=False

#funkciók

def egyenleg():
    print("Egyenleg jelenleg: ")

def utalas(osszeg):
    print("Utalás ")

def penzbetet(osszeg):
    print("Betét: ")

#összes tranzakció mennyiseg = 0 --> összes tranzakció
#utolsó mennyiseg tranzakció !=0 --> utolsó db tranzk.

def tortenet(mennyiseg):
    print("Tranzakciók: ")

#MŰKÖDÉS
hibasbelepes = 3

pk = int(input(f"Kérem adja meg a PIN kódot: "))
if pk == pin:
        jogosult = True
        print(f"Jogosultság ellenőrzése sikeres.")

while(not jogosult and hibasbelepes>1):
    print(f"Jogosultság ellenőrzése sikertelen.")
    pk = int(input("Kérem adja meg a PIN kódot: "))
    hibasbelepes -= 1
    
    if pk == pin:
        jogosult=True
        print(f"Jogosultság ellenőrzése sikeres.")

if not jogosult:
    print(f"Próbálkozások vége!")


#FUNKCIÓVÁLASZTÓ MENÜ
cim = "\nSZÁMLAKEZELŐ PROGRAM\n=====================\n"
menu = [
    "1. Egyenleg lekérdezés",
    "2. Pénz kivétel/utalás",
    "3.Pénz betét",
    "-------------------",
    "4.Tranzakciótörténet",
    "9.Kilépés"    

]

menupontok = [1,2,3,4,9]
print(cim)
for me in menu:
    print(f"{me}")

valasztas = int(input("Válassz tevékenységet"))

while valasztas not in menupontok:
    print("Nincs ilyen menüpont")
    
    print(cim)
    for me in menu:
        print(f"{me}\n")
    
    valasztas = int(input("Válassz tevékenységet"))






if valasztas == 1:
    egyenleg()

elif valasztas == 2:
    utalas(123)

elif valasztas == 3:
    penzbetet(10000)

elif valasztas == 4:
    pass

elif valasztas == 9:
    exit()

#######################################

