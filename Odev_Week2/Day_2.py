import Human

faiz=1.59
vade="36"
krediAdi="İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade) + 12)
#print(int(krediAdi))
faiz=str(faiz)
print(type(faiz))

vade=int(input("Lütfen istediğiniz vade sayısını giriniz : "))
print(type(vade))
vade=vade + 12

#string interpolation
#Seçtiğiniz vade sonucu ortaya çıkan vade:
print("#Seçtiğiniz vade sonucu ortaya çıkan vade : " + str(vade))
print("#Seçtiğiniz vade sonucu ortaya çıkan vade : {vadeSayisi}".format(vadeSayisi=vade))
print(f"#Seçtiğiniz vade sonucu ortaya çıkan vade : {vade}")

isim=input("İsminizi Giriniz : ")
metin="Merhaba {name}".format(name=isim)
print(metin)

# f-string
metin=f"Hoşgeldiniz {1+1}"
print(metin)

dizi=["İhtiyaç Kredisi",10,5.2,True]
print(dizi)

krediler=["İhtiyaç Kredisi","Taşıt Kredisi","Konut Kredisi"]
print(type(krediler))

print(krediler[0])

print(len(krediler)) #length

#print(krediler[3]) => Hata verir

krediler.append("Özel Kredi")
print(krediler)

krediler.append("X Kredisi")
print(krediler)

krediler.pop(0)
print(krediler)

krediler.remove("Taşıt Kredisi")
print(krediler)

krediler.extend(["Y kredisi","Z kredisi"])
print(krediler)

#for
# i=0 i<10

for i in range(10):
    print("xx")
    print(i)

print("*"*10)

for i in range(5,11):
    print(i)

print("*"*10)

for i in range(0,51,10):
    print(i)

print("*"*10)

#for i in range(0.1,0.5):
#   print(i)

krediler=["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]

for kredi in krediler:
    print(kredi)

print("*"*10)

for i in range(len(krediler)):
    print(krediler[i])

print("*"*10)

#Sonsuz döngü
i=0
while i < 10:
    print("x")
    i += 1
print("y")

print("*"*10)

while True:
    print("X")
    break

print("*"*10)

i=0
while i < len(krediler):
    i += 1
    print(i)
    print(krediler[i])
    if krediler[i] == "Konut Kredisi":
        break

# Fonksiyonlar
fiyat = 100
indirim = 20

#definition define
def calculate():
    print(100-20)

def calculateWithParams(fiyat,indirim):
    print(fiyat-indirim)

def sayHello(name):
    print(f"Merhaba {name}")

calculate()
calculateWithParams(50,10)
calculateWithParams(100,30)

sayHello("Halit")
sayHello("Arif")
sayHello("Mevlüt")

def calculateAndReturn(price,discount):
    return price-discount

yeniFiyat=calculateAndReturn(200,50)
print(yeniFiyat + 10)

#void
def calculatePrice(price,discount):
    print(price-discount)

def calculatePriceAndReturn(price,discount):
    return price-discount

print("*"*10)
#fonk1=calculatePrice(100-50)
fonk2=calculatePriceAndReturn(300,100)
#print(f"154. satır: {fonk1+100}")
print(f"160. satır: {fonk2+100}")
print("*"*10)

#instance => örnek
human1=Human("Melike")
#human1.name="Nur"
human1.talk("Merhaba")
human1.walk()
print(human1)

human2=Human("Ahmet")
#human2.name="Cem"
human2.talk("Selam")
human2.walk()
print(human2)
