'''
2. Basit Hesap Makinesi
Kullanıcıdan iki sayı ve bir işlem türü alarak sonucu döndüren bir fonksiyon yazın.

✅ Kurallar:
Kullanıcı +, -, *, / işlemlerinden birini seçmelidir.
Bölme işleminde, ikinci sayı 0 olursa "Bölme işlemi için ikinci sayı 0 olamaz!" şeklinde uyarı verin.
Kullanıcı geçersiz bir işlem girerse, "Geçersiz işlem türü!" mesajı gösterin.
'''

def hesap_makinesi(sayi1,sayi2,islem):
    if islem == "+":
        return f"{sayi1} + {sayi2} = {sayi1+sayi2}"
    elif islem == "-":
        return f"{sayi1} + {sayi2} = {sayi1-sayi2}"
    elif islem == "*":
        return f"{sayi1} + {sayi2} = {sayi1*sayi2}"
    elif islem == "/":
        if sayi2 == 0:
            return "Bölme işlemi için ikinci sayı 0 olamaz!"
        return f"{sayi1} + {sayi2} = {sayi1/sayi2}"
    else:
        return "Geçersiz işlem türü!"

sayi1 = int(input("Sayi1 Giriniz : "))
sayi2 = int(input("Sayi2 Giriniz : "))
islem = input("Yapmak istediğiniz işlemi seçiniz(+,-,*,/) : ")
sonuc = hesap_makinesi(sayi1,sayi2,islem)
print(sonuc)