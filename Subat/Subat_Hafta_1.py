'''
Ödev: Fonksiyonlar
Konu: Fonksiyonlar, parametreler, return.
Görev:
=>Girilen iki sayının toplamını, farkını, çarpımını ve bölümünü bulan bir hesap makinesi fonksiyonu yazın.
=>Kullanıcının girdiği bir kelimenin palindrom olup olmadığını kontrol eden bir fonksiyon yazın.
Örnek: "kek" -> palindrom, "masa" -> değil
=>Kullanıcının yaşını girerek kaç yıl sonra 100 yaşına ulaşacağını hesaplayan bir fonksiyon yazın.
'''


def hesap_makinesi():
    sayi1 = int(input("1. Sayıyı Giriniz : "))
    sayi2 = int(input("2. Sayıyı Giriniz : "))
    print(f"{sayi1} + {sayi2} = ", sayi1+sayi2)
    print(f"{sayi1} - {sayi2} = ", sayi1-sayi2)
    print(f"{sayi1} * {sayi2} = ", sayi1*sayi2)
    if (sayi2==0):
        print("0'a Bölünemez")
    else:
        print(f"{sayi1} / {sayi2} = ", sayi1/sayi2)


def palindrom_kontrol():
    kelime = input("Kelime Giriniz : ")
    kelime_ters=kelime[::-1]
    if (kelime==kelime_ters):
        print(f"{kelime} => palindrom")
    else:
        print(f"{kelime} => palindrom değil")


def yas_hesaplama():
    yas = int(input("Lütfen Yaşınızı Giriniz : "))
    print(f"{100-yas} yıl sonra 100 yaşına ulaşacaksınız.")