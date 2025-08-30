# Araba Yıllık Bakım Sistemi
from tabulate import tabulate

class Araba:
    def __init__(self, model, marka, yil, plaka):
        self.model = model
        self.marka = marka
        self.yil = yil
        self.plaka = plaka
        self.bakim_kayitlari = []  # Bu arabaya ait bakım kayıtlarını tutar

    def bakim_ekle(self, bakim):
        self.bakim_kayitlari.append(bakim)

    def bakimlari_tablo_goster(self):
        if not self.bakim_kayitlari:
            print(f"{self.plaka} plakalı arabanın bakım kaydı yok.")
        else:
            tablo = [[b.tarih, b.bakim_turu, b.aciklama, f"{b.maliyet} TL"] for b in self.bakim_kayitlari]
            print(tabulate(tablo, headers=["Tarih", "Bakım Türü", "Açıklama", "Maliyet"]))

    def __str__(self):
        return f"{self.marka} {self.model} ({self.yil}) - Plaka: {self.plaka}"


class Bakim:
    def __init__(self, bakim_turu, tarih, aciklama, maliyet):
        self.bakim_turu = bakim_turu
        self.tarih = tarih
        self.aciklama = aciklama
        self.maliyet = maliyet

    def __str__(self):
        return f"{self.tarih} - {self.bakim_turu} - Açıklama: {self.aciklama} - Maliyet: {self.maliyet} TL"


class Sahip:
    def __init__(self, ad, telefon, adres):
        self.ad = ad
        self.telefon = telefon
        self.adres = adres
        self.arabalar = []  # Bu sahibin arabalarını tutar

    def araba_ekle(self, araba):
        self.arabalar.append(araba)

    def arabalar_listele(self):
        if not self.arabalar:
            print(f"{self.ad} henüz sisteme araba eklemedi.")
        else:
            print(f"{self.ad} ait arabalar:")
            for i, araba in enumerate(self.arabalar, 1):
                print(f"{i}. {araba}")

    def __str__(self):
        return f"Sahip: {self.ad}, Telefon: {self.telefon}, Adres: {self.adres}"


def araba_bul(plaka, sahip):
    for araba in sahip.arabalar:
        if araba.plaka == plaka:
            return araba
    return None


def toplam_bakim_maliyeti(araba):
    toplam = sum(b.maliyet for b in araba.bakim_kayitlari)
    print(f"{araba.plaka} plakalı arabanın toplam bakım maliyeti: {toplam} TL")


def menu():
    print("--- Araba Yıllık Bakım Sistemi ---")
    sahip = Sahip("Ali Yılmaz", "123-456-7890", "Ankara")  # Varsayılan sahip

    while True:
        print("\n1. Sahip bilgilerini göster")
        print("2. Sahibe araba ekle")
        print("3. Arabaların bakım kayıtlarını listele")
        print("4. Arabaya bakım ekle")
        print("5. Toplam bakım maliyeti hesapla")
        print("6. Plakaya göre araba ara")
        print("7. Çıkış")

        secim = input("Seçiminizi yapın: ")

        if secim == "1":
            print(sahip)
            sahip.arabalar_listele()

        elif secim == "2":
            model = input("Araba modeli: ")
            marka = input("Araba markası: ")
            yil = int(input("Araba yılı: "))
            plaka = input("Plaka numarası: ")
            yeni_araba = Araba(model, marka, yil, plaka)
            sahip.araba_ekle(yeni_araba)
            print("Araba başarıyla eklendi!")

        elif secim == "3":
            for araba in sahip.arabalar:
                print(f"\n{araba}")
                araba.bakimlari_tablo_goster()

        elif secim == "4":
            sahip.arabalar_listele()
            araba_secim = int(input("Hangi arabaya bakım eklemek istiyorsunuz? (Numara girin): ")) - 1
            if 0 <= araba_secim < len(sahip.arabalar):
                bakim_turu = input("Bakım türü: ")
                tarih = input("Bakım tarihi (YYYY-AA-GG): ")
                aciklama = input("Bakım açıklaması: ")
                maliyet = float(input("Bakım maliyeti: "))
                yeni_bakim = Bakim(bakim_turu, tarih, aciklama, maliyet)
                sahip.arabalar[araba_secim].bakim_ekle(yeni_bakim)
                print("Bakım başarıyla eklendi!")
            else:
                print("Geçersiz seçim.")

        elif secim == "5":
            sahip.arabalar_listele()
            araba_secim = int(input("Hangi arabanın toplam bakım maliyetini hesaplamak istiyorsunuz? (Numara girin): ")) - 1
            if 0 <= araba_secim < len(sahip.arabalar):
                toplam_bakim_maliyeti(sahip.arabalar[araba_secim])
            else:
                print("Geçersiz seçim.")

        elif secim == "6":
            plaka = input("Aranacak plaka numarasını girin: ")
            bulunan_araba = araba_bul(plaka, sahip)
            if bulunan_araba:
                print(bulunan_araba)
                bulunan_araba.bakimlari_tablo_goster()
            else:
                print("Bu plakaya ait araba bulunamadı.")

        elif secim == "7":
            print("Çıkış yapılıyor...")
            break

        else:
            print("Geçersiz seçim, tekrar deneyin.")


# Programı başlat
menu()
