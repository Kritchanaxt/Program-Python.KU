class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)
        print(f"Subject {subject} has been added for {self.name} and {self.grade}")

student = Student("Wave", "Grade A")
# student.add_subject("Math")
# student.add_subject("Science")

# Loop
additional_subjects = ["Math", "Science", "History", "English", "Social"]

for subject in additional_subjects:
    student.add_subject(subject)

print(f"\n{student.name}'s subjects: {student.subjects}\n")
