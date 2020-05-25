class Soru():
    def __init__(self,yazi,secimler,cevap):
        self.yazi = yazi
        self.secimler = secimler
        self.cevap = cevap

    def cevabiKontrolEt(self, cevap):
        return self.cevap == cevap

class BilgiYarismasi():
    def __init__(self,sorular):
        self.sorular = sorular
        self.puan = 0
        self.soruIndeks = 0

    def soruGetir(self):
        return self.sorular[self.soruIndeks]

    def soruyuGoster(self):
        soru = self.soruGetir()
        print(f"Soru {self.soruIndeks + 1} : {soru.yazi}")

        for q in soru.secimler:
            print("-"+ q)

        cevap = input("Cevap: ")
        self.tahmin(cevap)
        self.soruyuYukle()

    def tahmin(self, cevap):
        soru = self.soruGetir()

        if soru.cevabiKontrolEt(cevap):
            self.puan += 1
        self.soruIndeks += 1

    def soruyuYukle(self):
        if len(self.sorular) == self.soruIndeks:
            self.puaniGoster()
        else:
            self.ilerlemeDurumunuGoster()
            self.soruyuGoster()

    def puaniGoster(self):
        print("Puan: ",self.puan)

    def ilerlemeDurumunuGoster(self):
        toplamSoru = len(self.sorular)
        sorunumara  = self.soruIndeks + 1

        if sorunumara > toplamSoru:
            print("Bilgi Yarismasi bitti")
        else:
            print(f"Soru {sorunumara} of {toplamSoru}".center(100,"*"))

q1 = Soru('en iyi programlama dili hangisidir ?', ['C#','python','javascript','java'], 'python')
q2 = Soru('en popüler programlama dili hangisidir ?', ['python','javascript','C#','java'], 'python')
q3 = Soru('en çok kazandıran programlama dili hangisidir ?', ['C#','javascript','java','python'], 'python')
q4 = Soru('en çok sevilen programlama dili hangisidir ?', ['C#','javascript','java','python'], 'python')
q5 = Soru('en kolay programlama dili hangisidir ?', ['C#','javascript','java','python'], 'python')

sorular = [q1,q2,q3,q4,q5]

bilgiYarismasi = BilgiYarismasi(sorular)

bilgiYarismasi.soruyuYukle()