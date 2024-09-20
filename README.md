# OOP

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

6. **Overloading**: ฟีเจอร์ที่ให้มีสองหรือมากกว่านั้นในเมธอดเดียวกันในคลาสเดียวกันมีชื่อเดียวกันแต่มีพารามิเตอร์ต่างกัน  
   *ตัวอย่าง*: เมธอด `add(x, y)` และ `add(x, y, z)`

7. **Special Methods**: หรือที่เรียกว่า dunder methods เป็นเมธอดที่กำหนดไว้ล่วงหน้าใน Python ซึ่งเริ่มและสิ้นสุดด้วยขีดล่างคู่ (เช่น `__init__`, `__str__`) ซึ่งช่วยในการโอเวอร์โหลดโอเปอเรเตอร์และการปรับแต่งวัตถุ

**ความแตกต่าง**:  
- **ประเภทการสืบทอด** เน้นที่ความสัมพันธ์ระหว่างคลาส (เช่น single, multiple ฯลฯ) ขณะที่ **Overloading** และ **Special Methods** เน้นที่พฤติกรรมของเมธอดและการโต้ตอบของวัตถุภายในคลาส
  
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
        - `insert`: แทรกค่าที่ตำแหน่งที่ระบุ
        - `extend`: ขยายรายการด้วย iterable อื่น
        - `clear`: ลบข้อมูลทั้งหมดในรายการ

### 2. tuple:
- ชุดข้อมูลที่จัดเก็บข้อมูลหลายค่าในลำดับ ไม่สามารถเปลี่ยนแปลงได้ (immutable)
    - ตัวอย่าง: `my_tuple = (1, 2, 3, 4)`
    - ฟังก์ชันที่ใช้บ่อย:
        - `count`: นับจำนวนครั้งที่ค่าเกิดขึ้นใน tuple
        - `index`: คืนค่าดัชนีของค่าแรกที่พบใน tuple

### 3. dictionary:
- โครงสร้างข้อมูลที่จัดเก็บคู่ค่า key-value ไม่เรียงลำดับ และสามารถเปลี่ยนแปลงได้ (mutable)
    - ตัวอย่าง: `my_dict = {'name': 'Alice', 'age': 25}`
    - ฟังก์ชันที่ใช้บ่อย:
        - `keys`: คืนค่าเป็นรายการของ keys ทั้งหมด
        - `values`: คืนค่าเป็นรายการของ values ทั้งหมด
        - `items`: คืนค่าเป็นรายการของคู่ key-value ทั้งหมด
        - `get`: คืนค่า value ที่สัมพันธ์กับ key ถ้าไม่พบคืนค่าเริ่มต้นที่กำหนด
        - `update`: อัพเดท dictionary ด้วย key-value จาก dictionary อื่น
        - `pop`: ลบค่า key ที่ระบุและคืนค่า value ที่สัมพันธ์กับ key นั้น
        - `popitem`: ลบและคืนคู่ key-value สุดท้ายที่ถูกเพิ่ม
        - `clear`: ลบข้อมูลทั้งหมดใน dictionary
        - `setdefault`: คืนค่า value ของ key ถ้าไม่มี key นี้ใน dictionary จะเพิ่ม key นี้เข้าไปและใช้ค่าเริ่มต้นที่กำหนด

### 4. reduce:
- ใช้ในการรวมค่าทั้งหมดในรายการให้เป็นค่าเดียวโดยใช้ฟังก์ชันที่กำหนด
    - ใช้กับ: `list`, `tuple`
    - ตัวอย่าง: รวมค่าทั้งหมดในรายการ
      ```
      from functools import reduce
      result = reduce(lambda x, y: x + y, [1, 2, 3, 4])  # ผลลัพธ์คือ 10
      ```
      
### 5. sum:
- ใช้ในการหาผลรวมของค่าทั้งหมดในรายการหรือ iterable
    - ใช้กับ: `list`, `tuple`, `set`
    - ตัวอย่าง: หาผลรวมของรายการ
      ```
      result = sum([1, 2, 3, 4])  # ผลลัพธ์คือ 10
      ```

