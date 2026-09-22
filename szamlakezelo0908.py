# ==========================================
# SZÁMLAKEZELŐ PROGRAM
# ==========================================

import os  # Rendszerszintű műveletekhez (fájlútvonalak, képernyőtörlés) szükséges modul

# ------------------------------------------
# GLOBÁLIS VÁLTOZÓK ÉS BEÁLLÍTÁSOK
# ------------------------------------------
egyenleg = 0  # Kezdő egyenleg (a funkció neve is ez, érdemes figyelni az átfedésre)
pin = 1234  # Helyes PIN kód az azonosításhoz
hasznalatidij = 1000  # Fix alapérték a tranzakciós díj számításához
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # A futó Python fájl könyvtára
adatfajl = os.path.join(BASE_DIR, "szamla.txt")  # A tranzakciókat tároló fájl teljes útvonala
jogosult = False  # Jelzi, hogy a felhasználó sikeresen bejelentkezett-e
tranzakciok = []  # Ebben a listában tároljuk a tranzakciókat 


# ------------------------------------------
# SEGÉDFUNKCIÓK ÉS ADATKEZELÉS
# ------------------------------------------

def clear_screen():
    """Letisztítja a konzol képernyőjét az operációs rendszertől függően."""
    os.system("cls" if os.name == "nt" else "clear")


def adatbeolvasas(fajl):
    """Beolvassa a korábbi tranzakciókat a megadott szöveges fájlból."""
    global tranzakciok
    try:
        with open(fajl, encoding='utf-8') as f:
            print("Sikeres beolvasás")
            # Beolvassa a sorokat, és eltávolítja a felesleges szóközöket/soremeléseket
            tranzakciok = [s.strip() for s in f.readlines() if s.strip()]
    except FileNotFoundError:
        # Ha a fájl még nem létezik (első indítás)
        print("A fájl még nem létezik, üres tranzakciólista jött létre.")
        tranzakciok = []
    except IOError as e:
        # Egyéb fájlkezelési hibák elkapása
        print(f"Fájl művelet hiba {e}")
        tranzakciok = []


def adatmentes(fajl):
    """Elmenti az aktuális tranzakciókat a fájlba."""
    try:
        with open(fajl, 'w', encoding='utf-8') as f:
            for i in range(len(tranzakciok)):
                f.write(f"{tranzakciok[i].rstrip()}\n")
    except IOError as e:
        print(f"Fájl művelet hiba {e}")


def print_sikeres(text):
    """Kiírja a megadott üzenetet a konzolra."""
    print(text)


# ------------------------------------------
# BANKI TRANZAKCIÓS FUNKCIÓK
# ------------------------------------------

def egyenleg():
    """Kiszámolja és kiírja a tranzakciók alapján az aktuális egyenleget."""
    szamlaegyenleg = 0 
    for sz in tranzakciok:
        szamlaegyenleg += int(sz)  # Átalakítja a szöveges tranzakciót számmá és hozzáadja
    
    print(f"Egyenleg jelenleg: {szamlaegyenleg} ")
    return szamlaegyenleg


def utalas(osszeg):
    """Kivét/utaltatás: levonja az összeget és a tranzakciós díjat az egyenlegből."""
    print("Utalás: ")
    osszeg += round(hasznalatidij * 0.05)  # Kiegészíti az összeget a használati díj 5%-ával (50 Ft)
    
    if osszeg > egyenleg():
        print("Nincs elég pénzed!")
    else:    
        tranzakciok.append(f"-{osszeg}")  # Negatív előjellel rögzíti a kiadást
    
    egyenleg()


def penzbetet(osszeg):
    """Új összeget ad hozzá a számlához (befizetés)."""
    print("Betét: ")
    tranzakciok.append(f"+{osszeg}")  # Pozitív előjellel rögzíti a betétet
    egyenleg()


def tortenet(darab):
    """Megjeleníti az utolsó 'darab' tranzakciót (ha 0, akkor az összeset)."""
    print("Tranzakciók: ")
    
    if darab == 0:
        kezdet = 0
    else:
        kezdet = len(tranzakciok) - darab 

    # Végighalad a meghatározott kezdőindex-től a lista végéig
    for i in range(kezdet, len(tranzakciok)):
        print(f"\t{tranzakciok[i].rstrip()}")    


