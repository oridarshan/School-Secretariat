class Person:

    def __init__(self, p_id: int, name: str):
        self.id = p_id
        self.name = name

    def __str__(self):
        return f'<{self.name}, {self.id}>'

    def __eq__(self, other):
        return self.id == other.id

class Student(Person):
    def __init__(self, p_id: int, name: str, subjects: list):
        super().__init__(p_id, name)
        self.subjects = subjects

    def add_class(self, new_class):
        self.subjects.append(new_class)


class Teacher(Person):
    def __init__(self, p_id: int, name: str, subjects: list, salary: int = 0):
        super().__init__(p_id, name)
        self.subjects = subjects
        self.salary = salary

    def set_salary(self, salary: int):
        self.salary = salary

    def get_raise(self, money_raise):
        self.salary += money_raise

    def __repr__(self):
        return super().__str__() + ' subjects: ' + str(self.subjects)


class Manager(Person):
    def __init__(self, p_id: int, name: str, teachers: list[Teacher], salary: int = 0):
        super().__init__(p_id, name)
        self.salary = salary
        self.teachers = {}
        for teacher in teachers:
            self.teachers[teacher.name] = teacher

    def fire_teacher(self, teacher_name):
        self.teachers.pop(teacher_name)

    def print_teachers(self):
        print(self.teachers)


