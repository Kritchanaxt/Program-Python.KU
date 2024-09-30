
#* 4.

class Person:
  def __init__(self, firstname='Supasima', lastname='Rungrote', age=50, country='Finland', city='Helsinki'):
    self.firstname = firstname
    self.lastname = lastname
    self.age = age
    self.country = country
    self.city = city

  def person_info(self):
    return f'{self.firstname} {self.lastname} is {self.age} years old. She lives in {self.country}, {self.city}'

p1 = Person()
print(p1.person_info())
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
