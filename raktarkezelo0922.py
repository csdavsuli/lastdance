#Raktárkészlet
import subprocess

from colorama import Fore,Back,Style

#GLOBAL VALTOZOK

raktarkeszlet=0

rjelszo="Labgyak2026"

adatfajl="raktar.txt"

belepes=False

valtozas=[]

#funkciók

def adatbeolvasas(fajl):

    try:

        with open(fajl, encoding='utf-8') as f:

            print("Sikeres beolvasás")

            global valtozas

            valtozas=f.readlines()

    except IOError as e:

        print(f"Fájl művelet hiba {e}")



def adatmentes(fajl):

    try:

        with open(fajl, 'w', encoding='utf-8') as f:

            for i in range(len(valtozas)):

                f.write(f"{valtozas[i].rstrip()}\n")

                print("Sikeres mentés!")

    except IOError as e:

        print(f"Fájl művelet hiba {e}")

def keszlet():

    raktarkeszlet=0

    for sz in valtozas:

        raktarkeszlet += int(sz)

   

   

   

    print(f"Készlet jelenleg: {raktarkeszlet} ")

    return raktarkeszlet

def kivetel(osszeg):

    print("Kivettél: ")

    if osszeg>keszlet():

        print("Nincs elég készleten!")

    else:    

        valtozas.append(f"-{osszeg}")

    keszlet()

def berakas(osszeg):

    print("Berakás a készletbe: ")

    valtozas.append(f"+{osszeg}")

    keszlet()



#összes tranzakció mennyiseg = 0 --> összes tranzakció

#utolsó mennyiseg tranzakció !=0 --> utolsó db tranzk.



def tortenet(darab):

    print("Tranzakciók: ")

   

    if darab == 0:

        kezdet = 0

    else:

        kezdet=len(valtozas)-darab

    for i in range(kezdet, len(valtozas)):

        print(f"\t{valtozas[i].rstrip()}")    

   

def kivetel_osszeg():

    osszeg=0

   

    for sz in valtozas:

        if int(sz)<0:

            osszeg+= int(sz)

   

    return osszeg



def berakas_osszeg():

    osszeg=0

    for sz in valtozas:

        if int(sz)>0:

            osszeg+=int(sz)

    return osszeg



def legnagyobb_kiadas():

    min=0

    for sz in valtozas:

        if int(sz)<min:

            min=int(sz)

           

    return min

   



#MŰKÖDÉS

hibasbelepes = 3

adatbeolvasas(adatfajl)

pk = input(f"Kérem adja meg a Rendszergazdai jelszót: ")

if pk == rjelszo:

        belepes = True

        print(f"{Fore.GREEN}belepesság ellenőrzése sikeres.{Style.RESET_ALL}")


while not belepes and hibasbelepes > 0:
    pk = input("Kérem adja meg a rendszergazdai jelszót: ")
    
    if pk == rjelszo:
        belepes = True
        print(f"{Fore.GREEN}Belépés ellenőrzése sikeres.{Style.RESET_ALL}")
    else:
        hibasbelepes -= 1
        print(f"{Fore.RED}Belépés ellenőrzése sikertelen.{Style.RESET_ALL}")

if not belepes:
    print(f"{Fore.RED}Próbálkozások vége!{Style.RESET_ALL}")







#FUNKCIÓVÁLASZTÓ MENÜ

cim = "\nRaktárkezelő PROGRAM\n=====================\n"

menu = [

    "1 Készlet lekérdezés",

    "2. Kivétel a készletből",

    "3.Berakás a készletbe",

    "4.Berakás története",

    "5.Készlet kivételek összege",

    "6.Készket berakások összege",

    "7.Legnagyobb készlet kivétel",

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

        keszlet()

       

    elif valasztas == 2:

        u=int(input("Kivétel mennyisége: "))

        kivetel(u)

       

    elif valasztas == 3:

        b=int(input("Berakás összege: "))

        berakas(b)



    elif valasztas == 4:

        m = int(input("Előzmények mérete(db): "))

        tortenet(m)

   

   

    elif valasztas == 5:

        print(f"\nÖsszes kivétel: {kivetel_osszeg()}")

   

    elif valasztas == 6:

        print(f"\nÖsszes betét: {berakas_osszeg()}")

   

    elif valasztas == 7:

        print(f"\nLegnagyobb készlet kivétel: {legnagyobb_kiadas()} DB")

   

    elif valasztas == 9:

        adatmentes(adatfajl)

        exit()

    input(f"Üss egy billentyűt a folytatáshoz...")

    subprocess.run(["cls"],shell=True)

#######################################

