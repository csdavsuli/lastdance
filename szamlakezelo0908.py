#SZÁMLAKEZELÉS

#GLOBAL VALTOZOK
egyenleg=0
pin=1234
hasznalatidij=1000
adatfajl="szamla.txt"
jogosult=False


#MŰKÖDÉS
hibasbelepes=2

pk=int(input("Kérem adja meg a PIN kódot: "))
if pk==pin:
        jogosult=True
        print("Jogosultság ellenőrzése sikeres.")

while(jogosult==False and hibasbelepes>0):
    pk=int(input("Kérem adja meg a PIN kódot: "))
    print("Jogosultság ellenőrzése sikertelen.")

    hibasbelepes-=1
    if pk==pin:
        jogosult=True
        print("Jogosultság ellenőrzése sikeres.")