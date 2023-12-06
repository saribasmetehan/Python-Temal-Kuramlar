"""""
#lambda fonksiyonu

def kare_al(x):
    return x**2

print(kare_al(3))

al_kare = lambda x : x**2

print(al_kare(3))

def ust_alma(n):
    return lambda x : x**n

kare_alma = ust_alma(2)
kup_alma = ust_alma(3)

print(kup_alma(4))
print(kare_alma(4))


#map fonksiyonu

tek_sayilar = [1,3,5,7,9]
cift_sayilar = [0,2,4,6,8]

cift_kareler = list(map(lambda x : x**2, cift_sayilar))
tek_kupler = list(map(lambda x: x**3,tek_sayilar))

print(cift_kareler)
print(tek_kupler)

carpım = list(map(lambda x,y : x*y,tek_sayilar,cift_sayilar))

print(carpım)


#filter fonksiyonu

liste = [1,2,3,4,5,6,6,7,8,9]

tek_sayilar = list(filter(lambda x : x % 2 != 0,liste))
cift_sayilar = list(filter(lambda x : x % 2 == 0, liste))

print(tek_sayilar)
print(cift_sayilar)

print(list(filter(lambda x : x % 2 == 0, range(100))))

def asal_bul(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2,x):
            if x % i == 0:
               return False
        return True

print(list(filter(asal_bul,range(1,100))))




#reduce fonksiyonu

import functools

liste = [1,2,3,4,5,6,7,8,9,10]
liste_karisik = [-12,232,445,-23,0,123,4563,0.2]
print("4 faktöriyel : "+ str(functools.reduce(lambda x,y : x*y , range(1,5))))


print(functools.reduce(lambda x,y : x+y,liste))

def max_deger(x,y):
    if x > y:
        return x
    else:
        return y
def min_deger(x,y):
    if x < y:
        return x
    else:
        return y

print("Maksimum değer : " + str(functools.reduce(max_deger,liste_karisik)))
print("Minimum değer : " + str(functools.reduce(min_deger, liste_karisik)))



#zip fonksiyonu

liste1 = [1,3,5,7,9]
liste2 = [0,2,4,6,8,10]

liste3 = list(zip(liste1,liste2))

print(liste3)

for x,y in zip(liste1,liste2):
    print("liste1'in elemanlanı :" + str(x))
    print("liste2'nin elemanı :" + str(y))


#enumarete fonksiyonu

liste = [0,1,2,3,4,5,6,7,8,9]

print(list(enumerate(liste)))


#lambda,filter ve reducenin birlikte kullanımı

import functools

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cift_sayilarin_toplami = []

cift_sayilar = list(filter(lambda x : x % 2 == 0,liste))

print(functools.reduce(lambda x,y:x+y,cift_sayilar))

"""""



















