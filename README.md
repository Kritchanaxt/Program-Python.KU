# Object Oriented Programming (OOP)

## Inheritance (การสืบทอด)
1. **Single Inheritance**: คลาสหนึ่งสืบทอดจากอีกคลาสหนึ่ง  
   *ตัวอย่าง*:
   ```python
   คลาส A → คลาส B (B สืบทอดจาก A)
   ```
   
3. **Multiple Inheritance**: คลาสหนึ่งสืบทอดจากหลายคลาส  
   *ตัวอย่าง*:
   ```python
   คลาส A, คลาส B → คลาส C (C สืบทอดจาก A และ B)
   ```
   
5. **Multilevel Inheritance**: คลาสหนึ่งสืบทอดจากอีกคลาสหนึ่งซึ่งสืบทอดจากคลาสอื่น  
   *ตัวอย่าง*:
   ```python
   คลาส A → คลาส B → คลาส C (C สืบทอดจาก B, B สืบทอดจาก A)
   ```
   
7. **Hierarchical Inheritance**: หลายคลาสสืบทอดจากคลาสแม่คลาสเดียว  
   *ตัวอย่าง*:
   ```python
   คลาส A → คลาส B, คลาส C (B และ C สืบทอดจาก A)
   ```
   
9. **Hybrid Inheritance**: การรวมกันของการสืบทอดหลายประเภท (เช่น Multiple และ Multilevel)  
   *ตัวอย่าง*:
   ```python
   คลาส A → คลาส B, คลาส C; คลาส D สืบทอดจาก B และ C
   ```
   
## Method Behavior
1. **Overloading (การโอเวอร์โหลดเมธอด)**  
   - เมธอดเดียวกันที่มีพารามิเตอร์ต่างกัน  
   **ตัวอย่าง**:
     ```python
     `add(x, y)` และ `add(x, y, z)`
     ```
2. **Overwriting (การเขียนทับ)**  
   - การตั้งค่าใหม่ให้กับตัวแปรเดิม  
   **ตัวอย่าง**:
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

# Special Methods

### 1. **`__init__(self, ...)`**
   - เมธอดตัวสร้าง (Constructor) ที่ใช้ในการกำหนดค่าเริ่มต้นให้กับออบเจ็กต์เมื่อถูกสร้างขึ้น
   - ตัวอย่าง:
     ```python
     class Person:
         def __init__(self, name):
             self.name = name
     ```

### 2. **`__str__(self)`**
   - เมธอดที่ใช้แปลงออบเจ็กต์ให้เป็นสตริงสำหรับการแสดงผลที่เข้าใจได้ง่าย
   - ตัวอย่าง:
     ```python
     class Person:
         def __str__(self):
             return f"Person(name={self.name})"
     ```

### 3. **`__repr__(self)`**
   - เมธอดที่ใช้แปลงออบเจ็กต์ให้เป็นสตริงที่สามารถใช้ในการสร้างออบเจ็กต์ใหม่ได้ โดยมักใช้สำหรับการดีบัก
   - ตัวอย่าง:
     ```python
     class Person:
         def __repr__(self):
             return f"Person('{self.name}')"
     ```

### 4. **`__len__(self)`**
   - เมธอดที่ใช้กำหนดความยาวของออบเจ็กต์ โดยมักใช้กับคอนเทนเนอร์ เช่น ลิสต์, สตริง เป็นต้น
   - ตัวอย่าง:
     ```python
     class MyList:
         def __init__(self, data):
             self.data = data
         
         def __len__(self):
             return len(self.data)
     ```

### 5. **`__getitem__(self, key)`**
   - เมธอดที่ใช้กำหนดการเข้าถึงค่าในออบเจ็กต์ด้วยการใช้ดัชนีหรือคีย์
   - ตัวอย่าง:
     ```python
     class MyList:
         def __getitem__(self, index):
             return self.data[index]
     ```

