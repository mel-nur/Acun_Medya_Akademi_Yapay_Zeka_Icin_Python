#entrypoint

#otomasyon programlama => e-ticaret, e-devlet

#yapay zeka =>

#değişkenler

#python dili type-safe değildir

#değişken tipleri

number = 10 #integer,int
print(number)

name="Halit" #string, String
print(name)
print(type(name))

#python değişken tipinin değişmesine izin veriyor
name = 20
print(name)
print(type(name))

#Değişken isimleri rakamla başlayamaz, ya harf ya da _ile başlamalı.
#Özel keywordler olamaz (def,while,if gib)

_age=25
print(_age)

#işlem => operatörler
print("*"*10)
print(25+50) #75
print(50-25) #25
print(100/2) #double,float => ondalıklı sayı  50.0
print(50*2) #100
print(100//2) #50
print(103//2) #51
print(101%2) #mod 1
print(5**3) #125

is_active=True

#Karşılaştırma operatörleri
print("Karşılaştırma : ")
print(1 == 1) #True
print(1 == 2) #False
print(1 != 2) #True
print(1 > 2) #False
print(1 >= 2) #False
print(1 < 2) #True
print(1 <= 2) #True
#Boolean, bool

#Mantıksal operatörleer => and,or,not
print("Mantıksal : ")
print("AND")
print(1 == 1 and 10 == 10) #True and True => True
print(1 == 1 and 10 == 11) #True and False => False
print(1 == 2 and 10 == 11) #False and False => False
print("OR")
print(1 == 1 or 10 == 10) #True or True => True
print(1 == 1 or 10 == 11) #True or False => True
print(1 == 2 or 10 == 11) #False or False => False

print("*"*10)
print(1==1 and 5==5 or 25>10 and 50<100) #True and True or True and True => True
print("*"*10)
print(not ( (( (5>3 and 5==5) and (3<5 or 5>3) ) and 3==3) or 5 < 3)) #False
print(not 1==1) #not True => False

#Atama operatörleri
print("Atama")
x=5

x+=3 #x=x+3
x-=2
x*=5
x/=1 #float
#x=x//5
x//=5 #float
print(x)
#**,%,//,/


students = ["Beyzanur","Ali","Yusuf",10,True,5.0]
students.append("Eda Nur")
print(students)
students.pop()
print(students)
print(students[3])

a=5
b=a
b+=10
print(a)
print(b)
#Value type-Reference Type => Immutable - Mutable typelar

a_list=["Eleman 1","Eleman 2"]
b_list = a_list
b_list.append("Eleman 3") # @123ABC
print(a_list)
print(b_list)