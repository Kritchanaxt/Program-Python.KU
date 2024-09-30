
#* Simple-Inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)  #? เรียกใช้เมธอดของคลาสแม่.
    
    def speak(self):
        print(f"{self.name} meows.")

cat_name = input("Name Cat: ")
cat = Cat(cat_name)
# cat = Cat("BukKuy")
cat.speak()
