
#* 6.
#? Inheritance

class Student(Person):
  pass

s1 = Student('Eyob', 'Yetateh', 30, 'Finland', 'Helsinki')
s2= Student('John', 'Doe', 20, 'Nomanland', 'Noman city')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)