### 6. ord:
- ใช้ในการหาค่าตัวเลข ASCII ของตัวอักษรที่กำหนด
    - ใช้กับ: ตัวอักษร (`str`)
    - ตัวอย่าง: หาค่า ASCII ของ 'a'
      ```
      result = ord('a')  # ผลลัพธ์คือ 97
      ```

### 7. cmp (Python 2 เท่านั้น):
- ใช้ในการเปรียบเทียบค่าสองค่า
    - ใช้กับ: ค่าใด ๆ (`int`, `str`, etc.)
    - ตัวอย่าง: เปรียบเทียบค่าที่ 1 กับ 2
      ```
      result = cmp(1, 2)  # ผลลัพธ์คือ -1
      ```

### 8. max:
- ใช้ในการหาค่ามากที่สุดจากรายการหรือ iterable
    - ใช้กับ: `list`, `tuple`, `set`
    - ตัวอย่าง: หาค่ามากที่สุดในรายการ
      ```
      result = max([1, 2, 3, 4])  # ผลลัพธ์คือ 4
      ```

### 9. min:
- ใช้ในการหาค่าน้อยที่สุดจากรายการหรือ iterable
    - ใช้กับ: `list`, `tuple`, `set`
    - ตัวอย่าง: หาค่าน้อยที่สุดในรายการ
      ```
      result = min([1, 2, 3, 4])  # ผลลัพธ์คือ 1
      ```

### 10. all:
- ใช้ในการตรวจสอบว่าทุกค่าของ iterable เป็นจริง (True) หรือไม่
    - ใช้กับ: `list`, `tuple`, `set`
    - ตัวอย่าง: ตรวจสอบค่าทั้งหมดในรายการ
      ```
      result = all([True, True, True])  # ผลลัพธ์คือ True
      ```

### 11. any:
- ใช้ในการตรวจสอบว่ามีค่าหนึ่งค่าใดใน iterable เป็นจริง (True) หรือไม่
    - ใช้กับ: `list`, `tuple`, `set`
    - ตัวอย่าง: ตรวจสอบว่ามีค่าใดเป็นจริงในรายการ
      ```
      result = any([False, True, False])  # ผลลัพธ์คือ True
      ```

### 12. len:
- ใช้ในการหาความยาวของ iterable
    - ใช้กับ: `list`, `tuple`, `set`, `str`, `dict`
    - ตัวอย่าง: หาความยาวของรายการ
      ```
      result = len([1, 2, 3, 4])  # ผลลัพธ์คือ 4
      ```

### 13. enumerate:
- ตือ รูปย่อของค่า เช่น mylist -> index
    - ใช้ในการสร้าง iterable ที่ประกอบด้วยคู่ของ index และค่าจาก iterable ที่กำหนด
    - ใช้กับ: `list`, `tuple`, `str`
    - ตัวอย่าง: สร้างคู่ index และค่าจากรายการ
      ```
      result = list(enumerate(['a', 'b', 'c']))  # ผลลัพธ์คือ [(0, 'a'), (1, 'b'), (2, 'c')]
      ```
### 14. split()
- เป็นเมธอดใน Python ที่ใช้แยกสตริงออกเป็นลิสต์ของซับสตริงตามตัวคั่นที่กำหนดไว้
  - **ค่าเริ่มต้น:** แยกตามช่องว่าง
  - **ใช้ตัวคั่น:** แยกตามตัวอักษรหรือตัวคั่นที่ระบุ
  - **จำกัดการแยก:** สามารถจำกัดจำนวนครั้งที่ต้องการแยก

ตัวอย่าง
การแยกโดยค่าเริ่มต้น (โดยช่องว่าง):
```
text = "Hello world Python"
result = text.split()
print(result)  # ผลลัพธ์: ['Hello', 'world', 'Python']
```

### 15. accumulate:
- ใช้ในการสะสมค่าจาก iterable โดยใช้ฟังก์ชันสะสม
    - ใช้กับ: `list`, `tuple`, `set`
    - ตัวอย่าง: สะสมค่าจากรายการ
      ```
      from itertools import accumulate
      result = list(accumulate([1, 2, 3, 4]))  # ผลลัพธ์คือ [1, 3, 6, 10]
      ```
