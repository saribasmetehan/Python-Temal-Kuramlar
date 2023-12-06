"""""
#Sayıları 2'lik taban sisteminde gösterme

sayi1 = 123
sayi2 = 10
sayi3 = 45678

print(bin(sayi1))
print(bin(sayi2))
print(bin(sayi3))

#Sayıları 16'lık taan sisteminde gösterme

print(hex(sayi1))
print(hex(sayi2))
print(hex(sayi3))

#Sayıların mutlak değerlerini bulma

print(abs(-23))
print(abs(12))
print(abs(-44565))

#Sayıları en yakın değerlerini göstermek

print(round(123.223))
print(round(123.223,2))
print(round(123.5))
print(round(123.7))

#Listelerein maximum ve minimum değerlerini bulma

liste = [1,23,445,55656,-12232,0.355]

print(max(liste))
print(min(liste))

#Listeddeki tüm sayıların toplamını bulma

print(sum(liste))

#Sayıların kuvvetlerini alma

print(pow(sayi3,sayi2))
print(pow(sayi1,sayi2))


#upper ve lower fonksiyonları

ad = "Metehan"
soyad = "Sarıbaş"

print(ad.upper())
print(soyad.lower())

#replace fonksiyonu

print(ad.replace("e","a"))
print(soyad.replace("a","e"))

#endswitch fonksiyonu

print(ad.endswith("han"))
print(soyad.endswith("ş"))
print(soyad.endswith("Ş"))

#split fonksiyonu

tarih = "19.04.1920"

liste = tarih.split(".")

print(liste)

#strip, lstrip ve rstrip fonksiyonları

giris_cumlesi = "-----Hoşgeldiniz-----"

print(giris_cumlesi.strip("-"))
print(giris_cumlesi.lstrip("-"))
print(giris_cumlesi.rsplit("-"))

#join fonksiyonu

print(".".join(liste))

#count fonksiyonu

print(ad.count("a"))
print(soyad.count("a",2))

#find ve rfind fonksiyonları

print(ad.find("a"))
print(soyad.rfind("ı"))


#Kümelerin detaylı incelenişi

kume1 = {1,3,5,7,9}
kume2 = {0,2,4,6,8}
liste = [1,2,3,4,5,6,7,8,9,10]

kume3 = set(liste)

print(kume3)

kume1.add(11)
kume2.add(10)
kume1.discard(1)
kume2.discard(0)

print(kume1)
print(kume2)

print(kume1.difference(kume2))
print(kume2.difference(kume1))

kume1.difference_update(kume2)
print(kume1)

print(kume1.intersection(kume2))

print(kume1.isdisjoint(kume2))
print(kume2.isdisjoint(kume3))

print(kume1.issubset(kume3))

print(kume1.union(kume2))

kume1.update(kume2)

print(kume1)



#Listeleri detaylı inceleme

liste1 = [0,2,4,6,8]
liste2 = [1,3,5,7,9]

liste1.extend(liste2)

print(liste1)
print(liste2)

liste1.pop()
liste1.pop(2)

print(liste1)

liste1.remove(3)
print(liste1)

print(liste1.index(8))

print(liste2.count(9))
print(liste2.count(1905))

liste1.sort()
print(liste1)
liste1.sort(reverse=True)
print(liste1)

"""""

