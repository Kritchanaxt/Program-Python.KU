
#? Polymorphism

class Cat:
    def sound(self):
        print("Cat meows, meows")


class Dog:
    def sound(self):
        print("Dog barks, woof")


def animal_sound(animal):
    animal.sound()

cat = Cat()
dog = Dog()

animal_sound(cat)
animal_sound(dog)