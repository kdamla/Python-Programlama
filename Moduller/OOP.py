import random
import time

class Kumanda():

    def __init__(self, tvDurum = "Kapalı", tvSes = 0, kanalListesi = ["Trt"], kanal = "Trt"):
        self.tvDurum = tvDurum
        self.tvSes = tvSes
        self.kanalListesi = kanalListesi
        self.kanal = kanal

    def tvAc(self):
        if self.tvDurum == "Açık":
            print("TV zaten açık")
        else:
            print("TV Açılıyor")
            self.tvDurum = "Açık"
    def tvKapat(self):
        if self.tvDurum == "Kapalı":
            print("TV zaten kapalı")
        else:
            print("TV kapanıyor")
            self.tvDurum = "Kapalı"
    def sesAyarlari(self):

        cevap = None
        while True:
            cevap = input("Sesi azalt: - \n Sesi artır + \n Çıkış: *")

            if cevap == "-":
                if self.tvSes != 0:
                    self.tvSes -= 1
                    print("Ses:",self.tvSes)
            elif cevap == "+":
                if self.tvSes != 31:
                    self.tvSes += 1
                    print("Ses:", self.tvSes)
            elif cevap == "*":
                print("Ses güncellendi.", self.tvSes)
                break
            else:
                print("Yanlış giriş yaptınız")
    def kanalEkle(self, kanal):
        print("Kanal ekleniyor")
        time.sleep(1)
        self.kanalListesi.append(kanal)
        print("Kanal eklendi")
    def rastgeleKanal(self):
        rastgele = random.randint(0,len(self.kanalListesi)-1)
        self.kanal = self.kanalListesi[rastgele]
        print("Şuanki kanal", self.kanal)
    def __len__(self):
        return len(self.kanalListesi)
    def __str__(self):
        return "Tv durumu: {}\nTv Ses:{}\nKanal listesi:{}\nŞuanki kanal:{}".format(self.tvDurum, self.tvSes, self.kanalListesi, self.kanal)


print("TV Uygulaması")
"""
1 TV aç
2 TV Kapat
3 Ses
4 Kanal Ekle
5 Kanal sayısı
6 Rastgele Kanal
7 TV Bilgileri
Çıkmak için q'ya basın
"""

islem = None
kumanda = Kumanda()
while True:
    islem = input("İşlemi seçiniz")

    if islem == "q":
        print("Program sonlandırılıyor")
        break
    elif islem == "1":
        kumanda.tvAc()
    elif islem == "2":
        kumanda.tvKapat()
    elif islem == "3":
        kumanda.sesAyarlari()
    elif islem == "4":
        kanalIsimleri = input("Kanal isimlerini virgülle giriniz")
        kanalListesi = kanalIsimleri.split(",")

        for eklenecekler in kanalListesi:
            kumanda.kanalEkle(eklenecekler)
    elif islem == "5":
        print("Kanal sayısı:", len(kumanda.kanalListesi))
    elif islem == "6":
        kumanda.rastgeleKanal()
    elif islem == "7":
        print(kumanda)
    else:
        print("Yanlış giriş")