import subprocess
from colorama import Fore, Back, Style

# GLOBÁLIS VÁLTOZÓK
pin_kod = 1234
egyenleg = 0
adatfajl = "Szamlakezelo2\\szamla3.csv"
jogosult = False
tranzakciok = []


#######################################
# FUNKCIÓK
#######################################
def adatbeolvasas(fajl):
    try:
        with open(fajl, "r", encoding="UTF-8") as f:
            global tranzakciok

            for s in f:
                sor = s.strip().split(",")  # sor: lista
                tranzakciok.append(sor)

    except IOError as e:
        print(f"Fájl művelet hiba: {e}")

def mentes(fajl):
    try:
        with open(fajl,"w",encoding="UTF-8") as f:
            for sor in tranzakciok:
                for i in range(len(sor)):
                    if i == 3:
                        f.write(f"{sor[i]}\n")
                    else:
                        f.write(f"{sor[i]},")
    
    except IOError as e:
        print("NEM JÓ VAÉA?o")

def egyenleg():
    szamla_egyenleg = 0

    for szl in tranzakciok:
        szamla_egyenleg += int(szl[2])
        # print(int(szl[2]))

    return szamla_egyenleg


def penz_kivetel():
    datum = input("\nDátum? (yyyy.mm.d): ")
    indok = input("Milyen kategóriába tartozik a költés?: ")
    kivetel = input("Mekkora összeget veszel ki?: ")
    megjegyzes = input("Megjegyzés: ")

    kivetellista = [datum, indok, "-" + kivetel, megjegyzes]
    tranzakciok.append(kivetellista)

    print(f"\nAz új egyenleged: {egyenleg()} Ft")


def penzbetet():
    datum = input("\nDátum? (yyyy.mm.d): ")
    indok = "-"
    betet = input("Mekkora összeget fizetsz be?: ")
    megjegyzes = "-"
    
    kivetellista = [datum, indok, "+" + betet, megjegyzes]
    tranzakciok.append(kivetellista)
    
    print(f"\nAz új egyenleged: {egyenleg()} Ft")


def atlagos_koltes():
    osszeg = 0
    db = 0
    
    for sor in tranzakciok:        
        akt_osszeg = int(sor[2])
        
        if akt_osszeg < 0:
            db += 1
            osszeg += akt_osszeg
    
    return (osszeg / db)


def legnagyobb_kiadas():
    min_ertek = 0    
    
    for sor in tranzakciok:
        akt_osszeg = int(sor[2])
        
        if akt_osszeg < min_ertek:
            min_ertek = akt_osszeg
            
    return min_ertek


# darab = 0 -> összes tranzakció
# darab !=0 -> utolsó darab tranzakcio
def tortenet(darab):
    print("Tranzakciók: ")
    
    if darab == 0:
        kezdet = 0
    else:
        kezdet = len(tranzakciok)-darab
    
    print(f"\n\t{'-'*83}")
    print(f"\t| {'Dátum':^12} | {'Kategória':^12} | {'Összeg':^16} | {'Megjegyzés':30} |")
    print(f"\t{'-'*83}")
    
    for i in range(kezdet, len(tranzakciok)):
        print(f"\t| {tranzakciok[i][0]:>12} | {tranzakciok[i][1]:<12} | {tranzakciok[i][2]:>13} Ft | {tranzakciok[i][3]:30} |")

    print(f"\t{'-'*83}\n")


def tranzakcio_szures(kategoria):
    szurt_lista = []
    
    for sor in tranzakciok:
        if sor[1] == kategoria:
            adatok = [sor[0], sor[2]]    
            szurt_lista.append(adatok)

    return szurt_lista


def tranzakcio_torles():
    #tranzakciok.pop()
    #tranzakciok.pop()
    
    global tranzakciok
    tranzakciok = tranzakciok[0:-2]

def havi_osszesito(honap):
    havi_egyenleg = 0
    
    for sor in tranzakciok:
        datum = sor[0].split(".")
        akt_ev=int(datum[0])
        akt_honap = int(datum[1])
        
        if akt_honap == honap:
            havi_egyenleg += int(sor[2])   
    return havi_egyenleg

def osszesito(kezdo, vege):
    idoszakos_egyenleg=0
    datum = sor[0].split(".")
    


#######################################
# A PROGRAM
#######################################

# BEJELENTKEZÉS
hibas_belepesszam = 3

pk = int(input("Add meg a PIN kódodat!: "))

if pk == pin_kod:
    jogosult = True
    print(f"{Fore.GREEN} Sikeres belépés!")

while not jogosult and hibas_belepesszam > 1:
    print(f"{Fore.RED} Hibás PIN kód!")
    pk = int(input("Add meg a PIN kódodat!: "))
    hibas_belepesszam -= 1

    if pk == pin_kod:
        jogosult = True
        print(f"{Fore.GREEN} Sikeres belépés!")

if not jogosult:
    print(f"{Fore.RED} Hibás PIN kód!")
    exit()

print(f"{Fore.RESET}", end="")

adatbeolvasas(adatfajl)

# Beolvasás teszt (kiírás)
# print(f"{tranzakciok}")


# FUNKCIÓVÁLASZTÓ MENÜ
cim = "\nSZÁMLAKEZELŐ PROGRAM\n====================\n"
menu = [
    "1. Egyenleg lekérdezés",
    "2. Pénz kivétel/átutalás",
    "3. Pénz betét",
    "--------------",
    "4. Átlagos kiadás",
    "5. Legnagyobb kiadás",
    "6. Tranzakció történet",
    "7. Szűrés kategória alapján",
    "8. Havi összesítő",
    "9. Időszakos összesítő",
    "10. Tranzakció törlése",
    "11. Tranzakció módosítása",
    "--------------",
    "13. Kilépés",
]

menupontok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13]

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
        print(f"\nAz egyenleged: {egyenleg()} Ft")
    elif valasztas == 2:
        penz_kivetel()
    elif valasztas == 3:
        penzbetet()
    elif valasztas == 4:
        print(f"Az átlagos költésed: {atlagos_koltes()} Ft")
    elif valasztas == 5:
        print(f"Legnagyobb kiadás: {legnagyobb_kiadas()} Ft")
    elif valasztas == 6:
        db = int(input("Mennyi tranzakciót szeretne látni? [0: összes]: "))
        tortenet(db)
        
    elif valasztas == 7:
        kategoriak = ["Fizetés", "Ajándék", "Utazás", "Vásárlás", "Szórakozás"]
        
        kategoria = input(f"Válassz kategóriát: {kategoriak}: ")
        lista = tranzakcio_szures(kategoria)

        print(f"{kategoria} tranzakciói:")
        for sor in lista:
            print(f"\t{sor}")

    elif valasztas ==8:
        honap_sorszam=int(input("Add meg egy hónap sorszámát: "))
        print(f"Az idei év {honap_sorszam} hónapjának egyenlege: {havi_osszesito(honap_sorszam)}")
    elif valasztas == 10:
        tranzakcio_torles()
        tortenet(2)

    elif valasztas == 13:
        mentes(adatfajl)
        exit()
        

    input(f"Üss egy billentyűt a folytatáshoz...")
    subprocess.run(["cls"], shell=True)