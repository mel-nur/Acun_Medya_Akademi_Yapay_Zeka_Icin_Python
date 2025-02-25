# Döngüler => Programda tekrarlayan işlevleri yerine getirmek için.
from Week2.Example1 import students

# for-while
print("***** 22.02.2025 *****")

# for => genellikle belirli bir koleksiyon(list.vb) veya aralık üzerinde iterasyon için kullanılır.
# aynı işlemi 5 kere yapmak istiyorsanız
# iteration, index
# python da scopeları(kapsam) indentation belirler

for i in range(5):
    print(i) #indentation, indent
print("Merhaba")

students = ["Ahmet","Ali","Ata","Barış"]
#koleksiyonlar
for student in students:
    print("Öğrenci : " + student)

text = "Merhaba" #string döngüsü, harf harf (char) iterasyon yapar.
for letter in text:
    print(letter)

#block, scope
for i in range(5,10):
    forVariable=5
    print(i)

print("X")
print(forVariable) #main scope
print("*"*10)

for i in range(5,20,2):
    print(forVariable) #4. for scope
    print(i)

# while => infinite loop (sonsuz döngü) oluşturma riskine sahiptir
# şart ile çalışır (koşul)
# while True: #ctrl+c => sonsuz döngüyü kır
    #print("Durum geçerli")

user_input=input("Bir değer seçin (çıkmak için q) : ")
while user_input != "q": #true-false
    print("Girdiğiniz değer " + user_input)
    user_input = input("Bir değer seçin (çıkmak için q) : ")

x = 10
while x <= 20:
    print(x)
    x += 1

# Döngülerdeki keywordler
# break => döngüyü manuel olarak kırmaya yarar.
for i in range(50):
    if i > 20:
        break
    print(i)

# continue => döngüde belirli bir şartta o iterasyonu atlamaya yarar
for i in range(50):
    if i == 25:
        continue
    print(i)

# şart-koşullu ifadeler
# program da belirli bir karara göre işlem yapmak

age=18
if age >= 18:
    print("Reşitsiniz")
elif age == 18:
    print("Sınırdan reşitsiniz")
else: # yukarıdaki şart(lar) sağlanmadığında çalışacak blok
    print("Reşit değilsiniz")

logging_enabled=False
if logging_enabled == True:
    print("Loglanıyor...")