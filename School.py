from Classroom import Classroom
import Personnel


class School:
    def __init__(self, name, principle: Personnel.Principle, budget: int):
        self.name = name
        self.principle = principle
        self.budget = budget
        self.classes = []
        self.teachers = []

    def add_class(self, new_class: Classroom):
        self.classes.append(new_class)

    def add_teacher(self, new_teacher: Personnel.Teacher):
        self.teachers.append(new_teacher)

    def budget_status(self):
        bdg = self.budget
        for teacher in self.teachers:
            bdg -= teacher.salary
        bdg -= self.principle.salary
        return bdg
