"""""
#Dosya açma işlemleri

dosya = open("Belge.txt","w")

dosya.close()

dosya1 = open("C:/Users/meteh/Desktop/Belge.txt","w")

dosya1.close()

dosya = open("Belge.txt","w",encoding="utf-8")

dosya.write("Merhaba Python!!!")

dosya.close()

dosya = open("Belge.txt","a")

dosya.write("\n=) Merhaba")

dosya.close()



#Dosya okuma işlemleri

dosya = open("Belge.txt","a",encoding="utf-8")

dosya.write("Toplum 4.0\n")

dosya.write("Bilgi Toplumu\n")

dosya.write("Yapay zeka çağı\n")

dosya.write("Hadi gelişelim\n")

dosya.close()

dosya = open("Belge.txt","r",encoding="utf-8")

print("-----Belgeler'in içeriği:-----\n")

for i in dosya:
    print(i,end="")
    
dosya.close()


dosya = open("Belge.txt","r",encoding="utf-8")

dosya_icerik = dosya.read()

print(dosya_icerik)

dosya.close()


dosya = open("Belge.txt","r",encoding="utf-8")

print(dosya.readline())
print(dosya.readline())
print(dosya.readline())
print(dosya.readline())
print(dosya.readline())
print(dosya.readline())

dosya.close()

x

dosya = open("Belge.txt","r",encoding="utf-8")

dosya_liste = dosya.readlines()

print(dosya_liste)

dosya.close()



#Dosya fonksiyonlarının bazı çeşitleri ve farklı kullanımları

with open("Belge.txt","r",encoding="utf-8") as dosya:
    for i in dosya:
        print(i)


with open("Belge.txt","r",encoding="utf-8") as dosya:
     print(dosya.tell())
     dosya.seek(10)
     print(dosya.tell())
     

with open("Belge.txt","r",encoding="utf-8") as dosya:
    print(dosya.tell())
    dosya.seek(10)
    icerik_10_20 = dosya.read(10)
    print(icerik_10_20)
    dosya.seek(0)
    print(dosya.read())
    dosya.seek(3)
    print(dosya.read(4))

with open("Belge.txt","r+",encoding="utf-8") as dosya:
    eski_icerik = dosya.read()
    dosya.seek(0)
    dosya.write("İlk cümle\n"+ eski_icerik)
    dosya.seek(0)
    print(dosya.read())


with open("Belge.txt","a",encoding="utf-8") as dosya:
    dosya.write("Son cümle\n")

with open("Belge.txt","r",encoding="utf-8") as dosya:
    print(dosya.read())


with open("Belge.txt","r+",encoding="utf-8") as dosya:
    liste = dosya.readlines()
    liste.insert(3,"Orta cümle\n")
    dosya.seek(0)
    dosya.writelines(liste)
    dosya.seek(0)
    print(dosya.read())


# Öğrencilerin isimleri ve aldığı notların olduğu bir .txt dosyasından yeni bir .txt dosyası oluşturarak bu dosyaya harf notlarıyla birlikte öğrencileri yazmak

def harf_hesaplama(bilgi):
    bilgi_liste = bilgi.strip().split(",")
    isim = bilgi_liste[0].strip()
    not1 = int(bilgi_liste[1])
    not2 = int(bilgi_liste[2])
    not3 = int(bilgi_liste[3])
    sonuc = not1 * 0.25 + not2 * 0.25 + not3 * 0.5

    if sonuc >= 90:
        sonuc = "AA"
    elif sonuc >= 80:
        sonuc = "BA"
    elif sonuc >= 70:
        sonuc = "BB"
    elif sonuc >= 60:
        sonuc = "CC"
    elif sonuc >= 50:
        sonuc = "DC"
    else:
        sonuc = "FF"
    return isim + ":" + sonuc + "\n"

with open("ogrencinotlari.txt", "r", encoding="utf-8") as ogrenci_notlari:
    liste = []
    for i in ogrenci_notlari:
        liste.append(harf_hesaplama(i))

with open("harflistesi.txt", "w", encoding="utf-8") as harf_listesi:
    for i in liste:
        harf_listesi.write(i)

with open("harflistesi.txt", "r", encoding="utf-8") as harf_listesi:
    with open("kalanlar.txt", "w", encoding="utf-8") as kalanlar:
        with open("gecenler.txt", "w", encoding="utf-8") as gecenler:
            kalanlar_listesi = []
            gecenler_listesi = []

            for i in harf_listesi:
                kontrol = i.strip().split(":")
                isim, not_durumu = kontrol[0], kontrol[1]

                if not_durumu == "FF":
                    kalanlar_listesi.append(isim)
                else:
                    gecenler_listesi.append(isim)

            for isim in gecenler_listesi:
                gecenler.write(isim + "\n")

            for isim in kalanlar_listesi:
                kalanlar.write(isim + "\n")

"""""
#isim soyisim ve rütbelerin olduğu bir .txt dosyasını rütbelerine göre farklı listelere yazdırma

with open("askerler.txt","r",encoding="utf-8") as askerler:
    er = []
    assubay = []
    subay = []
    for i in askerler:
        i = i[:-1]
        kontrol = i.split(":")
        isim,rutbe = kontrol[0],kontrol[1]
        if kontrol[1] == "er":
            er.append(isim)
        elif kontrol[1] == "assubay":
            assubay.append(isim)
        else:
            subay.append(isim)
    with open("er.txt","w",encoding="utf-8") as erler:
        for i in er:
            erler.write(i+"\n")
    with open("assubay.txt", "w", encoding="utf-8") as assubaylar:
        for i in assubay:
            assubaylar.write(i + "\n")
    with open("subay.txt", "w", encoding="utf-8") as subaylar:
        for i in subay:
            subaylar.write(i+"\n")




















































































