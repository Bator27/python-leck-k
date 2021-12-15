#importálom a randomot ,hogy működjön a program
import random
#bekérem a számokat
szam1 = int(input("Kérlek adj meg egy számot:"))
szam2 = random.randrange(10,50)
szam3 = '3'
#ki íratom a szamokat
print(szam1)
print(szam2)
print(szam3)

#szam2 páratlan
"""
if szam2 %2:
    print("Páros a szám2")
else:
    szam2 = random.randrange(10,50)
"""
#páratlan-e a bekért szám
if szam1 %2 ==0:
    print("páros")
else:
    print("páratlan")
#lista készítés
szamok = [szam1, szam2, szam3]
#elvégzek 5 műveletet
print(szamok)
print(szam1 + szam2)
print(szam1 - szam2)
print(szam1 % szam2)
print(szam1 * szam2)
print(szam1 // szam2)
#halmaz készítés
halmaz = {}

szamok = set()

szamok = set([szam1, szam2, szam3])

#halmazhoz adás ami nem akar működni
"""
halmaz.add(szam1)
halmaz.add(szam2)
halmaz.add(szam3)

print(szam1 + szam3)
print(szam1 - szam3)
print(szam1 * szam3)
print(szam1 % szam3)
print(szam1 // szam3)
"""
#fájl írásos rész
wr = open('Dávid.txt' , 'w')
wr.write("szam1, szam2, szam3")
"""
print(wr.read())
wr.read()
"""
wr.close
#aláúhzás:
def repeat(string):
    if "fontos" in string:
        print('aláhúzás')
        return string*4
    else:
        return string*8
print(repeat("_"))
print("aláhúzás")
print(repeat("~"))