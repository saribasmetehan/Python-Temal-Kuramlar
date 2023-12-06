""""
a = 12
b = 0

try:
    print(a/b)
except ZeroDivisionError:
    print("Hiçbir sayı 0'a bölünmez...")
    


a = 12
b= "asdfa"

try:
    print(a/b)
except TypeError:
    print("İnt değeri str değerine bölünmez")



try:
    a = int(input("İlk sayıyı giriniz..."))
    b = int(input("İkinci sayıyı giriniz..."))
    print(a*b)
except:
    print("Hatalı değerler girdiniz")



a = 12
b= "dsffsadf213123"

try:
    print(a/b)
except:
    print("Hatalı bir değer vardır...")
finally:
    print("Program sonlandırıldı")


#stringlerin içinde sadece rakam bulunanları ekrana bastırmak

liste = ["345","sadas","324a","14","kemal","sdsad234342","xfdsffds3434",123123,343453,"dffdgdfgdgf","sdfdwsf55"]

i = 0

while i < len(liste):
    try:
        int(liste[i])
    except :
        i +=1
        continue
    print(liste[i])
    i += 1
    
"""""

liste = []

def cift_sayi_bulma(x):
    if x % 2 ==0:
        liste.append(x)
        return x
    if x % 2 == 1:
        raise ValueError("Tek sayı girdin")

cift_sayi_bulma(3)








