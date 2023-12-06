#Fonksiyonlar


""""
def selamlama():
    print("Merhaba")

selamlama()


isim = input("İsminiz nedir?")

def selamla(isim):
    print("Merhaba", isim)

selamla(isim)



def toplama(a,b,c):
    return a+b+c
sonuc = toplama(1,2,3)

print(sonuc)




def toplama(a=0,b=0):
    return a+b

sonuc= toplama()

print(sonuc)



def toplama(a=0,b=0):
    return a +b

sonuc = toplama(b=1,a=3)

print(sonuc)




def toplama(*a):
    sonuc = 0
    for i in a:
        sonuc += i
    return sonuc

cevap = toplama(1,2,3,4,5,6,7)

print(cevap)



#İnput ile alınan bir değeri fonksiyon ile asal sayı olup olmadığını öğrenme

sayi = int(input("Sayıyı giriniz:"))

def asal_sorgulama(a):
    liste = []
    for i in range(2,a):
        if a % i == 0:
            liste.append(i)
    if len(liste) == 0  or a == 2 :
        print(a,"bir asal sayıdır...")
    else:
        print(a,"bir asal sayı değildir!")

asal_sorgulama(sayi)


# tekrarlı birşekilde istenilen  sayının tam bölenlerini fonksiyon kullanarak bulma

bolen_listesi = []

def bolen(x):
    for i in range(1,x+1):
        if x % i == 0:
            bolen_listesi.append(i)
    print(bolen_listesi)

while True:
    sayi = input("Tam bölenlerini bulmak istediğiniz sayıyıyı giriniz: (Çıkmak için 'q' ya basınınız)")
    if sayi == "q":
        print("Güle güle")
        break
    else:
        sayi = int(sayi)
        bolen(sayi)
bolen_listesi.clear()


#İstenilen aralıktaki kaç tane mükemmel sayı olup olmadığını ve neler olduğunu gösteren algoritma


def mukemmel_sayi(x,y):
    mukemmel_sayilar = []
    for i in range(x,y):
        bolenler = []
        sonuc = 0
        for k in range(1,i):
            if i % k == 0:
                bolenler.append(k)
        sonuc = sum(bolenler)
        if sonuc == i:
            mukemmel_sayilar.append(i)
    return mukemmel_sayilar

while True:
    sayi1 = input("Mükemmel sayılarınızı hangi aralıktan başlatmak istiyorsunuz ? (Çıkmak için 'q' ya basınız...)")
    sayi2 = input("Mükemmel sayılarınız hangi aralıkta sona ersin:")

    if sayi1 == "q":
        print("Güle güle")
    else:
        sayi1 = int(sayi1)
        sayi2 = int(sayi2)
        print(len(mukemmel_sayi(sayi1,sayi2)),"Adet mükemmel sayınız vardır")
        print(mukemmel_sayi(sayi1,sayi2))



#kullanıcıdan iki tane sayının alınması ve bu sayıların EBOB unun bulunması fonksiyon ile


def ebob(sayi1,sayi2):
    if sayi1 > sayi2:
        ebob_listesi = []
        for i in range(1,sayi1+1):
            if sayi1 % i  == 0 and sayi2 % i == 0:
                ebob_listesi.append(i)
    if sayi2 > sayi1:
        ebob_listesi = []
        for i in range(1, sayi2+1):
            if sayi1 % i == 0 and sayi2 % i == 0:
                ebob_listesi.append(i)
    return ebob_listesi[-1]

while True:
    x = input("Ebob'unu bulmak istediğiniz ilk sayıyı giriniz...(Çıkmak isterseniz 'q' yu giriniz)")
    y = input("Ebobunu bulmak istediğiniz ikinci sayıyı giriniz")

    if x == "q":
        print("Güle Güle")
        break
    else:
        x = int(x)
        y = int(y)
        print("EBOB:", ebob(x,y))



#kullanıcıdan iki tane sayının alınması ve bu sayıların EKOK unun bulunması fonksiyon ve tuple kullanarak



def ekok(x,y):
    ekok_listesi = []
    x_listesi = []
    y_listesi = []
    sonuc = 0
    for i in range(1,y+1):
        x_listesi.append(x*i)
    for i in range(1,x+1):
        y_listesi.append(y*i)
    ekok_listesi.extend(x_listesi)
    ekok_listesi.extend(y_listesi)
    ekok_listesi.sort()
    for i in range(len(ekok_listesi)-1):
        if ekok_listesi[i] == ekok_listesi[i+1]:
            sonuc = ekok_listesi[i]
            break
    return sonuc


while True:
    sayi1 = input("Ekok'unu bulmak istediğiniz ilk sayıyı giriniz...(Çıkmak isterseniz 'q' yu giriniz)")
    sayi2 = input("Ekokunu bulmak istediğiniz ikinci sayıyı giriniz")

    if sayi1 == "q":
            print("Güle Güle")
            break
    else:
        sayi1 = int(sayi1)
        sayi2 = int(sayi2)
        print("EKOK:", ekok(sayi1,sayi2))




# iki basamaklı sayıların okunuşunun fonksiyonu

def okunus(x):
    onlar = x // 10
    birler = x % 10

    y = ""
    z = ""

    if onlar == 1:
        y = "on"
    elif onlar == 2:
        y = "yirmi"
    elif onlar == 3:
        y = "otuz"
    elif onlar == 4:
        y = "kırk"
    elif onlar == 5:
        y = "elli"
    elif onlar == 6:
        y = "altmış"
    elif onlar == 7:
        y = "yetmiş"
    elif onlar == 8:
        y = "seksen"
    elif onlar == 9:
        y = "doksan"

    if birler == 1:
        z = "bir"
    elif birler == 2:
        z = "iki"
    elif birler == 3:
        z = "üç"
    elif birler == 4:
        z = "dört"
    elif birler == 5:
        z = "beş"
    elif birler == 6:
        z = "altı"
    elif birler == 7:
        z = "yedi"
    elif birler == 8:
        z = "sekiz"
    elif birler == 9:
        z = "dokuz"

    if birler == 0:
        z = "" 

    return print(y, z)

while True:
    sayi = input("Okunuşunu bilmek istediğiniz iki basamaklı sayıyı giriniz: ")

    if len(sayi) == 2:
        sayi = int(sayi)
        okunus(sayi)
    else:
        print("Yanlış değer girdiniz, tekrar deneyin...")
        continue

"""""

#istenilen değerler arasındaki tüm pisagor üçgenlerini ekrana bastırma

def pisagor(z):
    for x in range(1, z + 1):
        for y in range(1, z + 1):
            for i in range (1,((z+1)**2)):
                if (x**2) + (y**2) == (i**2):
                    print(f"ilk kenar: {x} ikinci kenar {y} hipotenüs {i} ")

while True:
    aralik = input("Maksimüm hipotenüs değeriniz kaç olsun? (Çıkmak isterseniz 'q' yu giriniz")

    if aralik == "q":
        print("Güle Güle...")
        break
    else:
        aralik = int(aralik)
        pisagor(aralik)
















