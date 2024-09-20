
## Practice Exercise Python 1

*โจทย์ 1:* 
- การสร้างคลาสคน (Person)
สร้างคลาส Person ที่มีตัวแปร name และ age และเมธอด introduce() ซึ่งพิมพ์ข้อความแนะนำตัวในรูปแบบ "My name is [name]. I am [age] years old."

*โจทย์ 2:* 
- คลาสลูกสุนัข (Puppy) และคลาสสัตว์เลี้ยง (Pet)
สร้างคลาส Pet ที่มีตัวแปร name และ species
สร้างคลาส Puppy ที่สืบทอดมาจาก Pet และเพิ่มตัวแปร age และเมธอด bark() ซึ่งพิมพ์ "Woof!"

*โจทย์ 3:* 
- ระบบบัญชีธนาคาร
สร้างคลาส BankAccount ที่มีตัวแปร balance
เพิ่มเมธอด deposit(amount) และ withdraw(amount) เพื่อลงเงินหรือถอนเงิน โดยห้ามถอนเกินเงินคงเหลือ

*โจทย์ 4:* 
- การสืบทอดคลาสรูปทรง (Shape)
สร้างคลาส Shape ที่มีเมธอด area() และ perimeter() (สามารถใช้ pass ในขั้นแรก)
สร้างคลาสย่อย Rectangle และ Circle ที่สืบทอดจาก Shape และคำนวณพื้นที่และเส้นรอบรูปของรูปสี่เหลี่ยมผืนผ้าและวงกลม

*โจทย์ 5:* 
- การจัดการข้อมูลนักเรียน
สร้างคลาส Student ที่มีตัวแปร name, grade และ subjects (เป็นลิสต์ของวิชาที่ลงทะเบียน)
เพิ่มเมธอด add_subject(subject) เพื่อลงทะเบียนวิชาเรียน

*โจทย์ 6:* 
- ระบบพนักงาน
สร้างคลาส Employee ที่มีตัวแปร name, position, และ salary
สร้างคลาส Manager ที่สืบทอดจาก Employee และเพิ่มเมธอด promote_employee(employee) เพื่อเลื่อนตำแหน่งให้พนักงาน

*โจทย์ 7:* 
- ระบบบัตรสมาชิก
สร้างคลาส MembershipCard ที่มีตัวแปร member_name และ points
เพิ่มเมธอด add_points(points) และ redeem_points(points) เพื่อสะสมและใช้คะแนน

*โจทย์ 8:* การจัดการห้องสมุด
สร้างคลาส Book ที่มีตัวแปร title, author และ isbn
สร้างคลาส Library ที่มีลิสต์ของ Book และเมธอด add_book(book) และ find_book_by_title(title) เพื่อเพิ่มหนังสือและค้นหาหนังสือตามชื่อเรื่อง

*โจทย์ 9:* เกมทอยลูกเต๋า
สร้างคลาส Die ที่มีเมธอด roll() ซึ่งสุ่มตัวเลขจาก 1 ถึง 6 (ใช้ random.randint)
เพิ่มคลาส Game ที่รับคลาส Die หลายลูกในการทอยพร้อมกัน

*โจทย์ 10:* การคำนวณเวลาจากนาฬิกา
สร้างคลาส Clock ที่มีตัวแปร hours, minutes, และ seconds
เพิ่มเมธอด add_time(hours, minutes, seconds) เพื่อเพิ่มเวลาและจัดการกับการทบจำนวนของนาทีและวินาที