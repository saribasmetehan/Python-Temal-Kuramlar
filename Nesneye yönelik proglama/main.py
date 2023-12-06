
"""""
#Sınıf tanımlamarı ve sınıfın içerisindeki bir nesne tabımlamarı
class ogrenciler():
    sinif = 
    bolum = 
    hobiler = []
    not_ort =

han = ogrenciler()

class ogrenciler():
    sinif = 1
    bolum = "Yazılım mühendisliği"
    hobiler = ["Futbol","Boks"]
    not_ort = 1

han = ogrenciler()

print(han.sinif)
print(han.bolum)
print(han.hobiler)
print(han.not_ort)


class ogrenciler():
    def __init__(self,bolum = "Yazılım Mühendisliği",sinif = None,hobiler = None,yas = None):
        self.bolum = bolum
        self.sinif = sinif
        self.hobiler = hobiler
        self.yas = yas

han = ogrenciler(sinif = 5,yas = 23,hobiler = ["futbol"])

print(han.sinif,han.hobiler,han.bolum,han.yasi,)



class yazilim_muhendisleri():
    def __init__(self,isim,soyisim,tecrube,bildigi_diller,maas):
        self.isim = isim
        self.soyisim = soyisim
        self.tecrube = tecrube
        self.bildigi_diller = bildigi_diller
        self.maas = maas
    def tecrube_artisi(self,gecirdigi_yil = 0):
        self.tecrube += gecirdigi_yil
    def zam(self,miktar = 0):
        self.maas += (miktar + (self.tecrube * 200))
    def dil_ekleme(self,*dil):
        self.bildigi_diller.append(dil)
    def bilgileri_goster(self):
        print(f"İsim = {self.isim} \n Soyisim = {self.soyisim} \n Tecrube = {self.tecrube} \n Bildiği diller = {self.bildigi_diller} \n Maaş = {self.maas}")

yazilimci1 = yazilim_muhendisleri(isim = "Metehan",soyisim = "Sarıbaş", tecrube = 3,maas = 10000, bildigi_diller = ["Python"])

yazilimci1.bilgileri_goster()

yazilimci1.tecrube_artisi(3)
yazilimci1.zam(3000)
yazilimci1.dil_ekleme("Java","C","C++")

yazilimci1.bilgileri_goster()



class calisanlar():
    def __init__(self,isim,soyisim,maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
    def zam(self,miktar):
        self.maas += miktar
    def bilgileri_goster(self):
        print(f"İsim = {self.isim} \n Soyisim = {self.soyisim} \n Maaş = {self.maas} ")


class halkla_iliskiler(calisanlar):
    def __init__(self,isim,soyisim,maas,gorusulen_kisi_sayisi = 0,randevu_sayisi = 0):
        super().__init__(isim,soyisim,maas)
        self.gorusulen_kisi_sayisi = gorusulen_kisi_sayisi
        self.randevu_sayisi = randevu_sayisi
    def randevu_talebi(self,kisi):
        self.randevu_sayisi += kisi
    def gorusulen_ekleme(self,kisi):
        self.gorusulen_kisi_sayisi += kisi
    def bilgileri_goster(self):
        print(f"İsim = {self.isim} \n Soyisim = {self.soyisim} \n Maaş = {self.maas} \n Görüşülen kişi sayısı = {self.gorusulen_kisi_sayisi} \n Randevu Sayısı = {self.randevu_sayisi}")

halkla_iliskiler_1 = halkla_iliskiler(isim = "Metehan", soyisim = "Saribas", maas = 30000)

halkla_iliskiler_1.bilgileri_goster()

halkla_iliskiler_1.randevu_talebi(3)
halkla_iliskiler_1.gorusulen_ekleme(2)

halkla_iliskiler_1.bilgileri_goster()

halkla_iliskiler_1.zam(3000)

halkla_iliskiler_1.bilgileri_goster()


import time

class bilgisayar():
    def __init__(self,calisma_durumu = "kapalı",oyunlar = ["RDR 2"],filmler = [], sarj = 30):
        self.calisma_durumu = calisma_durumu
        self.oyunlar = oyunlar
        self.filmer = filmler
        self.sarj = sarj
    def acma(self):
        if self.calisma_durumu == "kapalı":
            print("Bilgisayarınız Açıldı")
            self.calisma_durumu = "açık"
        elif self.calisma_durumu == "açık":
            print("Bilgisayarınız zaten açık")
    def kapama(self):
        print("Bilgisayarınız Kapandı")
        self.calisma_durumu = "kapalı"
    def oyun_indirme(self,*oyun):
        oyun = input("İndirmek istediğiniz oyunu yazın..")
        self.oyunlar.append(oyun)
        print("Oyun indirildi...")
    def oyun_goruntuleme(self):
        print(f"Oyunlar : {self.oyunlar}")
    def film_indirme(self,*film):
        film = input("İndirmek istediğiniz filmi giriniz")
        self.filmer.append(film)
        print("Film indirildi")
    def film_goruntuleme(self):
        print(f"Filmler : {self.filmer}")
    def sarj_goruntuleme(self):
        print(f"Şarj {self.sarj}")
    def sarj_tak(self):
        while self.sarj <= 100:
            print(f"Şarj %{self.sarj}")
            time.sleep(2)
            self.sarj += 1
            if self.sarj == 100:
                break
    def sarj_cıkar(self):
        while self.sarj <= 100:
            print(f"Şarj %{self.sarj}")
            time.sleep(3)
            self.sarj -= 1
            if self.sarj == 0:
                self.calisma_durumu = "Kapalı"
                print("Şarj bitti bilgisayarınız kapandı")
                break
    def genel_goruntuleme(self):
        print(f"Çalışma durumu : {self.calisma_durumu} \n Oyunlar : {self.oyunlar} \n Filmler : {self.filmer} ")

monster = bilgisayar()

print(" ***** Bilgisayar Programı *****"
      "\n1. Bilgisayarı Açma"
      "\n2. Bilgisayarı Kapama"
      "\n3. Oyunları Görüntüleme"
      "\n4. Oyun İndirme"
      "\n5. Filmleri Görüntüleme"
      "\n6. Film indirme"
      "\n7. Şarj Durumunu Görüntüleme"
      "\n8. Şarja Takma"
      "\n9. Şarjdan Çıkarma"
      "\n10. Genel Durum Öğrenme"
      "\nq. Programdan çıkma"
      "\nYapmak istediğiniz işlemin kodunu girin..."
       )

while True:
    islem = input("Kaç numaralı işlemei yapmak istiyorsunuz ?")
    if islem == "1":
        monster.acma()
    elif monster.calisma_durumu == "açık":
        if islem == "1":
            print("Bilgisayarınız zaten açık")
        if islem == "2":
            monster.kapama()
        elif islem == "3":
            monster.oyun_goruntuleme()
        elif islem == "4":
            monster.oyun_indirme()
        elif islem == "5":
            monster.film_goruntuleme()
        elif islem == "6":
            monster.film_indirme()
        elif islem == "7":
            monster.sarj_goruntuleme()
        elif islem == "8":
            monster.sarj_tak()
        elif islem == "9":
            monster.sarj_cıkar()
        elif islem == "10":
            monster.genel_goruntuleme()
        elif islem == "q":
            print("Güle Güle")
            break
        else:
            print("Geçersiz bir işlem girdiniz, tekrar deneyin")
    elif monster.calisma_durumu == "kapalı":
        print("Bilgisayarınız kapalı, ilk olarak açın sonrasında diğer işlemleri yapabilirsiniz...")


"""""


















