#SZÁMLAKEZELÉS
import subprocess
from colorama import Fore,Back,Style
#GLOBAL VALTOZOK
egyenleg=0
pin=1234
hasznalatidij=1000
adatfajl="szamla.txt"
jogosult=False
tranzakciok=[]
#funkciók
def adatbeolvasas(fajl):
    try:
        with open(fajl, encoding='utf-8') as f:
            print("Sikeres beolvasás")
            global tranzakciok
            tranzakciok=f.readlines()
    except IOError as e:
        print(f"Fájl művelet hiba {e}")

def adatmentes(fajl):
    try:
        with open(fajl, 'w', encoding='utf-8') as f:
            global tranzakciok
            tranzakciok= f.writelines(tranzakciok)
    except IOError as e:
        print(f"Fájl művelet hiba {e}")
def egyenleg():
    szamlaegyenleg=0 
    for sz in tranzakciok:
        
        szamlaegyenleg += int(sz) 
    
    
    
    print(f"Egyenleg jelenleg: {szamlaegyenleg} ")
    return szamlaegyenleg
def utalas(osszeg):
    print("Utalás: ")
    osszeg+= round(hasznalatidij*0.05)
    if osszeg>egyenleg():
        print("Nincs elég pénzed!")
    else:    
        tranzakciok.append(f"-{osszeg}")
    
    egyenleg()
def penzbetet(osszeg):
    print("Betét: ")
    tranzakciok.append(f"+{osszeg}")
    egyenleg()

#összes tranzakció mennyiseg = 0 --> összes tranzakció
#utolsó mennyiseg tranzakció !=0 --> utolsó db tranzk.

def tortenet(darab):
    print("Tranzakciók: ")
    
    if darab == 0:
        kezdet = 0
    else:
        kezdet=len(tranzakciok)-darab 
    for i in range(kezdet, len(tranzakciok)):
        print(f"\t{tranzakciok[i].rstrip()}")    
    
def koltes_osszeg():
    osszeg=0
    
    for sz in tranzakciok:
        if int(sz)<0:
            osszeg+= int(sz)
    
    return osszeg

def betet_osszeg():
    osszeg=0
    for sz in tranzakciok:
        if int(sz)>0:
            osszeg+=int(sz)
    return osszeg

def legnagyobb_kiadas():
    min=0 
    for sz in tranzakciok:
        if int(sz)<min:
            min=int(sz)
            
    return min
    

#MŰKÖDÉS
hibasbelepes = 3
adatbeolvasas(adatfajl)
pk = int(input(f"Kérem adja meg a PIN kódot: "))
if pk == pin:
        jogosult = True
        print(f"{Fore.GREEN}Jogosultság ellenőrzése sikeres.{Style.RESET_ALL}")

while(not jogosult and hibasbelepes>1):
    print(f"{Fore.RED}Jogosultság ellenőrzése sikertelen.{Style.RESET_ALL}")
    pk = int(input("Kérem adja meg a PIN kódot: "))
    hibasbelepes -= 1
    
    if pk == pin:
        jogosult=True
        print(f"{Fore.GREEN}Jogosultság ellenőrzése sikeres.{Style.RESET_ALL}")

if not jogosult:
    print(f"{Fore.RED}Próbálkozások vége!{Style.RESET_ALL}")

print(f"{tranzakciok}")

#FUNKCIÓVÁLASZTÓ MENÜ
cim = "\nSZÁMLAKEZELŐ PROGRAM\n=====================\n"
menu = [
    "1. Egyenleg lekérdezés",
    "2. Pénz kivétel/utalás",
    "3.Pénz betét",
    "4.Tranzakciótörténet",
    "5.Költések összege",
    "6.Betétek összege",
    "7.Legnagyobb kiadás",
    "-------------------",
    "9.Kilépés"    

]

menupontok = [1,2,3,4,5,6,7,9]
while True:
    print(Fore.BLUE)
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

    print(Style.RESET_ALL)

    print(f"{'\n '* 20}")


    if valasztas == 1:
        egyenleg()
        
    elif valasztas == 2:
        u=int(input("Utalás összege: "))
        utalas(u)
        
    elif valasztas == 3:
        b=int(input("Betét összege: "))
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
        adatmentes(adatfajl)
        exit()
    input(f"Üss egy billentyűt a folytatáshoz...")
    subprocess.run(["cls"],shell=True)
#######################################

