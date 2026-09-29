import subprocess
from colorama import Fore, Back, Style



# GLOBÁLIS VÁLTOZÓK
tag_id = 1234
akt_egyenleg = 0
napi_dij = 500
adatfajl = "Edzoterem\\berlet.txt"
jogosult = False
egyenleg = []


#######################################
# FUNKCIÓK
#######################################
def adatbeolvasas(fajl):
    try:
        with open(fajl, "r", encoding="UTF-8") as f:
            global egyenleg
            egyenleg = f.readlines()
    except IOError as e:
        print(f"Fájl művelet hiba: {e}")


def mentes(fajl):
    try:
        with open(fajl, "w", encoding="UTF-8") as f:
            for i in range(len(egyenleg)):
                f.write(f"{egyenleg[i].rstrip()}\n")
            
    except IOError as e:
        print(f"Fájl művelet hiba: {e}")


def egyenleg_fv():
    szamla_egyenleg = 0
    
    for sz in egyenleg:
        szamla_egyenleg += int(sz)
    
    print(f"\nAz egyenleged: {szamla_egyenleg} Ft")
    
    return szamla_egyenleg


def edzesnap():    
    if napi_dij > egyenleg_fv():
        print("\nNem áll rendelkezésre a megfelelő összeg!")
    else:        
        egyenleg.append(f"-{napi_dij}")
    
    egyenleg_fv()


def berlet_vasarlas(osszeg):
    print("Bérlet/belépő vásárlás: ")
    egyenleg.append(f"+{osszeg}")
    
    egyenleg_fv()


# darab = 0 -> összes edzés
# darab !=0 -> utolsó darab edzés
def tortenet(darab):
    print("Edzésnapok: ")
    
    if darab == 0:
        kezdet = 0
    else:
        kezdet = len(egyenleg)-darab
    
    for i in range(kezdet, len(egyenleg)):
        if int(egyenleg[i]) < 0:
            print(f"\t{egyenleg[i].rstrip()}")


def edzes_napok_szama():
    darab = 0
    
    for sz in egyenleg:        
        if int(sz) < 0:
            darab += 1
    
    return darab


def vasarolt_edzesnapok_szama():
    darab = 0
    
    for sz in egyenleg:        
        if int(sz) > 0:
            darab += (int(sz) / napi_dij)
    
    return darab


def legnagyobb_vasarlas():
    max_ertek = 0
    
    for sz in egyenleg:
        if int(sz) > max_ertek:
            max_ertek = int(sz)
            
    return max_ertek



#######################################
# A PROGRAM
#######################################

# BEJELENTKEZÉS
hibas_belepesszam = 3

pk = int(input("Add meg a azonosítódat!: "))

if pk == tag_id:
        jogosult = True
        print(f"{Fore.GREEN} Sikeres belépés!")

while(not jogosult and hibas_belepesszam > 1):
    print(f"{Fore.RED} Hibás azonosító!")
    pk = int(input("Add meg a PIN kódodat!: "))
    hibas_belepesszam -= 1
  
    if pk == tag_id:
        jogosult = True
        print(f"{Fore.GREEN} Sikeres belépés!")

if not jogosult:
    print(f"{Fore.RED} Hibás azonosító!")
    exit()

print(f"{Fore.RESET}", end="")

adatbeolvasas(adatfajl)

# Beolvasás teszt (kiírás)
# print(f"{tranzakciok}")

# FUNKCIÓVÁLASZTÓ MENÜ
cim = "\nSZÁMLAKEZELŐ PROGRAM\n====================\n"
menu = [
    "1. Egyenleg lekérdezés",
    "2. Edzés/teremhasználat",
    "3. Bérlet/alkalom vásárlás",
    "--------------",
    "4. Előzmények",
    "5. Edzések száma",
    "6. Összes vásárolt alkalom",
    "7. Legnagyobb feltöltés",
    "--------------",
    "9. Kilépés"
]

menupontok = [1, 2, 3, 4, 5, 6, 7, 9]

while True:
    print(f"{Back.LIGHTCYAN_EX}{cim}")
    print(f"{Back.RESET}", end="")
    
    print(f"{Fore.LIGHTCYAN_EX}", end="")
    
    for me in menu:
        print(f"{me}")

    valasztas = int(input("Válassz tevékenységet: "))

    while valasztas not in menupontok:
        print("Nincs ilyen menüpont!\n")
        
        print(cim)    
        for me in menu:
            print(f"{me}")

        valasztas = int(input("Válassz tevékenységet: "))

    print(f"{Fore.RESET}", end="")

    # "Képernyő törlése"
    # print(f"{'\n' * 20}")

    if valasztas == 1:
        egyenleg_fv()
    elif valasztas == 2:
        edzesnap()
    elif valasztas == 3:
        b = int(input("Vásárlás összege: "))
        berlet_vasarlas(b)
    elif valasztas == 4:
        m = int(input("Előzmény mérete (db) Minden: [0]: "))
        tortenet(m)
    elif valasztas == 5:
        print(f"\nEdzés napok száma: {edzes_napok_szama()} nap")
    elif valasztas == 6:
        print(f"\nVásárolt napok száma: {vasarolt_edzesnapok_szama()} nap")
    elif valasztas == 7:
        print(f"Legnagyobb kiadás: {legnagyobb_vasarlas()} Ft")
    elif valasztas == 9:
        mentes(adatfajl)
        exit()

    input(f"Üss egy billentyűt a folytatáshoz...")
    subprocess.run(["cls"], shell=True)