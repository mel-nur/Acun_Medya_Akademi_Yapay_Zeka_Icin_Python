# Inheritance (Kalıtım-Miras)

class Vehicle:
    def __init__(self,model):
        self.model=model
    def start(self): #classın kendisini methoda gönderme biçimi
        print(f"{self.model} araç çalıştırılıyor...")

# class => sınıf
class Car():
    # özellikler, fonksiyonlar
    # model=""
    # constructor - yapıcı blok
    # kapsülleme - encapsulation

    def __init__(self,model,year=2025):
        self._model=model
        self.year=year
        print("Bir car nesnesi oluşturuluyor")

    # self => classın kendisini ifade eder
    # class fonksiyonları ilk parametre olarak zorunlu "self" parametresi alırlar.

    def start(self): #classın kendisini methoda gönderme biçimi
        print(f"{self._model} {self.year} Araba çalıştırılıyor...")

    def increaseSpeed(self,speed):
        print(f"{self._model} arabasının hızı {speed} kadar artırılıyor.")

    def set_model(self,model): #setter
        if len(model) < 2:
            print("Model 2 haneden kısa olamaz")
            return
        self._model=model


    def get_model(self):
        return self._model

araba=Car("Toyota") # Car kalıbından üretilmiş bir nesne (instance)
# araba._model = "Nissan" YAPAMAZSIN!  -getter -setter
araba.set_model("N")
print(araba.get_model()) # _model değerini okumak
araba.start()
araba.increaseSpeed(50)
araba2 = Car("Mercedes",2024)
araba2.start()
araba2.increaseSpeed(100)

class Truck(Vehicle):
    def __init__(self,model,capacity):
        super().__init__(model)
        self.capacity=capacity

    def load(self):
        print(f"{self.model} kamyonetine yük yükleniyor...")

truck1=Truck("Scania",1000)
truck1.start()
truck1.load()