def koltes_osszeg():
    """Összegzi a negatív előjelű tranzakciókat (kiadásokat)."""
    osszeg = 0
    for sz in tranzakciok:
        if int(sz) < 0:
            osszeg += int(sz)
    return osszeg


def betet_osszeg():
    """Összegzi a pozitív előjelű tranzakciókat (befizetéseket)."""
    osszeg = 0
    for sz in tranzakciok:
        if int(sz) > 0:
            osszeg += int(sz)
    return osszeg


def legnagyobb_kiadas():
    """Megkeresi a legkisebb értéket (ami a legnagyobb összegű kiadás)."""
    min = 0 
    for sz in tranzakciok:
        if int(sz) < min:
            min = int(sz)
    return min


# ------------------------------------------
# PROGRAM INDÍTÁSA ÉS AZONOSÍTÁS
# ------------------------------------------

hibasbelepes = 3  # Három próbálkozási lehetőség
adatbeolvasas(adatfajl)  # Meglévő adatok betöltése

# Első PIN kód bekérés
pk = int(input("Kérem adja meg a PIN kódot: "))
if pk == pin:
    jogosult = True
    print_sikeres("Jogosultság ellenőrzése sikeres.")

# Ciklus a hibás próbálkozások kezelésére (max 3 lehetőség)
while not jogosult and hibasbelepes > 1:
    print_sikeres("Jogosultság ellenőrzése sikertelen.")
    pk = int(input("Kérem adja meg a PIN kódot: "))
    hibasbelepes -= 1
    
    if pk == pin:
        jogosult = True
        print_sikeres("Jogosultság ellenőrzése sikeres.")

# Ha 3 próbálkozásból sem sikerült a belépés
if not jogosult:
    print_sikeres("Próbálkozások vége!")

print(f"{tranzakciok}")


# ------------------------------------------
# FUNKCIÓVÁLASZTÓ MENÜ (FŐCIKLUS)
# ------------------------------------------

cim = "\nSZÁMLAKEZELŐ PROGRAM\n=====================\n"
menu = [
    "1. Egyenleg lekérdezés",
    "2. Pénz kivétel/utalás",
    "3. Pénz betét",
    "4. Tranzakciótörténet",
    "5. Költések összege",
    "6. Betétek összege",
    "7. Legnagyobb kiadás",
    "-------------------",
    "9. Kilépés"    
]

menupontok = [1, 2, 3, 4, 5, 6, 7, 9]

# A főmenü végtelen ciklusa, amíg a felhasználó a 9-es opcióval ki nem lép
while True:
    print(cim)
    for me in menu:
        print(f"{me}")

    valasztas = int(input("Válassz tevékenységet: "))

    # Bemenet ellenőrzése: újra kéri, ha érvénytelen opciót adott meg
    while valasztas not in menupontok:
        print("Nincs ilyen menüpont")
        print(cim)
        for me in menu:
            print(f"{me}\n")
        valasztas = int(input("Válassz tevékenységet: "))

    print()
    print("\n" * 20)  # Görgetés a jobb láthatóságért

    # --------------------------------------
    # MENÜPONTOK VÉGREHAJTÁSA
    # --------------------------------------
    if valasztas == 1:
        egyenleg()
        
    elif valasztas == 2:
        u = int(input("Utalás összege: "))
        utalas(u)
        
    elif valasztas == 3:
        b = int(input("Betét összege: "))
        penzbetet(b)

    elif valasztas == 4:
        m = int(input("Előzmények mérete(db): "))
        tortenet(m)
    
    elif valasztas == 5:
        print(f"\nÖsszes költés: {koltes_osszeg()}")
    
    elif valasztas == 6:
        print(f"\nÖsszes betét: {betet_osszeg()}")
    
    elif valasztas == 7:
        print(f"\nLegnagyobb kiadás: {legnagyobb_kiadas()} FT")
    
    elif valasztas == 9:
        # Adatok elmentése és a program leállítása
        adatmentes(adatfajl)
        exit()

    # Várakozás gombnyomásra a következő menüművelet előtt
    input("Üss egy billentyűt a folytatáshoz...")
    clear_screen()