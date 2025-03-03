#modules
#paket yönetimi
#self => this

class Human:
    #name="Melike"
    #built-in
    #constructor
    #initialize
    def __init__(self,name):
        self.name=name
        print("Bir human instance üretildi")
    def __str__(self):
        return f"STR Fonksiyonundan dönen değer : {self.name}"
    def talk(self,sentence):
        name="Beyza"
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} is walking...")

