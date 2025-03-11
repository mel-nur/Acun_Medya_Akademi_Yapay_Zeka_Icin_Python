'''
Ödev: Listeler ve Tuple'lar
Konu: Listeler, Tuple'lar, listelerde döngü.
Görev:
=>Kullanıcıdan 5 adet sayı alarak bir listeye ekleyin ve bu listenin toplamını, ortalamasını, en büyük ve en küçük elemanını bulun.
=>Kullanıcıdan aldığı kelimeleri bir listeye ekleyerek ters sıralayan bir program yazın.
=>Bir liste içindeki tekrar eden elemanları kaldıran bir program yazın.
'''

liste=[]
for i in range(1,6):
    sayi=int(input(f"{i}. Sayıyı Giriniz : "))
    liste.append(sayi)

toplam=sum(liste)
ortalama=toplam/5
maksimum=max(liste)
minimum=min(liste)
print("Toplam : ",toplam)
print("Ortalama : ",ortalama)
print("Maksimum Sayı : ",maksimum)
print("Minimum Sayı : ",minimum)


kelimeler=[]
kelime=input("Lütfen Kelime Giriniz (Çıkmak için q) : ")
while(kelime!="q"):
    kelimeler.append(kelime)
    kelime = input("Lütfen Kelime Giriniz (Çıkmak için q) : ")
kelimeler.reverse()
print(kelimeler)


def tekrarlayan_silme(liste):
    print(list(set(liste)))

liste=["melike","melike","nur","nur","çotak",5,5,7,4,10]
tekrarlayan_silme(liste)