"""
#Atamalar
a = 10
b = 7

a,b = 3,5
x = "metehan"
print(a,b)

#type komutu
type(a)
type(b)
type(x)

#Matematiksel ifadeler
a+=7
b+=12

print(a,b)
"""
#tekli yorum satırı kullanımı
""""
#len komutu

len(x)

#upper ve lower komutu

x.upper()
x.lower()


#replace komutu

y = x.replace("e","a")

#strip komutu

y = "+saribas+"
z = y.strip("+")


print(a//b) #Tam sayı bölmesi
print(a%b) #Kalan bulma
print(a**b)
print(b%a)
print(a**0.5) # Üst kuvvetini alma
print(b**(1/3))

#Stringeleder index çağırma

isim = "metehan"
print(isim[0])
print(isim[0::2])
print(isim[1::2])
print(isim[4:])
print(isim[:4])
print(isim)
print(isim[:])
print(isim[::-1])
print(len(isim))

soyisim = "sarıbaş"

print(isim+soyisim)

print((isim*3))

isim = isim + " sarıbaş"

print(isim)

yas = 24

print(float(-yas))

print("pi sayısı 3.14'tür")

#int ve str değerlerini değiştirme

x = "10"
y = str(7)

print(x+y)
print(int(x)+int(y))

pi = "3.14"
pisayisi = float(pi)
print(pi)
print(pisayisi)

#print komutunun farklı  kullanımları

print("metehan","sarıbaş")

print("metehan\nsarıbaş")

print("metehan\tsarıbaş")

print("metehan      sarıbaş")

isim = "metehan"
soyisim = "sarıbaş"
yas = 44

print(isim,soyisim,sep= "-") # İndexleri istenilen karekter ile ayırma 

print(isim,soyisim,yas,sep="\n")

print(23,04,1920,sep="/")

print(*isim,sep="\n")

gun = 23
ay = 04
yil = 1920

#format komutunun kullanımları

print("{} {} {}'doğum tarihiniz ".format(gun,ay,yil))

print("{1} {0} {2}'doğum tarihiniz ".format(gun,ay,yil))

x = 3.1485656456
y = 7.12321312
z = 5.5765675

print("{:.2f} {:.4f} {:.1f}".format(x,y,z)) #format ile float değerlerinin istenilen basak masyısına kadar ekrana bastırılması

print("{:.2f} {:.4f} {:.0f}".format(x,y,z))

#liste kullanımı

liste = ["mete","han",23,19.05,1923,"sarıbaş"]

print(liste)
print(liste[1])
print(liste[len(liste)-1]) 
print(liste[-1]) #son elemanı verir
print(liste[:2])
print(liste[4:])
print(liste[1::2]) # başlama indeksi : bitiş indeksi: atlama değeri
print(liste[::-1])


liste1 = [1,2,3,4]
liste2 = [5,6,7,8]
liste3 = liste1+liste2 #listeleri birleştirir
liste4 = liste1*3 #aynı listeyi 3 kere olmak kaydı ile tek listede birleştirir
liste5 = ["mete","han","sarı","baş"]
liste2[-1] = 10
print(liste2)
liste3[4] =34
print(liste3)
print(liste4[2::2])

liste2.append("mete")  #listenin sonuna eleman ekler
print(liste2)
liste5.pop()   
print(liste5)
liste5.pop(1) #listenin 1. indeksindeki elemanı çıkartır
print(liste5)
liste3.sort() #listeyi küçükten büyüğe yada alfabetik şekilde sıralar
print(liste3)
liste3.sort(reverse=True) #sortun işlevini tersten yapar
print(liste3)

liste6 = [[1453,1299,1071],[1905,2000,2001]]
print(liste6[1][0])
liste6[1].insert(1, "gs") #listedeki 1. indekse yeni değer atanır
print(liste6)


#Demet kullanımı

demet = (1,2,3,4,5,6,6,6,8,1,2,2,3,4)

print(len(demet))
print(demet[3])
print(demet[3:7])
print(demet[3:9:3])
print(demet.count(6)) #kaç defa olduğunu öğrenmek için
print(demet.index(8)) #kaçıncı sırada olduğunu bulmak için

#Küme kullanımı

kume= set()
liste = ["mete", "han","sarı","bas",1,9,0,0,0,37]

kume = set(liste)

kume.add(1923)
kume.add("celal bayar")
kume.remove(0)
kume.discard(0)

kume1 = set(["han","mete",1,9,0,5,37])

kumeninfarki = kume.difference(kume1)
kume1infarki = kume1.difference(kume)

kumelerintumfarklari = kume.symmetric_difference(kume1)

kumlerinortakkesisimi = kume.intersection(kume1)

kumlerinbirlesimi = kume.union(kume1)


#Sözlükler

sozluk1 = {"bir":1,"iki":2,"üç":3,"dört":4}

print(sozluk1["bir"])
print(sozluk1["iki"])

sozluk1["beş"] = 5

print(sozluk1)

sozluk1["beş"] *=2

print(sozluk1)

sozluk2 = {"sayılar":{"bir":1,"iki":2,"üç":3,"dört":4},"mevsimler":{"ilkbahar":"papatya","yaz":"güneş","kış":"kar","sonbahar":"yaprak"}}

print(sozluk2)

print(sozluk2["sayılar"]["iki"])
print(len(sozluk1))
print(sozluk2.keys())
print(sozluk2.values())
print(sozluk2["sayılar"].keys())
print(sozluk2.items())
print(sozluk2["sayılar"].items())


#kullaıcıdan girdi alma (input fonksiyonu)

input("İsminiz nedir :")

x = int(input("İlk değeri giriniz :"))
y = int(input("İkinci değeri giriniz :"))
z = int(input("Son değeri giriniz :"))

print("Toplamları :",x+y+z)
print("Çarpımları :",x*y*z)


#format methodu ile Oyuncu kaydetme programı

ad = input("Adınız :")
soyad = input("Soyadınız :")
nickname = input("Nickname'iniz :")

bilgiler = [ad,soyad,nickname]

print("Adınız: {}\nSoyadınız: {}\nNickname'iniz: {}\n ".format(bilgiler[0],bilgiler[1],bilgiler[2]))

#hipotenüs bulma

ilkkenar = int(input("İlk kenarı giriniz :"))
ikincikenar = int(input("İkinci kenarı girini8z :"))
hipotenus = int((ilkkenar**2 +ikincikenar**2 )**0.5)
print("İlk kenar : {}\n İkinci kenar : {}\n Hipotenüs : {}".format(ilkkenar,ikincikenar,hipotenus))


#format methodu ile 3 sayının çarpımı

x = int(input("İlk sayıyı girin :"))
y = int(input("İkinci sayıyı girin :"))
z = int(input("Son sayıyı girin :"))

print(" İlk sayınız : {}\n İkinci sayınız : {}\n Son sayınız : {}\n Çarpımları : {}".format(x,y,z,x*y*z))


#format methodu Vücut kitle indeksi hesaplama

kilo = float(input("Kilonuzu girin :"))
boy = float(input("Boyunuzu metre cinsinden girin :"))

print("Kilonuz : {}\n Boyunuz : {}\n Vücut kitle indeksiniz : {} ".format(kilo,boy,kilo/boy**2))


#2021 fiat doblo kaç tl yakıt harcar

ikm = float(input("Kaç km şehir içinde yol aldınız : "))
dkm = float(input("Kaç km şehir dışında yol aldınız "))
icilitre = float(ikm*0.66*22.16)
disilitre = float(dkm*0.43*22.16)
print("Şehir içi litre tüketiminizin maliyeti : ", int(icilitre),"TL")
print("Şehir dışı litre tüketiminiz : ", int(disilitre),"TL")
print("Toplam maliyet : ",int(icilitre+disilitre),"TL")


#bilgileri listeye kaydederek ekrana format methodu ile bastırma

ad = input("Adınız:")
soyad = input("Soyadınız:")
no = int(input("Numaranız:"))
bilgiler= [ad,soyad,no]

print("\n ..... BİLGİLERİNİZ ..... \n Adınız : {}\n Soyadınız: {}\n Numaranız : {}".format(bilgiler[0],bilgiler[1],bilgiler[2]))


#kullanıcının bilgilerini format methodu ile değiştirme

x = int(input("İlk değeri giriniz :"))
y = int(input("İkinci değeri giriniz : "))

print("Değiştirilmeden önceki değer ler:\n İlk sayı : {}\n İkinci sayı : {} \n ".format(x,y))

x,y =y,x

print("Değiştirilmeden sonraki değerler:\n İlk sayı : {}\n İkinci sayı : {} \n ".format(x,y))



#koşullu durumlar

#yaş kontrolü

yas = int(input("Yaşınızı giriniz :"))

if yas < 18 :
    print("Giremezsiniz!")
else:
    print("Hoşgeldiniz...")
    

#hesap makinesi
print("****Hesap Makinesi****\n 1.Toplama İşlemi \n 2.Çıkartma işlemi\n 3.Çarpma İşlemi\n 4.Bölme İşlemi\n")

islem = int(input("İşlem seçiniz:"))
x = float(input("Birinci sayıyı giriniz:"))
y = float(input("İkinci sayıyı giriniz:"))

if islem == 1:
    print("{} ile {}' ün toplamları {} eşittir ".format(x,y,x+y))
elif islem == 2:
    print("{} ile {}' ün farkı {} eşittir ".format(x,y,x-y))
elif islem == 3:
    print("{} ile {}' ün çarpımları {} eşittir ".format(x,y,x*y))
elif islem == 4:
    print("{} ile {}' ün bölümleri {} eşittir ".format(x,y,x/y))
else:
    print("Geçersiz işlem yaptınız....")
    

#kullanıcı adı ile sisteme giriş


kullaniciadi = "mete"
guvenlikno = "1905icardi"

nickname = input("Kullanıcı adınızı giriniz :")
parola = input("Parolanızı giriniz :")

if nickname == kullaniciadi and guvenlikno == parola :
    print("Sisteme hoş geldiniz")
elif nickname != kullaniciadi and guvenlikno == parola :
    print("Kullanıcı adınız yanlış!")
elif nickname == kullaniciadi and guvenlikno != parola :
    print("Parolanız yanlış!")
else:
    print("Kullanıcı adı ve parola yanlış!")



#vücut kitle indeksine göre sağlık durumu hesaplayan program

boy = float(input("Metre cinsinden boyunuzu giriniz : "))
kilo = float(input("Kg cinsinden kilonuzu giriniz : "))
indeks = kilo/(boy*boy)

if indeks <= 18.5 :
    print("Vücut kitle indeksiniz : {} Zayıfsınız.".format(indeks))
elif 18.5 <= indeks <= 25 :
    print("Vücut kitle indeksiniz : {} Normalsiniz.".format(indeks))
elif 25  <= indeks <= 30  :
    print("Vücut kitle indeksiniz : {} Fazla kilolusunuz.".format(indeks))
else:
    print("Vücut kitle indeksiniz : {} Obezsiniz.".format(indeks))


#En büyük değeri ekrana yazdıran programı
x = float(input("İlk değeri giriniz:"))
y = float(input("İkinci değeri giriniz:"))
z = float(input("Son değeri giriniz:"))

if x <= y < z :
    print("En büyük sayı {}'dir.".format(z))
elif x > y >= z :
    print("En büyük sayı {}'dir.".format(x))
elif y > x >= z :
    print("En büyük sayı {}'dir.".format(y))
elif x >= y > z :
    print("En büyük sayı {}'dir.".format(x))
elif x >= z > y :
    print("En büyük sayı {}'dir.".format(x))
elif y >= x > z :
    print("En büyük sayı {}'dir.".format(y))
elif y >= z > x :
    print("En büyük sayı {}'dir.".format(y))
elif z >= x > y :
    print("En büyük sayı {}'dir.".format(z))
elif z >= y > x :
    print("En büyük sayı {}'dir.".format(z))
else:
    print("Tüm değerler eşittir.")


#2 vize 1 final notu ile ağırlıkları hesaplanarak harf notu bulma

vize1 = int(input("Vize 1'in notunu giriniz :"))
vize2 = int(input("Vize 2'nin notunu giriniz:"))
final = int(input("Final notunu giriniz:"))
toplamnot = (vize1*30/100)+(vize2*30/100)+(final*40/100)

if toplamnot >= 90 :
    print("Sınavlarınızın ortalaması {}, harf notunuz AA.".format(toplamnot))
elif toplamnot >= 85:
    print("Sınavlarınızın ortalaması {}, harf notunuz BA.".format(toplamnot))
elif toplamnot >= 80:
    print("Sınavlarınızın ortalaması {}, harf notunuz BB.".format(toplamnot))
elif toplamnot >= 75:
    print("Sınavlarınızın ortalaması {}, harf notunuz CB.".format(toplamnot))
elif toplamnot >= 70:
    print("Sınavlarınızın ortalaması {}, harf notunuz CC.".format(toplamnot))
elif toplamnot >= 65:
    print("Sınavlarınızın ortalaması {}, harf notunuz DC.".format(toplamnot))
elif toplamnot >= 60:
    print("Sınavlarınızın ortalaması {}, harf notunuz DD.".format(toplamnot))
elif toplamnot >= 55:
    print("Sınavlarınızın ortalaması {}, harf notunuz FD.".format(toplamnot))
elif toplamnot < 55:
    print("Sınavlarınızın ortalaması {}, harf notunuz FF.".format(toplamnot))


#geometrik şekil tahmit etme

kenar = input("Bulmak istediğiniz geometrik yapı üç kenarlı mı dört kenarlı mı?")


if  kenar == "3" or kenar == "üç":
    x = float(input("İlk kenarı giriniz:"))
    y = float(input("İkinci kenarı giriniz:"))
    z = float(input("Son kenarı giriniz:"))
    if abs(x-y)<z<x+y and abs(x-z)<y<x+z and abs(y-z)<x<y+z and x != y != z:
        print("Sıradan bir üçgene sahipsiniz...")
    elif abs(x-y)<z<x+y and abs(x-z)<y<x+z and abs(y-z)<x<y+z and x == y != z:
        print("İkizkenar bir üçgene sahipsiniz...")
    elif abs(x-y)<z<x+y and abs(x-z)<y<x+z and abs(y-z)<x<y+z and x != y == z:
        print("İkizkenar bir üçgene sahipsiniz...")
    elif abs(x-y)<z<x+y and abs(x-z)<y<x+z and abs(y-z)<x<y+z and x ==z != y:
        print("İkizkenar bir üçgene sahipsiniz...")
    elif abs(x-y)<z<x+y and abs(x-z)<y<x+z and abs(y-z)<x<y+z and x == z == y:
        print("Eşkenar bir üçgene sahipsiniz...")
    else:
        print("Girilen değerler üçgen belirtmiyor...")

elif kenar == "4" or kenar == "dört":
    x = float(input("İlk kenarı giriniz:"))
    y = float(input("İkinci kenarı giriniz:"))
    z = float(input("Üçüncü kenarı giriniz:"))
    q = float(input("Son kenarı giriniz:"))
    if x == y == z == q :
        print("Bir kareye sahipsiniz...")
    elif x == y and z== q :
        print("Bir dikdörtgene sahipsiniz...")
    elif x == z and y == q :
        print("Bir dikdörtgene sahipsiniz...")
    elif x == q and y == z :
        print("Bir dikdörtgene sahipsiniz...")
    else:
        print("Sıradan bir dörtgene sahipsiniz...")

else:
    print("Doğru komut girmediniz...")


#for döngüsü

liste1 = [1,3,5,7,9,11,13]
liste2 = []
toplam = 0

for i in liste1:
    toplam = toplam + i
    liste2.append(i)
    print("Toplanılan elemanlar = {} , Toplam sonuç = {} ".format(liste2,toplam))

# for döngüsü ile çift sayıları ekrana bastırma

liste = [1,2,3,4,5,6,7,8,9,10,11,12]

for i in liste:
    if i % 2 == 0:
        print(i)


# for döngüsü ile stringlerle işlem yapma

isim = "metehan"

for str in isim:
    print(str*4)

#for method'unu iki girdi ile liste üzerinde gezinme

liste = [(1,2),("elma","karpuz"),(4,5),("armut",10)]

for (i1,i2) in liste:
    print("ilk eleman: {}, son eleman: {}".format(i1,i2))

#for methodu ile sözlük üzerinde gezinme

sozluk = {"bir": 1,"iki" : 2, "üç": 3, "dört": 4}

for key in sozluk:
    print(key)
for val in sozluk.values():
    print(val)
for  (key,val) in sozluk.items():
    print("Keys: {} Values: {}".format(key,val))


#while ile liste üzerinde gezinme

liste = [1,2,3,4,5,6,7]
i = 0

while(i<len(liste)):
    print(liste[i])
    i += 1



#while ile range fonksiyonunu kullanma

i=0

while (i<101):
    print(i)
    i +=1



#for ile range fonksiyonunu kullanma

i = 0

for i in range(1,101):
    print(i)
    



#for ile break fonksiyonunun kullanımı

liste = [1,3,4,2,5,6,7,0,9,78,785]

for i in liste:
    if (i == 0):
        break
    print(i)


#for ile listeyi küçükten büyüğe sıralayıp break fonksiyonunun kullanımı

liste = [1,3,4,2,5,6,7,0,9,78,785]

for i in liste:
    liste.sort()
    if (i == 4):
        break
    print(i)



#while döngüsü ile kullanıcı durdurana kadar girdi almak

while True:
    print("Çıkmak için 'x' e basınız...")
    isim = input("isminizi giriniz:")
    if (isim == "x"):
        print("Programdan çıktınız...")
        break
    print("İsminiz:", isim)



#liste ile range i listeye ekleyip for döngünde çalıştırma

liste = list(range(101))
liste1 = []

for i in liste:
    print(i)
    liste1.appened(i)



#while ile tek sayıları ve çift sayıları ayrı ayrı bastırma (100 e kadar)

listetek = []
listecift = []
i = 0

while (i < 101):
    if (i % 2 == 0):
        listecift.append(i)
    else:
        listetek.append(i)
    i += 1
print("Tek sayılar : {} Çift sayılar : {} ".format(listetek,listecift))



#while ile contunie yi birlikte kullanarak tek sayıları ve çift sayıları ayrı ayrı bastırma

listetek = []
listecift = []
i = 0

while (i< 101):
    if(i % 2 == 0):
        listecift.append(i)
        i += 1
        continue
    else:
        listetek.append(i)
    i += 1
print("Tek sayılar : {} Çift sayılar : {} ".format(listetek,listecift))



#while ile contunie ile sadece tek sayıları bastırma

i = 0

while (i < 101):
    if (i % 2 == 0):
        i += 1
        continue
    else:
        print(i)
        i += 1 
        


#for ile contunie yi birlikte kullanarak tek sayıları ve çift sayıları ayrı ayrı bastırma

liste = list(range(101))
listetek = []
listecift = []

for i in liste:
    if ( i % 2 == 0):
        listecift.append(i)
        
        continue
    else:
        listetek.append(i)
        
print("Tek sayılar : {} Çift sayılar : {} ".format(listetek,listecift))



#List Comprehension örnekleri

liste1 = [1,2,3,4,5,6]
liste2 = [i for i in liste1]
liste3 = [i * 4 for i in liste1]
liste4 = [(1,2),(3,4),(5,6),(7,8)]
liste5 = [j*k for j,k in liste4]
isim = "metehan"
isim2 = [i*7 for i in isim]

print(liste2)
print(liste3)
print(liste5)
print(isim2)


#while döngüsü ile kullanıcı  giriş algoritması (3 giriş hakkı ile)


kullaniciadi = "3424dsdsfdf"
parola = "sdasd12323"
girissayisi = 3

while True:
    username = input("Kullanıcı adınızı giriniz...")
    pasword = input("Parolanızı giriniz...")
    if (kullaniciadi != username and parola == pasword):
        girissayisi -=1
        print("Kullanıcı adı veya parola hatalı...")
    elif (kullaniciadi == username and parola != pasword):
        girissayisi -=1
        print("Kullanıcı adı veya parola hatalı...")
    elif (kullaniciadi != username and parola != pasword):
        girissayisi -=1
        print("Kullanıcı adı veya parola hatalı...")
    else:
        print("Sisteme hoşgeldiniz...")
        break
    if (girissayisi == 0):
        print("Sisteme giriş hakkınız kalmadı...")
        break


#while içinde while ile Atm programı

 #print("""#********** Hoşgeldiniz **********

