'''
Ödev: Değişkenler ve Veri Tipleri
Konu: Değişkenler, veri tipleri (int, float, string, boolean), kullanıcıdan veri alma.
Görev:
=>Kullanıcıdan adını, yaşını ve doğum yılını alarak ekrana aşağıdaki gibi yazdıran bir Python programı yazın:
Merhaba Ali! 25 yaşındasın ve 1998 yılında doğmuşsun.
=>Kullanıcıdan iki sayı alarak bu sayıların toplamını, farkını, çarpımını ve bölümünü ekrana yazdırın.
'''

ad=input("Adınızı Giriniz : ")
yas=int(input("Yaşınızı Giriniz : "))
dogumYil=int(input("Doğum Yılınızı Giriniz : "))

text=f"Merhaba {ad}! {yas} yaşındasın ve {dogumYil} yılında doğmuşsun."
print(text)

sayi1=int(input("1. Sayıyı Giriniz : "))
sayi2=int(input("2. Sayıyı Giriniz : "))

print(f"{sayi1} ve {sayi2} Toplamı : ", sayi1+sayi2)
print(f"{sayi1} ve {sayi2} Farkı : ", sayi1-sayi2)
print(f"{sayi1} ve {sayi2} Çarpımı : ", sayi1*sayi2)
print(f"{sayi1} ve {sayi2} Bölümü : ", sayi1/sayi2)