### 6. **`__setitem__(self, key, value)`**
   - เมธอดที่ใช้กำหนดการตั้งค่าของออบเจ็กต์ผ่านดัชนีหรือคีย์
   - ตัวอย่าง:
     ```python
     class MyList:
         def __setitem__(self, index, value):
             self.data[index] = value
     ```

### 7. **`__delitem__(self, key)`**
   - เมธอดที่ใช้กำหนดการลบค่าจากออบเจ็กต์ผ่านดัชนีหรือคีย์
   - ตัวอย่าง:
     ```python
     class MyList:
         def __delitem__(self, index):
             del self.data[index]
     ```

### 8. **`__add__(self, other)`**
   - เมธอดที่ใช้กำหนดพฤติกรรมของการใช้เครื่องหมายบวก (`+`) กับออบเจ็กต์
   - ตัวอย่าง:
     ```python
     class Vector:
         def __add__(self, other):
             return Vector(self.x + other.x, self.y + other.y)
     ```

### 9. **`__eq__(self, other)`**
   - เมธอดที่ใช้กำหนดพฤติกรรมการเปรียบเทียบความเท่ากัน (`==`)
   - ตัวอย่าง:
     ```python
     class Person:
         def __eq__(self, other):
             return self.name == other.name
     ```

### 10. **`__call__(self, ...)`**
   - เมธอดที่ใช้ทำให้ออบเจ็กต์สามารถถูกเรียกใช้งานได้เหมือนกับเป็นฟังก์ชัน
   - ตัวอย่าง:
     ```python
     class MyFunction:
         def __call__(self, x):
             return x * 2
     ```

### 11. **`__iter__(self)` และ `__next__(self)`**
   - เมธอดที่ใช้ทำให้ออบเจ็กต์สามารถใช้งานในลูป `for` ได้ (Iterable และ Iterator)
   - ตัวอย่าง:
     ```python
     class MyRange:
         def __iter__(self):
             self.current = 0
             return self
         
         def __next__(self):
             if self.current < 5:
                 self.current += 1
                 return self.current
             else:
                 raise StopIteration
     ```

  
# Highlight Python

### 1. list:
- ชุดข้อมูลที่จัดเก็บข้อมูลหลายค่าในลำดับ สามารถเปลี่ยนแปลงได้ (mutable)
    - ตัวอย่าง: `my_list = [1, 2, 3, 4]`
    - ฟังก์ชันที่ใช้บ่อย:
        - `append`: เพิ่มค่าเข้าไปที่ท้ายรายการ
        - `remove`: ลบค่าตัวแรกที่พบในรายการที่ตรงกับค่าที่ระบุ
        - `pop`: ลบและคืนค่าตัวสุดท้ายของรายการ หรือค่าที่ตำแหน่งที่ระบุ
          - ตัวอย่าง: `value = my_list.pop()` หรือ `value = my_list.pop(1)`
        - `del`: ลบค่าที่ตำแหน่งที่ระบุ หรือลบรายการทั้งหมด
          - ตัวอย่าง: `del my_list[1]` หรือ `del my_list`
        - `sort`: เรียงลำดับข้อมูลในรายการ
        - `reverse`: กลับลำดับของรายการ
        - `insert`: แทรกค่าที่ตำแหน่งที่ระบุ### 1. List
- เก็บข้อมูลหลายค่าที่เปลี่ยนแปลงได้ เช่น `[1, 2, 3]`
    - ฟังก์ชัน:
        - `append()`: เพิ่มค่าเข้าไป
        - `remove()`: ลบค่าที่ตรงกัน
        - `pop()`: ลบค่าตำแหน่งที่ระบุ
        - `del`: ลบค่า หรือลบทั้งรายการ
        - `sort()`, `reverse()`, `clear()`, `insert()`, `extend()`: จัดการข้อมูล

### 2. Tuple
- เก็บข้อมูลหลายค่าที่แก้ไขไม่ได้ เช่น `(1, 2, 3)`
    - ฟังก์ชัน:
        - `count()`, `index()`: นับและค้นหาข้อมูล

