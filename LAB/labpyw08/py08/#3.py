
#* 3.

class Person:
  def __init__(self, name, lastname, age, country, city):
    self.name = name
    self.lastname = lastname
    self.age = age
    self.country = country
    self.city = city

  def person_info(self):
    return f'{self.name} {self.lastname} is {self.age} years old. She lives in {self.country}, {self.city}'

p = Person('Supasima' , 'Tongma' , 21 , 'Thailand' , 'Sriracha')
# print(p.name,p.lastname,p.age,p.country,p.city)
print(p.person_info())
