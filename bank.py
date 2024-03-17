class BankHesabi:
    def _init_(self, isim, balans=0):
        self.isim = isim
        self.balans = balans

    def pul_artır(self, məbləğ):
        self.balans +=məbləğ
        print(f"{məbləğ} TL yatırıldı. Yeni balans: {self.balans} ")

    def pul_cək(self, məbləğ):
        if self.balans >= məbləğ:
            self.balans -= məbləğ
            print(f"{məbləğ} TL çekildi. Yeni balans: {self.balans} ")
        else:
            print("Yetersiz balans!")

    def hesabi_sifirla(self):
        self.balans = 0
        print("Hesap sıfırlandı.")

    def _str_(self):
        return f"{self.isim} hesabı, balans: {self.balans} TL"


# Hesap oluşturma
hesap = BankHesabi("", 1000)

# Paul yatırma
hesap.pul_artır(500)

# Pul çekme
hesap.pul_cek(200)

# Hesabı sıfırlama
hesap.hesabi_sifirla()

# Yeniden hesap oluşturma
yeniden_hesap_oluşdur = BankHesabi("Ali")
print(yeniden_hesap_oluşdur)