### 16. set:
- ใช้ในการเก็บค่าที่ไม่ซ้ำกันและไม่มีลำดับ
    - ตัวอย่าง: `set([1, 2, 2, 3])` -> `{1, 2, 3}`

### 17. filter:
- ใช้สำหรับกรองข้อมูลใน Collection โดยให้เงื่อนไข ค่าที่เป็นจริงจะถูกเก็บไว้
    - ตัวอย่าง: `list(filter(lambda x: x > 2, [1, 2, 3, 4]))` -> `[3, 4]`

### 18. map:
- ใช้ในการแปลงค่าข้อมูลใน Collection โดยใช้เงื่อนไขหรือการประมวลผลที่กำหนด
    - ตัวอย่าง: `list(map(lambda x: x * 2, [1, 2, 3, 4]))` -> `[2, 4, 6, 8]`

### 19. lambda:
- นิพจน์ที่กำหนดฟังก์ชันแบบไม่ระบุชื่อ
    - ใช้กับ: การสร้างฟังก์ชันเล็ก ๆ ที่ใช้งานเพียงครั้งเดียว
    - ตัวอย่าง: `lambda x: x + 1`
```
# ฟังก์ชัน Lambda ที่หาผลรวมของสองค่า
sum = lambda x, y: x + y
print(sum(3, 4))  # ผลลัพธ์: 7
```
### 20. Iterators
- Iterators เป็นออบเจ็กต์ที่ช่วยให้เราสามารถทำงานกับองค์ประกอบของ collection ทีละรายการได้
  - ใช้กับ: `list`, `tuple`, `set`, `dict`, `str`
  - เมธอดหลัก: `__iter__()` และ `__next__()`

ตัวอย่าง:
```
my_list = [1, 2, 3]
iterator = iter(my_list)  # สร้าง iterator จาก list

print(next(iterator))  # ผลลัพธ์: 1
print(next(iterator))  # ผลลัพธ์: 2
print(next(iterator))  # ผลลัพธ์: 3
```

### 21. Inheritance (การสืบทอด)
- Inheritance ช่วยให้เราสามารถสร้างคลาสใหม่ที่ใช้คุณสมบัติและพฤติกรรมจากคลาสแม่และเพิ่มคุณสมบัติใหม่หรือปรับปรุงคุณสมบัติเก่าได้
  - ใช้กับ: การออกแบบคลาสเพื่อแบ่งปันคุณสมบัติและพฤติกรรมระหว่างคลาส

ตัวอย่าง:
```
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

dog = Dog("Buddy")
print(dog.speak())  # ผลลัพธ์: Buddy says Woof!
```

### 22. Classes and Objects
- Classes เป็นพิมพ์เขียวสำหรับการสร้าง objects (ออบเจ็กต์) ที่มีคุณสมบัติและพฤติกรรมที่กำหนด
  - ใช้กับ: การออกแบบและสร้างออบเจ็กต์ที่มีคุณสมบัติและพฤติกรรมเฉพาะ

ตัวอย่าง:
```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# สร้างออบเจ็กต์จากคลาส
person = Person("Alice", 30)
print(person.greet())  # ผลลัพธ์: Hello, my name is Alice and I am 30 years old.
```
### 23.zip() 
- เป็นฟังก์ชันใน Python ที่ใช้ในการจับคู่หรือรวมลิสต์หลายลิสต์เข้าด้วยกัน
- โดยฟังก์ชัน zip() จะทำงานโดยจับคู่สมาชิกจากแต่ละลิสต์ตามลำดับเดียวกันและสร้างเป็น tuple ในแต่ละรอบ

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

ตัวอย่างเช่น:
```
zipped = zip(list1, list2)
print(list(zipped))
```
ผลลัพธ์:
```
[(1, 'a'), (2, 'b'), (3, 'c')]
```

**การใช้งาน zip ในโค้ด**
```
products = [Product("Pencil", 1200, 22), Product("Lotion", 5000, 200)]
quantities = [5, 10]

for product, qty in zip(products, quantities):
    print(product.name, qty)
```
- ในกรณีนี้ zip(products, quantities) จะจับคู่สินค้าแต่ละตัวกับจำนวนที่กำหนดไว้ (เช่น "Pencil" จับคู่กับ 5 และ "Lotion" จับคู่กับ 10)

