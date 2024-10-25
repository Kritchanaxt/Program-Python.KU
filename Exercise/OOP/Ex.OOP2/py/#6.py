
#? Large project management system

from datetime import datetime

class TeamMember:
    def __init__(self, name, role):
        self.name = name
        self.role = role

class Task:
    def __init__(self, name, start_date, end_date, team_members=[]):
        self.name = name
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.team_members = team_members
        self.status = "Not Started"

    def update_status(self, new_status):
        self.status = new_status

    def time_spent(self):
        return (self.end_date - self.start_date).days

class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def project_report(self):
        print(f"Project report: {self.name}")
        for task in self.tasks:
            print(f"Task: {task.name}, Status: {task.status}, Duration: {task.time_spent()} days")

member1 = TeamMember("Somchai", "Developer")
member2 = TeamMember("Somying", "Tester")

task1 = Task("Develop feature", "2024-10-01", "2024-10-15", [member1])
task2 = Task("Test system", "2024-10-16", "2024-10-20", [member2])

project = Project("Project Management System")
project.add_task(task1)
project.add_task(task2)

project.project_report()
