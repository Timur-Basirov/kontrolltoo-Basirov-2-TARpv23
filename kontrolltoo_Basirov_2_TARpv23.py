#1
try:
    n=int(input("Sisestage, mitu küülikut soovite näha."))
    for i in range(n):
        print("(\_/)\n(o o)\n/ | \*")
        print()
except:
    print("Järgmine kord sisestage number, mitte tekst või sümbol")
print()

#2
summa=0
for i in range(0,14,1):
    print(i,end=" ")
    summa+=i
print()
print("nende numbrite summa on",summa)
print()

#3
from random import randint
try:
    print("arvata number vahemikus 0-100")
    n = randint(0, 100)
    i = 0
    while True:
       a = int(input())
       if a == n:
           print("Õnnitleme, et sa arvasid ära numbri")
           break
       if a < n:
          print("arvatav arv on suurem kui")
       else:
           print("arvatav arv on väiksem kui")
       i += 1
       if i == 10:
           print(f"Sa kaotad. Arvatud number on {n}")
           break
except:
    print("Järgmine kord sisestage number, mitte tekst või sümbol")
print()

#4
try:
    a = (abs(int(input("Sisestage täisarv => "))))
    print("*Pöörake* sisestatud number ümber")
    print()
    b=0
    while a>0:
        number = a%10
        a=a//10
        b=b*10+ number
    print("*Ümberpööratud* number",b)
except:
    print("Järgmine kord sisestage number, mitte tekst või sümbol")
print()

#5
try:
    number=input("Sisestage number:")
    summa=0
    teose=1
    for num in number:
        num=int(num)
        summa+=num
        teose*=num
    print("Summa on:", summa)
    print("Teose on:", teose)
except:
    print("Järgmine kord sisestage number, mitte tekst või sümbol")
print()
print("Tänan teid, et vaatasite minu tööd! ")
print("TARpv23 Baširov Timur")