#İşlemler:

#1. Bakiye Sorgulama

#2. Para Yatırma

#3. Para Çekme

#Programı kapatmak için 'q' ya basınız...

""")

bakiye = int(1000)

while True:
    islem = input("Yapmak istediğiniz işlemin numarasını giriniz...")

    if (islem == "q"):
        print("Programdan çıktınız. İyi günler...")
        break
    if (islem == "1"):
        print("Bakiyeniz :", bakiye)
    elif (islem == "2"):
        yatirilan_para = int(input("Yatırmak istediğiniz parayı miktarını giriniz..."))
        bakiye += yatirilan_para
        print("Bakiyeniz: ", bakiye)
    elif (islem == "3"):
        while True:
           cekilen_para = int(input("Çekmek istediğiniz para miktarını giriniz..."))
           if (cekilen_para > bakiye):
               print("Bakiyenizden {} miktar fazla para istediniz, çekebileceğiniz para miktarına uygun miktar giriniz...".format(abs(bakiye-cekilen_para)))
               break
           else:
               bakiye -=cekilen_para
               print("Kalan bakiyeniz:",bakiye)

    else:
        print("Yanlış işlem seçeneği girdiniz...")


#istenilen sayının faktöriyelini bulma

faktoriyel = 1

while True:
    sayi = int(input("Bulmak istediğiniz faktöriyeli giriniz..."))
    for i in range(2,sayi+1):
        faktoriyel *= i
    print(faktoriyel)
    faktoriyel = 1

#kullanıcının girdiği sayının mükemmel sayı olup olmadığını öğrenme (for ile)

sayi = int(input("Sayıyı giriniz:"))
bolenler = []
for i in range(1, sayi):
    if sayi % i == 0:
        bolenler.append(i)
toplam = 0
for eleman in bolenler:
    toplam += eleman
if toplam ==  sayi:
    print(sayi, "bir mükemmel sayıdır.")
else:
    print(sayi, "bir mükemmel sayı değildir.")


#çarpım tablosu for ile range kullnarak

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print("------------------")

# input değerinin asal sayı olup olmadığını öğrenme (while)

sayi = int(input("Değeri giriniz:"))
bolenler = []
i= 2

if sayi>1:
    while i<=sayi:
        if sayi % i ==0:
            bolenler.append(i)
            i += 1
        else:
            i+=1
    if len(bolenler)== 1:
        print(sayi,"Asal sayıdır.")
    else:
        print(sayi,"Asal değildir.")
else:
    print("Geçersiz sayı girdiniz...")


#  Palindrom Kontrolü

kelime = input("Kelime :")

if kelime == kelime[::-1]:
    print("doğru")
else:
    print("Değil")



# kullancıdan alınan iki sayının EBOB unu bulma

ilk = int(input("İlk sayi:"))
iki = int(input("İkinci sayi:"))
ebob = []
if ilk > iki:
    for i in range(1,iki+1):
        if ilk % i == 0 and iki % i == 0:
            ebob.append(i)
    print(ebob[-1])
elif iki > ilk:
    for i in range(1,ilk+1):
        if ilk % i == 0 and iki % i == 0:
            ebob.append(i)
    print(ebob[-1])
else:
    print("ebob:", ilk)

"""
""""
#Kullanıcıdan alınan  bir sayının Armstrong sayısı olup olmadığını bulmak

sayi = input("Hangi sayının Armstrong sayısı olup olmadığını bulmak istiyorsunuz ? ")
basamak_sayisi= len(sayi)
basamak_sayisi_ilk= basamak_sayisi = len(sayi)
sayi2 = int(sayi)
kalan_listesi = []
kalan = 0
sonuc = 0

while sayi2 > 0:
    kalan = (sayi2 // (10**(int(basamak_sayisi)-1)))
    kalan_listesi.append(kalan)
    sayi2 -= (kalan * (10**(int(basamak_sayisi)-1)))
    basamak_sayisi -= 1
    kalan = 0


for toplam in kalan_listesi:
    sonuc += (toplam**basamak_sayisi_ilk)

if sonuc == int(sayi):
    print("Sayınız bir Armstrong sayısıdır...")
else:
    print("Sayınız bir Armstrong sayısı değildir...")
"""
"""""
#Kullanıcıdan alınan bir sayının Armstrong sayısı olup olmadığını bulmak EN KISA YÖNTEM İLE

sayi = input("Hangi sayının Armstrong sayısı olup olmadığını bulmak istiyorsunuz ? ")
basamak_sayisi = len(sayi)
rakamlar = []
sonuc = 0
for rakam in sayi:
    rakamlar.append(int(rakam))
for toplanılanlar in rakamlar:
    sonuc += (toplanılanlar **(basamak_sayisi))
if sonuc == int(sayi):
    print("Sayınız bir Armstrong sayısıdır...")
else:
    print("Sayınız bir Armstrong sayısı değildir...")


"""""