### 3. Dictionary
- เก็บข้อมูลเป็นคู่ `key-value` เช่น `{'name': 'Alice', 'age': 25}`
    - ฟังก์ชัน:
        - `keys()`, `values()`, `items()`, `get()`, `update()`, `pop()`: จัดการข้อมูล

### 4. Reduce
- รวมค่าทั้งหมดในรายการให้เป็นค่าเดียว
```python
from functools import reduce
result = reduce(lambda x, y: x + y, [1, 2, 3])  # ผลลัพธ์: 6
```

### 5. Sum
- คำนวณผลรวมของรายการ
```python
result = sum([1, 2, 3])  # ผลลัพธ์: 6
```

### 6. Ord
- หาค่า ASCII ของตัวอักษร
```python
result = ord('a')  # ผลลัพธ์: 97
```

### 7. Max, Min
- หาค่ามากหรือน้อยที่สุดในรายการ
```python
max_value = max([1, 2, 3])  # ผลลัพธ์: 3
min_value = min([1, 2, 3])  # ผลลัพธ์: 1
```

### 8. All, Any
- ตรวจสอบว่าค่าทั้งหมดเป็นจริงหรือมีค่าใดเป็นจริง
```python
result = all([True, True, False])  # ผลลัพธ์: False
result = any([False, True, False])  # ผลลัพธ์: True
```

### 9. Len
- หาความยาวของข้อมูล
```python
result = len([1, 2, 3])  # ผลลัพธ์: 3
```

### 10. Enumerate
- เพิ่มหมายเลขลำดับให้ข้อมูล
```python
for index, value in enumerate(['a', 'b']):
    print(index, value)  # ผลลัพธ์: 0 a, 1 b
```

### 11. Split
- แยกสตริงเป็นลิสต์
```python
result = "Hello world".split()  # ผลลัพธ์: ['Hello', 'world']
```

### 12. Accumulate
- สะสมค่าจากข้อมูล
```python
from itertools import accumulate
result = list(accumulate([1, 2, 3]))  # ผลลัพธ์: [1, 3, 6]
```

### 13. Set
- เก็บค่าที่ไม่ซ้ำกัน
```python
unique_values = set([1, 1, 2])  # ผลลัพธ์: {1, 2}
```

### 14. Filter
- กรองข้อมูลตามเงื่อนไข
```python
result = list(filter(lambda x: x > 1, [1, 2, 3]))  # ผลลัพธ์: [2, 3]
```

### 15. Map
- แปลงค่าตามเงื่อนไข
```python
result = list(map(lambda x: x * 2, [1, 2, 3]))  # ผลลัพธ์: [2, 4, 6]
```

### 16. Lambda
- ฟังก์ชันแบบย่อ
```python
add = lambda x, y: x + y
result = add(3, 4)  # ผลลัพธ์: 7
```

### 17. Iterator
- วนลูปผ่านข้อมูลได้
```python
my_list = [1, 2, 3]
iterator = iter(my_list)
print(next(iterator))  # ผลลัพธ์: 1
```

### 18. Inheritance
- สร้างคลาสใหม่ที่มีคุณสมบัติของคลาสแม่
```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

dog = Dog()
print(dog.speak())  # ผลลัพธ์: Woof!
```

### 19. Class and Object
- คลาสเป็นพิมพ์เขียวสำหรับสร้างออบเจ็กต์
```python
class Person:
    def __init__(self, name):
        self.name = name

person = Person("Alice")
print(person.name)  # ผลลัพธ์: Alice
```

### 20. Zip
- รวมลิสต์เข้าด้วยกัน
```python
zipped = zip([1, 2], ['a', 'b'])
print(list(zipped))  # ผลลัพธ์: [(1, 'a'), (2, 'b')]
```

### 21. Pass
- ใช้เป็นตัวแทนคำสั่งที่ยังไม่พร้อม
```python
def my_function():
    pass
```

