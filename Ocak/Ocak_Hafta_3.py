'''
Ödev: Döngüler (for & while)
Konu: For ve while döngüleri.
Görev:
=>1’den 100’e kadar olan sayıları ekrana yazdırın.
=>1’den 100’e kadar sadece çift sayıları ekrana yazdıran bir program yazın.
=>Kullanıcıdan bir sayı alıp, bu sayının faktöriyelini hesaplayan bir program yazın.
Örnek: 5! = 5 * 4 * 3 * 2 * 1 = 120
=>1’den 100’e kadar olan tüm asal sayıları bulan bir program yazın.
'''

print("1’den 100’e kadar olan sayıları ekrana yazdırın")
for i in range(1,101):
    print(i,end="  ")
print()


print("1’den 100’e kadar sadece çift sayıları ekrana yazdırın")
for i in range(2,101,2):
    print(i,end="  ")
print()


for i in range(1,101):
    if(i%2==0):
        print(i,end="  ")
print()


print("Kullanıcıdan bir sayı alıp, bu sayının faktöriyelini hesaplayan bir program")
sayi=int(input("Faktöriyelini almak istediğiniz sayıyı giriniz : "))
faktöriyel=1
for i in range(1,sayi+1):
    faktöriyel*=i
print(f"{sayi} Faktöriyel = {faktöriyel}")


print("1’den 100’e kadar olan tüm asal sayıları bulan bir program")
for i in range(2,101):
    asalMi=True
    for j in range(2,i):
        if (i%j==0):
            asalMi=False
            break
    if asalMi:
        print(i)

