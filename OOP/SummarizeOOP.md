
# Object Oriented Programming

## Inheritance (การสืบทอด)
1. **Single Inheritance**: คลาสหนึ่งสืบทอดจากอีกคลาสหนึ่ง  
   *ตัวอย่าง*: คลาส A → คลาส B (B สืบทอดจาก A)

2. **Multiple Inheritance**: คลาสหนึ่งสืบทอดจากหลายคลาส  
   *ตัวอย่าง*: คลาส A, คลาส B → คลาส C (C สืบทอดจาก A และ B)

3. **Multilevel Inheritance**: คลาสหนึ่งสืบทอดจากอีกคลาสหนึ่งซึ่งสืบทอดจากคลาสอื่น  
   *ตัวอย่าง*: คลาส A → คลาส B → คลาส C (C สืบทอดจาก B, B สืบทอดจาก A)

4. **Hierarchical Inheritance**: หลายคลาสสืบทอดจากคลาสแม่คลาสเดียว  
   *ตัวอย่าง*: คลาส A → คลาส B, คลาส C (B และ C สืบทอดจาก A)

5. **Hybrid Inheritance**: การรวมกันของการสืบทอดหลายประเภท (เช่น Multiple และ Multilevel)  
   *ตัวอย่าง*: คลาส A → คลาส B, คลาส C; คลาส D สืบทอดจาก B และ C

## Method Behavior
1. **Overloading (การโอเวอร์โหลดเมธอด)**  
   - เมธอดเดียวกันที่มีพารามิเตอร์ต่างกัน  
   - **ตัวอย่าง**: `add(x, y)` และ `add(x, y, z)`

2. **Overwriting (การเขียนทับ)**  
   - การตั้งค่าใหม่ให้กับตัวแปรเดิม  
   - **ตัวอย่าง**:
     ```python
     x = 5
     x = 10  # x ถูกเขียนทับเป็น 10
     ```

3. **Overriding (การเขียนทับเมธอดในคลาสลูก)**  
   - เมธอดในคลาสลูกที่เขียนทับเมธอดในคลาสแม่  
   - **ตัวอย่าง**:
     ```python
     class Parent:
         def show(self):
             print("ข้อความจากคลาสแม่")

     class Child(Parent):
         def show(self):
             print("ข้อความจากคลาสลูก")

     obj = Child()
     obj.show()  # แสดงผล: "ข้อความจากคลาสลูก"
     ```

4. **Special Methods**  
   - เมธอดที่เริ่มและจบด้วย `__` เช่น `__init__`, `__str__`  
   - **ตัวอย่าง**:
     ```python
     class Person:
         def __init__(self, name):
             self.name = name

         def __str__(self):
             return f"ชื่อ: {self.name}"

     p = Person("Alice")
     print(p)  # แสดงผล: "ชื่อ: Alice"
     ```

5. **Static Methods (เมธอดแบบคงที่)**  
   - เมธอดที่ไม่ต้องการการอ้างอิงข้อมูลภายในคลาส  
   - **ตัวอย่าง**:
     ```python
     class MathOperations:
         @staticmethod
         def add(x, y):
             return x + y

     result = MathOperations.add(3, 4)
     print("ผลบวกคือ:", result)  # แสดงผล: "ผลบวกคือ: 7"
     ```

## Key OOP Concepts
1. **Polymorphism (พหุสัณฐาน)**  
   - การใช้เมธอดเดียวกันกับออบเจ็กต์หลายประเภท  
   - **ตัวอย่าง**:
     ```python
     class Cat:
         def sound(self):
             print("แมวร้อง เหมียว")

     class Dog:
         def sound(self):
             print("สุนัขเห่า โฮ่ง")

     def animal_sound(animal):
         animal.sound()

     animal_sound(Cat())  # แสดงผล: "แมวร้อง เหมียว"
     animal_sound(Dog())  # แสดงผล: "สุนัขเห่า โฮ่ง"
     ```

2. **Abstraction Class (คลาสนามธรรม)**  
   - คลาสที่ไม่สามารถสร้างออบเจ็กต์ได้โดยตรง  
   - **ตัวอย่าง**:
     ```python
     from abc import ABC, abstractmethod

     class Animal(ABC):
         @abstractmethod
         def make_sound(self):
             pass

     class Dog(Animal):
         def make_sound(self):
             print("สุนัขเห่า โฮ่ง")

     Dog().make_sound()  # แสดงผล: "สุนัขเห่า โฮ่ง"
     ```

3. **Encapsulation (การห่อหุ้มข้อมูล)**  
   - การซ่อนข้อมูลและเข้าถึงผ่านเมธอดที่กำหนด  
   - **ตัวอย่าง**:
     ```python
     class BankAccount:
         def __init__(self, balance):
             self.__balance = balance

         def deposit(self, amount):
             self.__balance += amount

         def get_balance(self):
             return self.__balance

     account = BankAccount(1000)
     account.deposit(500)
     print("ยอดเงิน:", account.get_balance())  # แสดงผล: "ยอดเงิน: 1500"
     ```

## ความแตกต่าง
- **การสืบทอด** เน้นความสัมพันธ์ระหว่างคลาส
- **Method Behavior** (Overloading, Overwriting, Overriding, Special Methods, Static Methods) เน้นพฤติกรรมการทำงานของเมธอด
- **Key Concepts** (Polymorphism, Abstraction, Encapsulation) เน้นแนวทางการจัดการข้อมูลและพฤติกรรมของออบเจ็กต์