import time
import sys
import random

a= int(1000)
random.seed(3)

print("Üdvözöllek a RandomPerLine programban. Ez a program másodpercenként beleír" 
" egy random számot egy általad elnevezett fájlba, annyi soron ahányon szeretnéd")

loopnumber= int(input("Kérlek írd be hányszor generáljon a program egy random számot:  "))

if loopnumber > a:
    loopnumber= int(input("Túl nagy szám kérlek adj meg egy kisebbet:  "))

filename= str(input("Mi legyen a fájl neve? Ékezeteket, és speciális karaktereket ne használj :) ")+".txt")

filehandler= open(filename,'w')

for x in range(1,loopnumber+1):
    randomszam= random.randint(0,1000)
    print("Az " + str(x) +". szám a " + str(randomszam))
    filehandler.write("Az " + str(x) +". szám a " + str(randomszam) + "\n")
    time.sleep(0.5)
filehandler.close

sys.exit