#Geliştirilmiş hesap makinesi(While True kullanarak sonuç ile de işlem yapabilen ve sonuç sıfırlanabilinen

"""""
print("****Hesap Makinesi****\n 1.Toplama İşlemi \n 2.Çıkartma işlemi\n 3.Çarpma İşlemi\n 4.Bölme İşlemi\n '5' Çıkmak için kullanın")



while True:
    sayi1 = float(input("İlk sayiyi girin..."))
    sayi2 = float(input("Diğer sayiyi girin..."))
    islem = int(input("Kaç numaralı işlem yapmak istiyorsunuz ? "))
    sonuc= 0
    if islem == 1:
        print("Sonuc :",sayi1+sayi2  )
        sonuc = sayi1 + sayi2
        while True:
            cevap = input(" Sonuca göre islem yapmak istiyorsanız 'e' Hayır ise 'h' tuşunu giriniz...")
            if cevap == "h":
                break
            elif cevap == "e":
                sayi3 = float(input("Diğer sayıyı giriniz: "))
                islem2 = int(input("Kaç numaralı işlemi yapmak istiyorsunuz: "))
                if islem2 == 1:
                    print("Sonuç :" , sonuc+sayi3 )
                    sonuc += sayi3
                elif islem2 == 2:
                    print( "Sonuc :" , sonuc-sayi3 )
                    sonuc -= sayi3
                elif islem2 == 3:
                    print("Sonuç :" , sonuc*sayi3 )
                    sonuc *= sayi3
                elif islem2 ==4:
                    sonuc /= sayi3
                else:
                    print("Geçersiz komut girdiniz...")
                    continue
            else:
                print("Yanlış değer girdiniz...")
                continue
    elif islem == 2:
        print("Sonuc :" , sayi1-sayi2 )
        sonuc = sayi1 - sayi2
        while True:
            cevap = input(" Sonuca göre islem yapmak istiyorsanız 'e' Hayır ise 'h' tuşunu giriniz...")
            if cevap == "h":
                break
            elif cevap == "e":
                sayi3 = float(input("Diğer sayıyı giriniz: "))
                islem2 = int(input("Kaç numaralı işlemi yapmak istiyorsunuz: "))
                if islem2 == 1:
                    print("Sonuc :" , sonuc+sayi3 )
                    sonuc += sayi3
                elif islem2 == 2:
                    print("Sonuc :" , sonuc-sayi3 )
                    sonuc -= sayi3
                elif islem2 == 3:
                    print("Sonuç :" , sonuc*sayi3)
                    sonuc *= sayi3
                elif islem2 == 4:
                    print("Sonuc :" , sonuc/sayi3)
                    sonuc /= sayi3
                else:
                    print("Geçersiz komut girdiniz...")
                    continue
            else:
                print("Geçersiz komut girdiniz...")
                continue
    elif islem == 3:
         print("Sonuç :" , sayi1*sayi2)
         sonuc = sayi1*sayi2
         while True:
            cevap = input(" Sonuca göre islem yapmak istiyorsanız 'e' Hayır ise 'h' tuşunu giriniz...")
            if cevap == "h":
                 break
            elif cevap == "e":
                sayi3 = float(input("Diğer sayıyı giriniz: "))
                islem2 = int(input("Kaç numaralı işlemi yapmak istiyorsunuz: "))
                if islem2 == 1:
                    print("Sonuc : ", sonuc+sayi3)
                    sonuc+= sayi3
                elif islem2 ==2:
                    print("Sonuc :" , sonuc - sayi3)
                    sonuc -= sayi3
                elif islem2 ==3:
                    print("Sonuç :" , sonuc*sayi3)
                    sonuc *= sayi3
                elif islem2 ==4:
                    print("Sonuc :" , sonuc/sayi3)
                    sonuc /=sayi3
                else:
                    print("Geçersiz komut girdiniz...")
                    continue
            else:
                print("Geçersiz komut girdiniz...")
                continue
    elif islem == 4:
        print("Sonuç :" , sayi1/sayi2)
        sonuc = sayi1/sayi2
        while True:
            cevap = input(" Sonuca göre islem yapmak istiyorsanız 'e' Hayır ise 'h' tuşunu giriniz...")
            if cevap == "h":
                break
            elif cevap == "e":
                sayi3 = float(input("Diğer sayıyı giriniz: "))
                islem2 = int(input("Kaç numaralı işlemi yapmak istiyorsunuz: "))
                if islem2 ==1:
                    print("Sonuc : ", sonuc+sayi3)
                    sonuc += sayi3
                elif islem2 == 2:
                    print("Sonuc : ", sonuc-sayi3)
                    sonuc -= sayi3
                elif islem2 == 3:
                    print("Sonuc : ", sonuc*sayi3)
                    sonuc *= sayi3
                elif islem2 ==4:
                    print("Sonuc : ", sonuc/sayi3)
                    sonuc /= sayi3
                else:
                    print("Geçersiz komut girdiniz...")
                    continue
            else:
                print("Geçersiz komut girdiniz...")
                continue
    elif islem == 5:
        print("Güle güle")
        break
    else:
        print("Geçersiz komut girdiniz")
        continue


""""""
#1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırıp Bu işlemi *continue* ile yapmak

for i in range(1,100):
    if i % 3 != 0:
        continue
    else:
        print(i)
""

# List comprehension kullanarak 1'den 100'e kadar olan sayılardan sadece çift sayıları bir listeye atmayı yapmak

cift_sayılar = [ i for i in range(1,100) if i % 2 == 0]

print(cift_sayılar)

""""""








