
#* 10. Count Even and Odd Numbers in a List

numbers = list(map(int, input("Enter numbers: ").split()))
evens = sum(1 for x in numbers if x % 2 == 0)
odds = sum(1 for x in numbers if x % 2 != 0)
print(f"Even numbers: {evens}, Odd numbers: {odds}")

#? 1: สำหรับทุกจำนวนที่ตรงตามเงื่อนไข (คือเป็นเลขคี่) จะคืนค่า 1
#* for x in ทำการวนลูปผ่านแต่ละสมาชิก x ในลิสต์ numbers