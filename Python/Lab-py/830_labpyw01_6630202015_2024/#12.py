
#* 12. Grade with Function

def get_grade(score):
    if score >= 90 and score <= 100:
        print("Grade: A")
    elif score >= 80 and score <= 89:
        print("Grade: B")
    elif score >= 70 and score <= 79:
        print("Grade: C")
    elif score >= 60 and score <= 69:
        print("Grade: D")
    elif score >= 50 and score <= 59:
        print("Grade: E")
    else:
        print("ERROR")

score = int(input("Input Score: "))
get_grade(score)


#* 12.1. Grade with Ternary Operator
#! ternary operator
#? Struct: "value" if_true if condition else "value" if_false

# def get_grade(score):
#     return "Grade A" if 90 <= score <= 100 else (
#            "Grade B" if 80 <= score <= 89 else (
#            "Grade C" if 70 <= score <= 79 else (
#            "Grade D" if 60 <= score <= 69 else (
#            "Grade E" if 50 <= score <= 59 else "ERROR"))))

# score = int(input("Input Score: "))
# print(get_grade(score))



#python by nuttaphon
l = [1,2,3,4,5,6,7,8,9,10,11,12,13]
for i in l:
    print(f"Floor {i} is {i-1} actual floor") if i > 13 else print(f"Floor {i} is actual floor") 