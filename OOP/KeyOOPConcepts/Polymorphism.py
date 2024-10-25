
class Cat:
   def sound(self):
       print("Cat meows, meows")

class Dog:
   def sound(self):
       print("Dog barks, woof, woof")

   # Function that can accept Animal objects, both cats and dogs
def animal_sound(animal):
    animal.sound()

# Create objects from Cat and Dog classes
cat = Cat()
dog = Dog()

animal_sound(cat) # Cat meows
animal_sound(dog) # Dog barks