
#? Ex.OOP1 - #10

class Clock:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def normalize(self):
        if self.seconds >=60 :
            self.minutes += self.seconds // 60
            self.seconds %= 60
        if self.minutes >= 60 :
            self.hours += self.minutes // 60
            self.minutes %= 60
        self.hours %= 24

    def add_time(self, hours, minutes, seconds):
        self.hours += hours
        self.minutes += minutes
        self.seconds += seconds
        self.normalize()

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
    

clock = Clock(10, 30, 45)
print("\nInitial time:", clock)

clock.add_time(1, 40, 30)
print("After adding time:", clock)

clock.add_time(0, 0, 50)
print("After adding more time:", clock)
print("\n")