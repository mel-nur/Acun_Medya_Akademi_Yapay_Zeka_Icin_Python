'''
Ödev: Koşullu İfadeler (if-else)
Konu: Karar yapıları (if-elif-else).
Görev:
=>Kullanıcının girdiği bir sayının tek mi çift mi olduğunu bulan bir Python programı yazın.
=>Kullanıcının notunu alarak aşağıdaki not sistemine göre harf notunu hesaplayın:
90-100 -> A
80-89  -> B
70-79  -> C
60-69  -> D
0-59   -> F
=>Kullanıcının yaşına göre hangi yaş grubunda olduğunu bulan bir program yazın:
0-12 yaş: Çocuk
13-19 yaş: Genç
20-59 yaş: Yetişkin
60 ve üzeri: Yaşlı
'''

#Tek mi çift mi
sayi=int(input("Bir Sayı Giriniz : "))

if (sayi>=0):
    if(sayi%2==0):
        print(f"{sayi} çift")
    else:
        print(f"{sayi} tek")
else:
    print("Negatif sayılar da teklik çiftlik aranmaz.")



#Harf notu hesaplama
girilenNot=int(input("Lütfen Aldığınız Notu Giriniz : "))

if (girilenNot>=0 and girilenNot<=100):
    if (girilenNot<=100 and girilenNot>=90):
        print(f"Harf Notunuz A. Aldığınız Not : {girilenNot}")
    elif (girilenNot<=89 and girilenNot>=80):
        print(f"Harf Notunuz B. Aldığınız Not : {girilenNot}")
    elif (girilenNot<=79 and girilenNot>=70):
        print(f"Harf Notunuz C. Aldığınız Not : {girilenNot}")
    elif (girilenNot<=69 and girilenNot>=60):
        print(f"Harf Notunuz D. Aldığınız Not : {girilenNot}")
    elif (girilenNot<=59 and girilenNot>=0):
        print(f"Harf Notunuz F. Aldığınız Not : {girilenNot}")
else:
    print("Geçersiz Not Girdiniz")



#Yaş grubu bulma
yas=int(input("Yaşınızı Giriniz : "))
if yas>=0:
    if (yas<=12 and yas>=0):
        print("Çocuk")
    elif (yas<=19 and yas>=13):
        print("Genç")
    elif (yas<=59 and yas>=20):
        print("Yetişkin")
    elif (yas>=60):
        print("Yaşlı")
else:
    print("Geçersiz yaş girdiniz")


