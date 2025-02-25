'''
1. Asal Sayı Kontrolü
Bir sayının asal sayı olup olmadığını kontrol eden bir Python fonksiyonu yazın.

✅ Kurallar:
Asal sayı, sadece kendisine ve 1’e bölünebilen 1’den büyük pozitif sayılardır.
Fonksiyon, kullanıcıdan bir sayı almalı ve asal olup olmadığını kontrol etmelidir.
'''

def asal_sayi_mi(sayi):
    asal_mi=True
    if sayi < 2:
        asal_mi = False

    for i in range(2,sayi):
        if sayi % i == 0:
            asal_mi = False
            break

    if asal_mi:
        return f"{sayi} asal sayıdır."
    else:
        return f"{sayi} asal sayı değildir."

input_sayi = int(input("Lütfen bir sayı giriniz : "))
cikti=asal_sayi_mi(input_sayi)
print(cikti)