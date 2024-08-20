
#* 5.

class Person:
  def __init__(self, firstname='Supasima', lastname='Rungrote', age=50, country='Finland', city='Helsinki'):
    self.firstname = firstname
    self.lastname = lastname
    self.age = age
    self.country = country
    self.city = city
    self.skills = []

  def person_info(self):
    return f'{self.firstname} {self.lastname} is {self.age} years old. She lives in {self.country}, {self.city}'

  def add_skill(self, skill):
    self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
print(p1.skills)
print(p2.skills)
p2.add_skill('Python')
p2.add_skill('MongoDB')
print(p2.skills)
