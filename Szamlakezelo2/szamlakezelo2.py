import subprocess
from colorama import Fore, Back, Style



# GLOBÁLIS VÁLTOZÓK
pin_kod = 1234
egyenleg = 0
adatfajl = "szamla3.csv"
jogosult = False
tranzakciok = []


#######################################
# FUNKCIÓK
#######################################

def adatbeolvasas(fajl):
    try:
        with open(fajl, "r", encoding="UTF-8") as f:
            global tranzakciok
            sor =f.readline().strip().split(',')    #sor:lista
            tranzakciok.app(sor)            
            
            
            
    except IOError as e:
        print(f"Fájl művelet hiba: {e}")





# BEJELENTKEZÉS
hibas_belepesszam = 3

pk = int(input("Add meg a PIN kódodat!: "))

if pk == pin_kod:
        jogosult = True
        print(f"{Fore.GREEN} Sikeres belépés!")

while(not jogosult and hibas_belepesszam > 1):
    print(f"{Fore.RED} Hibás PIN kód!")
    pk = int(input("Add meg a PIN kódodat!: "))
    hibas_belepesszam -= 1
  
    if pk == pin_kod:
        jogosult = True
        print(f"{Fore.GREEN} Sikeres belépés!")

if not jogosult:
    print(f"{Fore.RED} Hibás PIN kód!")

print(f"{Fore.RESET}", end="")

# adatbeolvasas(adatfajl)

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
    "13. Kilépés"
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
    # print(f"{'\n' * 20}")q

    # if valasztas == 1:
    #     egyenleg()
    # elif valasztas == 2:
    #     u = int(input("Kivétel vagy utalás összege: "))
    #     utalas(u)
    # elif valasztas == 3:
    #     b = int(input("Betét összege: "))
    #     penzbetet(b)
    # elif valasztas == 4:
    #     m = int(input("Előzmény mérete (db) Minden: [0]: "))
    #     tortenet(m)
    # elif valasztas == 5:
    #     print(f"\nÖsszes költés: {koltes_osszeg()} Ft")
    # elif valasztas == 6:
    #     print(f"\nÖsszes pénzbetét: {betet_osszeg()} Ft")
    # elif valasztas == 7:
    #     print(f"Legnagyobb kiadás: {legnagyobb_kiadas()} Ft")
    # elif valasztas == 9:
    #     mentes(adatfajl)
    #     exit()

    input(f"Üss egy billentyűt a folytatáshoz...")
    subprocess.run(["cls"], shell=True)

