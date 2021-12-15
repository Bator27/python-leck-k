import random
"""
nev = input("Kérem adja meg a nevét")
szam1 = float(input("adjon meg egy számot"))
szam2 = random.randrange(10 , 50)
while szam2%2 == 1:
    szam2 = random.randrange(10 , 50)
SZAM3 = 5
#halmaz
szamok2 = {23}
szamok2.add(szam1)
szamok2.add(szam2)
szamok2.add(SZAM3)
print(szamok2)
#lista
szamok = []
szamok.append(szam1)
szamok.append(szam2)
szamok.append(SZAM3)
if szam1 % 2 == 0:
    print("páros")
else:
    print("Páratlan")
print(szam1, szam2)
szam4 = str(szam1)
wr = open("jozsi.txt","w")
wr.write(nev)
wr.write(szam4)
wr.close()
lista = [1,2,3,4,5,"abc","def"]
with open("jozsii.txt",'w') as file:
    for item in lista:
        file.write("%s\n" % item) 
gyomulcsok = ["eper","barack","ananász"] 
print(f'a gyomulcsok lista a következőket tartalmazza:{gyomulcsok}')
for (i,y) in enumerate (gyomulcsok):
    print(i,y)
print("".join(gyomulcsok))
"""

for téglalap in range (3):
    for sor in range (4):
        for oszlop in range(5):
            print('o', end ='')
        print('')
    print('')
